# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\kalio\.spyder-py3\Program\PYQT\pannel2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Pannel2(object):
    def setupUi(self, Pannel2):
        Pannel2.setObjectName("Pannel2")
        Pannel2.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Pannel2)
        self.pushButton.setGeometry(QtCore.QRect(40, 80, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Pannel2)
        QtCore.QMetaObject.connectSlotsByName(Pannel2)

    def retranslateUi(self, Pannel2):
        _translate = QtCore.QCoreApplication.translate
        Pannel2.setWindowTitle(_translate("Pannel2", "Form"))
        self.pushButton.setText(_translate("Pannel2", "PushButton"))