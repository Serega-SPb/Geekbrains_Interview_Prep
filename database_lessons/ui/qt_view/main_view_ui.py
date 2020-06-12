# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Repositories\Geekbrains_Interview_Prep\database_lessons\pyqt_ui\main_view.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.dbPathLnEd = QtWidgets.QLineEdit(self.centralwidget)
        self.dbPathLnEd.setEnabled(True)
        self.dbPathLnEd.setText("")
        self.dbPathLnEd.setReadOnly(True)
        self.dbPathLnEd.setObjectName("dbPathLnEd")
        self.gridLayout.addWidget(self.dbPathLnEd, 0, 1, 1, 1)
        self.opeDbBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.opeDbBtn.sizePolicy().hasHeightForWidth())
        self.opeDbBtn.setSizePolicy(sizePolicy)
        self.opeDbBtn.setMinimumSize(QtCore.QSize(25, 0))
        self.opeDbBtn.setMaximumSize(QtCore.QSize(35, 16777215))
        self.opeDbBtn.setObjectName("opeDbBtn")
        self.gridLayout.addWidget(self.opeDbBtn, 0, 2, 1, 1)
        self.dbTabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.dbTabWidget.setObjectName("dbTabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.dbTabWidget.addTab(self.tab, "")
        self.gridLayout.addWidget(self.dbTabWidget, 1, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.dbTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Db path"))
        self.opeDbBtn.setText(_translate("MainWindow", "..."))
        self.dbTabWidget.setTabText(self.dbTabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
