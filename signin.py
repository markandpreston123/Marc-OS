import os
import time
password = open('user/password.mos')
username = open('user/username.mos')
l_p = password.read()
l_un = username.read()
print("""

███╗░░░███╗░█████╗░██████╗░░█████╗░  ░█████╗░░██████╗
████╗░████║██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██╔════╝
██╔████╔██║███████║██████╔╝██║░░╚═╝  ██║░░██║╚█████╗░
██║╚██╔╝██║██╔══██║██╔══██╗██║░░██╗  ██║░░██║░╚═══██╗
██║░╚═╝░██║██║░░██║██║░░██║╚█████╔╝  ╚█████╔╝██████╔╝
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░  ░╚════╝░╚═════╝░
""")

while True:
    sign_in = input(f"Enter password for {l_un}: ")

    if sign_in == l_p:
        print(f"Welcome to Marc OS, {l_un}!")
        time.sleep(1.15)
        os.startfile("home.py")
    else:
        print(f"The password is incorrect for {l_un}. Please try again.")