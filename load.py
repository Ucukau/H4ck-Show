import clean
import time
from colorama import init, Fore, Back, Style

def load():
   for i in range(1, 10):
      print(Fore.GREEN + Back.GREEN+ "[ " "█" * i + " ]" * i, end='\r')
      end='\n'
      time.sleep(0.10)      
   print(f"Succes ✓{Style.RESET_ALL}")
