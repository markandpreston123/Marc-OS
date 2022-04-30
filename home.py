import time
import os
import socket

username = open('user/username.mos')
password = open('user/password.mos')
l_un = username.read()
l_p = password.read()
print("""

███╗░░░███╗░█████╗░██████╗░░█████╗░  ░█████╗░░██████╗
████╗░████║██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██╔════╝
██╔████╔██║███████║██████╔╝██║░░╚═╝  ██║░░██║╚█████╗░
██║╚██╔╝██║██╔══██║██╔══██╗██║░░██╗  ██║░░██║░╚═══██╗
██║░╚═╝░██║██║░░██║██║░░██║╚█████╔╝  ╚█████╔╝██████╔╝
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░  ░╚════╝░╚═════╝░""")
print(f"Welcome, {l_un}!")
print("The current date is: " + time.strftime("%B-%d-%Y7 %I:%M %p"))
print("""
Apps:
1) Google
2) Marc Edit
3) Marc File Explorer
4) Settings
5) Terminal/Command Prompt
6) Marc Calculator
7) Marc Calculator (GUI)
78) Shut Down""")

while True:
        home_input = input("Enter a choice: ")

        if home_input == '1':
            os.startfile('browser.py')
            
        if home_input == '2':
            os.startfile('edit.pyw')
            
        if home_input == '3':
            os.startfile('file.pyw')
            
        if home_input == '4':
            while True:
                settings_signin = input(str(f"Please enter password for {l_un} to enter Settings Mode: "))
                if settings_signin == l_p:
                    hostname = socket.gethostname()
                    host_ip = socket.gethostbyname(hostname)
                    print(f"""1) Change username (Current is {l_un})
2) Change password (Current is {l_p})
Hostname: {hostname}
                              Local IP address: {host_ip}""")
                    edit_settings = input("Enter a choice: ")
                    if edit_settings == '1':
                        edit_u = input("Enter new username: ")
                        with open('user/username.mos', 'w') as f:
                            f.writelines(edit_u)
                        print(f"Username changed to {edit_u}.")
                        print("Restarting...")
                        os.startfile('home.py')
                        exit()
                    if edit_settings == '2':
                        edit_p = input("Enter new password: ")
                        with open('user/password.mos', 'w') as f:
                            f.writelines(edit_p)
                        print(f"Password changed to {edit_p}")
                        print("Restarting...")
                        os.startfile('home.py')
                        exit()
        if home_input == '6':
            os.startfile('calculator.py')
        if home_input == '7':
            os.startfile('calc_ui.pyw')
        if home_input == '8':
            os.startfile('shutdown.py')
            exit()