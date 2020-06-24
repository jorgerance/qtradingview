# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/dialog_config.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogConfig(object):
    def setupUi(self, DialogConfig):
        DialogConfig.setObjectName("DialogConfig")
        DialogConfig.setWindowModality(QtCore.Qt.WindowModal)
        DialogConfig.resize(250, 463)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogConfig.sizePolicy().hasHeightForWidth())
        DialogConfig.setSizePolicy(sizePolicy)
        DialogConfig.setMinimumSize(QtCore.QSize(250, 300))
        DialogConfig.setMaximumSize(QtCore.QSize(250, 800))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/actions/actions/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogConfig.setWindowIcon(icon)
        DialogConfig.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogConfig)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(DialogConfig)
        self.label.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.combo_languages = QtWidgets.QComboBox(DialogConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_languages.sizePolicy().hasHeightForWidth())
        self.combo_languages.setSizePolicy(sizePolicy)
        self.combo_languages.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.combo_languages.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.combo_languages.setObjectName("combo_languages")
        self.combo_languages.addItem("")
        self.combo_languages.addItem("")
        self.horizontalLayout.addWidget(self.combo_languages)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(DialogConfig)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(DialogConfig)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.combo_initial_market = QtWidgets.QComboBox(DialogConfig)
        self.combo_initial_market.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.combo_initial_market.setObjectName("combo_initial_market")
        self.verticalLayout_2.addWidget(self.combo_initial_market)
        self.combo_initial_exchange = QtWidgets.QComboBox(DialogConfig)
        self.combo_initial_exchange.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.combo_initial_exchange.setObjectName("combo_initial_exchange")
        self.verticalLayout_2.addWidget(self.combo_initial_exchange)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.line_2 = QtWidgets.QFrame(DialogConfig)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.list_exchanges = QtWidgets.QListWidget(DialogConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_exchanges.sizePolicy().hasHeightForWidth())
        self.list_exchanges.setSizePolicy(sizePolicy)
        self.list_exchanges.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.list_exchanges.setFont(font)
        self.list_exchanges.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.list_exchanges.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.list_exchanges.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.list_exchanges.setLineWidth(1)
        self.list_exchanges.setMidLineWidth(0)
        self.list_exchanges.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.list_exchanges.setAlternatingRowColors(True)
        self.list_exchanges.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.list_exchanges.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.list_exchanges.setIconSize(QtCore.QSize(24, 24))
        self.list_exchanges.setMovement(QtWidgets.QListView.Static)
        self.list_exchanges.setFlow(QtWidgets.QListView.TopToBottom)
        self.list_exchanges.setViewMode(QtWidgets.QListView.ListMode)
        self.list_exchanges.setObjectName("list_exchanges")
        item = QtWidgets.QListWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/exchanges/binance"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.list_exchanges.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/exchanges/bitfinex"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        self.list_exchanges.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_exchanges.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_exchanges.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/exchanges/bittrex"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon3)
        self.list_exchanges.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_exchanges.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/exchanges/kraken"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon4)
        self.list_exchanges.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_exchanges.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/exchanges/poloniex"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon5)
        self.list_exchanges.addItem(item)
        self.verticalLayout.addWidget(self.list_exchanges)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogConfig)
        self.buttonBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DialogConfig)
        self.buttonBox.accepted.connect(DialogConfig.accept)
        self.buttonBox.rejected.connect(DialogConfig.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogConfig)

    def retranslateUi(self, DialogConfig):
        _translate = QtCore.QCoreApplication.translate
        DialogConfig.setWindowTitle(_translate("DialogConfig", "Settings"))
        self.label.setText(_translate("DialogConfig", "Language"))
        self.combo_languages.setItemText(0, _translate("DialogConfig", "es_ES"))
        self.combo_languages.setItemText(1, _translate("DialogConfig", "en_EN"))
        self.label_2.setText(_translate("DialogConfig", "Initial market"))
        self.list_exchanges.setSortingEnabled(True)
        __sortingEnabled = self.list_exchanges.isSortingEnabled()
        self.list_exchanges.setSortingEnabled(False)
        item = self.list_exchanges.item(0)
        item.setText(_translate("DialogConfig", "Binance"))
        item = self.list_exchanges.item(1)
        item.setText(_translate("DialogConfig", "Bitfinex"))
        item = self.list_exchanges.item(2)
        item.setText(_translate("DialogConfig", "Bitmex"))
        item = self.list_exchanges.item(3)
        item.setText(_translate("DialogConfig", "Bitstamp"))
        item = self.list_exchanges.item(4)
        item.setText(_translate("DialogConfig", "Bittrex"))
        item = self.list_exchanges.item(5)
        item.setText(_translate("DialogConfig", "Coinbase"))
        item = self.list_exchanges.item(6)
        item.setText(_translate("DialogConfig", "Kraken"))
        item = self.list_exchanges.item(7)
        item.setText(_translate("DialogConfig", "Kucoin"))
        item = self.list_exchanges.item(8)
        item.setText(_translate("DialogConfig", "Poloniex"))
        self.list_exchanges.setSortingEnabled(__sortingEnabled)
import iconos_rc
