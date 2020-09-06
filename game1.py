
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal
import sqlite3

class Ui_MainWindow(QtWidgets.QWidget):
    signal=pyqtSignal()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(835, 833)
        MainWindow.setMaximumSize(QtCore.QSize(1100, 1100))
        MainWindow.setStyleSheet("background-color:rgb(161, 161, 161);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.selection = QtWidgets.QGroupBox(self.centralwidget)
        self.selection.setAutoFillBackground(False)
        self.selection.setStyleSheet("background-color:rgb(199, 255, 240);\n"
"border-color:rgb(199, 255, 240);\n"
"border-radius:10px;\n"
"border:2px solid black;")
        self.selection.setTitle("")
        self.selection.setObjectName("selection")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.selection)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.selection)
        self.label_3.setStyleSheet("font-weight: bold;\n"
"font-size:20px;\n"
"border:0px;")
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.groupBox_5 = QtWidgets.QGroupBox(self.selection)
        self.groupBox_5.setStyleSheet("border:0;")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_12 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_12.setTitle("")
        self.groupBox_12.setObjectName("groupBox_12")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_12)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.groupBox_12)
        self.label_8.setStyleSheet("font-weight: bold;\n"
"font-size:15px;")
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.noofbat = QtWidgets.QLabel(self.groupBox_12)
        self.noofbat.setStyleSheet("color:blue;font-weight: bold;\n"
"font-size:15px;")
        self.noofbat.setObjectName("noofbat")
        self.horizontalLayout_5.addWidget(self.noofbat)
        self.horizontalLayout.addWidget(self.groupBox_12)
        self.groupBox_11 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_11.setTitle("")
        self.groupBox_11.setObjectName("groupBox_11")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.groupBox_11)
        self.label_6.setStyleSheet("font-weight: bold;\n"
"font-size:15px;")
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.noofbwl = QtWidgets.QLabel(self.groupBox_11)
        self.noofbwl.setStyleSheet("color:blue;font-weight: bold;\n"
"font-size:15px;")
        self.noofbwl.setObjectName("noofbwl")
        self.horizontalLayout_6.addWidget(self.noofbwl)
        self.horizontalLayout.addWidget(self.groupBox_11)
        self.groupBox_10 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_10.setTitle("")
        self.groupBox_10.setObjectName("groupBox_10")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.groupBox_10)
        self.label_7.setStyleSheet("font-weight: bold;\n"
"font-size:15px;")
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.noofar = QtWidgets.QLabel(self.groupBox_10)
        self.noofar.setStyleSheet("color:blue;font-weight: bold;\n"
"font-size:15px;")
        self.noofar.setObjectName("noofar")
        self.horizontalLayout_7.addWidget(self.noofar)
        self.horizontalLayout.addWidget(self.groupBox_10)
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_11 = QtWidgets.QLabel(self.groupBox_9)
        self.label_11.setStyleSheet("font-weight: bold;\n"
"font-size:15px;")
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_8.addWidget(self.label_11)
        self.noofwk = QtWidgets.QLabel(self.groupBox_9)
        self.noofwk.setStyleSheet("color:blue;font-weight: bold;\n"
"font-size:15px;")
        self.noofwk.setObjectName("noofwk")
        self.horizontalLayout_8.addWidget(self.noofwk)
        self.horizontalLayout.addWidget(self.groupBox_9)
        self.verticalLayout.addWidget(self.groupBox_5)
        self.progressBar = QtWidgets.QProgressBar(self.selection)
        self.progressBar.setStyleSheet("border:2px solid black;\n"
"border-radius:5px;\n"
"font-size:15px;\n"
"font-weight:bold;\n"
"")
        self.progressBar.setMaximum(11)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.verticalLayout_6.addWidget(self.selection)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setStyleSheet("border:0px;")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setStyleSheet("border-color:black;\n"
"width: 500px;\n"
"")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_4.setMaximumSize(QtCore.QSize(350, 600))
        self.groupBox_4.setStyleSheet("width: px;")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_3.setContentsMargins(11, -1, 11, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_14 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_14.setStyleSheet("background-color:rgb(229, 167, 255);\n"
"border-radius:10px;\n"
"border:2px solid black;")
        self.groupBox_14.setTitle("")
        self.groupBox_14.setObjectName("groupBox_14")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.groupBox_14)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label = QtWidgets.QLabel(self.groupBox_14)
        self.label.setStyleSheet("font-weight: bold;\n"
"font-size:15px;\n"
"border:0px;")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_9.addWidget(self.label)
        self.pointsAvailable = QtWidgets.QLabel(self.groupBox_14)
        self.pointsAvailable.setStyleSheet("color:blue;font-weight: bold;\n"
"font-size:15px;border:0px;")
        self.pointsAvailable.setObjectName("pointsAvailable")
        self.horizontalLayout_9.addWidget(self.pointsAvailable)
        self.verticalLayout_3.addWidget(self.groupBox_14)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.groupBox_6.setMouseTracking(True)
        self.groupBox_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_6.setStyleSheet("background-color:rgb(255, 170, 127);\n"
"border-radius:10px;\n"
"border:2px solid black;")
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioBAT = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioBAT.setEnabled(True)
        self.radioBAT.setMouseTracking(False)
        self.radioBAT.setStyleSheet("font-weight: bold;\n"
"font-size:15px;border:0px;")
        self.radioBAT.setChecked(False)
        self.radioBAT.setObjectName("radioBAT")
        self.horizontalLayout_3.addWidget(self.radioBAT)
        self.radioBWL = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioBWL.setStyleSheet("font-weight: bold;\n"
"font-size:15px;border:0px;")
        self.radioBWL.setObjectName("radioBWL")
        self.horizontalLayout_3.addWidget(self.radioBWL)
        self.radioAR = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioAR.setStyleSheet("font-weight: bold;\n"
"font-size:15px;border:0px;")
        self.radioAR.setObjectName("radioAR")
        self.horizontalLayout_3.addWidget(self.radioAR)
        self.radioWK = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioWK.setWhatsThis(str(0))
        self.radioWK.setStyleSheet("font-weight: bold;\n"
"font-size:15px;border:0px;")
        self.radioWK.setObjectName("radioWK")
        self.horizontalLayout_3.addWidget(self.radioWK)
        self.verticalLayout_3.addWidget(self.groupBox_6)
        self.AvailablePlayersList = QtWidgets.QListWidget(self.groupBox_4)
        self.AvailablePlayersList.setMinimumSize(QtCore.QSize(200, 450))
        self.AvailablePlayersList.setMaximumSize(QtCore.QSize(500, 750))
        self.AvailablePlayersList.setStyleSheet("background-color:rgb(255, 255, 127);\n"
"border-radius:20px;\n"
"border:2px solid black;")
        self.AvailablePlayersList.setObjectName("AvailablePlayersList")
        self.verticalLayout_3.addWidget(self.AvailablePlayersList)
        self.horizontalLayout_2.addWidget(self.groupBox_4)
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        self.label_15.setStyleSheet("font-weight:bold;font-size:25px;")
        self.label_15.setScaledContents(False)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_2.addWidget(self.label_15)
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_7.setMaximumSize(QtCore.QSize(500, 600))
        self.groupBox_7.setStyleSheet("width: 65px;")
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_15 = QtWidgets.QGroupBox(self.groupBox_7)
        self.groupBox_15.setStyleSheet("background-color:rgb(229, 167, 255);\n"
"border-radius:10px;\n"
"border:2px solid black;")
        self.groupBox_15.setTitle("")
        self.groupBox_15.setObjectName("groupBox_15")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.groupBox_15)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_2 = QtWidgets.QLabel(self.groupBox_15)
        self.label_2.setStyleSheet("font-weight: bold;\n"
"font-size:15px;border:0px;")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_10.addWidget(self.label_2)
        self.pointsUsed = QtWidgets.QLabel(self.groupBox_15)
        self.pointsUsed.setStyleSheet("border:0px;color:blue;font-weight: bold;\n"
"font-size:15px;")
        self.pointsUsed.setObjectName("pointsUsed")
        self.horizontalLayout_10.addWidget(self.pointsUsed)
        self.verticalLayout_4.addWidget(self.groupBox_15)
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox_7)
        self.groupBox_8.setStyleSheet("background-color:rgb(255, 170, 127);\n"
"border-radius:10px;\n"
"border:2px solid black;")
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radioTeamName = QtWidgets.QRadioButton(self.groupBox_8)
        self.radioTeamName.setStyleSheet("font-weight: bold;\n"
"font-size:15px;border:0px;")
        self.radioTeamName.setChecked(True)
        self.radioTeamName.setObjectName("radioTeamName")
        self.horizontalLayout_4.addWidget(self.radioTeamName)
        self.TeamName = QtWidgets.QLabel(self.groupBox_8)
        self.TeamName.setStyleSheet("border:0px;color:blue;font-weight: bold;\n"
"font-size:15px;")
        self.TeamName.setObjectName("TeamName")
        self.horizontalLayout_4.addWidget(self.TeamName)
        self.verticalLayout_4.addWidget(self.groupBox_8)
        self.SelectedPlayerList = QtWidgets.QListWidget(self.groupBox_7)
        self.SelectedPlayerList.setMinimumSize(QtCore.QSize(200, 450))
        self.SelectedPlayerList.setMaximumSize(QtCore.QSize(500, 750))
        self.SelectedPlayerList.setStyleSheet("background-color:rgb(255, 255, 127);\n"
"border-radius:20px;\n"
"border:2px solid black;")
        self.SelectedPlayerList.setObjectName("SelectedPlayerList")
        self.verticalLayout_4.addWidget(self.SelectedPlayerList)
        self.horizontalLayout_2.addWidget(self.groupBox_7)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.verticalLayout_6.addWidget(self.groupBox_2)
        self.groupBox_13 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_13.setStyleSheet("border:0px;\n"
"")
        self.groupBox_13.setTitle("")
        self.groupBox_13.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_13.setObjectName("groupBox_13")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.groupBox_13)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.SaveButton = QtWidgets.QPushButton(self.groupBox_13)
        self.SaveButton.setEnabled(False)
        self.SaveButton.setStyleSheet("background-color:rgb(148, 205, 255);\n"
"border-radius:10px;\n"
"border:2px solid black;\n"
"font-weight: bold;\n"
"font-size:20px;\n"
"min-width:100px;")
        self.SaveButton.setObjectName("SaveButton")
        self.horizontalLayout_11.addWidget(self.SaveButton)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(spacerItem1)
        self.verticalLayout_6.addWidget(self.groupBox_13)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 835, 26))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        self.actionNEW_Team.setCheckable(True)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.setEnabled(False)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setEnabled(False)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setEnabled(False)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.menuManage_Teams.addAction(self.actionNEW_Team)
        self.menuManage_Teams.addAction(self.actionOPEN_Team)
        self.menuManage_Teams.addAction(self.actionSAVE_Team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionEVALUATE_Team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.AvailablePlayersList.setFont(font)
        self.SelectedPlayerList.setFont(font)
        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "My Fantasy Cricket Game"))
        self.label_3.setText(_translate("MainWindow", "Your Selections:"))
        self.label_8.setText(_translate("MainWindow", "Batsmen(BAT)"))
        self.noofbat.setText(_translate("MainWindow", "###"))
        self.label_6.setText(_translate("MainWindow", "Bowler(BWL)"))
        self.noofbwl.setText(_translate("MainWindow", "###"))
        self.label_7.setText(_translate("MainWindow", "All-Rounder(AR)"))
        self.noofar.setText(_translate("MainWindow", "###"))
        self.label_11.setText(_translate("MainWindow", "Wicket-Keeper(WK)"))
        self.noofwk.setText(_translate("MainWindow", "###"))
        self.progressBar.setFormat(_translate("MainWindow", "%p%"))
        self.label.setText(_translate("MainWindow", "Points Available: "))
        self.pointsAvailable.setText(_translate("MainWindow", "###"))
        self.radioBAT.setText(_translate("MainWindow", "BAT"))
        self.radioBWL.setText(_translate("MainWindow", "BWL"))
        self.radioAR.setText(_translate("MainWindow", "AR"))
        self.radioWK.setText(_translate("MainWindow", "WK"))
        self.label_15.setText(_translate("MainWindow", ">>"))
        self.label_2.setText(_translate("MainWindow", "Points Used: "))
        self.pointsUsed.setText(_translate("MainWindow", "###"))
        self.radioTeamName.setText(_translate("MainWindow", "Team Name"))
        self.TeamName.setText(_translate("MainWindow", "###"))
        self.SaveButton.setText(_translate("MainWindow", "Save"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))
    
    def reset(self):
        self.AvailablePlayersList.clear()
        self.SelectedPlayerList.clear()
        self.batsmen=[]
        self.bowlers=[]
        self.allrounders=[]
        self.wicketkeepers=[]
        self.counter=0
        self.batcount=0
        self.bwlcount=0
        self.arcount=0
        self.wkcount=0
        self.poiAvail=1000
        self.poiUsed=0

    selPlayers=[]
    batsmen=[]
    bowlers=[]
    allrounders=[]
    wicketkeepers=[]
    counter=0
    batcount=0
    bwlcount=0
    arcount=0
    wkcount=0
    poiAvail=1000
    poiUsed=0
    savedTeams=[]
    name=''
    gamedb=sqlite3.connect('database.db')
    dbcur=gamedb.cursor()
    font = QtGui.QFont()
    font.setFamily("Arial")
    font.setPointSize(12)
    font.setBold(True)
    font.setWeight(75)

    def databaseload(self,MainWindow):
        self.dbcur.execute("SELECT player from stats")
        players=self.dbcur.fetchall()
        for i in players:
            self.AvailablePlayersList.addItem(i[0])
        self.dbcur.execute("SELECT player from stats where ctg='BAT'")
        players=self.dbcur.fetchall()
        for i in players:
            self.batsmen.append(i[0])
        self.dbcur.execute("SELECT player from stats where ctg='BWL'")
        players=self.dbcur.fetchall()
        for i in players:
            self.bowlers.append(i[0])
        self.dbcur.execute("SELECT player from stats where ctg='AR'")
        players=self.dbcur.fetchall()
        for i in players:
            self.allrounders.append(i[0])
        self.dbcur.execute("SELECT player from stats where ctg='WK'")
        players=self.dbcur.fetchall()
        for i in players:
            self.wicketkeepers.append(i[0])

    def getTeamName(self):
        self.teamselected=False
        self.name, temp = QtWidgets.QInputDialog.getText(self, 'Team Name', 'Enter a Unique Team-Name:')

        if self.name not in self.savedTeams:
            self.teamselected=True
            _translate=QtCore.QCoreApplication.translate
            self.TeamName.setText(_translate("MainWindow",str(self.name)))
        else:
            #team Already exists popup message
            self.errorMessage("Team Already Exists!")
        

    def openTeam(self,MainWindow):
        self.name, temp = QtWidgets.QInputDialog.getText(self, 'Team Name', 'Enter a Unique Team-Name:')

        if self.name not in self.savedTeams:
            #team Doesn't exists popup message
            self.errorMessage("Team Doesn't Exist!")
        else:    
            self.reset()
            self.databaseload(MainWindow)
            self.dbcur.execute("SELECT players from teams where name=?",(self.name,))
            temp=self.dbcur.fetchall()[0][0]
            self.selPlayers=list(map(str,temp.split(',')))
            for i in self.selPlayers:
                self.SelectedPlayerList.addItem(i)
                self.dbcur.execute("SELECT ctg from stats where player=?",(i,))
                playerctg=self.dbcur.fetchall()[0][0]
                self.dbcur.execute("SELECT value from stats where player=?",(i,))
                playerValue=self.dbcur.fetchall()[0][0]
                self.poiUsed+=playerValue
                if playerctg=='BAT':
                    self.batsmen.remove(i)
                    self.batcount+=1
                elif playerctg=='BWL':
                    self.bowlers.remove(i)
                    self.bwlcount+=1
                elif playerctg=='AR':
                    self.allrounders.remove(i)
                    self.arcount+=1
                elif playerctg=='WK':
                    self.wicketkeepers.remove(i)
                    self.wkcount+=1
            self.radioBAT.setChecked(True)
            self.radBatList(MainWindow)
            self.counter=11
            self.progressBar.setProperty("value", self.counter)
            self.poiAvail=1000-self.poiUsed
            _translate = QtCore.QCoreApplication.translate
            self.TeamName.setText(_translate("MainWindow",str(self.name)))
            self.countupdate(MainWindow)

    def newTeam(self,MainWindow):
        self.AvailablePlayersList.clear()
        self.SelectedPlayerList.clear()
        self.getTeamName()

        if self.teamselected:
            self.selPlayers=[]
            self.batsmen=[]
            self.bowlers=[]
            self.allrounders=[]
            self.wicketkeepers=[]
            self.counter=0
            self.batcount=0
            self.bwlcount=0
            self.arcount=0
            self.wkcount=0
            self.poiAvail=1000
            self.poiUsed=0
            self.databaseload(MainWindow)
            self.countupdate(MainWindow)

    def countupdate(self,MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.noofbat.setText(_translate("MainWindow",str(self.batcount)))
        self.noofbwl.setText(_translate("MainWindow",str(self.bwlcount)))
        self.noofar.setText(_translate("MainWindow",str(self.arcount)))
        self.noofwk.setText(_translate("MainWindow",str(self.wkcount)))
        self.pointsAvailable.setText(_translate("MainWindow",str(self.poiAvail)))
        self.pointsUsed.setText(_translate("MainWindow",str(self.poiUsed)))    

    def onClickEvents(self,MainWindow):
        self.radioBAT.clicked.connect(self.radBatList)
        self.radioBWL.clicked.connect(self.radBwlList)
        self.radioAR.clicked.connect(self.radArList)
        self.radioWK.clicked.connect(self.radWkList)
        self.AvailablePlayersList.itemDoubleClicked.connect(self.removeAvailablePlayersList)
        self.SelectedPlayerList.itemDoubleClicked.connect(self.removeSelectedPlayerList)
        self.actionNEW_Team.triggered.connect(self.newTeam)
        self.actionSAVE_Team.triggered.connect(self.saveTeam)
        self.SaveButton.clicked.connect(self.saveTeam)
        self.actionOPEN_Team.triggered.connect(self.openTeam)
        self.actionEVALUATE_Team.triggered.connect(self.Evaluate)

    def radBatList(self,MainWindow):
        if self.radioBAT.isChecked()==True:
            self.AvailablePlayersList.clear()
            self.dbcur.execute("SELECT player from stats where ctg='BAT'")
            players=self.dbcur.fetchall()
            for i in players:
                if i[0] not in self.selPlayers:
                    self.AvailablePlayersList.addItem(i[0])

    def radBwlList(self,MainWindow):
        if self.radioBWL.isChecked()==True:
            self.AvailablePlayersList.clear()
            self.dbcur.execute("SELECT player from stats where ctg='BWL'")
            players=self.dbcur.fetchall()
            for i in players:
                if i[0] not in self.selPlayers:
                    self.AvailablePlayersList.addItem(i[0])

    def radArList(self,MainWindow):
        if self.radioAR.isChecked()==True:
            self.AvailablePlayersList.clear()
            self.dbcur.execute("SELECT player from stats where ctg='AR'")
            players=self.dbcur.fetchall()
            for i in players:
                if i[0] not in self.selPlayers:
                    self.AvailablePlayersList.addItem(i[0])

    def radWkList(self,MainWindow):
        if self.radioWK.isChecked()==True:
            self.AvailablePlayersList.clear()
            self.dbcur.execute("SELECT player from stats where ctg='WK'")
            players=self.dbcur.fetchall()
            for i in players:
                if i[0] not in self.selPlayers:
                    self.AvailablePlayersList.addItem(i[0])

    def removeAvailablePlayersList(self, item):
        _translate = QtCore.QCoreApplication.translate
        self.dbcur.execute("SELECT value from stats where player=?",(item.text(),))
        playerValue=self.dbcur.fetchall()[0][0]
        if self.counter==10 and item.text() not in self.wicketkeepers and self.wkcount==0:
            self.errorMessage("Select Atleast One Wicketkeeper!")
            return

        if self.counter<11 and self.poiAvail>=playerValue:
            if item.text() in self.batsmen:
                if self.batcount==4:
                    self.errorMessage("Cannot Add More than 4 batsmen!")
                    return
                else:
                    self.batsmen.remove(item.text())
                    self.batcount+=1
                    self.noofbat.setText(_translate("MainWindow",str(self.batcount)))
            if item.text() in self.bowlers:
                if self.bwlcount==4:
                    self.errorMessage("Cannot Add More than 4 bowlers!")
                    return
                else:
                    self.bowlers.remove(item.text())
                    self.bwlcount+=1
                    self.noofbwl.setText(_translate("MainWindow",str(self.bwlcount)))
            if item.text() in self.allrounders:
                if self.arcount==4:
                    self.errorMessage("Cannot Add More than 4 Allrounders!")
                    return
                else:
                    self.allrounders.remove(item.text())
                    self.arcount+=1
                    self.noofar.setText(_translate("MainWindow",str(self.arcount)))
            if item.text() in self.wicketkeepers:
                if self.wkcount==1:
                    self.errorMessage("Cannot Add More than 1 Wicketkeeper!")
                    return
                else:
                    self.wicketkeepers.remove(item.text())
                    self.wkcount+=1
                    self.noofwk.setText(_translate("MainWindow",str(self.wkcount)))

            self.selPlayers.append(item.text())
            self.AvailablePlayersList.takeItem(self.AvailablePlayersList.row(item))
            self.SelectedPlayerList.addItem(item.text())
            self.poiAvail-=playerValue
            self.pointsAvailable.setText(_translate("MainWindow",str(self.poiAvail)))
            self.poiUsed+=playerValue
            self.pointsUsed.setText(_translate("MainWindow",str(self.poiUsed)))
            self.counter+=1
            self.progressBar.setProperty("value", self.counter)
            if self.counter==11:
                self.SaveButton.setEnabled(True)
                self.actionSAVE_Team.setEnabled(True)
        else:
            if self.counter==11:
                self.errorMessage("Team Full! Cannot Add Players More Than 11")
            else:
                self.errorMessage("Not Enough Points!")

    def removeSelectedPlayerList(self, item):
        _translate = QtCore.QCoreApplication.translate
        self.selPlayers.remove(item.text())
        self.dbcur.execute("SELECT ctg from stats where player=?",(item.text(),))
        playerctg=self.dbcur.fetchall()[0][0]
        self.dbcur.execute("SELECT value from stats where player=?",(item.text(),))
        playerValue=self.dbcur.fetchall()[0][0]

        if playerctg=='BAT':
            self.batsmen.append(item.text())
            self.batcount-=1
            self.noofbat.setText(_translate("MainWindow",str(self.batcount)))
            if self.radioBAT.isChecked()==True:
                self.AvailablePlayersList.addItem(item.text())

        elif playerctg=='BWL':
            self.bowlers.append(item.text())
            self.bwlcount-=1
            self.noofbwl.setText(_translate("MainWindow",str(self.bwlcount)))
            if self.radioBWL.isChecked()==True:
                self.AvailablePlayersList.addItem(item.text())

        elif playerctg=='AR':
            self.allrounders.append(item.text())
            self.arcount-=1
            self.noofar.setText(_translate("MainWindow",str(self.arcount)))
            if self.radioAR.isChecked()==True:
                self.AvailablePlayersList.addItem(item.text())

        elif playerctg=='WK':
            self.wicketkeepers.append(item.text())
            self.wkcount-=1
            self.noofwk.setText(_translate("MainWindow",str(self.wkcount)))
            if self.radioWK.isChecked()==True:
                self.AvailablePlayersList.addItem(item.text())
                 
        if self.radioBAT.isChecked()==False and self.radioBWL.isChecked()==False and self.radioAR.isChecked()==False and self.radioWK.isChecked()==False:
            self.AvailablePlayersList.addItem(item.text())

        self.SelectedPlayerList.takeItem(self.SelectedPlayerList.row(item))
        self.counter-=1
        self.progressBar.setProperty("value", self.counter)
        self.poiAvail+=playerValue
        self.pointsAvailable.setText(_translate("MainWindow",str(self.poiAvail)))
        self.poiUsed-=playerValue
        self.pointsUsed.setText(_translate("MainWindow",str(self.poiUsed)))
        self.SaveButton.setEnabled(False)
        self.actionSAVE_Team.setEnabled(False)

    def errorMessage(self,message):
        self.popup=QtWidgets.QMessageBox()
        self.popup.setText(message)
        self.popup.setIcon(self.popup.Information)
        self.popup.setWindowTitle("Application Message")
        self.popup.setStandardButtons(self.popup.Ok)
        self.popup.exec()

    def saveTeam(self,MainWindow):
        playersString=''
        for i in self.selPlayers:
            playersString+=i+','
        playersString=playersString[:-1]

        if self.name not in self.savedTeams:
            self.dbcur.execute('INSERT INTO teams (name, players, value) VALUES ( ?, ?, ? )', (self.name,playersString,self.poiUsed))
        else:
            self.dbcur.execute('UPDATE teams SET players=?,value=? where name=?',(playersString,self.poiUsed,self.name))

        self.gamedb.commit()
        self.SaveButton.setEnabled(False)
        self.actionOPEN_Team.setEnabled(True)
        self.actionEVALUATE_Team.setEnabled(True)
        self.actionSAVE_Team.setEnabled(False)
        #saved successfully pop-up message
        self.errorMessage("Team Saved")
        self.savedTeams.append(self.savedTeams)
    
    def Evaluate(self):
        self.window=QtWidgets.QWidget()
        self.ui=Ui_Form()
        self.ui.setupUi(self.window)
        self.ui.windowload(self.window)
        self.ui.signal.connect(self.ui.playerload)
        self.window.show()
        
    @QtCore.pyqtSlot()

    def TeamCheck(self,MainWindow):
        self.dbcur.execute("SELECT count(*) from teams")
        noOfTeams=self.dbcur.fetchall()[0][0]
        if noOfTeams!=0:
            self.actionOPEN_Team.setEnabled(True)
            self.actionEVALUATE_Team.setEnabled(True)
            self.dbcur.execute("SELECT name from teams")
            teamlist=self.dbcur.fetchall()
            for i in teamlist:
                self.savedTeams.append(i[0])

class Ui_Form(QtWidgets.QWidget):

    signal=pyqtSignal()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(584, 591)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        Form.setStyleSheet("background-color:rgb(161, 161, 161);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_7 = QtWidgets.QGroupBox(Form)
        self.groupBox_7.setStyleSheet("background-color:rgb(199, 255, 240);\n"
"border-color:rgb(199, 255, 240);\n"
"border-radius:10px;\n"
"border:2px solid black;")
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox_7)
        self.label.setStyleSheet("font-weight: bold;\n"
"font-size:20px;\n"
"border:0px;\n"
"text-align:center;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.DropDownGroup = QtWidgets.QGroupBox(self.groupBox_7)
        self.DropDownGroup.setStyleSheet("border:0px;")
        self.DropDownGroup.setTitle("")
        self.DropDownGroup.setObjectName("DropDownGroup")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.DropDownGroup)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(self.DropDownGroup)
        self.comboBox.setMinimumSize(QtCore.QSize(250, 0))
        self.comboBox.setMaximumSize(QtCore.QSize(250, 50))

        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color:rgb(229, 167, 255);\n"
"border-radius:0px;\n"
"border:2px solid black;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(1, "")
        self.horizontalLayout.addWidget(self.comboBox)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout.addItem(spacerItem)
        self.comboBox_2 = QtWidgets.QComboBox(self.DropDownGroup)
        self.comboBox_2.setMinimumSize(QtCore.QSize(250, 0))
        self.comboBox_2.setMaximumSize(QtCore.QSize(250, 16777215))

        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("background-color:rgb(229, 167, 255);\n"
"border:2px solid black;\n"
"border-radius:0px;")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_2)
        self.verticalLayout_2.addWidget(self.DropDownGroup)
        self.verticalLayout.addWidget(self.groupBox_7)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setStyleSheet("border:0px;")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_6.setStyleSheet("background-color:rgb(255, 170, 127);\n"
"border-radius:10px;\n"
"border:2px solid black;")
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.groupBox_6)
        self.label_2.setStyleSheet("font-weight: bold;\n"
"font-size:15px;border:0px;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.verticalLayout_3.addWidget(self.groupBox_6)
        self.listView_2 = QtWidgets.QListWidget(self.groupBox_3)

        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.listView_2.setFont(font)
        self.listView_2.setStyleSheet("background-color:rgb(255, 255, 127);\n"
"border-radius:20px;\n"
"border:2px solid black;")
        self.listView_2.setObjectName("listView_2")
        self.verticalLayout_3.addWidget(self.listView_2)
        self.horizontalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_5.setStyleSheet("background-color:rgb(255, 170, 127);\n"
"border-radius:10px;\n"
"border:2px solid black;")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.label_3.setStyleSheet("font-weight: bold;\n"
"font-size:15px;border:0px;")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.pointsScored = QtWidgets.QLabel(self.groupBox_5)
        self.pointsScored.setStyleSheet("border:0px;color:blue;font-weight: bold;\n"
"font-size:15px;")
        self.pointsScored.setObjectName("pointsScored")
        self.horizontalLayout_3.addWidget(self.pointsScored)
        self.verticalLayout_4.addWidget(self.groupBox_5)
        self.listView = QtWidgets.QListWidget(self.groupBox_4)
        self.listView.setMinimumSize(QtCore.QSize(200, 350))
        self.listView_2.setMinimumSize(QtCore.QSize(200, 350))

        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.listView.setFont(font)
        self.listView.setStyleSheet("background-color:rgb(255, 255, 127);\n"
"border-radius:20px;\n"
"border:2px solid black;")
        self.listView.setObjectName("listView")
        self.verticalLayout_4.addWidget(self.listView)
        self.horizontalLayout_2.addWidget(self.groupBox_4)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setStyleSheet("border:0px;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setEnabled(True)
        self.pushButton.setMinimumSize(QtCore.QSize(104, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(200, 50))
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setStyleSheet("background-color:rgb(148, 205, 255);\n"
"border-radius:10px;\n"
"border:2px solid black;\n"
"font-weight: bold;\n"
"font-size:20px;\n"
"min-width:100px;")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.groupBox)
        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)
        '''self.comboBox.currentIndexChanged(self.playerload)
        self.comboBox_2.currentIndexChanged(self.pointsload)'''

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Evaluate"))
        self.label.setText(_translate("Form", "Evaluate the performance of Your Team"))
        self.comboBox.setItemText(0, _translate("Form", "Select Team"))
        self.comboBox_2.setItemText(0, _translate("Form", "Select Match"))
        self.label_2.setText(_translate("Form", "Team-Players"))
        self.label_3.setText(_translate("Form", "Points: "))
        self.pointsScored.setText(_translate("Form", "###"))
        self.pushButton.setText(_translate("Form", "Evaluate Score"))
        self.pushButton.clicked.connect(self.evaluateScore)
        
    gamedb=sqlite3.connect('database.db')
    dbcur=gamedb.cursor()

    def windowload(self,Form):
        self.dbcur.execute("SELECT name from teams")
        teamlist=self.dbcur.fetchall()
        for i in teamlist:
            self.comboBox.addItem(i[0])
        self.comboBox_2.addItem("Match-1")
        #I have included data for match 1 alone in database, hence the other matches also takes same data as match-1
        self.comboBox_2.addItem("Match-2")
        self.comboBox_2.addItem("Match-3")
        self.comboBox_2.addItem("Match-4")

    def playerload(self):
        self.listView_2.clear()
        self.listView.clear()

        if self.comboBox.currentIndex()!=0:
            self.name=self.comboBox.currentText()
            self.dbcur.execute("SELECT players from teams where name=?",(self.name,))
            temp=self.dbcur.fetchall()[0][0]
            self.Players=list(map(str,temp.split(',')))
            for i in self.Players:
                self.listView_2.addItem(i)
            self.teampoints=0

            for i in self.Players:
                self.points=0
                
                #Batting-Points Calculation
                self.dbcur.execute("SELECT Scored from match where Player=?",(i,))
                runs=self.dbcur.fetchall()[0][0]
                self.points+=runs//2
                if runs>=100:
                    self.points+=15
                elif runs>=50:
                    self.points+=5
                self.dbcur.execute("SELECT Faced from match where Player=?",(i,))
                faced=self.dbcur.fetchall()[0][0]
                if faced!=0:
                    if runs/faced>100:
                        self.points+=6
                    elif runs/faced>=80:
                        self.points+=2
                self.dbcur.execute("SELECT Fours from match where Player=?",(i,))
                fours=self.dbcur.fetchall()[0][0]
                self.dbcur.execute("SELECT Sixes from match where Player=?",(i,))
                sixes=self.dbcur.fetchall()[0][0]
                self.points+=fours+2*sixes

                #Bowling-points Calculation
                self.dbcur.execute("SELECT Wkts from match where Player=?",(i,))
                wkts=self.dbcur.fetchall()[0][0]
                self.dbcur.execute("SELECT Bowled from match where Player=?",(i,))
                bowled=self.dbcur.fetchall()[0][0]
                self.dbcur.execute("SELECT Given from match where Player=?",(i,))
                given=self.dbcur.fetchall()[0][0]
                self.points+=wkts*10
                if wkts>=5:
                    self.points+=15
                elif wkts>=3:
                    self.points+=5
                if bowled!=0:
                    economy=given/(bowled/6)
                    if economy<=2:
                        self.points+=10
                    elif economy<=3.5:
                        self.points+=7
                    elif economy<=4.5:
                        self.points+=4
                
                #Fielding-Points Calculation
                self.dbcur.execute("SELECT Catches from match where Player=?",(i,))
                catches=self.dbcur.fetchall()[0][0]
                self.points+=10*catches
                self.dbcur.execute("SELECT Stumping from match where Player=?",(i,))
                stumping=self.dbcur.fetchall()[0][0]
                self.points+=10*stumping
                self.dbcur.execute("SELECT RO from match where Player=?",(i,))
                runouts=self.dbcur.fetchall()[0][0]
                self.points+=10*runouts

                self.listView.addItem(str(self.points))
                self.teampoints+=self.points
            self.pointsScored.setText(str(self.teampoints))

    def evaluateScore(self,Form):
        self.signal.emit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.TeamCheck(MainWindow)
    ui.onClickEvents(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
