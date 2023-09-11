
from PyQt5 import QtCore, QtGui, QtWidgets
import icons_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1103, 830)
        MainWindow.setMinimumSize(QtCore.QSize(1103, 830))
        MainWindow.setMaximumSize(QtCore.QSize(1103, 830))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icons8-hacker-70.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(60, 60))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0.015, y1:0.75, x2:0.87, y2:0.0681818, stop:0 rgba(51, 147, 41, 255), stop:0.39801 rgba(0, 0, 0, 255), stop:1 rgba(63, 145, 0, 255));}")
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 20, 1081, 91))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 41, 41))
        self.label.setObjectName("label")
        self.input_ip = QtWidgets.QLineEdit(self.centralwidget)
        self.input_ip.setGeometry(QtCore.QRect(50, 30, 113, 22))
        self.input_ip.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0);")
        self.input_ip.setObjectName("input_ip")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 20, 61, 41))
        self.label_2.setObjectName("label_2")
        self.input_port = QtWidgets.QLineEdit(self.centralwidget)
        self.input_port.setGeometry(QtCore.QRect(230, 30, 61, 22))
        self.input_port.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 75 9pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.input_port.setObjectName("input_port")
        self.push_dinle = QtWidgets.QPushButton(self.centralwidget)
        self.push_dinle.setGeometry(QtCore.QRect(310, 20, 171, 41))
        self.push_dinle.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(30, 33, 41);")
        self.push_dinle.setIcon(icon)
        self.push_dinle.setIconSize(QtCore.QSize(25, 25))
        self.push_dinle.setObjectName("push_dinle")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 70, 1311, 811))
        self.groupBox.setStyleSheet("border-color:rgb(0,0,0);\n"
"\n"
"")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 13, 341, 760))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.push_ses_kaydedici = QtWidgets.QPushButton(self.formLayoutWidget)
        self.push_ses_kaydedici.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"background-color: rgb(30, 33, 41);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.push_ses_kaydedici.setObjectName("push_ses_kaydedici")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.push_ses_kaydedici)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(6, 83, 15, 255));\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_3)
        self.push_snap = QtWidgets.QPushButton(self.formLayoutWidget)
        self.push_snap.setStyleSheet("\n"
"background-color: rgb(30, 33, 41);\n"
"color: rgb(255, 255, 255);")
        self.push_snap.setObjectName("push_snap")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.push_snap)
        self.label_15 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_15.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(6, 83, 15, 255));\n"
"color: rgb(255, 255, 255);")
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_15)
        self.push_sound = QtWidgets.QPushButton(self.formLayoutWidget)
        self.push_sound.setStyleSheet("background-color: rgb(30, 33, 41);\n"
"color: rgb(255, 255, 255);")
        self.push_sound.setObjectName("push_sound")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.push_sound)
        self.label_18 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_18.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(6, 83, 15, 255));\n"
"color: rgb(255, 255, 255);")
        self.label_18.setObjectName("label_18")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_18)
        self.push_wifi = QtWidgets.QPushButton(self.formLayoutWidget)
        self.push_wifi.setStyleSheet("background-color: rgb(30, 33, 41);\n"
"color: rgb(255, 255, 255);")
        self.push_wifi.setObjectName("push_wifi")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.push_wifi)
        self.label_17 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_17.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(6, 83, 15, 255));\n"
"color: rgb(255, 255, 255);")
        self.label_17.setObjectName("label_17")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_17)
        self.push_tasklist = QtWidgets.QPushButton(self.formLayoutWidget)
        self.push_tasklist.setStyleSheet("background-color: rgb(30, 33, 41);\n"
"color: rgb(255, 255, 255);")
        self.push_tasklist.setObjectName("push_tasklist")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.push_tasklist)
        self.label_16 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_16.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(6, 83, 15, 255));\n"
"color: rgb(255, 255, 255);")
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_16)
        self.push_shutdown = QtWidgets.QPushButton(self.formLayoutWidget)
        self.push_shutdown.setStyleSheet("background-color: rgb(30, 33, 41);\n"
"\n"
"color: rgb(255, 255, 255);")
        self.push_shutdown.setObjectName("push_shutdown")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.push_shutdown)
        self.label_19 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_19.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(6, 83, 15, 255));\n"
"color: rgb(255, 255, 255);")
        self.label_19.setObjectName("label_19")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.label_19)
        self.push_video = QtWidgets.QPushButton(self.formLayoutWidget)
        self.push_video.setStyleSheet("background-color: rgb(30, 33, 41);\n"
"color: rgb(255, 255, 255);")
        self.push_video.setObjectName("push_video")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.push_video)
        self.push_persistence = QtWidgets.QPushButton(self.formLayoutWidget)
        self.push_persistence.setStyleSheet("background-color: rgb(30, 33, 41);\n"
"color: rgb(255, 255, 255);")
        self.push_persistence.setObjectName("push_persistence")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.push_persistence)
        self.label_38 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_38.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(6, 83, 15, 255));\n"
"color: rgb(255, 255, 255);")
        self.label_38.setObjectName("label_38")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.label_38)
        self.push_upload = QtWidgets.QPushButton(self.formLayoutWidget)
        self.push_upload.setStyleSheet("background-color: rgb(30, 33, 41);\n"
"color: rgb(255, 255, 255);")
        self.push_upload.setObjectName("push_upload")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.push_upload)
        self.label_22 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_22.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(6, 83, 15, 255));\n"
"color: rgb(255, 255, 255);")
        self.label_22.setObjectName("label_22")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.label_22)
        self.push_wallpaper = QtWidgets.QPushButton(self.formLayoutWidget)
        self.push_wallpaper.setStyleSheet("background-color: rgb(30, 33, 41);\n"
"color: rgb(255, 255, 255);")
        self.push_wallpaper.setObjectName("push_wallpaper")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.push_wallpaper)
        self.label_24 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_24.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(6, 83, 15, 255));\n"
"color: rgb(255, 255, 255);")
        self.label_24.setObjectName("label_24")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.label_24)
        self.push_alert = QtWidgets.QPushButton(self.formLayoutWidget)
        self.push_alert.setStyleSheet("background-color: rgb(30, 33, 41);\n"
"color: rgb(255, 255, 255);")
        self.push_alert.setObjectName("push_alert")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.push_alert)
        self.label_23 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_23.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(6, 83, 15, 255));\n"
"color: rgb(255, 255, 255);")
        self.label_23.setObjectName("label_23")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.label_23)
        self.push_screenshot = QtWidgets.QPushButton(self.formLayoutWidget)
        self.push_screenshot.setStyleSheet("background-color: rgb(30, 33, 41);\n"
"color: rgb(255, 255, 255);")
        self.push_screenshot.setObjectName("push_screenshot")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.push_screenshot)
        self.label_37 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_37.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(6, 83, 15, 255));\n"
"color: rgb(255, 255, 255);")
        self.label_37.setObjectName("label_37")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.label_37)
        self.push_ekran_kaydedici = QtWidgets.QPushButton(self.formLayoutWidget)
        self.push_ekran_kaydedici.setStyleSheet("background-color: rgb(30, 33, 41);\n"
"color: rgb(255, 255, 255);")
        self.push_ekran_kaydedici.setObjectName("push_ekran_kaydedici")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.push_ekran_kaydedici)
        self.label_36 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_36.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(6, 83, 15, 255));\n"
"color: rgb(255, 255, 255);")
        self.label_36.setObjectName("label_36")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.label_36)
        self.push_keylogger = QtWidgets.QPushButton(self.formLayoutWidget)
        self.push_keylogger.setStyleSheet("background-color: rgb(30, 33, 41);\n"
"color: rgb(255, 255, 255);")
        self.push_keylogger.setObjectName("push_keylogger")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.push_keylogger)
        self.label_43 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_43.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(6, 83, 15, 255));\n"
"color: rgb(255, 255, 255);")
        self.label_43.setObjectName("label_43")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.label_43)
        self.push_speak = QtWidgets.QPushButton(self.formLayoutWidget)
        self.push_speak.setStyleSheet("background-color: rgb(30, 33, 41);\n"
"color: rgb(255, 255, 255);")
        self.push_speak.setObjectName("push_speak")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.push_speak)
        self.label_40 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_40.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(6, 83, 15, 255));\n"
"color: rgb(255, 255, 255);")
        self.label_40.setObjectName("label_40")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.label_40)
        self.push_download = QtWidgets.QPushButton(self.formLayoutWidget)
        self.push_download.setStyleSheet("background-color: rgb(30, 33, 41);\n"
"color: rgb(255, 255, 255);")
        self.push_download.setObjectName("push_download")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.push_download)
        self.label_39 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_39.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(6, 83, 15, 255));\n"
"color: rgb(255, 255, 255);")
        self.label_39.setObjectName("label_39")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.label_39)
        self.push_whoami = QtWidgets.QPushButton(self.formLayoutWidget)
        self.push_whoami.setStyleSheet("background-color: rgb(30, 33, 41);\n"
"color: rgb(255, 255, 255);")
        self.push_whoami.setObjectName("push_whoami")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.push_whoami)
        self.label_41 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_41.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(6, 83, 15, 255));\n"
"color: rgb(255, 255, 255);")
        self.label_41.setObjectName("label_41")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.label_41)
        self.push_crunk = QtWidgets.QPushButton(self.formLayoutWidget)
        self.push_crunk.setStyleSheet("background-color: rgb(30, 33, 41);\n"
"color: rgb(255, 255, 255);")
        self.push_crunk.setObjectName("push_crunk")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.LabelRole, self.push_crunk)
        self.label_42 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_42.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(6, 83, 15, 255));\n"
"color: rgb(255, 255, 255);")
        self.label_42.setObjectName("label_42")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.FieldRole, self.label_42)
        self.push_indirilen_veriler = QtWidgets.QPushButton(self.formLayoutWidget)
        self.push_indirilen_veriler.setStyleSheet("background-color: rgb(30, 33, 41);\n"
"color: rgb(255, 255, 255);")
        self.push_indirilen_veriler.setObjectName("push_indirilen_veriler")
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.LabelRole, self.push_indirilen_veriler)
        self.label_21 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_21.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(6, 83, 15, 255));\n"
"color: rgb(255, 255, 255);")
        self.label_21.setObjectName("label_21")
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.FieldRole, self.label_21)
        self.push_picture = QtWidgets.QPushButton(self.formLayoutWidget)
        self.push_picture.setStyleSheet("background-color: rgb(30, 33, 41);\n"
"color: rgb(255, 255, 255);")
        self.push_picture.setObjectName("push_picture")
        self.formLayout.setWidget(19, QtWidgets.QFormLayout.LabelRole, self.push_picture)
        self.push_close = QtWidgets.QPushButton(self.formLayoutWidget)
        self.push_close.setStyleSheet("background-color: rgb(30, 33, 41);\n"
"color: rgb(255, 255, 255);")
        self.push_close.setObjectName("push_close")
        self.formLayout.setWidget(20, QtWidgets.QFormLayout.LabelRole, self.push_close)
        self.label_35 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_35.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(6, 83, 15, 255));\n"
"color: rgb(255, 255, 255);")
        self.label_35.setObjectName("label_35")
        self.formLayout.setWidget(20, QtWidgets.QFormLayout.FieldRole, self.label_35)
        self.label_20 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_20.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(6, 83, 15, 255));\n"
"color: rgb(255, 255, 255);")
        self.label_20.setObjectName("label_20")
        self.formLayout.setWidget(19, QtWidgets.QFormLayout.FieldRole, self.label_20)
        self.label_44 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_44.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(6, 83, 15, 255));\n"
"color: rgb(255, 255, 255);")
        self.label_44.setObjectName("label_44")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.label_44)
        self.input_ekrankayit_spin = QtWidgets.QSpinBox(self.groupBox)
        self.input_ekrankayit_spin.setGeometry(QtCore.QRect(350, 400, 41, 41))
        self.input_ekrankayit_spin.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.input_ekrankayit_spin.setObjectName("input_ekrankayit_spin")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(680, 10, 81, 21))
        self.label_9.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(84, 208, 68);\n"
"border-radius:9px;")
        self.label_9.setObjectName("label_9")
        self.input_cmd = QtWidgets.QTextEdit(self.groupBox)
        self.input_cmd.setGeometry(QtCore.QRect(400, 260, 591, 171))
        self.input_cmd.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(84, 208, 68);\n"
"border: 0.5px solid #828790;")
        self.input_cmd.setObjectName("input_cmd")
        self.input_ses_spin = QtWidgets.QSpinBox(self.groupBox)
        self.input_ses_spin.setGeometry(QtCore.QRect(350, 10, 41, 31))
        self.input_ses_spin.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.input_ses_spin.setObjectName("input_ses_spin")
        self.push_cmd_calistir = QtWidgets.QPushButton(self.groupBox)
        self.push_cmd_calistir.setGeometry(QtCore.QRect(1000, 260, 71, 28))
        self.push_cmd_calistir.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(30, 33, 41);")
        self.push_cmd_calistir.setObjectName("push_cmd_calistir")
        self.push_cmd_reset = QtWidgets.QPushButton(self.groupBox)
        self.push_cmd_reset.setGeometry(QtCore.QRect(1000, 290, 31, 31))
        self.push_cmd_reset.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border:none;\n"
"background-color: rgb(30, 33, 41);\n"
"border-radius:15px;")
        self.push_cmd_reset.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icons8-restart-144 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.push_cmd_reset.setIcon(icon1)
        self.push_cmd_reset.setIconSize(QtCore.QSize(35, 35))
        self.push_cmd_reset.setObjectName("push_cmd_reset")
        self.output_cmd = QtWidgets.QScrollArea(self.groupBox)
        self.output_cmd.setGeometry(QtCore.QRect(400, 460, 671, 281))
        self.output_cmd.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:1 rgba(0, 0, 0, 147));\n"
"border: 0.5px solid #828790;")
        self.output_cmd.setWidgetResizable(True)
        self.output_cmd.setObjectName("output_cmd")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 669, 279))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.outputcmdlabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.outputcmdlabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"border:none;")
        self.outputcmdlabel.setObjectName("outputcmdlabel")
        self.gridLayout.addWidget(self.outputcmdlabel, 0, 0, 1, 1)
        self.output_cmd.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea.setGeometry(QtCore.QRect(400, 35, 671, 201))
        self.scrollArea.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:1 rgba(0, 0, 0, 147));\n"
"QScrollBar{\n"
"background-color: rgb(25,2,255);\n"
"border: 0.5px solid #828790;\n"
"};")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.help_Scroll = QtWidgets.QWidget()
        self.help_Scroll.setGeometry(QtCore.QRect(0, 0, 648, 334))
        self.help_Scroll.setStyleSheet("")
        self.help_Scroll.setObjectName("help_Scroll")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.help_Scroll)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.help_label = QtWidgets.QLabel(self.help_Scroll)
        self.help_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:1 rgba(0, 0, 0, 147));")
        self.help_label.setObjectName("help_label")
        self.gridLayout_2.addWidget(self.help_label, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.help_Scroll)
        self.input_video_spin = QtWidgets.QSpinBox(self.groupBox)
        self.input_video_spin.setGeometry(QtCore.QRect(350, 200, 41, 41))
        self.input_video_spin.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.input_video_spin.setObjectName("input_video_spin")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(490, 20, 171, 41))
        self.label_5.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius:9px;")
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(870, 30, 161, 31))
        self.label_8.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius:9px;")
        self.label_8.setObjectName("label_8")
        self.push_veriac = QtWidgets.QPushButton(self.centralwidget)
        self.push_veriac.setGeometry(QtCore.QRect(1020, 30, 51, 31))
        self.push_veriac.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(0, 0, 0);")
        self.push_veriac.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icons8-opened-folder-80.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.push_veriac.setIcon(icon2)
        self.push_veriac.setIconSize(QtCore.QSize(29, 30))
        self.push_veriac.setObjectName("push_veriac")
        self.label_islem_durumu = QtWidgets.QLabel(self.centralwidget)
        self.label_islem_durumu.setGeometry(QtCore.QRect(650, 20, 211, 41))
        self.label_islem_durumu.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius:9px;")
        self.label_islem_durumu.setObjectName("label_islem_durumu")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Backdoorz"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">ip:</span></p></body></html>"))
        self.input_ip.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic;\">ip numarasını giriniz.</span></p></body></html>"))
        self.input_ip.setText(_translate("MainWindow", "127.0.0.1"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">port:</span></p></body></html>"))
        self.input_port.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic;\">port numarasını girin.</span></p></body></html>"))
        self.input_port.setText(_translate("MainWindow", "4242"))
        self.push_dinle.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt; font-style:italic;\">Dinleyiciyi başlat</span></p></body></html>"))
        self.push_dinle.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Listen</p></body></html>"))
        self.push_dinle.setText(_translate("MainWindow", "Dinle"))
        self.push_ses_kaydedici.setText(_translate("MainWindow", "record"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Ses kaydeder</span></p></body></html>"))
        self.push_snap.setText(_translate("MainWindow", "snap"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Fotoğraf Çeker</span></p></body></html>"))
        self.push_sound.setText(_translate("MainWindow", "sound"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Ses Açar</span></p></body></html>"))
        self.push_wifi.setText(_translate("MainWindow", "wifi"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Wifi Menüsünü Açar</span></p></body></html>"))
        self.push_tasklist.setText(_translate("MainWindow", "tasklist"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Görev Yöneticisini Açar</span></p></body></html>"))
        self.push_shutdown.setText(_translate("MainWindow", "shutdown"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Kapatma Menüsünü Açar</span></p></body></html>"))
        self.push_video.setText(_translate("MainWindow", "video"))
        self.push_persistence.setText(_translate("MainWindow", "persistence"))
        self.label_38.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Virüs başlangıca yerleşir</span></p></body></html>"))
        self.push_upload.setText(_translate("MainWindow", "upload"))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Veri Gönderir</span></p></body></html>"))
        self.push_wallpaper.setText(_translate("MainWindow", "wallpaper"))
        self.label_24.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Arkaplanı değiştirir</span></p></body></html>"))
        self.push_alert.setText(_translate("MainWindow", "alert"))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Uyarı mesajı çıkarır</span></p></body></html>"))
        self.push_screenshot.setText(_translate("MainWindow", "screenshot"))
        self.label_37.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Ekran fotoğrafı alır</span></p></body></html>"))
        self.push_ekran_kaydedici.setText(_translate("MainWindow", "s_record"))
        self.label_36.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Ekran kaydı alır</span></p></body></html>"))
        self.push_keylogger.setText(_translate("MainWindow", "keylogger"))
        self.label_43.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Keylogger menüsünü açar</span></p></body></html>"))
        self.push_speak.setText(_translate("MainWindow", "speak"))
        self.label_40.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Kelime Okur</span></p></body></html>"))
        self.push_download.setText(_translate("MainWindow", "download"))
        self.label_39.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Veri alır</span></p></body></html>"))
        self.push_whoami.setText(_translate("MainWindow", "whoami"))
        self.label_41.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Yetkinizi Verir</span></p></body></html>"))
        self.push_crunk.setText(_translate("MainWindow", "crunk"))
        self.label_42.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Hazır fonksiyon menüsünü açar</span></p></body></html>"))
        self.push_indirilen_veriler.setText(_translate("MainWindow", "veriler"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Kaydedilen veri menüsünü açar</span></p></body></html>"))
        self.push_picture.setText(_translate("MainWindow", "picture"))
        self.push_close.setText(_translate("MainWindow", "close"))
        self.label_35.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Bağlantıyı Sonlandırır</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Resim açar</span></p></body></html>"))
        self.label_44.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Video Kaydı alır</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; color:#ffffff;\">CMD</span></p></body></html>"))
        self.input_cmd.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.push_cmd_calistir.setText(_translate("MainWindow", "Çalıştır"))
        #self.outputcmdlabel.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.help_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ff0004;\">1-)</span><span style=\" font-weight:600; color:#ffffff;\">mkdir &lt;name&gt; : Klasör Oluşturur</span></p><p><span style=\" font-weight:600; color:#ff0004;\">2-)</span><span style=\" font-weight:600; color:#ffffff;\">cd || cd .. || cd &lt;path&gt; : Konumu Verir || Bir Klasör geri gider || Konuma gider</span></p><p><span style=\" font-weight:600; color:#ff0004;\">3-)</span><span style=\" font-weight:600; color:#ffffff;\">dir : Bulunduğunuz konumdaki verileri listeler</span></p><p><span style=\" font-weight:600; color:#ff0004;\">4-)</span><span style=\" font-weight:600; color:#ffffff;\"> systeminfo &lt;path&gt; : Hedefin sistem bilgisini alır</span></p><p><span style=\" font-weight:600; color:#ff0004;\">5-)</span><span style=\" font-weight:600; color:#ffffff;\"> getmac &lt;path&gt; : Hedefin mac adresini alır</span></p><p><span style=\" font-weight:600; color:#ff0004;\">6-)</span><span style=\" font-weight:600; color:#ffffff;\">ipconfig &lt;name&gt; : Hedefin ip bilgisini verir</span></p><p><span style=\" font-weight:600; color:#ff0004;\">7-)</span><span style=\" font-weight:600; color:#ffffff;\">rmdir <name> &lt;path&gt; : Hedeften klasör siler </span></p><p><span style=\" font-weight:600; color:#ff0004;\">8-)</span><span style=\" font-weight:600; color:#ffffff;\">driverquery : Hedefin sürücülerini listeler </span></p><p><span style=\" font-weight:600; color:#ff0004;\">9-)</span><span style=\" font-weight:600; color:#ffffff;\"> del <name> &lt;filename&gt; : Hedeften veriyi siler</span></p><p><span style=\" font-weight:600; color:#ff0004;\">Bunlar örnek kodlar. Bütün cmd komutlarını hedefte çalıştırabilirsiniz..</span><br/></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Yapılan İşlem:</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Alınan Veriler:</span></p></body></html>"))
        self.label_islem_durumu.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">Hedef bilgileri bekleniyor..</span></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
