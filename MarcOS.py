import os
import time

data_info = open('user/info.data')
data = data_info.read()

if data == '0':
    print("Starting Marc OS")
    time.sleep(1.15)
    print("Loading Setup...")
    os.startfile("setup.py")

if data == '1':
    
    time.sleep(1.15)
    print("Loading Lock Screen...")
    os.startfile("signin.py")