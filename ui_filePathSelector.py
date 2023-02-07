# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'filePathSelectorlPHasu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_filePathSelector(object):
    def setupUi(self, filePathSelector):
        if not filePathSelector.objectName():
            filePathSelector.setObjectName(u"filePathSelector")
        filePathSelector.resize(415, 37)
        filePathSelector.setMinimumSize(QSize(415, 37))
        self.pushButton = QPushButton(filePathSelector)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(320, 5, 90, 27))
        self.textEdit = QTextEdit(filePathSelector)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 3, 301, 31))

        self.retranslateUi(filePathSelector)

        QMetaObject.connectSlotsByName(filePathSelector)
    # setupUi

    def retranslateUi(self, filePathSelector):
        filePathSelector.setWindowTitle(QCoreApplication.translate("filePathSelector", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("filePathSelector", u"Browse...", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("filePathSelector", u"Enter file path", None))
    # retranslateUi

