# Form implementation generated from reading ui file 'banve.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 50, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(120, 160, 491, 101))
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 47, 13))
        self.label_2.setObjectName("label_2")
        self.name = QtWidgets.QLineEdit(parent=self.groupBox)
        self.name.setGeometry(QtCore.QRect(70, 30, 113, 20))
        self.name.setObjectName("name")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 51, 20))
        self.label_3.setObjectName("label_3")
        self.sex = QtWidgets.QComboBox(parent=self.groupBox)
        self.sex.setGeometry(QtCore.QRect(84, 70, 69, 22))
        self.sex.setObjectName("sex")
        self.sex.addItem("")
        self.sex.addItem("")
        self.sex.addItem("")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(120, 290, 501, 131))
        self.groupBox_2.setObjectName("groupBox_2")
        self.cafe = QtWidgets.QCheckBox(parent=self.groupBox_2)
        self.cafe.setGeometry(QtCore.QRect(10, 40, 70, 17))
        self.cafe.setObjectName("cafe")
        self.snack = QtWidgets.QCheckBox(parent=self.groupBox_2)
        self.snack.setGeometry(QtCore.QRect(200, 40, 70, 17))
        self.snack.setObjectName("snack")
        self.nguoi_lon = QtWidgets.QSpinBox(parent=self.groupBox_2)
        self.nguoi_lon.setGeometry(QtCore.QRect(80, 80, 42, 22))
        self.nguoi_lon.setObjectName("nguoi_lon")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(200, 80, 47, 13))
        self.label_5.setObjectName("label_5")
        self.tre_em = QtWidgets.QSpinBox(parent=self.groupBox_2)
        self.tre_em.setGeometry(QtCore.QRect(250, 80, 42, 22))
        self.tre_em.setObjectName("tre_em")
        self.tien_tra_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.tien_tra_2.setGeometry(QtCore.QRect(220, 440, 75, 23))
        self.tien_tra_2.setObjectName("tien_tra_2")
        self.show_tien_tra = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.show_tien_tra.setGeometry(QtCore.QRect(310, 440, 113, 20))
        self.show_tien_tra.setObjectName("show_tien_tra")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(450, 450, 47, 13))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.tien_tra_2.clicked.connect(self.tientra)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "UNG DUNG BAN VE"))
        self.groupBox.setTitle(_translate("MainWindow", "THONG TIN KHACH HANG"))
        self.label_2.setText(_translate("MainWindow", "HO TEN"))
        self.label_3.setText(_translate("MainWindow", "GIOI TINH"))
        self.sex.setItemText(0, _translate("MainWindow", "Nam"))
        self.sex.setItemText(1, _translate("MainWindow", "Nu"))
        self.sex.setItemText(2, _translate("MainWindow", "Gioi tinh thu 3"))
        self.groupBox_2.setTitle(_translate("MainWindow", "DICH VU"))
        self.cafe.setText(_translate("MainWindow", "CAFE"))
        self.snack.setText(_translate("MainWindow", "SNACK"))
        self.label_4.setText(_translate("MainWindow", "NGUOI LON"))
        self.label_5.setText(_translate("MainWindow", "TRE EM"))
        self.tien_tra_2.setText(_translate("MainWindow", "TIEN TRA"))
        self.label_6.setText(_translate("MainWindow", "VND"))

    def tientra(self):
        price = {
            "cafe" : 100,
            "snack": 5,
            "nguoi_lon": 200,
            "tre_em": 50
        }

        price_cafe = 0
        if self.cafe.checkState() != 0:
            price_cafe = price["cafe"]
        price_snack = 0
        if self.snack.checkState() != 0:
            price_snack = price["snack"]
        price_nguoi_lon = int(self.nguoi_lon.text()) * price["nguoi_lon"]
        price_tre_em = int(self.tre_em.text()) * price["tre_em"]

        sumprice = price_cafe + price_snack + price_nguoi_lon + price_tre_em
        self.show_tien_tra.setText(str(sumprice))

        msg=QtWidgets.QMessageBox()
        msg.setInformativeText(f'Tong tien phai tra:', sumprice)
        msg.exec()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())