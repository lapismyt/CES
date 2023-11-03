import os
from smtplib import SMTP_SSL as smtp
import sys
import time
if os.sys.platform == "win32":
    def cls():
        os.system("cls")
else:
    def cls():
        os.system("clear")
ascii = """
            ____ _   _ ____ _____ ___  __  __
           / ___| | | / ___|_   _/ _ \|  \/  |
          | |   | | | \___ \ | || | | | |\/| |
          | |___| |_| |___) || || |_| | |  | |
           \____|\___/|____/ |_| \___/|_|  |_|
  _____                 _ _   ____
 | ____|_ __ ___   __ _(_) | / ___| _ __   __ _ _ __ ___
 |  _| | '_ ` _ \ / _` | | | \___ \| '_ \ / _` | '_ ` _  \\
 | |___| | | | | | (_| | | |  ___) | |_) | (_| | | | | | |
 |_____|_| |_| |_|\__,_|_|_| |____/| .__/ \__,_|_| |_| |_|
                                   |_|

             <={[Сделано для Hackers Academy]}=>
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
                        server.sendmail(x[0], j, mail)
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
