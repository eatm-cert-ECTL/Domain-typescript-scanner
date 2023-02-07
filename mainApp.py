import sqlite3
from sqlite3.dbapi2 import OperationalError

from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import QThread, Qt
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox, QSplashScreen, QStyleOptionViewItem, QStyledItemDelegate

from ui_main import Ui_MainWindow

import re #regular expressions
import time 
import sys
import os
import magic
import idna
import database
import openpyxl
from pathlib import Path

import dns_requesting
import list_generation
import analyser

import argparse

class MainApp(QtWidgets.QMainWindow,Ui_MainWindow):
    parser = argparse.ArgumentParser()
    parser.add_argument('--extended',action='store_true',help="Enable reversewhois and report generation")
    args = parser.parse_args()
    EXTENDED = args.extended

    def __init__(self, parent=None) -> None:
        """Main window

        Args:
            parent (QWidget, optional): Parent widget. Defaults to None.
        """
        super(MainApp,self).__init__(parent)
        self.setupUi(self)

        if not MainApp.EXTENDED:
            self.reverseWhoisGenerationGroupBox.setVisible(False)

        # Bind buttons to function
        self.Load.clicked.connect(self.load)
        self.typosquattingGenerateButton.clicked.connect(self.generate1)
        self.reverseWhoisGenerateButton.clicked.connect(self.generate2)
        self.New.clicked.connect(self.new)
        self.checkDNSButton.clicked.connect(self.checkDNS)
        self.addToWhitelistButton.clicked.connect(self.toggleToWhitelist)
        self.addToBlacklistButton.clicked.connect(self.toggleToBlacklist)
        self.analyseButton.clicked.connect(self.analyse)
        self.adduserlistButton.clicked.connect(self.addUserList)
        
        # Disable the dynamic necessary elements which at the beginning
        self.progressBar.setDisabled(True)
        self.checkDNSButton.setDisabled(True)
        self.addToWhitelistButton.setDisabled(True)
        self.addToBlacklistButton.setDisabled(True)

        # Model containing generated domains
        self.model = None
        # Model containing domains used for generation
        self.domainsModel = None
        # Model containing keywords used for generation
        self.keywordsModel = None
        self.dbLoaded = False

        # Database init
        self.con = QSqlDatabase.addDatabase("QSQLITE")
        self.typosquatDomainTableName = "data"
        self.keywordsTableName = "keywords"
        self.domainsTableName = "domains"
        
    def __del__(self) -> None:
        """Close database if it is open
        """
        if self.con.isOpen():
            self.con.close()

    def new(self) -> None:
        """Called when new button is clicked. Remove file if already exist. Initialize a database.

        Returns:
            String: File path selected by the user. None if no file was selected
        """

        file = QFileDialog.getSaveFileName(self,"Create new database file")
        if file[0] != '':
            #Erase file if already exists
            if os.path.exists(file[0]):
                os.remove(file[0])

            con = sqlite3.connect('{}'.format(file[0]))
            cur = con.cursor()
            request = f"CREATE TABLE {self.typosquatDomainTableName}(domains text, isWhitelisted integer DEFAULT 0, isBlacklisted integer DEFAULT 0, registered integer DEFAULT 0)" 
            try:
                cur.execute(request)
            except OperationalError as err:
                QMessageBox.critical(None, "Database Error",str(err))
            request = f"CREATE TABLE {self.keywordsTableName}(keyword text)"
            try:
                cur.execute(request)
            except OperationalError as err:
                QMessageBox.critical(None, "Database Error",str(err))
            request = f"CREATE TABLE {self.domainsTableName}(domain text)"
            try:
                cur.execute(request)
            except OperationalError as err:
                QMessageBox.critical(None, "Database Error",str(err))
            con.commit()
            con.close()
            self.loadDB(file[0])
            return file
        return None


    def parseDomains(self,domains : str) -> list[str]:
        """Parse domains entered in the dedicated text field.

        Args:
            domains (:class:`str`): String containing the domains to parse separated by a simicolon.

        Returns:
            :class:`list`: List of parsed domains
        """

        domains = domains.split(";")
        if domains[len(domains)-1] == "":
            domains = domains[:len(domains)-1]
        

        for domain in domains:
            if not self.validate_domain(domain):
                QMessageBox.critical(None, "Error","{} is not a valid domain name".format(domain))
                return []
        return domains

    
    
    def addUserList(self) -> None:
        """Add a list of domains to the database, taken from a file, supports plain text files with one domain per line, and excel files, with the domains in the first column
        """
        if not self.dbLoaded:
            if self.new() == None:
                return
        output = []
        content = ""
        file = QFileDialog.getOpenFileName(self,"Open Userlist","~/")
        if file[0] != "":
            print(magic.from_file(file[0], mime=True))
            if magic.from_file(file[0], mime=True) == 'text/plain':
                with open(file[0]) as f:
                    content = f.readlines()
                for elem in content:
                    x = str(elem.strip())
                    if self.validate_domain(x):
                        output.append(x)
                database.insertIntoDatabase(output, self)
            elif magic.from_file(file[0], mime=True) == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
                xlsx_file = openpyxl.load_workbook(file[0])
                sheet = xlsx_file.active
                for row in sheet.iter_rows():
                    x = str(row[0].value.strip())
                    if self.validate_domain(x):
                        output.append(x)
                database.insertIntoDatabase(output,self)
                #QMessageBox.critical(None, "Error","xslx not supported")
            else:
                QMessageBox.critical(None, "Error","You must choose a valid plaintext or xlsx file database")
    
    
    def generate1(self) -> None:
        self.generate(True, False)
        pass
    
    def generate2(self) -> None:
        self.generate(False, True)
        pass
    
    
    # Generate database depending on parameters
    def generate(self, domain : bool, keyword : bool) -> bool:
        """Generates domains depending on parameters read on the UI.

        Returns:
            bool: True if generation has started succesfully, False ortherwise.
        """

        if not self.dbLoaded:
            QMessageBox.information(self,"No database loaded","You must create and/or load a database before generating any domain")
            return False

        self.thread = QThread()

        if domain:
            domains = self.parseDomains(self.domains.text())
            if domains == []:
                QMessageBox.information(self,"No domain name","You must enter a domain name to generate domains")
                return False
            self.worker = list_generation.Worker(self, domains,self.dnstwitstCheckBox.isChecked(),self.TLDCheckBox.isChecked(),self.urlcrazyCheckBox.isChecked(),False,False)
        elif keyword:
            if self.keywordsListSelectorWidget.path == "":
                QMessageBox.information(self,"No keyword file","You must enter a keyword file to generate domains")
                return False
            self.worker = list_generation.Worker(self, [],False,False,False,True,self.useVirustotalCheckBox.isChecked())
        
        

        self.disableButtons()

        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.finished.connect(self.enableButtons)
        self.worker.errorSignal.connect(self.showErrorBox,QtCore.Qt.BlockingQueuedConnection)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.finished.connect(self.typosquatDomainsTableView.resizeColumnsToContents)
        self.thread.finished.connect(self.domainsTableView.resizeColumnsToContents)
        self.thread.finished.connect(self.keywordsTableView.resizeColumnsToContents)

        self.thread.start()

        return True

    def disableButtons(self) -> None:
        self.Load.setDisabled(True)
        self.reverseWhoisGenerateButton.setDisabled(True)
        self.typosquattingGenerateButton.setDisabled(True)
        self.New.setDisabled(True)
        self.checkDNSButton.setDisabled(True)
        self.addToWhitelistButton.setDisabled(True)
        self.addToBlacklistButton.setDisabled(True)
        self.analyseButton.setDisabled(True)
        self.adduserlistButton.setDisabled(True)
    
    def enableButtons(self) -> None:
        self.Load.setDisabled(False)
        self.reverseWhoisGenerateButton.setDisabled(False)
        self.typosquattingGenerateButton.setDisabled(False)
        self.New.setDisabled(False)
        self.checkDNSButton.setDisabled(False)
        self.addToWhitelistButton.setDisabled(False)
        self.addToBlacklistButton.setDisabled(False)
        self.analyseButton.setDisabled(False)
        self.adduserlistButton.setDisabled(False)

    def load(self) -> None:
        """Called when the load button is clicked. Check if the selected file is a valid sqlite file.
        """
        file = QFileDialog.getOpenFileName(self,"Open Database","~/")
        if file[0] != "":
            if magic.from_file(file[0], mime=True) == 'application/x-sqlite3':
                self.loadDB(file[0])
            else:
                QMessageBox.critical(None, "Error","You must choose a valid sqlite3 database. If you never genrated one please use the New button")

    def loadDB(self,path : Path) -> None:
        """Load database into a :class:`QSqlTableModel`. If a database is already loaded this function will unload it before loading the new one.

        Args:
            path (:class:`str`): Path to the database.
        """
        self.disableButtons()
        if self.dbLoaded:
            self.con.close()
            self.dbLoaded = False
        self.con.setDatabaseName(path)
        self.databaseName = path
        self.con.open()
        if self.con.isOpen():
            self.model = QSqlTableModel(self,self.con)
            self.model.setTable(self.typosquatDomainTableName)
            self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
            self.model.select()
            self.typosquatDomainsTableView.setModel(self.model)
            self.typosquatDomainsTableView.setItemDelegate(TableDelegate())
            self.typosquatDomainsTableView.resizeColumnsToContents()
            self.typosquatDomainsTableView.setSortingEnabled(True)

            self.domainsModel = QSqlTableModel(self,self.con)
            self.domainsModel.setTable(self.domainsTableName)
            self.domainsModel.select()
            self.domainsTableView.setModel(self.domainsModel)
            self.domainsTableView.resizeColumnsToContents()
            self.domainsTableView.setSortingEnabled(True)

            self.keywordsModel = QSqlTableModel(self,self.con)
            self.keywordsModel.setTable(self.keywordsTableName)
            self.keywordsModel.select()
            self.keywordsTableView.setModel(self.keywordsModel)
            self.keywordsTableView.resizeColumnsToContents()
            self.keywordsTableView.setSortingEnabled(True)

            self.dbLoaded = True
            self.loadedDatabaseLabel.setText(f"Loaded: {self.databaseName.split('/')[-1]}")
        else:
            print("unable to open db")
            QMessageBox.critical(None, "Database Error", self.con.lastError().text())
        self.enableButtons()
        
    def checkDNS(self) -> None:
        """Called when check DNS button is clicked. This function starts dns check thread.
        """
        self.disableButtons()
        self.progressBar.setValue(0)
        self.progressBar.setDisabled(False)
        self.thread = QThread()
        self.worker = dns_requesting.Worker(self)
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.finished.connect(self.enableButtons)
        self.worker.finished.connect(lambda : self.progressBar.setDisabled(True))
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.advancement.connect(self.progressBar.setValue)
        
        self.thread.start()


    def toggleToBlacklist(self) -> None:
        """Add / remove from black list the selected domains in the model.
        """
        if self.typosquatDomainsTableView.selectionModel().hasSelection():
            indexes = self.typosquatDomainsTableView.selectedIndexes()
            for index in indexes:
                row = index.row()
                record = self.model.record(row)
                if record.value("isBlacklisted") == 0:
                    record.setValue("isBlacklisted",1)
                else:
                    record.setValue("isBlacklisted",0)
                self.model.setRecord(row,record)
        self.repaint()

    def toggleToWhitelist(self) -> None:
        """Add / remove from white list the selected domains in the model.
        """
        if self.typosquatDomainsTableView.selectionModel().hasSelection():
            indexes = self.typosquatDomainsTableView.selectedIndexes()
            for index in indexes:
                row = index.row()
                record = self.model.record(row)
                if record.value("isWhitelisted") == 0:
                    record.setValue("isWhitelisted",1)
                else:
                    record.setValue("isWhitelisted",0)
                self.model.setRecord(row,record)
        self.repaint()

    def analyse(self) -> None:
        """Starts the analysis window if the a database is loaded. Otherwise asks for fast analysis.
        """
        if self.dbLoaded:
            analys = analyser.Analyser(self.model,parent=self)
            analys.show()
        else:
            reply = QMessageBox.question(self,"No database loaded","No database is loaded. Would you like to do fast analysis ?", buttons = QMessageBox.Yes | QMessageBox.No, defaultButton=QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.fastAnalyse()

    def fastAnalyse(self) -> None:
        """Function called when no database is loaded. This function uses the domains field to get and start the analysis window and process on them.
        """
        domains = self.parseDomains(self.domains.text())
        if domains == []:
            QMessageBox.critical(self, "No domains to analyse", "No domains were entered in the domains field for analysis. Unable to procced")
            return
        analys = analyser.Analyser(domains,parent=self)
        analys.show()

    def validate_domain(self, domain : str) -> bool:
        """Check if a domain name is valid.

        Args:
            domain (:class:`str`): domain to check.

        Returns:
            bool: True if the doman is valid. False if the domain is invalid.
        """
        VALID_FQDN_REGEX = re.compile(r'(?=^.{4,253}$)(^((?!-)[a-zA-Z0-9-]{1,63}(?<!-)\.)+[a-zA-Z]{2,63}$)', re.IGNORECASE)
        if len(domain) > 253:
            return False
        if VALID_FQDN_REGEX.match(domain):
            try:
                _ = idna.decode(domain)
            except Exception:
                return False
            else:
                return True
        return False

    def showErrorBox(self,title: str, text: str) -> None:
        QMessageBox.critical(self, title, text)


class TableDelegate(QStyledItemDelegate):

    def __init__(self) -> None:
        """Manage the colors of the table view.
        """
        super().__init__()

    def paint(self, painter:QtGui.QPainter,option:QStyleOptionViewItem,index:QtCore.QModelIndex) -> None:
        color = Qt.GlobalColor.white
        if index.siblingAtColumn(1).data() == 1:
            color = Qt.GlobalColor.green
        elif index.siblingAtColumn(2).data() == 1:
            color = Qt.GlobalColor.red
        else:
            color = Qt.GlobalColor.transparent
        painter.fillRect(option.rect,color)
        super().paint(painter,option,index)



def main() -> None:
    app = QApplication(sys.argv)
    splashPixmap = QPixmap("./TYDEA_logo.png")
    splashscreen = QSplashScreen(splashPixmap)
    splashscreen.show()
    app.processEvents()
    time.sleep(1)
    form = MainApp()
    form.show()
    splashscreen.finish(form)
    app.exec_()


if __name__ == "__main__":
    main()