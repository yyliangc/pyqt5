# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\kalio\.spyder-py3\Program\PYQT\config.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Config_Form(object):
    def setupUi(self, Config_Form):
        Config_Form.setObjectName("Config_Form")
        Config_Form.resize(349, 310)
        self.widget = QtWidgets.QWidget(Config_Form)
        self.widget.setGeometry(QtCore.QRect(10, 1, 341, 251))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.file_pushButton = QtWidgets.QPushButton(self.widget)
        self.file_pushButton.setObjectName("file_pushButton")
        self.gridLayout.addWidget(self.file_pushButton, 0, 0, 1, 1)
        self.clear_pushButton = QtWidgets.QPushButton(self.widget)
        self.clear_pushButton.setObjectName("clear_pushButton")
        self.gridLayout.addWidget(self.clear_pushButton, 2, 0, 1, 1)
        self.config_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.config_lineEdit.setObjectName("config_lineEdit")
        self.gridLayout.addWidget(self.config_lineEdit, 0, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 2)

        self.retranslateUi(Config_Form)
        QtCore.QMetaObject.connectSlotsByName(Config_Form)

    def retranslateUi(self, Config_Form):
        _translate = QtCore.QCoreApplication.translate
        Config_Form.setWindowTitle(_translate("Config_Form", "Form"))
        self.file_pushButton.setText(_translate("Config_Form", "select"))
        self.clear_pushButton.setText(_translate("Config_Form", "clear"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Config_Form", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Config_Form", "2"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Config_Form", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Config_Form", "value"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Config_Form", "hIIII"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
