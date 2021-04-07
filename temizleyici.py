import os
import time
os.system("clear")
print ("Hânedan-ı Root Alan Boşaltıcı")
evet = input("TEMİZLEMEK İSTİYOR MUSUNUZ? (evet/hayır)")

while True:
    if evet==("evet"):

	        print("Temizleniyor...")
	        time.sleep(5)
	        os.system("sudo apt-get clean && sudo apt-get autoremove -y  && sudo apt-get autoclean && free -m")
	        print("Başarıyla temizlendi")
	        exit()

    else:
	        print("Görüşmek üzere")
        	exit()
