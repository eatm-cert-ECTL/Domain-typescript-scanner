# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainvLzynq.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from filePathSelector import FilePathSelector


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1438, 806)
        MainWindow.setMouseTracking(False)
        icon = QIcon()
        icon.addFile(u"../TYDEA_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.LeftVerticalLayout = QVBoxLayout(self.layoutWidget)
        self.LeftVerticalLayout.setObjectName(u"LeftVerticalLayout")
        self.LeftVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.reverseWhoisGenerationGroupBox = QGroupBox(self.layoutWidget)
        self.reverseWhoisGenerationGroupBox.setObjectName(u"reverseWhoisGenerationGroupBox")
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.reverseWhoisGenerationGroupBox.setFont(font)
        self.gridLayout_2 = QGridLayout(self.reverseWhoisGenerationGroupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.useVirustotalCheckBox = QCheckBox(self.reverseWhoisGenerationGroupBox)
        self.useVirustotalCheckBox.setObjectName(u"useVirustotalCheckBox")

        self.gridLayout_2.addWidget(self.useVirustotalCheckBox, 3, 1, 1, 1)

        self.useVirustotalLabel = QLabel(self.reverseWhoisGenerationGroupBox)
        self.useVirustotalLabel.setObjectName(u"useVirustotalLabel")

        self.gridLayout_2.addWidget(self.useVirustotalLabel, 3, 0, 1, 1)

        self.keywordsListLabel = QLabel(self.reverseWhoisGenerationGroupBox)
        self.keywordsListLabel.setObjectName(u"keywordsListLabel")

        self.gridLayout_2.addWidget(self.keywordsListLabel, 0, 0, 1, 1)

        self.keywordsListSelectorWidget = FilePathSelector(self.reverseWhoisGenerationGroupBox)
        self.keywordsListSelectorWidget.setObjectName(u"keywordsListSelectorWidget")

        self.gridLayout_2.addWidget(self.keywordsListSelectorWidget, 0, 1, 1, 1)

        self.reverseWhoisGenerateButton = QPushButton(self.reverseWhoisGenerationGroupBox)
        self.reverseWhoisGenerateButton.setObjectName(u"reverseWhoisGenerateButton")

        self.gridLayout_2.addWidget(self.reverseWhoisGenerateButton, 4, 0, 1, 2)

        self.label = QLabel(self.reverseWhoisGenerationGroupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.reverseWhoisCalendar = QCalendarWidget(self.reverseWhoisGenerationGroupBox)
        self.reverseWhoisCalendar.setObjectName(u"reverseWhoisCalendar")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reverseWhoisCalendar.sizePolicy().hasHeightForWidth())
        self.reverseWhoisCalendar.setSizePolicy(sizePolicy)
        self.reverseWhoisCalendar.setFirstDayOfWeek(Qt.Monday)
        self.reverseWhoisCalendar.setGridVisible(False)
        self.reverseWhoisCalendar.setSelectionMode(QCalendarWidget.SingleSelection)
        self.reverseWhoisCalendar.setHorizontalHeaderFormat(QCalendarWidget.ShortDayNames)
        self.reverseWhoisCalendar.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.reverseWhoisCalendar.setNavigationBarVisible(True)
        self.reverseWhoisCalendar.setDateEditEnabled(True)

        self.gridLayout_2.addWidget(self.reverseWhoisCalendar, 2, 0, 1, 1)

        self.label_2 = QLabel(self.reverseWhoisGenerationGroupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 1)

        self.endCalendarWidget = QCalendarWidget(self.reverseWhoisGenerationGroupBox)
        self.endCalendarWidget.setObjectName(u"endCalendarWidget")
        sizePolicy.setHeightForWidth(self.endCalendarWidget.sizePolicy().hasHeightForWidth())
        self.endCalendarWidget.setSizePolicy(sizePolicy)
        self.endCalendarWidget.setFirstDayOfWeek(Qt.Monday)
        self.endCalendarWidget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)

        self.gridLayout_2.addWidget(self.endCalendarWidget, 2, 1, 1, 1)


        self.LeftVerticalLayout.addWidget(self.reverseWhoisGenerationGroupBox)

        self.typosquattingGroupBox = QGroupBox(self.layoutWidget)
        self.typosquattingGroupBox.setObjectName(u"typosquattingGroupBox")
        self.typosquattingGroupBox.setFont(font)
        self.gridLayout = QGridLayout(self.typosquattingGroupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.TLDCheckBox = QCheckBox(self.typosquattingGroupBox)
        self.TLDCheckBox.setObjectName(u"TLDCheckBox")
        self.TLDCheckBox.setChecked(False)

        self.gridLayout.addWidget(self.TLDCheckBox, 2, 1, 1, 1)

        self.dnstwitstCheckBox = QCheckBox(self.typosquattingGroupBox)
        self.dnstwitstCheckBox.setObjectName(u"dnstwitstCheckBox")
        self.dnstwitstCheckBox.setChecked(True)

        self.gridLayout.addWidget(self.dnstwitstCheckBox, 1, 1, 1, 1)

        self.domains = QLineEdit(self.typosquattingGroupBox)
        self.domains.setObjectName(u"domains")

        self.gridLayout.addWidget(self.domains, 0, 2, 1, 1)

        self.urlcrazyLabel = QLabel(self.typosquattingGroupBox)
        self.urlcrazyLabel.setObjectName(u"urlcrazyLabel")

        self.gridLayout.addWidget(self.urlcrazyLabel, 3, 0, 1, 1)

        self.urlcrazyCheckBox = QCheckBox(self.typosquattingGroupBox)
        self.urlcrazyCheckBox.setObjectName(u"urlcrazyCheckBox")
        self.urlcrazyCheckBox.setEnabled(True)
        self.urlcrazyCheckBox.setChecked(True)

        self.gridLayout.addWidget(self.urlcrazyCheckBox, 3, 1, 1, 1)

        self.userFunctionsLabel = QLabel(self.typosquattingGroupBox)
        self.userFunctionsLabel.setObjectName(u"userFunctionsLabel")

        self.gridLayout.addWidget(self.userFunctionsLabel, 4, 0, 1, 1)

        self.dnstwistLabel = QLabel(self.typosquattingGroupBox)
        self.dnstwistLabel.setObjectName(u"dnstwistLabel")

        self.gridLayout.addWidget(self.dnstwistLabel, 1, 0, 1, 1)

        self.enterDomainsLabel = QLabel(self.typosquattingGroupBox)
        self.enterDomainsLabel.setObjectName(u"enterDomainsLabel")

        self.gridLayout.addWidget(self.enterDomainsLabel, 0, 0, 1, 1)

        self.userFunctionsSelectorWidget = FilePathSelector(self.typosquattingGroupBox)
        self.userFunctionsSelectorWidget.setObjectName(u"userFunctionsSelectorWidget")

        self.gridLayout.addWidget(self.userFunctionsSelectorWidget, 4, 2, 1, 1)

        self.useAllTLDsLabel = QLabel(self.typosquattingGroupBox)
        self.useAllTLDsLabel.setObjectName(u"useAllTLDsLabel")

        self.gridLayout.addWidget(self.useAllTLDsLabel, 2, 0, 1, 1)

        self.typosquattingGenerateButton = QPushButton(self.typosquattingGroupBox)
        self.typosquattingGenerateButton.setObjectName(u"typosquattingGenerateButton")

        self.gridLayout.addWidget(self.typosquattingGenerateButton, 5, 0, 1, 3)


        self.LeftVerticalLayout.addWidget(self.typosquattingGroupBox)

        self.commandGroupBox = QGroupBox(self.layoutWidget)
        self.commandGroupBox.setObjectName(u"commandGroupBox")
        self.gridLayout_3 = QGridLayout(self.commandGroupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.New = QPushButton(self.commandGroupBox)
        self.New.setObjectName(u"New")

        self.gridLayout_3.addWidget(self.New, 1, 0, 1, 1)

        self.Load = QPushButton(self.commandGroupBox)
        self.Load.setObjectName(u"Load")

        self.gridLayout_3.addWidget(self.Load, 1, 1, 1, 1)

        self.adduserlistButton = QPushButton(self.commandGroupBox)
        self.adduserlistButton.setObjectName(u"adduserlistButton")

        self.gridLayout_3.addWidget(self.adduserlistButton, 2, 0, 1, 1)

        self.checkDNSButton = QPushButton(self.commandGroupBox)
        self.checkDNSButton.setObjectName(u"checkDNSButton")

        self.gridLayout_3.addWidget(self.checkDNSButton, 2, 1, 1, 1)

        self.analyseButton = QPushButton(self.commandGroupBox)
        self.analyseButton.setObjectName(u"analyseButton")

        self.gridLayout_3.addWidget(self.analyseButton, 2, 2, 1, 1)

        self.loadedDatabaseLabel = QLabel(self.commandGroupBox)
        self.loadedDatabaseLabel.setObjectName(u"loadedDatabaseLabel")

        self.gridLayout_3.addWidget(self.loadedDatabaseLabel, 1, 2, 1, 1)


        self.LeftVerticalLayout.addWidget(self.commandGroupBox)

        self.DatabaseManagmentLayout = QHBoxLayout()
        self.DatabaseManagmentLayout.setObjectName(u"DatabaseManagmentLayout")

        self.LeftVerticalLayout.addLayout(self.DatabaseManagmentLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.keywordsTableView = QTableView(self.layoutWidget)
        self.keywordsTableView.setObjectName(u"keywordsTableView")

        self.horizontalLayout_2.addWidget(self.keywordsTableView)

        self.domainsTableView = QTableView(self.layoutWidget)
        self.domainsTableView.setObjectName(u"domainsTableView")

        self.horizontalLayout_2.addWidget(self.domainsTableView)


        self.LeftVerticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.LeftVerticalLayout.addItem(self.verticalSpacer)

        self.splitter.addWidget(self.layoutWidget)
        self.verticalLayoutWidget = QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.RightVerticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.RightVerticalLayout.setObjectName(u"RightVerticalLayout")
        self.RightVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.typosquatDomainsTableView = QTableView(self.verticalLayoutWidget)
        self.typosquatDomainsTableView.setObjectName(u"typosquatDomainsTableView")

        self.RightVerticalLayout.addWidget(self.typosquatDomainsTableView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addToWhitelistButton = QPushButton(self.verticalLayoutWidget)
        self.addToWhitelistButton.setObjectName(u"addToWhitelistButton")

        self.horizontalLayout.addWidget(self.addToWhitelistButton)

        self.addToBlacklistButton = QPushButton(self.verticalLayoutWidget)
        self.addToBlacklistButton.setObjectName(u"addToBlacklistButton")

        self.horizontalLayout.addWidget(self.addToBlacklistButton)


        self.RightVerticalLayout.addLayout(self.horizontalLayout)

        self.splitter.addWidget(self.verticalLayoutWidget)

        self.verticalLayout.addWidget(self.splitter)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1438, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TYDEA Pro", None))
        self.reverseWhoisGenerationGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Reverse Whois Generation from  Keywords", None))
        self.useVirustotalCheckBox.setText("")
        self.useVirustotalLabel.setText(QCoreApplication.translate("MainWindow", u"Use Virustotal resolver", None))
        self.keywordsListLabel.setText(QCoreApplication.translate("MainWindow", u"Keywords list", None))
        self.reverseWhoisGenerateButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"From :", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"To :", None))
        self.typosquattingGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Typosquatting Generation from Domain", None))
        self.TLDCheckBox.setText("")
        self.dnstwitstCheckBox.setText("")
        self.urlcrazyLabel.setText(QCoreApplication.translate("MainWindow", u"Urlcrazy", None))
        self.urlcrazyCheckBox.setText("")
        self.userFunctionsLabel.setText(QCoreApplication.translate("MainWindow", u"User function", None))
        self.dnstwistLabel.setText(QCoreApplication.translate("MainWindow", u"Dnstwist", None))
        self.enterDomainsLabel.setText(QCoreApplication.translate("MainWindow", u"Enter domains", None))
        self.useAllTLDsLabel.setText(QCoreApplication.translate("MainWindow", u"Use all TLDs", None))
        self.typosquattingGenerateButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.commandGroupBox.setTitle("")
        self.New.setText(QCoreApplication.translate("MainWindow", u"New Database", None))
        self.Load.setText(QCoreApplication.translate("MainWindow", u"Load Database", None))
        self.adduserlistButton.setText(QCoreApplication.translate("MainWindow", u"Add Userlist", None))
        self.checkDNSButton.setText(QCoreApplication.translate("MainWindow", u"Check DNS", None))
        self.analyseButton.setText(QCoreApplication.translate("MainWindow", u"Analyse", None))
        self.loadedDatabaseLabel.setText("")
        self.addToWhitelistButton.setText(QCoreApplication.translate("MainWindow", u"Toggle whitelist", None))
        self.addToBlacklistButton.setText(QCoreApplication.translate("MainWindow", u"Toggle blacklist", None))
    # retranslateUi

