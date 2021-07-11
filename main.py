import sys
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, QtCore
from Ui_test import Ui_Form
from Ui_config import Ui_Config_Form
from Ui_pannel2 import Ui_Pannel2

class MyMainForm(QtWidgets.QWidget, Ui_Form):
    #頁面dict
    dict_ = {
        "pushButton" : [0, "config_form"],
        "yylifo_pushButton" : [1, "Pannel2"]
    }
    def __init__(self):
        super(MyMainForm,self).__init__()
        self.setupUi(self)
        self.qsl = QtWidgets.QStackedLayout(self.frame2)

        #頁面Instance
        self.config_form = Ui_Config_Form()
        self.Pannel2 = Ui_Pannel2()

        # 多个页面的绑定
        for k, v in self.dict_.items():
            exec('self.w{} = QtWidgets.QWidget()'.format(v[0]))
            eval('self.{}.setupUi(self.w{})'.format(v[1],v[0]))
            eval('self.qsl.addWidget(self.w{})'.format(v[0]))
            eval('self.{}.clicked.connect(self.show_page)'.format(k))
        self.listWidget.currentRowChanged.connect(self.show_page2)
        self.config_form.file_pushButton.clicked.connect(self.openfile)
        self.config_form.clear_pushButton.clicked.connect(self.clear)
        self.config_form.clear_pushButton.clicked.connect(self.showdialog)

    def showdialog(self):
        AAA.show()
        AAA.setWindowModality(QtCore.Qt.ApplicationModal)
    def show_page2(self):
        self.qsl.setCurrentIndex(self.listWidget.currentRow())

    #顯示頁面
    def show_page(self):
        index = self.dict_[self.sender().objectName()][0]
        self.qsl.setCurrentIndex(index)

    def openfile(self):
        get_filename_path = QtWidgets.QFileDialog.getOpenFileName(self, "選取設定檔", ".")
        #self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        
        '''
        self.tableWidget.setItem(0, 1, item)
        item = self.tableWidget.item(0,1)
        item.setText("GGGGG")

        self.tableWidget.setVerticalHeaderItem(2,item)
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText("welcome")
        #self.tableWidget.clearContents()
        '''
        
    def clear(self):
        self.config_form.tableWidget.clearContents()
class Config_Form(QtWidgets.QWidget, Ui_Config_Form):
    def __init__(self):
        super(Config_Form,self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myWin = MyMainForm()
    AAA = Config_Form()
    myWin.show()
    sys.exit(app.exec_())