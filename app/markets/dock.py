import logging

from PyQt5 import QtWidgets, QtGui, QtCore

from ui.dock_markets_Ui import Ui_dock_markets

from .widgets import CustomItem, CustomItemDelegate
from .updater import UpdateMarkets

from models.markets import Markets
from db import db


# ─── DOCK MARKETS ───────────────────────────────────────────────────────────────

class DockMarkets(QtWidgets.QDockWidget, Ui_dock_markets):

    def __init__(self, parent):
        QtWidgets.QDockWidget.__init__(self, parent=parent)
        self.setupUi(self)
        #
        self.lista_mode = "all"
        self.updater = UpdateMarkets()
        self._load_exchanges()
        self._signals()
        #
        self.delegate = CustomItemDelegate()
        self.list_markets.setItemDelegate(self.delegate)
        self.list_markets.customContextMenuRequested.connect(self._get_context_menu)
        self.onClickAllButton(True)

    def _signals(self):
        self.combo_exchange.currentTextChanged.connect(self.onExchangeChanged)
        self.list_markets.itemDoubleClicked.connect(self.onDoubleClickMarket)
        self.edit_filtro.textEdited.connect(self.onFiltroChanged)
        self.btn_all.toggled.connect(self.onClickAllButton)
        self.btn_favorite.toggled.connect(self.onClickFavoriteButton)
        self.btn_margin.toggled.connect(self.onClickMarginButton)
        self.btn_update.clicked.connect(self.start_update_market)

    @property
    def selected_exchange(self):
        return self.combo_exchange.currentText().lower()

    @property
    def fav_is_checked(self):
        return self.btn_favorite.isChecked()

    def setVisible(self, visible):
        super().setVisible(visible)
        if visible:
            self.raise_()

    # ─── EVENTS ─────────────────────────────────────────────────────────────────────
    def start_update_market(self):
        self.updater.update_markets(self.selected_exchange)
        self.onExchangeChanged()
        self.parent().statusbar.showMessage('Updated markets', 2000)

    def onClickAllButton(self, all_actived):
        self.lista_mode = "all"
        filtro = self.edit_filtro.text()
        for index in range(self.list_markets.count()):
            item = self.list_markets.item(index)
            item.mostrar(self.lista_mode, filtro)

    def onClickFavoriteButton(self, fav_actived):
        self.lista_mode = "fav"
        filtro = self.edit_filtro.text()
        for index in range(self.list_markets.count()):
            item = self.list_markets.item(index)
            item.mostrar(self.lista_mode, filtro)

    def onClickMarginButton(self, margin_actived):
        self.lista_mode = "margin"
        filtro = self.edit_filtro.text()
        for index in range(self.list_markets.count()):
            item = self.list_markets.item(index)
            item.mostrar(self.lista_mode, filtro)

    def onFiltroChanged(self, text):
        for index in range(self.list_markets.count()):
            item = self.list_markets.item(index)
            item.mostrar(self.lista_mode, text)

    def onExchangeChanged(self):
        self.edit_filtro.clear()
        self._load_markets()

    def onDoubleClickMarket(self, item):
        self.parentWidget().load_chart(item.text(), self.selected_exchange)

    # ─── PRIVATE METHODS ────────────────────────────────────────────────────────────

    def _get_context_menu(self, position):
        item = self.list_markets.itemAt(position)
        # market = Markets.get_symbol_by_exchange(item.text(), self.selected_exchange)
        menu = QtWidgets.QMenu(self.list_markets)
        if item.is_favorite:
            favoriteAction = menu.addAction("Eliminar de favoritos")
            favoriteAction.setIcon(QtGui.QIcon(":/base/voidstar.svg"))
        else:
            favoriteAction = menu.addAction("Añadir a favoritos".encode("utf-8"))
            favoriteAction.setIcon(QtGui.QIcon(":/base/star.svg"))
        # alarmAction = menu.addAction("Crear nueva alarma")
        action = menu.exec_(self.list_markets.viewport().mapToGlobal(position))
        if action == favoriteAction:
            item.toggle_favorite()
    #     elif action == alarmAction:
    #         self._new_alarm(self.selected_exchange, item.text())

    # def _new_alarm(self, exchange, market):
    #     dialog = DialogAlarm(self)
    #     dialog.new_alarm(exchange, market)
    #     result = dialog.exec_()
    #     if result:
    #         self.parentWidget().dock_alarms.refresh_alarms()
    #         self.parentWidget().dock_alarms.raise_()

    def _load_exchanges(self):
        """ Carga la lista de exchanges en el combo,
        selecciona el definido por defecto y llama al evento de cambio """
        self.combo_exchange.clear()
        for x in self.parentWidget().config['exchanges']:
            path = f":/exchanges/{x.lower()}.png"
            self.combo_exchange.addItem(QtGui.QIcon(path), x.title())
        # initial config
        default_index = self.combo_exchange.findText(self.parentWidget().config['initial_exchange'].title())
        if default_index != -1:
            self.combo_exchange.setCurrentIndex(default_index)
        # load markets
        self.onExchangeChanged()

    def _load_markets(self):
        filtro = self.edit_filtro.text()
        self.list_markets.clear()
        for it in Markets.get_all_by_exchange(self.selected_exchange):
            nuevo = CustomItem(self.list_markets)
            nuevo.configurar(it.symbol, self.selected_exchange)
            nuevo.mostrar(self.lista_mode, filtro)

    # ─── PUBLIC METHODS ─────────────────────────────────────────────────────────────

    def clear_currentInfo(self):
        self.label_currentMarket.setText(" ")
        self.label_currentExchange.setPixmap(QtGui.QPixmap())

    def set_currentInfo(self, exchange, market):
        pixmap = QtGui.QPixmap(f":/exchanges/{exchange}.png").scaledToWidth(100)
        self.label_currentMarket.setText(market)
        self.label_currentExchange.setPixmap(pixmap)

# ────────────────────────────────────────────────────────────────────────────────
