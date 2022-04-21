import os
import time

with open('user/info.data', 'w') as f:
    f.write("1")

print("""
███╗░░░███╗░█████╗░██████╗░░█████╗░  ░█████╗░░██████╗  ░██████╗███████╗████████╗██╗░░░██╗██████╗░
████╗░████║██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██╔════╝  ██╔════╝██╔════╝╚══██╔══╝██║░░░██║██╔══██╗
██╔████╔██║███████║██████╔╝██║░░╚═╝  ██║░░██║╚█████╗░  ╚█████╗░█████╗░░░░░██║░░░██║░░░██║██████╔╝
██║╚██╔╝██║██╔══██║██╔══██╗██║░░██╗  ██║░░██║░╚═══██╗  ░╚═══██╗██╔══╝░░░░░██║░░░██║░░░██║██╔═══╝░
██║░╚═╝░██║██║░░██║██║░░██║╚█████╔╝  ╚█████╔╝██████╔╝  ██████╔╝███████╗░░░██║░░░╚██████╔╝██║░░░░░
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░  ░╚════╝░╚═════╝░  ╚═════╝░╚══════╝░░░╚═╝░░░░╚═════╝░╚═╝░░░░░
""")

username = input("""Welcome to Marc OS Setup!

This wizard will quide you through setting up Marc OS.

Enter a Username: """)
password = input("Enter a password: ")

print("Setup is now setting up Marc OS.")
with open('user/username.mos', 'w') as f:
    f.writelines(username)
with open('user/password.mos', 'w') as f:
    f.writelines(password)
print("Setup has completed succsessfuly!")
print("Loading Lock Screen...")
time.sleep(1.15)
os.startfile('signin.py')

