# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MQTTVehicelWasherDebuggingPanel.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogMainWindow(object):
    def setupUi(self, DialogMainWindow):
        DialogMainWindow.setObjectName("DialogMainWindow")
        DialogMainWindow.resize(949, 711)
        font = QtGui.QFont()
        font.setFamily("黑体")
        DialogMainWindow.setFont(font)
        self.layoutWidget = QtWidgets.QWidget(DialogMainWindow)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 911, 671))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayoutMain = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayoutMain.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutMain.setObjectName("gridLayoutMain")
        self.groupBoxMessageSave = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBoxMessageSave.setMaximumSize(QtCore.QSize(500, 16777215))
        self.groupBoxMessageSave.setObjectName("groupBoxMessageSave")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBoxMessageSave)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 30, 461, 281))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayoutMessageSave = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayoutMessageSave.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutMessageSave.setObjectName("gridLayoutMessageSave")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.gridLayoutMessageSave.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEditNewestReturnMessage = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEditNewestReturnMessage.setEnabled(False)
        self.lineEditNewestReturnMessage.setObjectName("lineEditNewestReturnMessage")
        self.gridLayoutMessageSave.addWidget(self.lineEditNewestReturnMessage, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.gridLayoutMessageSave.addWidget(self.label_3, 1, 0, 1, 1)
        self.listWidgetHistoryReturnMessage = QtWidgets.QListWidget(self.layoutWidget1)
        self.listWidgetHistoryReturnMessage.setEnabled(True)
        self.listWidgetHistoryReturnMessage.setObjectName("listWidgetHistoryReturnMessage")
        self.gridLayoutMessageSave.addWidget(self.listWidgetHistoryReturnMessage, 1, 1, 1, 1)
        self.gridLayoutMain.addWidget(self.groupBoxMessageSave, 0, 0, 3, 1)
        self.groupBoxWash = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBoxWash.setMaximumSize(QtCore.QSize(400, 120))
        self.groupBoxWash.setObjectName("groupBoxWash")
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBoxWash)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 30, 361, 71))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayoutWsah = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayoutWsah.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutWsah.setObjectName("gridLayoutWsah")
        self.pushButtonRichLocation = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButtonRichLocation.setObjectName("pushButtonRichLocation")
        self.gridLayoutWsah.addWidget(self.pushButtonRichLocation, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget2)
        self.label.setObjectName("label")
        self.gridLayoutWsah.addWidget(self.label, 0, 1, 1, 1)
        self.lineEditCarNumber = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEditCarNumber.setObjectName("lineEditCarNumber")
        self.gridLayoutWsah.addWidget(self.lineEditCarNumber, 0, 2, 1, 1)
        self.pushButtonFinshWashCar = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButtonFinshWashCar.setObjectName("pushButtonFinshWashCar")
        self.gridLayoutWsah.addWidget(self.pushButtonFinshWashCar, 1, 2, 1, 1)
        self.pushButtonStarWashCar = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButtonStarWashCar.setObjectName("pushButtonStarWashCar")
        self.gridLayoutWsah.addWidget(self.pushButtonStarWashCar, 1, 0, 1, 2)
        self.gridLayoutMain.addWidget(self.groupBoxWash, 0, 1, 1, 1)
        self.groupBoxWarning = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBoxWarning.setMaximumSize(QtCore.QSize(16777215, 80))
        self.groupBoxWarning.setObjectName("groupBoxWarning")
        self.layoutWidget3 = QtWidgets.QWidget(self.groupBoxWarning)
        self.layoutWidget3.setGeometry(QtCore.QRect(20, 24, 361, 41))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayoutWarning = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayoutWarning.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutWarning.setObjectName("gridLayoutWarning")
        self.pushButtonWarning2 = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButtonWarning2.setObjectName("pushButtonWarning2")
        self.gridLayoutWarning.addWidget(self.pushButtonWarning2, 0, 2, 1, 1)
        self.pushButtonWarning0 = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButtonWarning0.setObjectName("pushButtonWarning0")
        self.gridLayoutWarning.addWidget(self.pushButtonWarning0, 0, 0, 1, 1)
        self.pushButtonWarning1 = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButtonWarning1.setObjectName("pushButtonWarning1")
        self.gridLayoutWarning.addWidget(self.pushButtonWarning1, 0, 1, 1, 1)
        self.gridLayoutMain.addWidget(self.groupBoxWarning, 1, 1, 1, 1)
        self.groupBoxMessage = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBoxMessage.setObjectName("groupBoxMessage")
        self.widget = QtWidgets.QWidget(self.groupBoxMessage)
        self.widget.setGeometry(QtCore.QRect(32, 32, 841, 281))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidgetMessage = QtWidgets.QTableWidget(self.widget)
        self.tableWidgetMessage.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidgetMessage.sizePolicy().hasHeightForWidth())
        self.tableWidgetMessage.setSizePolicy(sizePolicy)
        self.tableWidgetMessage.setMinimumSize(QtCore.QSize(0, 200))
        self.tableWidgetMessage.setMaximumSize(QtCore.QSize(16777215, 250))
        self.tableWidgetMessage.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tableWidgetMessage.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidgetMessage.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.tableWidgetMessage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidgetMessage.setLineWidth(0)
        self.tableWidgetMessage.setMidLineWidth(0)
        self.tableWidgetMessage.setObjectName("tableWidgetMessage")
        self.tableWidgetMessage.setColumnCount(4)
        self.tableWidgetMessage.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetMessage.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetMessage.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetMessage.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetMessage.setHorizontalHeaderItem(3, item)
        self.tableWidgetMessage.horizontalHeader().setVisible(True)
        self.tableWidgetMessage.horizontalHeader().setCascadingSectionResizes(False)
        self.gridLayout.addWidget(self.tableWidgetMessage, 0, 0, 1, 3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.lineEditWasherOrderMessage = QtWidgets.QLineEdit(self.widget)
        self.lineEditWasherOrderMessage.setObjectName("lineEditWasherOrderMessage")
        self.gridLayout.addWidget(self.lineEditWasherOrderMessage, 1, 1, 1, 1)
        self.pushButtonDeliverOrderMessage = QtWidgets.QPushButton(self.widget)
        self.pushButtonDeliverOrderMessage.setObjectName("pushButtonDeliverOrderMessage")
        self.gridLayout.addWidget(self.pushButtonDeliverOrderMessage, 1, 2, 1, 1)
        self.gridLayoutMain.addWidget(self.groupBoxMessage, 3, 0, 1, 2)
        self.groupBoxMQTTSetting = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBoxMQTTSetting.setMaximumSize(QtCore.QSize(16777215, 120))
        self.groupBoxMQTTSetting.setObjectName("groupBoxMQTTSetting")
        self.layoutWidget4 = QtWidgets.QWidget(self.groupBoxMQTTSetting)
        self.layoutWidget4.setGeometry(QtCore.QRect(20, 20, 361, 91))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.gridLayoutMQTTSetting = QtWidgets.QGridLayout(self.layoutWidget4)
        self.gridLayoutMQTTSetting.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutMQTTSetting.setObjectName("gridLayoutMQTTSetting")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_5.setObjectName("label_5")
        self.gridLayoutMQTTSetting.addWidget(self.label_5, 0, 0, 1, 1)
        self.lineEditMQTTAddress = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lineEditMQTTAddress.setObjectName("lineEditMQTTAddress")
        self.gridLayoutMQTTSetting.addWidget(self.lineEditMQTTAddress, 0, 1, 1, 1)
        self.pushButtonMQTTAdressConfirm = QtWidgets.QPushButton(self.layoutWidget4)
        self.pushButtonMQTTAdressConfirm.setObjectName("pushButtonMQTTAdressConfirm")
        self.gridLayoutMQTTSetting.addWidget(self.pushButtonMQTTAdressConfirm, 1, 0, 1, 2)
        self.gridLayoutMain.addWidget(self.groupBoxMQTTSetting, 2, 1, 1, 1)

        self.retranslateUi(DialogMainWindow)
        QtCore.QMetaObject.connectSlotsByName(DialogMainWindow)

    def retranslateUi(self, DialogMainWindow):
        _translate = QtCore.QCoreApplication.translate
        DialogMainWindow.setWindowTitle(_translate("DialogMainWindow", "Dialog"))
        self.groupBoxMessageSave.setTitle(_translate("DialogMainWindow", "信息记录"))
        self.label_2.setText(_translate("DialogMainWindow", "最新返回信息："))
        self.label_3.setText(_translate("DialogMainWindow", "历史信息："))
        self.groupBoxWash.setTitle(_translate("DialogMainWindow", "洗车机清洗流程模拟"))
        self.pushButtonRichLocation.setText(_translate("DialogMainWindow", "到达洗车点"))
        self.label.setText(_translate("DialogMainWindow", "请输入车牌号："))
        self.pushButtonFinshWashCar.setText(_translate("DialogMainWindow", "完成洗车"))
        self.pushButtonStarWashCar.setText(_translate("DialogMainWindow", "开始洗车"))
        self.groupBoxWarning.setTitle(_translate("DialogMainWindow", "洗车机警告模拟"))
        self.pushButtonWarning2.setText(_translate("DialogMainWindow", "发出警告2"))
        self.pushButtonWarning0.setText(_translate("DialogMainWindow", "发出警告0"))
        self.pushButtonWarning1.setText(_translate("DialogMainWindow", "发出警告1"))
        self.groupBoxMessage.setTitle(_translate("DialogMainWindow", "订单信息模拟"))
        item = self.tableWidgetMessage.horizontalHeaderItem(0)
        item.setText(_translate("DialogMainWindow", "预约时间"))
        item = self.tableWidgetMessage.horizontalHeaderItem(1)
        item.setText(_translate("DialogMainWindow", "订单号"))
        item = self.tableWidgetMessage.horizontalHeaderItem(2)
        item.setText(_translate("DialogMainWindow", "车牌号"))
        item = self.tableWidgetMessage.horizontalHeaderItem(3)
        item.setText(_translate("DialogMainWindow", "车型"))
        self.label_4.setText(_translate("DialogMainWindow", "洗车机编号"))
        self.pushButtonDeliverOrderMessage.setText(_translate("DialogMainWindow", "确认提交"))
        self.groupBoxMQTTSetting.setTitle(_translate("DialogMainWindow", "MQTT地址设置"))
        self.label_5.setText(_translate("DialogMainWindow", "地址"))
        self.pushButtonMQTTAdressConfirm.setText(_translate("DialogMainWindow", "确认"))
