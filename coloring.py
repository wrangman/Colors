import os
from colors import bcolors         #you import the color values from this class


os.system('cls')

print(bcolors.BLUE + "blå" + bcolors.CYAN + "cyan")


print("Ingen färg")




name = input(bcolors.YELLOW + "Skriv ditt namn: ")      #You can use colors for both input and print - no problem!




print(bcolors.DEFAULT)              # Restore default color to system