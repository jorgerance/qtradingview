# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(673, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(600, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/base/logo"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks|QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks|QtWidgets.QMainWindow.ForceTabbedDocks|QtWidgets.QMainWindow.GroupedDragging|QtWidgets.QMainWindow.VerticalTabs)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        MainWindow.setProperty("currentExchange", "")
        MainWindow.setProperty("currentMarket", "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.webview = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webview.setObjectName("webview")
        self.horizontalLayout.addWidget(self.webview)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setOrientation(QtCore.Qt.Horizontal)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionMarkets = QtWidgets.QAction(MainWindow)
        self.actionMarkets.setCheckable(True)
        self.actionMarkets.setChecked(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/actions/markets"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMarkets.setIcon(icon1)
        self.actionMarkets.setObjectName("actionMarkets")
        self.actionSalir = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/actions/exit"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSalir.setIcon(icon2)
        self.actionSalir.setObjectName("actionSalir")
        self.actionPantalla_completa = QtWidgets.QAction(MainWindow)
        self.actionPantalla_completa.setCheckable(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/actions/screen"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPantalla_completa.setIcon(icon3)
        self.actionPantalla_completa.setObjectName("actionPantalla_completa")
        self.actionInfo = QtWidgets.QAction(MainWindow)
        self.actionInfo.setCheckable(True)
        self.actionInfo.setObjectName("actionInfo")
        self.actionDebug = QtWidgets.QAction(MainWindow)
        self.actionDebug.setCheckable(True)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/actions/debug"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDebug.setIcon(icon4)
        self.actionDebug.setObjectName("actionDebug")
        self.actionAlarms = QtWidgets.QAction(MainWindow)
        self.actionAlarms.setCheckable(True)
        self.actionAlarms.setEnabled(True)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/actions/alarms"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAlarms.setIcon(icon5)
        self.actionAlarms.setObjectName("actionAlarms")
        self.actionConfigurar = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/actions/settings"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConfigurar.setIcon(icon6)
        self.actionConfigurar.setObjectName("actionConfigurar")
        self.toolBar.addAction(self.actionMarkets)
        self.toolBar.addAction(self.actionAlarms)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPantalla_completa)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionConfigurar)
        self.toolBar.addAction(self.actionDebug)
        self.toolBar.addAction(self.actionSalir)

        self.retranslateUi(MainWindow)
        self.actionSalir.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QTradingview"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "Toolbar"))
        self.actionMarkets.setText(_translate("MainWindow", "Markets"))
        self.actionMarkets.setToolTip(_translate("MainWindow", "Markets (F1)"))
        self.actionMarkets.setStatusTip(_translate("MainWindow", "Show/hide markets panel (F1)"))
        self.actionMarkets.setShortcut(_translate("MainWindow", "F1"))
        self.actionSalir.setText(_translate("MainWindow", "Quit"))
        self.actionSalir.setToolTip(_translate("MainWindow", "Quit (Control+Q)"))
        self.actionSalir.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionPantalla_completa.setText(_translate("MainWindow", "Full Screen"))
        self.actionPantalla_completa.setToolTip(_translate("MainWindow", "Full Screen (F11)"))
        self.actionPantalla_completa.setStatusTip(_translate("MainWindow", "Turn on/off full screen (F11)"))
        self.actionPantalla_completa.setShortcut(_translate("MainWindow", "F11"))
        self.actionInfo.setText(_translate("MainWindow", "Info"))
        self.actionDebug.setText(_translate("MainWindow", "Debug"))
        self.actionDebug.setToolTip(_translate("MainWindow", "Debug (F10)"))
        self.actionDebug.setStatusTip(_translate("MainWindow", "Show/hide debug panel (F10)"))
        self.actionDebug.setShortcut(_translate("MainWindow", "F10"))
        self.actionAlarms.setText(_translate("MainWindow", "Alarms"))
        self.actionAlarms.setToolTip(_translate("MainWindow", "Alarms (F2)"))
        self.actionAlarms.setStatusTip(_translate("MainWindow", "Show/hide alarms panel (F2)"))
        self.actionAlarms.setShortcut(_translate("MainWindow", "F2"))
        self.actionConfigurar.setText(_translate("MainWindow", "Settings"))
        self.actionConfigurar.setToolTip(_translate("MainWindow", "Settings (F9)"))
        self.actionConfigurar.setStatusTip(_translate("MainWindow", "Show settings window (F9)"))
        self.actionConfigurar.setShortcut(_translate("MainWindow", "F9"))
from PyQt5 import QtWebEngineWidgets
import iconos_rc
