import suport
import tutor
import donasi
import hang
import menu
import clean
import load
import erot
import time
import erMsg
from colorama import init, Fore, Back, Style
import os
import time
import sys

clean.clear()
print(Fore.BLUE + "Klik Enter Untuk Kembali Ke Menu.." + Style.RESET_ALL)
import time

def h_mundur():
    for i in range(3, 0, -1):
        sys.stdout.write("\r")  # Menghapus baris sebelumnya
        sys.stdout.write(f"left: {Fore.YELLOW}{i}")
        sys.stdout.flush()
        time.sleep(1)
    
    sys.stdout.write("\r")  # Menghapus baris terakhir
    sys.stdout.write(f"      {Fore.RED}0\n")
    sys.stdout.flush()
    print(f"{Fore.YELLOW}Program diHentikan! {Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Ketik {Fore.BLUE}make run {Fore.YELLOW} untuk menjalankan program...")

while True:   
        pilih = input(f"{Fore.BLACK}_   {Fore.WHITE}╚══{Fore.BLUE}⟩ {Style.RESET_ALL}" )
    if pilih == "":
        clean.clear()
        print('''
            
            
            
            
            ''')
        load.load()
        menu.icon_main()
        menu.main_menu()
    elif pilih == "1":
        clean.clear()
        load.load()       
        hang.hack()
    elif pilih == "2":
        clean.clear()
        erot.start()
    elif pilih == "3":
        clean.clear()
        suport.suport()
    elif pilih == "4":
        clean.clear()
        donasi.donasi()
    elif pilih == "5":
        load.load()
        clean.clear()
        tutor.tutor()
    elif pilih == "6":
        clean.clear()
        h_mundur()     
        break 
    else:
        clean.clear()
       
        erMsg.error()
