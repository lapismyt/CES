import os
from smtplib import SMTP_SSL as smtp
import sys
import time
from email.message import EmailMessage
import re

if os.sys.platform == "win32":
    def cls():
        os.system("cls")
else:
    def cls():
        os.system("clear")
ascii = """
      ____ _____ ____  
     / ___| ____/ ___| 
    | |   |  _| \___ \ 
    | |___| |___ ___) |
     \____|_____|____/ 
 
"""

def main():
    cls()
    print(ascii)
    print("                 <ВВЕДИТЕ КОЛИЧЕСТВО ПИСЕМ>")
    count = int(input("                  "))
    cls()
    print(ascii)
    print("                <ВВЕДИТЕ ЗАДЕРЖКУ В СЕКУНДАХ>")
    sleep = int(input("                 "))
    with open("mail.txt") as f:
        mail = f.read().strip()
    with open("from.txt") as f:
        fromm = f.read().strip()
    with open("to.txt") as f:
        to = f.read().strip()
    spam(count, sleep, mail, fromm, to)

def spam(count, sleep, mail, fromm, to):
    cls()
    print(ascii)
    fromm = fromm.split("\n")
    frommm = []
    for x in range(len(fromm)):
        frommm.append(fromm[x].split(":"))
    to = to.split("\n")
    for x in frommm:
        try:
            server = smtp(f"smtp.{x[0].split('@')[1]}", 465)
            server.ehlo()
            server.login(x[0], x[1])
            print(f" [+] Удалось войти в аккаунт {x[0]}:{x[1]}")
            for j in to:
                for i in range(count):
                    try:
                        email = EmailMessage()
                        email.charset = "utf-8"
                        email["From"] = x[0]
                        email["To"] = j
                        if "\n\n" in mail:
                            subject = mail.strip().split("\n\n")[0]
                            email["Subject"] = subject
                            email.set_content(mail.replace(subject, "").strip())
                        else:
                            email.set_content(mail.strip())
                        server.sendmail(x[0], j, email.as_string())
                        print(f" [+] Успешно отправлено письмо №{i} с {x[0]} на {j}")
                    except BaseException as err:
                        print(f" [-] Не удалось отправить письмо №{i} с {x[0]} на {j}:")
                        print(repr(err))
                    time.sleep(sleep)
                print(f" [+] Отправлены все письма с {x[0]} на {j}")
            print(f" [+] Отправлены все письма с {x[0]}")
            server.quit()
        except BaseException as err:
            print(f" [-] Не удалось войти в аккаунт {x[0]}:{x[1]}:")
            print(repr(err))
    print(f" [+] Отправлены все письма со всех аккаунтов")
main()
