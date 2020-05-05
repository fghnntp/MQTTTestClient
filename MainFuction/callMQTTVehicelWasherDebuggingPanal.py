import sys
import paho.mqtt.client as mqtt
from PyQt5.QtWidgets import QDialog, QApplication, QHeaderView, QTableWidgetItem
from PyQt5.QtCore import QTimer
from MQTTVehicelWasherDebuggingPanel import *
from logInInterface import *
from mqttRemoteMessage import *

class LoginInterface(QDialog):
    """This is the user login window to check if user input the right username and matchint password"""
    def __init__(self, mainWindow):
        #initial the login interface 
        super().__init__()
        self.ui=Ui_DialogLoginInterface()
        self.ui.setupUi(self)
        self.setWindowTitle("登入窗口")
        self.ui.lineEditUser.setFocus()
        self.ui.lineEditUser.setText("liuleyong")
        self.ui.lineEditPassword.setText("liuleyong")
        self.mainWindow=mainWindow
        self.ui.pushButtonLogin.clicked.connect(self.tryLogin)
        #check the if the user input the right username and matching password
        self.show()
    def tryLogin(self):
        if self.ui.lineEditUser.text()=="liuleyong" and self.ui.lineEditPassword.text()=="liuleyong":
            self.mainWindow.show()
            self.close()
        else:
            exit()

class UserInterface(QDialog):
    """This is the mainwindow to give user every function they need"""
    def __init__(self):
        super().__init__()
        self.ui=Ui_DialogMainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("自动洗车机MQTT调试面板")
        self.ui.lineEditMQTTAddress.setFocus()
        self.ui.listWidgetHistoryReturnMessage.setViewMode
        self.mqttAdress=""
        #save the MQTT Server address
        self.client=False
        self.clientUp=False
        self.theCarCanInWasher=False
        self.washingStart=False
        self.carNumbers=[]
        self.carOrders=[]
        self.ui.lineEditMQTTAddress.setText("broker.ravws.dloa.xyz")
        self.ui.lineEditCarNumber.setText("苏A12345")
        self.ui.lineEditWasherOrderMessage.setText("5ea2aec00a9afa5a60ea00b3")
        #set a null list to save the comeing car number
        #set the default client objection as False
        self.topics=["ravws/carwashes/0/status/patch", "ravws/orders/0/post", "ravws/orders/complete/patch", "ravws/warnings/0/post", "ravws/orders/undo"]
        #when link the MQTT Server, the topics wo should subscribe 
        self.ui.tableWidgetMessage.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #set the tableWidgetMessage in ui can match the space I give
        self.ui.pushButtonMQTTAdressConfirm.clicked.connect(self.setMQTTAdress)
        #set the MQTTAdress in this application and subscribe the messages form the
        #given topics and simulate publish a washer sate message in washer state topic
        self.ui.pushButtonDeliverOrderMessage.clicked.connect(self.setSimulationOrderMessage)
        #set the message in local client
        self.ui.pushButtonRichLocation.clicked.connect(self.checkTheArrivalCarNumber)
        #checktheCarNumber if the number is right
        self.ui.pushButtonStarWashCar.clicked.connect(self.startWashingCar)
        #startWashingCar and publish the MQTT Message
        self.ui.pushButtonFinshWashCar.clicked.connect(self.finishWashingCar)
        #finishWasingCar and publish the MQTT Message
        self.ui.pushButtonWarning0.clicked.connect(self.sendWarning0)
        self.ui.pushButtonWarning1.clicked.connect(self.sendWarning1)
        self.ui.pushButtonWarning2.clicked.connect(self.sendWarning2)
    def setMQTTAdress(self):
        #set the MQTT address and check it if it's a right address
        #when set the right MQTT address, subscribe the default address
        if len(self.ui.lineEditMQTTAddress.text())==0:
            self.ui.lineEditNewestReturnMessage.setText("请输入正确的地址")
            self.ui.listWidgetHistoryReturnMessage.addItem("")
        else:
            if self.client or self.clientUp:
                self.ui.listWidgetHistoryReturnMessage.clear()
                self.client.loop_stop()
                self.client.loop_stop()
                self.theCarCanInWasher=False
                self.washingStart=False
                self.carNumbers=[]
                self.carOrders=[]
            self.mqttAdress=self.ui.lineEditMQTTAddress.text()
            self.ui.lineEditNewestReturnMessage.setText(self.mqttAdress)
            self.ui.listWidgetHistoryReturnMessage.addItem(self.mqttAdress)
            self.client=mqtt.Client("test")
            self.clientUp=mqtt.Client("up")
            self.ui.lineEditNewestReturnMessage.setText("正在尝试连接 "+self.mqttAdress)
            self.ui.listWidgetHistoryReturnMessage.addItem("正在尝试连接 "+self.mqttAdress)
            self.ui.listWidgetHistoryReturnMessage.addItem("")
            try:
                self.client.connect(self.mqttAdress, 1883)
                self.clientUp.connect(self.mqttAdress, 1883)
                self.ui.lineEditNewestReturnMessage.setText("连接成功，你的客户端名称为 test")
                self.ui.listWidgetHistoryReturnMessage.addItem("连接成功，你的客户端名称为 test")
                self.ui.lineEditNewestReturnMessage.setText("设置MQTT地址成功")
                self.ui.listWidgetHistoryReturnMessage.addItem("设置MQTT地址成功")
                self.ui.listWidgetHistoryReturnMessage.addItem("")
            except:
                self.mqttAdress=""
                self.client=False
                self.clientUp=False
                self.ui.lineEditNewestReturnMessage.setText("连接错误，请检查MQTT地址")
                self.ui.listWidgetHistoryReturnMessage.addItem("连接错误，请检查MQTT地址")
                self.ui.listWidgetHistoryReturnMessage.addItem("")
        #when connect the MQTT sever correctly, subscribe the topics
        if self.client and self.clientUp:
            self.client.loop_start()
            self.clientUp.loop_start()
            for _ in self.topics:
                try:
                    self.client.subscribe(_)
                    self.clientUp.subscribe(_)
                    self.client.on_message=self.onMessageCome
                    self.ui.lineEditNewestReturnMessage.setText("成功连接"+self.mqttAdress+"下的"+_+"主题")
                    self.ui.listWidgetHistoryReturnMessage.addItem("成功连接"+self.mqttAdress+"下的"+_+"主题")
                except:
                    self.ui.lineEditNewestReturnMessage.setText("连接失败"+self.mqttAdress+"下的"+_+"主题")
                    self.ui.listWidgetHistoryReturnMessage.addItem("连接失败"+self.mqttAdress+"下的"+_+"主题")
                    self.client.loop_stop()
                    self.clientUp.loop_stop()
                #if the circle can run over, publish in topic with the state message
                if _==self.topics[-1]:
                        self.client.publish(self.topics[0], "0")
    def onMessageCome(self, client, userdata, msg):
        #when MQTT Client connect the server correctly,start the receve the message
        #published by the server, the server is simulated by ClientUp
        self.ui.lineEditNewestReturnMessage.setText("客户端收到数据"+msg.topic+""+":"+str(msg.payload.decode("utf-8")))
        self.ui.listWidgetHistoryReturnMessage.addItem("客户端收到数据"+msg.topic+""+":"+str(msg.payload))
        self.ui.listWidgetHistoryReturnMessage.addItem("")
    def setSimulationOrderMessage(self):
        #try to set zhe order message if the message set is right
        #and then append the car number message into the bulid-in data structure
        wahserOrderMessage=self.ui.lineEditWasherOrderMessage.text()
        messages=[]
        for _ in wahserOrderMessage.split(','):
            messages.append(_)
        rowCount=self.ui.tableWidgetMessage.rowCount()
        self.ui.tableWidgetMessage.insertRow(rowCount)
        i=0
        for _ in messages:
            self.ui.tableWidgetMessage.setItem(rowCount, i, QTableWidgetItem(_))
            i=i+1
        self.ui.lineEditWasherOrderMessage.clear()
        self.clientUp.publish(self.topics[1],"orderNumber:"+messages[0])
        self.clientUp.publish(self.topics[1],"plateNumber:"+messages[1])
        self.clientUp.publish(self.topics[1],"appointmenTimes:"+messages[2])
        self.clientUp.publish(self.topics[1],"vehicle:"+messages[3])
        self.carNumbers.append(messages[2])
        self.carOrders.append(messages[1])
    def checkTheArrivalCarNumber(self):
        realCarNumber=self.ui.lineEditCarNumber.text()
        if realCarNumber==self.carNumbers[0]:
            self.theCarCanInWasher=True
            self.ui.lineEditNewestReturnMessage.setText("前来的车辆车牌号正确")
            self.ui.listWidgetHistoryReturnMessage.addItem("前来的车辆车牌号正确")
        else:
            self.theCarCanInWasher=False
            self.ui.lineEditNewestReturnMessage.setText("前来的车辆车牌号不正确")
            self.ui.listWidgetHistoryReturnMessage.addItem("前来的车辆车牌号不正确")
    def startWashingCar(self):
        #startWashingCar and publish the MQTT Message
        if self.theCarCanInWasher:
            self.client.publish(self.topics[0], "1")
            self.washingStart=True
            self.theCarCanInWasher=False
    def finishWashingCar(self):
        #finishWasingCar and publish the MQTT Message
        self.carNumbers.pop(0)
        self.client.publish(self.topics[0], 0)
        self.client.publish(self.topics[2], self.carOrders.pop(0))
        self.ui.tableWidgetMessage.removeRow(0)
    def sendWarning0(self):
        self.client.publish(self.topics[3], "0")
        self.client.publish(self.topics[4], "True")
        self.ui.lineEditNewestReturnMessage.setText("汽车及故障，请重新连接MQTT服务器")
        self.ui.listWidgetHistoryReturnMessage.clear()
        self.client.loop_stop()
        self.client.loop_stop()
        self.theCarCanInWasher=False
        self.washingStart=False
        self.carNumbers=[]
        self.carOrders=[]
        self.ui.tableWidgetMessage.clear()
    def sendWarning1(self):
        self.client.publish(self.topics[3], "1")
        self.client.publish(self.topics[4], "True")
        self.ui.lineEditNewestReturnMessage.setText("汽车及故障，请重新连接MQTT服务器")
        self.ui.listWidgetHistoryReturnMessage.clear()
        self.client.loop_stop()
        self.client.loop_stop()
        self.theCarCanInWasher=False
        self.washingStart=False
        self.carNumbers=[]
        self.carOrders=[]
    def sendWarning2(self):
        self.client.publish(self.topics[3], "2")
        self.client.publish(self.topics[4], "True")
        self.ui.lineEditNewestReturnMessage.setText("汽车及故障，请重新连接MQTT服务器")
        self.ui.listWidgetHistoryReturnMessage.clear()
        self.client.loop_stop()
        self.client.loop_stop()
        self.theCarCanInWasher=False
        self.washingStart=False
        self.carNumbers=[]
        self.carOrders=[]


if __name__ == "__main__":
    app=QApplication(sys.argv)
    mainWindow=UserInterface()
    loginWindow=LoginInterface(mainWindow)
    sys.exit(app.exec_())
