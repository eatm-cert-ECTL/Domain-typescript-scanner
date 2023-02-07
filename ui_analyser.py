# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'analyserjdctha.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from collapsableTreeview import CollapsableTreeView


class Ui_Analyser(object):
    def setupUi(self, Analyser):
        if not Analyser.objectName():
            Analyser.setObjectName(u"Analyser")
        Analyser.resize(1413, 788)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Analyser.sizePolicy().hasHeightForWidth())
        Analyser.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(Analyser)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.scrollArea = QScrollArea(self.splitter)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(600, 0))
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 689, 423))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.domainNameLabel = QLabel(self.scrollAreaWidgetContents)
        self.domainNameLabel.setObjectName(u"domainNameLabel")
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.domainNameLabel.setFont(font)
        self.domainNameLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.domainNameLabel)

        self.whoisLabel = QLabel(self.scrollAreaWidgetContents)
        self.whoisLabel.setObjectName(u"whoisLabel")

        self.verticalLayout_4.addWidget(self.whoisLabel)

        self.whoisCollapsableTreeView = CollapsableTreeView(self.scrollAreaWidgetContents)
        self.whoisCollapsableTreeView.setObjectName(u"whoisCollapsableTreeView")

        self.verticalLayout_4.addWidget(self.whoisCollapsableTreeView)

        self.IPQSLayout = QHBoxLayout()
        self.IPQSLayout.setObjectName(u"IPQSLayout")
        self.IPQSLabel = QLabel(self.scrollAreaWidgetContents)
        self.IPQSLabel.setObjectName(u"IPQSLabel")

        self.IPQSLayout.addWidget(self.IPQSLabel)

        self.IPQSValueLabel = QLabel(self.scrollAreaWidgetContents)
        self.IPQSValueLabel.setObjectName(u"IPQSValueLabel")
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.IPQSValueLabel.setFont(font1)

        self.IPQSLayout.addWidget(self.IPQSValueLabel)


        self.verticalLayout_4.addLayout(self.IPQSLayout)

        self.IPQSCollapsableTreeView = CollapsableTreeView(self.scrollAreaWidgetContents)
        self.IPQSCollapsableTreeView.setObjectName(u"IPQSCollapsableTreeView")

        self.verticalLayout_4.addWidget(self.IPQSCollapsableTreeView)

        self.virustotalLayout = QHBoxLayout()
        self.virustotalLayout.setObjectName(u"virustotalLayout")
        self.virustotalLabel = QLabel(self.scrollAreaWidgetContents)
        self.virustotalLabel.setObjectName(u"virustotalLabel")

        self.virustotalLayout.addWidget(self.virustotalLabel)

        self.virustotalValueLabel = QLabel(self.scrollAreaWidgetContents)
        self.virustotalValueLabel.setObjectName(u"virustotalValueLabel")
        self.virustotalValueLabel.setFont(font1)

        self.virustotalLayout.addWidget(self.virustotalValueLabel)


        self.verticalLayout_4.addLayout(self.virustotalLayout)

        self.virustotalCollapsableTreeView = CollapsableTreeView(self.scrollAreaWidgetContents)
        self.virustotalCollapsableTreeView.setObjectName(u"virustotalCollapsableTreeView")

        self.verticalLayout_4.addWidget(self.virustotalCollapsableTreeView)

        self.waybackMachineLayout = QHBoxLayout()
        self.waybackMachineLayout.setObjectName(u"waybackMachineLayout")
        self.waybackMachineLabel = QLabel(self.scrollAreaWidgetContents)
        self.waybackMachineLabel.setObjectName(u"waybackMachineLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.waybackMachineLabel.sizePolicy().hasHeightForWidth())
        self.waybackMachineLabel.setSizePolicy(sizePolicy1)

        self.waybackMachineLayout.addWidget(self.waybackMachineLabel)

        self.nbrArchivesLabel = QLabel(self.scrollAreaWidgetContents)
        self.nbrArchivesLabel.setObjectName(u"nbrArchivesLabel")
        self.nbrArchivesLabel.setFont(font1)

        self.waybackMachineLayout.addWidget(self.nbrArchivesLabel)


        self.verticalLayout_4.addLayout(self.waybackMachineLayout)

        self.waybackMachineLayout2 = QHBoxLayout()
        self.waybackMachineLayout2.setObjectName(u"waybackMachineLayout2")
        self.firstDateLabel = QLabel(self.scrollAreaWidgetContents)
        self.firstDateLabel.setObjectName(u"firstDateLabel")
        sizePolicy1.setHeightForWidth(self.firstDateLabel.sizePolicy().hasHeightForWidth())
        self.firstDateLabel.setSizePolicy(sizePolicy1)

        self.waybackMachineLayout2.addWidget(self.firstDateLabel)

        self.firstDateValueLabel = QLabel(self.scrollAreaWidgetContents)
        self.firstDateValueLabel.setObjectName(u"firstDateValueLabel")
        self.firstDateValueLabel.setFont(font1)

        self.waybackMachineLayout2.addWidget(self.firstDateValueLabel)

        self.lastDateLabel = QLabel(self.scrollAreaWidgetContents)
        self.lastDateLabel.setObjectName(u"lastDateLabel")
        sizePolicy1.setHeightForWidth(self.lastDateLabel.sizePolicy().hasHeightForWidth())
        self.lastDateLabel.setSizePolicy(sizePolicy1)

        self.waybackMachineLayout2.addWidget(self.lastDateLabel)

        self.lastDateValueLabel = QLabel(self.scrollAreaWidgetContents)
        self.lastDateValueLabel.setObjectName(u"lastDateValueLabel")
        self.lastDateValueLabel.setFont(font1)

        self.waybackMachineLayout2.addWidget(self.lastDateValueLabel)


        self.verticalLayout_4.addLayout(self.waybackMachineLayout2)

        self.waybackMachineLayout3 = QHBoxLayout()
        self.waybackMachineLayout3.setObjectName(u"waybackMachineLayout3")
        self.archivesLinkLabel = QLabel(self.scrollAreaWidgetContents)
        self.archivesLinkLabel.setObjectName(u"archivesLinkLabel")
        sizePolicy1.setHeightForWidth(self.archivesLinkLabel.sizePolicy().hasHeightForWidth())
        self.archivesLinkLabel.setSizePolicy(sizePolicy1)

        self.waybackMachineLayout3.addWidget(self.archivesLinkLabel)

        self.archivesLinkValueLabel = QLabel(self.scrollAreaWidgetContents)
        self.archivesLinkValueLabel.setObjectName(u"archivesLinkValueLabel")
        self.archivesLinkValueLabel.setFont(font1)
        self.archivesLinkValueLabel.setOpenExternalLinks(True)

        self.waybackMachineLayout3.addWidget(self.archivesLinkValueLabel)


        self.verticalLayout_4.addLayout(self.waybackMachineLayout3)

        self.blackWhitelistLayout = QHBoxLayout()
        self.blackWhitelistLayout.setObjectName(u"blackWhitelistLayout")
        self.blacklistButton = QPushButton(self.scrollAreaWidgetContents)
        self.blacklistButton.setObjectName(u"blacklistButton")

        self.blackWhitelistLayout.addWidget(self.blacklistButton)

        self.whitelistButton = QPushButton(self.scrollAreaWidgetContents)
        self.whitelistButton.setObjectName(u"whitelistButton")

        self.blackWhitelistLayout.addWidget(self.whitelistButton)


        self.verticalLayout_4.addLayout(self.blackWhitelistLayout)

        self.reportLayout = QHBoxLayout()
        self.reportLayout.setObjectName(u"reportLayout")
        self.stakeholderLabel = QLabel(self.scrollAreaWidgetContents)
        self.stakeholderLabel.setObjectName(u"stakeholderLabel")

        self.reportLayout.addWidget(self.stakeholderLabel)

        self.stakeholderLineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.stakeholderLineEdit.setObjectName(u"stakeholderLineEdit")

        self.reportLayout.addWidget(self.stakeholderLineEdit)

        self.UUIDLabel = QLabel(self.scrollAreaWidgetContents)
        self.UUIDLabel.setObjectName(u"UUIDLabel")

        self.reportLayout.addWidget(self.UUIDLabel)

        self.UUIDLineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.UUIDLineEdit.setObjectName(u"UUIDLineEdit")

        self.reportLayout.addWidget(self.UUIDLineEdit)


        self.verticalLayout_4.addLayout(self.reportLayout)

        self.generateReportButton = QPushButton(self.scrollAreaWidgetContents)
        self.generateReportButton.setObjectName(u"generateReportButton")

        self.verticalLayout_4.addWidget(self.generateReportButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.splitter.addWidget(self.scrollArea)
        self.scrollArea_2 = QScrollArea(self.splitter)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy2)
        self.scrollArea_2.setMinimumSize(QSize(700, 0))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidget = QWidget()
        self.scrollAreaWidget.setObjectName(u"scrollAreaWidget")
        self.scrollAreaWidget.setEnabled(True)
        self.scrollAreaWidget.setGeometry(QRect(0, 0, 27, 423))
        sizePolicy1.setHeightForWidth(self.scrollAreaWidget.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidget.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.imageArea = QLabel(self.scrollAreaWidget)
        self.imageArea.setObjectName(u"imageArea")
        sizePolicy1.setHeightForWidth(self.imageArea.sizePolicy().hasHeightForWidth())
        self.imageArea.setSizePolicy(sizePolicy1)
        self.imageArea.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.imageArea)

        self.scrollArea_2.setWidget(self.scrollAreaWidget)
        self.splitter.addWidget(self.scrollArea_2)

        self.verticalLayout.addWidget(self.splitter)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.previousButton = QPushButton(self.centralwidget)
        self.previousButton.setObjectName(u"previousButton")

        self.horizontalLayout_4.addWidget(self.previousButton)

        self.nextButton = QPushButton(self.centralwidget)
        self.nextButton.setObjectName(u"nextButton")

        self.horizontalLayout_4.addWidget(self.nextButton)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.horizontalLayout.addWidget(self.progressBar)

        self.countLabel = QLabel(self.centralwidget)
        self.countLabel.setObjectName(u"countLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.countLabel.sizePolicy().hasHeightForWidth())
        self.countLabel.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.countLabel)


        self.verticalLayout.addLayout(self.horizontalLayout)

        Analyser.setCentralWidget(self.centralwidget)

        self.retranslateUi(Analyser)

        QMetaObject.connectSlotsByName(Analyser)
    # setupUi

    def retranslateUi(self, Analyser):
        Analyser.setWindowTitle(QCoreApplication.translate("Analyser", u"Analyser", None))
        self.domainNameLabel.setText("")
        self.whoisLabel.setText(QCoreApplication.translate("Analyser", u"Whois", None))
        self.IPQSLabel.setText(QCoreApplication.translate("Analyser", u"IPQS", None))
        self.IPQSValueLabel.setText("")
        self.virustotalLabel.setText(QCoreApplication.translate("Analyser", u"Virustotal", None))
        self.virustotalValueLabel.setText("")
        self.waybackMachineLabel.setText(QCoreApplication.translate("Analyser", u"Wayback machine archives:", None))
        self.nbrArchivesLabel.setText("")
        self.firstDateLabel.setText(QCoreApplication.translate("Analyser", u"First date:", None))
        self.firstDateValueLabel.setText("")
        self.lastDateLabel.setText(QCoreApplication.translate("Analyser", u"Last date:", None))
        self.lastDateValueLabel.setText("")
        self.archivesLinkLabel.setText(QCoreApplication.translate("Analyser", u"Archives link:", None))
        self.archivesLinkValueLabel.setText("")
        self.blacklistButton.setText(QCoreApplication.translate("Analyser", u"Blacklist", None))
        self.whitelistButton.setText(QCoreApplication.translate("Analyser", u"Whitelist", None))
        self.stakeholderLabel.setText(QCoreApplication.translate("Analyser", u"Stakeholder :", None))
        self.UUIDLabel.setText(QCoreApplication.translate("Analyser", u"UUID :", None))
        self.generateReportButton.setText(QCoreApplication.translate("Analyser", u"Generate report", None))
        self.imageArea.setText("")
        self.previousButton.setText(QCoreApplication.translate("Analyser", u"Previous", None))
        self.nextButton.setText(QCoreApplication.translate("Analyser", u"Next", None))
        self.countLabel.setText(QCoreApplication.translate("Analyser", u"0/0", None))
    # retranslateUi

