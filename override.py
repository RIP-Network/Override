import smtplib, ssl
import os
import time
import getpass
from turtle import clear
import sys, os, webbrowser, platform, subprocess, time
from colorama import Fore


#colores
negro = '\033[30m'
rojo = '\033[31m'
verde = '\033[32m'
amarillo = '\033[33m'
azul = '\033[34m'
rosado = '\033[35m'
calipso= '\033[36m'
blanco = '\033[37m'
cierre = '\033[39m'

os.system("clear")

a = open(os.devnull,'w')

print(rojo+"Recuerde usar root"+cierre)
time.sleep(5)

if input("\n\033[1;41;37mADVERTENCIA\033[0;m \033[1;33m¿Desea activar el modo Override seguro?\033\033[0;m [\033[1;32my\033[0;m/\033[1;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
    os.system('clear') 
    print("\n\n\033[1;42;37mADVERTENCIA\033[0;m \033[1;31mDesactivando el modo Override \033[0;m\n\n")
    print(rojo+"Nos veremos muy pronto"+cierre)
    exit(0)

import os
banner = Fore.RED + """
               ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO\
       ::::::;       ;          OOOOO\
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
:::`:::::::`;; ;:::::::::##                OO
::::`:::::::`;::::::::;:::#                OO
`:::::`::::::::::::;'`:;::#                O
`:::::`::::::::;' /  / `:#
::::::`:::::;'  /  /   `#
RIP-Network 
"""
print(banner)
time.sleep(1)
os.system('clear')

print(rojo+"Activando el modo Override"+cierre)
time.sleep(0.2)
print(rojo+"Activando el modo Override"+cierre)
time.sleep(0.2)
print(rojo+"Activando el modo Override"+cierre)
time.sleep(0.2)
print(rojo+"Activando el modo Override"+cierre)
time.sleep(0.2)
print(rojo+"Activando el modo Override"+cierre)
time.sleep(0.2)
print(rojo+"Activando el modo Override"+cierre)
time.sleep(0.2)
print(rojo+"Activando el modo Override"+cierre)
time.sleep(0.2)
print(rojo+"Activando el modo Override"+cierre)
time.sleep(0.2)
print(rojo+"Activando el modo Override"+cierre)
time.sleep(0.2)
print(rojo+"Activando el modo Override"+cierre)
time.sleep(0.2)
print(rojo+"Activando el modo Override"+cierre)
time.sleep(0.2)
print(rojo+"Activando el modo Override"+cierre)
time.sleep(0.2)
print(rojo+"Activando el modo Override"+cierre)
time.sleep(0.2)
print(rojo+"Activando el modo Override"+cierre)
time.sleep(0.2)
print(rojo+"Activando el modo Override"+cierre)
time.sleep(0.2)
print(rojo+"Activando el modo Override"+cierre)
time.sleep(0.2)
print(rojo+"Activando el modo Override"+cierre)
time.sleep(0.2)
print(rojo+"Activando el modo Override"+cierre)
time.sleep(0.2)
print(rojo+"Activando el modo Override"+cierre)
time.sleep(0.2)
print(rojo+"Activando el modo Override"+cierre)
time.sleep(0.2)
print(rojo+"Activando el modo Override"+cierre)
time.sleep(0.2)
print(rojo+"Activando el modo Override"+cierre)
time.sleep(0.2)
print(rojo+"Activando el modo Override"+cierre)
time.sleep(0.2)
print(rojo+"Activando el modo Override"+cierre)
time.sleep(0.2)
os.system('clear')
banner = Fore.RED + """

                            ,-.                               
       ___,---.__          /'|`\          __,---,___          
    ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.       
  ,'        |           ~'\     /`~           |        `.      
 /      ___//              `. ,'          ,  , \___      \    
|    ,-'   `-.__   _         |        ,    __,-'   `-.    |    
|   /          /\_  `   .    |    ,      _/\          \   |   
\  |           \ \`-.___ \   |   / ___,-'/ /           |  /  
 \  \           | `._   `\\  |  //'   _,' |           /  /      
  `-.\         /'  _ `---'' , . ``---' _  `\         /,-'     
     ``       /     \    ,='/ \`=.    /     \       ''          
             |__   /|\_,--.,-.--,--._/|\   __|                  
             /  `./  \\`\ |  |  | /,//' \,'  \                  
            /   /     ||--+--|--+-/-|     \   \ RIP-Network                
           |   |     /'\_\_\ | /_/_/`\     |   |                
            \   \__, \_     `~'     _/ .__/   /            
             `-._,-'   `-._______,-'   `-._,-'
"""
print(banner)

def menu():
    while True:
     print(Fore.RED + "Herrmientas\n")
     print("1) MI IP")
     print("2) Paginas Blancas")
     print("3) SMS spam solo num ofc")
     print("4) You are an Idiot Pagina Plantilla")
     print("5) Verificador de Gmail")
     print("6) Ataques DDos")
     print("7) Spam masivo a un Gmail")
     print("Para salir pulse CTRL+C o CTRL+Z")

     d = input(Fore.RED + "Override System --> ")

     if d == "1":
        webbrowser.open('https://www.ip-adress.com/')

     elif d == "2":
        webbrowser.open('http://www.paginasblancas.com.ar/')
        webbrowser.open('https://chiletelefonos.com/paginas_blancas.htm')
        webbrowser.open('https://registronacional.com/paginas_blancas/')
        webbrowser.open('https://venezuelatelefonos.com/paginas_blancas.htm')
    
     elif d == "3":
        webbrowser.open('https://www.instagram.com/accounts/password/reset/')
        time.sleep(2)
        webbrowser.open('https://accounts.snapchat.com/accounts/password_reset/phone')
        time.sleep(2)
        webbrowser.open('https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0')
        time.sleep(2)
        webbrowser.open('https://twitter.com/i/flow/password_reset?input_flow_data=%7B%22requested_variant%22%3A%22eyJwbGF0Zm9ybSI6IlJ3ZWIifQ%3D%3D%22%7D')
        time.sleep(2)
    
     elif d == "4":
        webbrowser.open('https://piv.pivpiv.dk/')
    
     elif d == "5": 
        webbrowser.open('https://verify-email.org/')
    
     elif d == "6":
         webbrowser.open('https://github.com/RIP-Network/DDos-Web')
    
        
     elif d == "7":
        print("\n")                                                                             
        c=input(amarillo+"Ingresar su cuenta de Gmail :" + cierre)
        time.sleep(1.0)
        p=getpass.getpass(amarillo+"Ingresar su Contraseña :" + cierre)
        time.sleep(1.0)
        destinatario=input(amarillo+"Correo de la Victima:" + cierre)
        time.sleep(1.0)
        mensaje=input(azul+"Escriba el mensaje:" + cierre)

        
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
         server.login(c, p)
         server.sendmail(c, destinatario, mensaje)
         print(rojo+"Correo enviado"+cierre)
        break



    input("Presiona enter para volver como antes")
    os.system('clear')
menu()