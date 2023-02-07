from typing import Dict
import mainApp
import os
from libs.qjsonmodel import QJsonModel

import thread_analysis
import report_generator

from PyQt5 import QtWidgets,QtGui
from PyQt5.QtCore import QModelIndex, QThread, QTimer
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtWidgets import QWidget

from ui_analyser import Ui_Analyser

import json



class Analyser(QtWidgets.QMainWindow,Ui_Analyser):
    def __init__(self, model, parent:QWidget=None) -> None:
        """Window for domain analysis

        Args:
            model (:class:`PyQt5.QtSql.QSqlTableModel`): SqlTableModel containing previously generated domains and reated attributes. Can be a list in case no database is opened (fast analysis mode)
            parent (:class:`QWidget`, optional): Parent widget. Defaults to None.
        """
        super(Analyser,self).__init__(parent)
        self.setupUi(self)

        self.IPQSJsonModel = QJsonModel(parent=self)
        self.virustotalJsonModel = QJsonModel(parent=self)
        self.whoisJsonModel = QJsonModel(parent=self)

        # list of domain names for which a report was generated
        self.generatedReports = []
        if not mainApp.MainApp.EXTENDED:
            for i in range(self.reportLayout.count()):
                self.reportLayout.itemAt(i).widget().setVisible(False)
            self.generateReportButton.setVisible(False)

        
        self.whitelistButton.setVisible(True)
        self.blacklistButton.setVisible(True)
        self.whitelistButton.setDisabled(True)
        self.blacklistButton.setDisabled(True)
        self.nextButton.setDisabled(True)
        self.previousButton.setDisabled(True)
        self.generateReportButton.setDisabled(True)
        self.whitelistButton.clicked.connect(self.addWhitelist)
        self.blacklistButton.clicked.connect(self.addBlacklist)
        self.nextButton.clicked.connect(self.next)
        self.previousButton.clicked.connect(self.previous)
        self.generateReportButton.clicked.connect(self.generateReport)
        self.progressBar.setValue(0)

        if isinstance(model,list):
            self.domainList = model
            self.whitelistButton.setVisible(False)
            self.blacklistButton.setVisible(False)
            self.model = QSqlTableModel()
        else:
            self.model = model
            self.model.setFilter("registered == 1 AND isWhitelisted == 0 AND isBlacklisted == 0")
            self.model.select()
            self.domainList = [self.model.record(row).field(0).value() for row in range(self.model.rowCount(QModelIndex()))] # Get all domains names needing analysis
        self.startAnalysis()
    
    def closeEvent(self,event:QtGui.QCloseEvent) -> None:
        for index,elt in enumerate(self.domainList):
            record = self.model.record(index)
            if record.value("isBlacklisted") == 1 and not elt in self.generatedReports:
                reply = QtWidgets.QMessageBox.question(self,"No report generated","No report was generated for the following domain : {}\nDo you want to generate one ?".format(elt), buttons = QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Yes, defaultButton=QtWidgets.QMessageBox.No)
                if reply == QtWidgets.QMessageBox.Yes:   
                    event.ignore()
                    return
        event.accept()

    def __del__(self) -> None:
        """Check if the analysis thread is finished and quit it if not
        """
        if not self.thread.isFinished():
            self.thread.quit()

    def addWhitelist(self) -> None:
        """Add domain to whitelist and go to the next domain
        """
        record = self.model.record(self.index)
        record.setValue("isBlacklisted",0)
        record.setValue("isWhitelisted",1)
        self.model.setRecord(self.index,record)
        self.next()

    def addBlacklist(self) -> None:
        """Add domain to blacklist and go to the next domain
        """
        record = self.model.record(self.index)
        record.setValue("isBlacklisted",1)
        record.setValue("isWhitelisted",0)
        self.model.setRecord(self.index,record)
        self.next()

    def next(self) -> None:
        """Increment index if possible or close the window if the last domain is analysed
        """
        self.index += 1
        if self.index >= len(self.domainList):
            self.close()
        else:
            self.updateUI()

    def previous(self) -> None:
        """Go back to the previous domain
        """
        self.index -= 1
        self.updateUI()

    def getOutput(self,output : dict) -> None:
        """Function called when the analysis thread has finished its job

        Args:
            output (dict): dictionary key are domains and values are :class:`thread_analysis.FullAnalysis`
        """
        self.output = output
        self.progressBar.setValue(100)
        self.progressBar.setDisabled(True)
        self.progressBar.setVisible(False)
        self.whitelistButton.setDisabled(False)
        self.blacklistButton.setDisabled(False)
        self.nextButton.setDisabled(False)
        self.generateReportButton.setDisabled(False)
        self.whoisCollapsableTreeView.expand()
        self.updateUI()

    def updateUI(self) -> None:
        """Update the UI when the analysed domain change
        """
        item = self.output[self.domainList[self.index]]

        self.domainNameLabel.setText(item.domain)

        self.countLabel.setText("{}/{}".format(self.index+1,len(self.domainList)))

        self.imageArea.setPixmap(QtGui.QPixmap(os.fspath(item.imagePath)))

        if item.ipqs.score != None:
            if item.ipqs.score >= 75:
                self.IPQSValueLabel.setStyleSheet("color: #FF0000")
            else:
                self.IPQSValueLabel.setStyleSheet("color: #000000")
            self.IPQSJsonModel.load(item.ipqs.response)
            self.IPQSCollapsableTreeView.treeView.setModel(self.IPQSJsonModel)
            self.IPQSCollapsableTreeView.treeView.resizeColumnToContents(0)
            self.IPQSCollapsableTreeView.setVisible(True)
        else:
            self.IPQSCollapsableTreeView.setVisible(False)
        self.IPQSValueLabel.setText(str(item.ipqs.score))

        nbrPositive = item.virustotal_analysis.nbrPositive
        if nbrPositive != "":
            if int(nbrPositive) > 0:
                self.virustotalValueLabel.setStyleSheet("color: #FF0000")
            else: 
                self.virustotalValueLabel.setStyleSheet("color: #000000")
            self.virustotalJsonModel.load(item.virustotal_analysis.response)
            self.virustotalCollapsableTreeView.treeView.setModel(self.virustotalJsonModel)
            self.virustotalCollapsableTreeView.treeView.resizeColumnToContents(0)
            self.virustotalCollapsableTreeView.setVisible(True)
        else:
            self.virustotalCollapsableTreeView.setVisible(False)
        self.virustotalValueLabel.setText(str(nbrPositive))
        

        self.nbrArchivesLabel.setText(str(item.waybackAnalysis.number_archives))
        self.lastDateValueLabel.setText(item.waybackAnalysis.last_date)
        self.firstDateValueLabel.setText(item.waybackAnalysis.first_date)
        self.archivesLinkValueLabel.setText("<a href=\"{}\">'{}'</a>".format(item.waybackAnalysis.wayback_url,item.waybackAnalysis.wayback_url))

        self.whoisJsonModel.load(item.whois_analysis.response)
        self.whoisCollapsableTreeView.treeView.setModel(self.whoisJsonModel)
        self.whoisCollapsableTreeView.treeView.resizeColumnToContents(0)


        self.nextButton.setDisabled(False)
        self.previousButton.setDisabled(False)
        if self.index >= (len(self.domainList)-1):
            self.nextButton.setDisabled(True)
        if self.index <= 0:
            self.previousButton.setDisabled(True)

    def startAnalysis(self) -> None:
        """This function is called at window's creation and starts a thread for domains analysis. 
        Once all domains are analysed the results are displayed one by one in the window thanks to :func:`updateUI`.
        """
        if(len(self.domainList) > 0):
            self.index = 0
            self.thread = QThread()
            self.worker = thread_analysis.Worker(self.domainList)
            self.worker.moveToThread(self.thread)

            self.thread.started.connect(self.worker.run)
            self.worker.output.connect(self.getOutput)
            self.worker.advancement.connect(self.progressBar.setValue)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)
            
            self.thread.start()

        else:
            QtWidgets.QMessageBox.critical(None, "Error", "No new domains were found")
            QTimer.singleShot(1, self.destroy)
            #FIXME Maybe destroy is too much but close doesn't always work

    def generateReport(self) -> None:
        if self.stakeholderLineEdit.text() == "" or self.UUIDLineEdit.text() == "":
            reply = QtWidgets.QMessageBox.question(self,"Missing parameters","One or more fields are empty. Do you want to generate a report anyway ?", buttons = QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Yes, defaultButton=QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.No:
                return
        template = report_generator.load_template()
        screenshotPath = self.output[self.domainList[self.index]].imagePath
        jsonData = self.output[self.domainList[self.index]].whois_analysis.response
        #print(json.dumps(jsonData, indent=4))

        def keySearchJSON(key, dic):
            if isinstance(dic, dict):
                for k in dic.keys():
                    if k == "audit":
                        continue
                    elif k == key:
                        return str(dic[k])
                    elif isinstance(dic[k], dict):
                        if (result := keySearchJSON(key, dic[k])) != "":
                            return result
            elif isinstance(dic, list):
                for e in dic:
                    if (result:= keySearchJSON(key, e)) != "":
                        return result
            return ""

        whoisJson = ""
        whoisJson += "createdDate: " + keySearchJSON("createdDate", jsonData) + "\n"
        whoisJson += "updatedDate: " + keySearchJSON("updatedDate", jsonData) + "\n"
        whoisJson += "expiresDate: " + keySearchJSON("expiresDate", jsonData) + "\n"
        whoisJson += "registrarName: " + keySearchJSON("registrarName", jsonData) + "\n"
        whoisJson += "registrarIANAID: " + keySearchJSON("registrarIANAID", jsonData) + "\n"
        whoisJson += "whoisServer: " + keySearchJSON("whoisServer", jsonData) + "\n"
        whoisJson = whoisJson.replace("}","")
        whoisJson = whoisJson.replace("{","")
        whoisJson = whoisJson.replace("\"","")
        whoisJson = whoisJson.replace("\\n","\n")
        path = report_generator.generate_report(report_generator.gen_context(str(screenshotPath),template,Stakeholder=self.stakeholderLineEdit.text(),Fraudulent_website=self.domainList[self.index],UUID=self.UUIDLineEdit.text(),whoisJson=whoisJson),template)
        self.generatedReports.append(self.domainList[self.index])
        QtWidgets.QMessageBox.information(None,"Report saved", "A report was saved : {}".format(os.fspath(path)))
    
    