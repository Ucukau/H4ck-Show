#tutor
from colorama import init, Fore, Back, Style
import time

def tutor():
     print(f"{Fore.BLACK} {Back.WHITE} LANGKAH")
     print(f'''
         
         {Fore.RED} {Back.BLACK} TERMUX INSTALASI {Style.RESET_ALL}
         
         {Fore.YELLOW}apt update && apt upgrade -y
         pkg update && pkg upgrade -y
         pkg install python-pip
         pip install time
         pip install os
         pip install colorama
         git clone https://github.com/Ucukau/Hack-Show
         cd Hack-Show
         make run
         
         Select your menu
                
         {Style.RESET_ALL}
    ╔══════════════════════════════[]
    ║ {Fore.YELLOW}For Termux To Active This Script 
    ║ {Fore.BLUE}Klik Enter For Menu{Style.RESET_ALL}''')
