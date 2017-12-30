import sys
<<<<<<< HEAD
=======
import os
>>>>>>> bb0c4ee7dbc2ed576118fafd154ad057b7938555
import time
import logging
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
<<<<<<< HEAD
import socket 
=======
import matplotlib.pyplot as plt
from Phidget22.Devices.VoltageRatioInput import *
from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Net import *
import socket
>>>>>>> bb0c4ee7dbc2ed576118fafd154ad057b7938555
import subprocess

class Client(QMainWindow):
	def __init__(self):
		super().__init__()
<<<<<<< HEAD
		self.left = 260
		self.top = 40
		self.width = 1500
		self.height = 1000
		self.setGeometry(self.left,self.top,self.width,self.height)
		self.client_settings = ClientSettings()
		self.initUI()
		self.MenuBar()
		self.Buttons()
		self.show()

=======
		self.setWindowState(Qt.WindowMaximized)
		self.yGeom = QDesktopWidget().height()
		self.xGeom = QDesktopWidget().width()
		self.xScalar = (self.xGeom/1920)*2
		self.xCenter = self.xGeom/self.xScalar
		self.yCenter = self.yGeom/2
		self.client_settings = ClientSettings()
		self.initUI()
		self.MenuBar()
		self.Pictures()
		self.Labels()
		self.Buttons()
		self.show()


>>>>>>> bb0c4ee7dbc2ed576118fafd154ad057b7938555
	def initUI(self):
		self.title = 'Test Stand'
		self.setWindowTitle(self.title)
		self.setWindowIcon(QIcon('pictures/icon.png'))
		# Set window background color
		self.setAutoFillBackground(True)
		p = self.palette()
<<<<<<< HEAD
		p.setColor(self.backgroundRole(), Qt.gray)
		self.setPalette(p)


		def createLabel(self, stext, smovex, smovey, sresizex, sresizey, sfontsize, storf, scolor):
			# makes code smaller, all the labels in the program

			slabel = QtWidgets.QLabel(self)
			slabel.setText(stext)
			slabel.move(smovex, smovey)
			slabel.resize(sresizex, sresizey)
			slabel.setFont(QtGui.QFont('Times', sfontsize, QtGui.QFont.Bold, storf))
			slabel.setPalette(scolor)
=======
		p.setColor(self.backgroundRole(), Qt.white)
		self.setPalette(p)

		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		# sets up the logging text box in the console

		self.logTextBox = QTextBrowser(self)
		self.font = QFont()
		self.font.setPointSize(12)
		self.logTextBox.setFont(self.font)
		self.logTextBox.setReadOnly(True)
		self.logTextBox.resize(400, 974)
		self.logTextBox.move(self.xCenter+560, 75)
		self.logTextBox.append("  =========Action Log=========")

		#Centers of Certain Objects, such as the test stand picture.
		self.testStandCenter = self.xCenter -50
		self.testStandDepth = self.yCenter - 450

		#Used to animate the Tanks, tough because the height function changes from the center of the picture.
		self.engineInit = 0
		self.engineInit_Move = 0
		self.tank_1_Init = 0
		self.tank_1_Init_Move = 0
		self.tank_2_Init = 0
		self.tank_2_Init_Move = 0

		server_IP = '192.168.1.132' #This is the IP of the ESB Pi. It is a static IP. 
		port = 5000
		BUFF = 1024
		self.server_address = (server_IP,port)
		#s = socket.create_connection(self.server_address,timeout = 1.5)

		#Initializing variables that will be used later in the program
		self.connection_status = False
		self.phidget_status = False
		self.loadcelltare = False


	def Labels(self):

		self.palettered = QPalette()
		self.palettered.setColor(QPalette.Foreground, Qt.red)

		self.paletteblack = QPalette()
		self.paletteblack.setColor(QPalette.Foreground, Qt.black)

		self.paletteblue = QPalette()
		self.paletteblue.setColor(QPalette.Foreground, Qt.blue)

		def createLabel(self, stext, smovex, smovey, sresizex, sresizey, sfontsize, storf, scolor):
			# makes code smaller, all the labels in the program
			slabel = QLabel(self)
			slabel.setText(stext)
			slabel.move(smovex, smovey)
			slabel.resize(sresizex, sresizey)
			slabel.setFont(QFont('Times', sfontsize, QFont.Bold, storf))
			slabel.setPalette(scolor)
			return slabel

		self.rocketlabel = createLabel(self, 'SDSU ROCKET PROJECT',0,25,500,50,20,True,self.paletteblack)
		self.teststandlabel = createLabel(self, 'TEST STAND',0,73,300,50,20,True,self.paletteblack)
		self.loadcelllabel = createLabel(self, '0',self.testStandCenter+150,self.testStandDepth+800,300,50,20,True,self.paletteblack)

	def Pictures(self):
>>>>>>> bb0c4ee7dbc2ed576118fafd154ad057b7938555

		def createPicture(self, spicture, smovex, smovey, sresizex, sresizey):
			# makes code smaller, all the pictures in the program
			# you have to save pictures to the pictures/ path in order to show
<<<<<<< HEAD

			pix = QtWidgets.QLabel(self)
			pix.setPixmap(QtGui.QPixmap('pictures/' + spicture))
			pix.move(smovex, smovey)
			pix.resize(sresizex, sresizey)

	def Buttons(self):

		states = [ False, False, False, False, False, False ]
		def getStatus(relayNum):
			if states[relayNum-1]:
				return "OPEN"
			else:
				return "CLOSED"

		def toggleState(relayNum):
			states[relayNum-1] = not states[relayNum-1]
=======
			pix = QLabel(self)
			pix.setPixmap(QPixmap('pictures/' + spicture))
			pix.resize(sresizex, sresizey)
			pix.move(smovex,smovey)
			return pix

		self.stand = createPicture(self,'stand.png',self.testStandCenter-350,self.testStandDepth,741,807)
		self.engine = createPicture(self,'Rocket_Engine.png',self.testStandCenter-40,self.testStandDepth + 750,80,186)
		self.engineHot = createPicture(self,'Rocket_Engine_Hot.png',self.testStandCenter-40,self.testStandDepth+843,80,0)
		self.load_cell = createPicture(self,'loadcell.png',self.testStandCenter-40,self.testStandDepth+740,80,87)
		self.tank1 = createPicture(self,'tank.png',self.testStandCenter-266,self.testStandDepth,171,711)
		self.tank2 = createPicture(self,'tank.png',self.testStandCenter+90,self.testStandDepth,171,711)
		self.blue = createPicture(self,'blue.png',self.testStandCenter-203,718,47,0)
		self.purple = createPicture(self,'purple.png',self.testStandCenter+90,718,47,0)
		self.redtopborder = createPicture(self,'red.png',0,25,1980,50)
		self.rocketlogo = createPicture(self,'rp.png',self.testStandCenter-87.5,self.testStandDepth+95,175,91)
		self.box = createPicture(self,'box.png',0,73,215,50)
		self.loxgauge = createPicture(self,'gauge.png',self.testStandCenter-570,self.testStandDepth+7,300,300)
		self.ch4gauge = createPicture(self,'gauge.png',self.testStandCenter+260,self.testStandDepth+7,300,300)
		self.connectionsymbol = createPicture(self,'pingred.png',self.testStandCenter+40,self.testStandDepth,80,80)

	def Buttons(self):

		def createButton(self, stext, smovex, smovey, sresizex, sresizey, senabled, sfontsize, sfunction, sicon, siconx, sicony):
			# makes code smaller, all the labels in the program

			sbutton = QPushButton(stext, self)
			sbutton.move(smovex, smovey)
			sbutton.resize(sresizex, sresizey)
			sbutton.setEnabled(senabled)
			sbutton.setFont(sfontsize)
			sbutton.clicked.connect(sfunction)
			if stext == '':
				sbutton.setIcon(QIcon("pictures/"+sicon))
				sbutton.setIconSize(QSize(siconx, sicony))
			return sbutton

>>>>>>> bb0c4ee7dbc2ed576118fafd154ad057b7938555

		#sets 4 different font sizes for the buttons created. Pick one.
		self.font2 = QFont()
		self.font2.setPointSize(18)
		self.font3 = QFont()
		self.font3.setPointSize(12)
		self.font4 = QFont()
		self.font4.setPointSize(10)
		self.font5 = QFont()
		self.font5.setPointSize(24)

<<<<<<< HEAD
		server_IP = '192.168.1.132' #This is the IP of the ESB Pi. It is a static IP. 
		port = 5000
		BUFF = 1024
		self.server_address = (server_IP,port)
		s = socket.create_connection(self.server_address,timeout = 1.5)

		def toggler_1(self):
			s.send(b'relay_1')
			toggleState(1)

		def toggler_2(self):
			s.send(b'relay_2')
			toggleState(2)

		def toggler_3(self):
			s.send(b'relay_3')
			toggleState(3)

		def toggler_4(self):
			s.send(b'relay_4')
			toggleState(4)

		def toggler_5(self):
			s.send(b'relay_5')
			toggleState(5)

		def toggler_6(self):
			s.send(b'relay_6')
			toggleState(6)

		self.toggle_1 = QPushButton("1: {}".format(getStatus(1)), self)
		self.toggle_1.resize(290, 170)
		self.toggle_1.move(100, 70)
		self.toggle_1.setEnabled(True)
		self.toggle_1.setFont(self.font5)
		self.toggle_1.clicked.connect(toggler_1)
		states.valueUpdated.connect(self.handleValueUpdated)

		self.toggle_2 = QPushButton("Toggle_2", self)
		self.toggle_2.resize(290, 170)
		self.toggle_2.move(400, 70)
		self.toggle_2.setEnabled(True)
		self.toggle_2.setFont(self.font5)
		self.toggle_2.clicked.connect(toggler_2)

		self.toggle_3 = QPushButton("Toggle_3", self)
		self.toggle_3.resize(290, 170)
		self.toggle_3.move(700, 70)
		self.toggle_3.setEnabled(True)
		self.toggle_3.setFont(self.font5)
		self.toggle_3.clicked.connect(toggler_3)

		self.toggle_4 = QPushButton("Toggle_4", self)
		self.toggle_4.resize(290, 170)
		self.toggle_4.move(1000, 70)
		self.toggle_4.setEnabled(True)
		self.toggle_4.setFont(self.font5)
		self.toggle_4.clicked.connect(toggler_4)

		self.toggle_5 = QPushButton("Toggle_5", self)
		self.toggle_5.resize(290, 170)
		self.toggle_5.move(1300, 70)
		self.toggle_5.setEnabled(True)
		self.toggle_5.setFont(self.font5)
		self.toggle_5.clicked.connect(toggler_5)

		self.toggle_6 = QPushButton("Toggle_6", self)
		self.toggle_6.resize(290, 170)
		self.toggle_6.move(1600, 70)
		self.toggle_6.setEnabled(True)
		self.toggle_6.setFont(self.font5)
		self.toggle_6.clicked.connect(toggler_6)

		def handleValueUpdated(self,states):
			self.toggle_1.setText(getStatus(1))

		def createButton(self, saction, smovex, smovey, sresizex, sresizey, senabled, sfontsize, sfunction):
			#makes code smaller, all buttons in program
			self.launchBtn = QtWidgets.QPushButton("Launch!", self)
			self.launchBtn.resize(290, 170)
			self.launchBtn.move(5, 70)
			self.launchBtn.setEnabled(False)
			self.launchBtn.setFont(self.font5)
			self.launchBtn.clicked.connect(self.launch_app)


=======
		self.connectbtn = createButton(self,'Connect',self.testStandCenter-120,self.testStandDepth+23,150,40,True,self.font5,self.connect_app,'icon.png',100,100)
		self.firebtn = createButton(self,'Fire!',5,130,285,90,True,self.font5,self.connect_app,'icon.png',100,100)
		self.loadcellbtn = createButton(self,'Start Load Cell',10,300,270,70,True,self.font5,self.loadcell_app,'icon.png',100,100)
		self.loadcelltarebtn = createButton(self,'Tare Load Cell',10,400,270,70,True,self.font5,self.loadcelltare_app,'icon.png',100,100)


	def loadcelltare_app(self):
		try:
			self.loadcelltare = True
			self.infotimer.stop()
			self.loadcell_app()
		except:
			self.logTextBox.append("  >  Cannot Tare a Load Cell That is Not Running{}".format(time.strftime(" -\t(%H:%M:%S)", time.localtime())))

	def loadcell_app(self):

		def VoltageRatioInputAttached(e):
			print("Attached!")
			self.phidget_status = True

		def VoltageRatioInputDetached(e):
			print("Detached") 
			self.phidget_status = False

		def VoltageRatioChangeHandler(e, voltageRatio):
			voltageRatio = (877420*voltageRatio)
			voltageZero.append(voltageRatio)
			print("VoltageRatio: %f" % voltageRatio)

		def ErrorEvent(e, eCode, description):
			print("Error %i : %s" % (eCode, description))
		if self.phidget_status == False or self.loadcelltare == True:
			try:
				self.ch = VoltageRatioInput()
				self.ch.setOnErrorHandler(ErrorEvent)
				self.ch.setOnAttachHandler(VoltageRatioInputAttached)
				self.ch.setOnVoltageRatioChangeHandler(VoltageRatioChangeHandler)
				self.ch.openWaitForAttachment(5000)
				self.ch.setBridgeEnabled(1)
				voltageZero = []

				time.sleep(5)
				self.voltavg = float(sum(voltageZero)) / float(len(voltageZero))

				self.loadcelltare = False
				self.infotimer = QTimer()
				self.infotimer.timeout.connect(self.loadcell)
				self.infotimer.setInterval(50)
				self.infotimer.start()
			except PhidgetException as e:
				print("Phidget Exception %i: %s" % (e.code, e.details))
				self.loadcelllabel.setText("Error")
				self.logTextBox.append("  >  Phidget Not Found{}".format(time.strftime("\t     -\t(%H:%M:%S)", time.localtime())))
				reply = QMessageBox.critical(self, "Phidget Results", "Couldn't connect to Phidget. Error is: \n{}: {}.\nMake sure Phidget is attached.".format(e.code, e.details),
														QMessageBox.Cancel | QMessageBox.Retry)
				if reply == QMessageBox.Cancel:
					self.logTextBox.append("  >  Phidget Canceled{}".format(time.strftime(" -\t(%H:%M:%S)", time.localtime())))
				elif reply == QMessageBox.Retry:
					self.logTextBox.append("  >  Retrying Phidget{}".format(time.strftime(" -\t(%H:%M:%S)", time.localtime())))
					self.loadcell_app()
		else:
			self.logTextBox.append("  >  Phidget already attached{}".format(time.strftime("\t     -\t(%H:%M:%S)", time.localtime())))

	def loadcell(self):
		def VoltageRatioInputAttached(e):
			print("Attached!")
			self.phidget_status = True

		def VoltageRatioInputDetached(e):
			print("Detached") 
			self.phidget_status = False

		def VoltageRatioChangeHandler1(e, voltageRatio):
			voltageRatio = (877420*voltageRatio - self.voltavg)
			voltlist = []
			voltlist.append(voltageRatio)
			print("VoltageRatio: %f" % voltageRatio)
			self.loadcelllabel.setText(str(voltageRatio))

		self.ch.setOnDetachHandler(VoltageRatioInputDetached)
		self.ch.setOnAttachHandler(VoltageRatioInputAttached)
		self.ch.setOnVoltageRatioChangeHandler(VoltageRatioChangeHandler1)

	def paintEvent(self, e):

		# sets up the "paint brush" in order to use the drawLines function

		qp = QPainter()
		qp.begin(self)
		self.drawLines(qp)
		qp.end()

	def drawLines(self, qp):

		# draws the lines found in the program

		pen = QPen(Qt.black, 4, Qt.SolidLine)
		qp.setPen(pen)
		qp.drawLine(self.testStandCenter+178, self.testStandDepth+30, self.testStandCenter+210, self.testStandDepth+10)
		qp.drawLine(self.testStandCenter+210, self.testStandDepth+10, self.testStandCenter+420, self.testStandDepth+10)
		qp.drawLine(self.testStandCenter-178, self.testStandDepth+30, self.testStandCenter-210, self.testStandDepth+10)
		qp.drawLine(self.testStandCenter-210, self.testStandDepth+10, self.testStandCenter-420, self.testStandDepth+10)
		#qp.drawLine(self.testStandCenter+178, self.testStandDepth+29, 950, 100)
		#qp.drawLine(307.5, 260, 307.5, 730)
>>>>>>> bb0c4ee7dbc2ed576118fafd154ad057b7938555


	def MenuBar(self):

		# Sets up File and About on top left of page. Most Functions are not completed yet.

		settingAction = QAction(QIcon('pictures/settings.png'), '&Settings', self)
		settingAction.setShortcut('Ctrl+S')
		settingAction.setStatusTip("Doesn't Work Right Now")
		settingAction.triggered.connect(self.client_settings.call_window)

		exitAction = QAction(QIcon('pictures/exit.png'), '&Exit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit Application')
		exitAction.triggered.connect(self.close_app)

		helpAction = QAction(QIcon('pictures/help.png'), '&Help', self)
		helpAction.setShortcut('Ctrl+H')
		helpAction.setStatusTip("Doesn't Wort Right Now")
		# helpAction.triggered.connect(QtWidgets.)

		aboutAction = QAction(QIcon('pictures/about.png'), '&About', self)
		aboutAction.setShortcut('Ctrl+A')
		aboutAction.setStatusTip("Doesn't Work Right Now")
		# aboutAction.triggered.connect(QtWidgets.)

		self.statusBar()

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		aboutMenu = menubar.addMenu('&About')
		fileMenu.addAction(settingAction)
		fileMenu.addAction(exitAction)
		aboutMenu.addAction(helpAction)
		aboutMenu.addAction(aboutAction)

<<<<<<< HEAD
=======
	def connect_app(self):

		self.logTextBox.append("  >  Connecting...{}".format(time.strftime("\t     -\t(%H:%M:%S)", time.localtime())))

		try:
			self.s = socket.create_connection(self.server_address,timeout = 1.5)
			QMessageBox.information(self, 'Connection Results', 'Socket Successfully Bound.\nClick "Read Statuses " to start')
			self.connection_status = True
			self.logTextBox.append("  >  Connected{}".format(time.strftime("\t     -\t(%H:%M:%S)", time.localtime())))
			self.connectionsymbol.setPixmap(QPixmap('pictures/pinggreen.png'))
			#logger.debug("Connection Successful at {}".format(time.asctime()))

		except socket.error as e:
			#logger.debug("Connection Unsuccessful at {}".format(time.strftime("(%H:%M:%S)", time.localtime())))
			self.logTextBox.append("  >  Connection Unsuccessful{}".format(time.strftime("\t     -\t(%H:%M:%S)", time.localtime())))
			reply = QMessageBox.critical(self, "Connection Results", "Couldn't connect to {} at {}. Error is: \n{}.\nMake sure server is listening.".format(self.server_address[0],self.server_address[1],e),
													QMessageBox.Cancel | QMessageBox.Retry)
			if reply == QMessageBox.Cancel:
				self.logTextBox.append("  >  Connection Canceled{}".format(time.strftime(" -\t(%H:%M:%S)", time.localtime())))
			elif reply == QMessageBox.Retry:
				self.logTextBox.append("  >  Retrying Connection{}".format(time.strftime(" -\t(%H:%M:%S)", time.localtime())))
				self.connect_app()


>>>>>>> bb0c4ee7dbc2ed576118fafd154ad057b7938555
	def close_app(self):
		# exits GUI
		#self.logTextBox.append(">  Exiting...{}".format(time.strftime("\t-           (%H:%M:%S)", time.localtime())))
		choice = QMessageBox.question(self, "Confirmation.", "Are you sure you want to exit?",
<<<<<<< HEAD
		                                        QMessageBox.Yes | QMessageBox.No)
		if choice == QMessageBox.Yes:
		    print("System Closed")
		    logger.debug("Application Exited at {}".format(time.strftime("(%H:%M:%S)", time.localtime())))
		    sys.exit()
		else:
		    pass
		    #self.logTextBox.append("> Exit Stopped{}".format(time.strftime("\t-         (%H:%M:%S)", time.localtime())))
=======
												QMessageBox.Yes | QMessageBox.No)
		if choice == QMessageBox.Yes:
			print("System Closed")
			#logger.debug("Application Exited at {}".format(time.strftime("(%H:%M:%S)", time.localtime())))
			sys.exit()
		else:
			pass
			#self.logTextBox.append("> Exit Stopped{}".format(time.strftime("\t-         (%H:%M:%S)", time.localtime())))

	def animations(self,data):

		if data == "engine_up" and self.engineInit <= 186:
			self.engineInit += 9.3
			self.engineInit_Move += 9.3/2
			self.engineHot.move(self.testStandCenter-40,self.testStandDepth+843-self.engineInit_Move)
			self.engineHot.resize(80, self.engineInit)
			#self.engineHot.move(685, engineInit_move)
		elif data == "engine_down" and self.engineInit >= 9.3:
			self.engineInit -= 9.3
			self.engineInit_Move -= 9.3/2
			self.engineHot.resize(80, self.engineInit)
			self.engineHot.move(self.testStandCenter-40,self.testStandDepth+843-self.engineInit_Move)
		elif data == "tank_1_up" and self.tank_1_Init <= 1212:
			if self.tank_1_Init == 1212:
				self.blue.setPixmap(QPixmap('pictures/green.png'))
			self.tank_1_Init += 12
			self.tank_1_Init_Move += 12/2
			self.blue.move(self.testStandCenter-203, self.testStandDepth+668-self.tank_1_Init_Move)
			self.blue.resize(47, self.tank_1_Init)
		elif data == "tank_1_down" and self.tank_1_Init >= 12:
			if self.tank_1_Init <= 1224:
				self.blue.setPixmap(QPixmap('pictures/blue.png'))
			self.tank_1_Init -= 12
			self.tank_1_Init_Move -= 12/2
			self.blue.move(self.testStandCenter-203, self.testStandDepth+668-self.tank_1_Init_Move)
			self.blue.resize(47, self.tank_1_Init)
		elif data == "tank_2_up" and self.tank_2_Init <= 1212:
			if self.tank_2_Init == 1212:
				self.purple.setPixmap(QPixmap('pictures/green.png'))
			self.tank_2_Init += 12
			self.tank_2_Init_Move += 12/2
			self.purple.move(self.testStandCenter+153, self.testStandDepth+668-self.tank_2_Init_Move)
			self.purple.resize(47, self.tank_2_Init)
		elif data == "tank_2_down" and self.tank_2_Init >= 12:
			if self.tank_2_Init <= 1224:
				self.purple.setPixmap(QPixmap('pictures/purple.png'))
			self.tank_2_Init -= 12
			self.tank_2_Init_Move -= 12/2
			self.purple.move(self.testStandCenter+153, self.testStandDepth+668-self.tank_2_Init_Move)
			self.purple.resize(47, self.tank_2_Init)
>>>>>>> bb0c4ee7dbc2ed576118fafd154ad057b7938555


class ClientSettings(QWidget):
	def __init__(self):
		super().__init__()

		self.title = 'Client Settings'
		self.left = 50
		self.top = 50
		self.width = 500
		self.height = 500

		self.setWindowTitle(self.title)
		self.setWindowIcon(QIcon('pictures/settings.png'))
		self.setFixedSize(500, 500)

		self.log_folder_label = QLabel('Log Folder:', self)
		self.log_folder_label.move(10,10)
		self.log_folder_field = QLineEdit(self)
		self.log_folder_field.move(10,30)

		self.time_folder_label = QLabel('Time:', self)
		self.time_folder_label.move(10,60)
		self.time_folder_field = QLineEdit(self)
		self.time_folder_field.move(10,80)


		self.settings_init()

	def call_window(self):
		#This functioned is called everytime the window is opened so that
		#settings init is called to reload whatever settings are saved in config
		self.settings_init()
		self.show()

	def settings_init(self):
		#Unfinished
		#Would load current setting from config
		self.log_folder_field.setText('log')
		self.time_folder_field.setText(str(10))

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Client()
	sys.exit(app.exec_())
<<<<<<< HEAD
=======





'''self.toggle_1 = createButton(self,'',100,200,100,100,True,self.font5,self.toggler_1,'icon.png',100,100)
		self.toggle_2 = createButton(self,'',100,320,100,100,True,self.font5,self.toggler_2,'icon.png',100,100)
		self.toggle_3 = createButton(self,'',100,500,100,100,True,self.font5,self.toggler_3,'icon.png',100,100)
		self.toggle_4 = createButton(self,'',100,630,100,100,True,self.font5,self.toggler_4,'icon.png',100,100)
		self.toggle_5 = createButton(self,'',220,350,100,100,True,self.font5,self.toggler_5,'icon.png',100,100)
		self.toggle_6 = createButton(self,'',220,480,100,100,True,self.font5,self.toggler_6,'icon.png',100,100)
		#toggle_5 = createButton(self,'Toggle_2',400,70,290,170,True,self.font5,self.toggler_2,'',100,100)
		#toggle_6 = createButton(self,'Toggle_3',700,70,290,170,True,self.font5,self.toggler_3,'icon.png',100,100)

		#self.toggle_1.setStyleSheet("background-color: white")

	def toggler_1(self):
		#s.send(b'relay_1')
		self.animations("engine_up")

	def toggler_2(self):
		#s.send(b'relay_2')
		self.animations("engine_down")

	def toggler_3(self):
		#s.send(b'relay_3')
		self.animations("tank_1_up")

	def toggler_4(self):
		#s.send(b'relay_3')
		self.animations("tank_1_down")

	def toggler_5(self):
		#s.send(b'relay_3')
		self.animations("tank_2_up")

	def toggler_6(self):
		#s.send(b'relay_3')
		self.animations("tank_2_down")'''
>>>>>>> bb0c4ee7dbc2ed576118fafd154ad057b7938555
