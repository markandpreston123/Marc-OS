import webbrowser

print("""
███╗░░░███╗░█████╗░██████╗░░█████╗░  ░██╗░░░░░░░██╗███████╗██████╗░
████╗░████║██╔══██╗██╔══██╗██╔══██╗  ░██║░░██╗░░██║██╔════╝██╔══██╗
██╔████╔██║███████║██████╔╝██║░░╚═╝  ░╚██╗████╗██╔╝█████╗░░██████╦╝
██║╚██╔╝██║██╔══██║██╔══██╗██║░░██╗  ░░████╔═████║░██╔══╝░░██╔══██╗
██║░╚═╝░██║██║░░██║██║░░██║╚█████╔╝  ░░╚██╔╝░╚██╔╝░███████╗██████╦╝
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░  ░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░

██████╗░██████╗░░█████╗░░██╗░░░░░░░██╗░██████╗███████╗██████╗░
██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║██╔════╝██╔════╝██╔══██╗
██████╦╝██████╔╝██║░░██║░╚██╗████╗██╔╝╚█████╗░█████╗░░██████╔╝
██╔══██╗██╔══██╗██║░░██║░░████╔═████║░░╚═══██╗██╔══╝░░██╔══██╗
██████╦╝██║░░██║╚█████╔╝░░╚██╔╝░╚██╔╝░██████╔╝███████╗██║░░██║
╚═════╝░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═════╝░╚══════╝╚═╝░░╚═╝""")
while True:
    browser = input("Search the Web or Enter a URL: ")
    webbrowser.open(browser)