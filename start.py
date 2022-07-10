import os
import sys
from subprocess import call

os.system('clear')

terminal_title = "MC Server Launcher"
print(f'\33]0;{terminal_title}\a', end='', flush=True)

print("1337 Local-Hosted Minecraft Server Launcher. Made by: Making new Github...\n")
print("   [1] Launch Existing Minecraft Server With Ngrok\n")
print("   [2] Launch Existing Minecraft Server\n")
option = int(input(">>> "))

if option == 1:
    os.system('clear')

    mem_option_ngrok = str(input("\n   How Much Memory(Mb)?\n\n>>> "))
    mem_option_ngrok_check = str(input("\n   Are you sure you want to give this server " + mem_option_ngrok + "Mb of Memory? (Y/n)\n\n>>> "))

    if mem_option_ngrok_check == "y" or "Y":
        os.system('clear')

        call(["gnome-terminal", "-x", "sh", "-c", "sudo ngrok tcp 25565; bash"])
        terminal_title2 = "MC Server"
        print(f'\33]0;{terminal_title2}\a', end='', flush=True)
        os.system('sudo java -Xmx' + mem_option_ngrok + 'M -Xms' + mem_option_ngrok + 'M -jar server.jar nogui') 
    if mem_option_ngrok_check == "n" or "N":
        os.system('clear')

        mem_option_ngrok = str(input("\n   How Much Memory(Mb)?\n\n>>> "))

        call(["gnome-terminal", "-x", "sh", "-c", "sudo ngrok tcp 25565; bash"])
        terminal_title2 = "MC Server"
        print(f'\33]0;{terminal_title2}\a', end='', flush=True)
        os.system('sudo java -Xmx' + mem_option_ngrok + 'M -Xms' + mem_option_ngrok + 'M -jar server.jar nogui') 

if option == 2:
    os.system('clear')

    mem_option = str(input("\n   How Much Memory(Mb)?\n\n>>> "))
    mem_option_check = str(input("\n   Are you sure you want to give this server " + mem_option + "Mb of Memory? (Y/n)\n\n>>> "))

    if mem_option_check == "y" or "Y":
        os.system('clear')

        terminal_title2 = "MC Server"
        print(f'\33]0;{terminal_title2}\a', end='', flush=True)
        os.system('sudo java -Xmx' + mem_option + 'M -Xms' + mem_option + 'M -jar server.jar nogui')
    if mem_option_check == "n" or "N":
        os.system('clear')

        mem_option = str(input("\n   How Much Memory(Mb)?\n\n>>> "))
        terminal_title2 = "MC Server"
        print(f'\33]0;{terminal_title2}\a', end='', flush=True)
        os.system('sudo java -Xmx' + mem_option + 'M -Xms' + mem_option + 'M -jar server.jar nogui')


