import os


print("""
███╗░░░███╗░█████╗░██████╗░░█████╗░  
████╗░████║██╔══██╗██╔══██╗██╔══██╗  
██╔████╔██║███████║██████╔╝██║░░╚═╝  
██║╚██╔╝██║██╔══██║██╔══██╗██║░░██╗  
██║░╚═╝░██║██║░░██║██║░░██║╚█████╔╝  
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░  

░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░
██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝
██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
1) +
2) -
3) *
4) / or :
5) Close""")
while True:
    choice = input("Enter a choice: ")

    if choice == '1':
        a = input("Enter 1st number: ")
        print("+")
        b = input("Enter 2nd number: ")
        result = int(a)+int(b)
        print(result)


    if choice == '2':
        a = input("Enter 1st number: ")
        print("-")
        b = input("Enter 2nd number: ")
        result = int(a)-int(b)
        print(result)

        
    if choice == '3':
        a = input("Enter 1st number: ")
        print("*")
        b = input("Enter 2nd number: ")
        result = int(a)*int(b)
        print(result)
        
    if choice == '4':
        a = input("Enter 1st number: ")
        print("/ or :")
        b = input("Enter 2nd number: ")
        result = int(a)/int(b)
        print(result)
        
    if choice == '5':
        print("Closing Calculator...")
        os.startfile('home.py')