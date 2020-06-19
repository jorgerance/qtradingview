import logging

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QCoreApplication as qapp

from ui.mainwindow_Ui import Ui_MainWindow

from markets.dock import DockMarkets
from debug.dock import DockDebug, Qlogger

from .widgets import CustomWebEnginePage
from .dialog_config import DialogConfig


# ─── MAIN WINDOW ────────────────────────────────────────────────────────────────

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, ctx, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.html = None
        self.ctx = ctx
        self.config = ctx.config

        # logs
        log_mode = logging.INFO
        if self.ctx.debug:
            log_mode = logging.DEBUG
        qlog = Qlogger(self)
        logging.getLogger().addHandler(qlog)
        logging.getLogger().setLevel(log_mode)

        # webenginepage
        page = CustomWebEnginePage(self.webview)
        self.webview.setPage(page)

        # signals
        self._docks()
        self._signals()

        # carga market inicial
        self.load_chart(self.config['initial_market'], self.config['initial_exchange'])

    def _tr(self, contexto, mensaje):
        return self.ctx.tr(contexto, mensaje)

    # signal connectors
    def _signals(self):
        self.actionConfigurar.triggered.connect(self.openDialogConfigurar)
        self.actionPantalla_completa.toggled.connect(self.onActionPantallaCompleta)
        # docks actions
        self.actionMarkets.toggled['bool'].connect(self.dock_markets.setVisible)
        self.actionDebug.toggled['bool'].connect(self.dock_debug.setVisible)

    def _docks(self):
        self.setTabPosition(QtCore.Qt.AllDockWidgetAreas, QtWidgets.QTabWidget.North)
        self.dock_markets = DockMarkets(self)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dock_markets)
        self.dock_debug = DockDebug(self)
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, self.dock_debug)

    # ─── EVENTS ─────────────────────────────────────────────────────────────────────

    def openDialogConfigurar(self):
        dialog = DialogConfig(self)
        dialog.load_config(self.config)
        dialog.exec_()

    # fullscreen
    def onActionPantallaCompleta(self):
        if self.actionPantalla_completa.isChecked():
            self.showFullScreen()
        else:
            self.showNormal()
            self.showMaximized()

    # confirmacion de salida
    def closeEvent(self, event):
        result = QMessageBox.question(
            self, self._tr("mainwindow", 'Exit'), self._tr("mainwindow", "Do you want quit?"),
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.No:
            event.ignore()

    # ────────────────────────────────────────────────────────────────────────────────

    # carga un market en la pagina
    def load_chart(self, market, exchange):
        mar, ket = market.split("/")
        url = f"https://es.tradingview.com/chart/?symbol={exchange.upper()}:{mar}{ket}"
        self.webview.setUrl(QtCore.QUrl(url))
        self.currentExchange = exchange
        self.currentMarket = market