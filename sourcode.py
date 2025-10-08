#might add more stuff in the future as at the moment this project is very simple.

import colorama #colours
import subprocess #allows access to powershell cmd etc
import os #operatingsystem
import webbrowser #webbrowser module
import time #time module
import sys #imports system

from colorama import init, Fore #imports some colours

init(autoreset=False, convert=sys.stdout.isatty()) #checks where colours are running and stops it from essentially not displaying properly

print(Fore.RED, end="") #forceseverythingred



myself = ("""

███    ██ ███████ ████████ ██     ██  ██████  ██████  ██   ██   
████   ██ ██         ██    ██     ██ ██    ██ ██   ██ ██  ██    
██ ██  ██ █████      ██    ██  █  ██ ██    ██ ██████  █████     
██  ██ ██ ██         ██    ██ ███ ██ ██    ██ ██   ██ ██  ██    
██   ████ ███████    ██     ███ ███   ██████  ██   ██ ██   ██   
                                                                

 █████  ███    ██  █████  ██   ██    ██ ███████ ███████ ██████  
██   ██ ████   ██ ██   ██ ██    ██  ██  ██      ██      ██   ██ 
███████ ██ ██  ██ ███████ ██     ████   ███████ █████   ██████  
██   ██ ██  ██ ██ ██   ██ ██      ██         ██ ██      ██   ██ 
██   ██ ██   ████ ██   ██ ███████ ██    ███████ ███████ ██   ██ 
                                                                



          By LiquiditySweep-FVG""")
print(Fore.RED + f"{myself} ")  # shows the stuff


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()  # checks if admin
    except:
        return False


#powershell commands
checkifcomputerconnectedtointernet = "Test-Connection -ComputerName www.google.com -Count 1 -Quiet"
ips = "(Get-NetIPAddress -AddressFamily IPv4).IPAddress"
shownetworkadapterdetailsonyourcomputer = "Get-NetAdapter -Name * -IncludeHidden"
listingipconfigdata = "Get-CimInstance -Class Win32_NetworkAdapterConfiguration -Filter IPEnabled=$true"
showtcpipconfigvaluesetc = "ipconfig"
showallstuffconnectedtopc = "Get-PnpDevice -PresentOnly"
showsmaxinternetspeedavailableforyou = "Get-NetAdapter | select interfaceDescription, name, status, linkSpeed"
actualwifispeedtestwebsite = "https://www.speedtest.net/"
staticip = "Get-NetIPConfiguration | Select-Object InterfaceAlias, IPv4Address, DhcpEnabled"

def run_powershell(command):
    try: #prevents errors if use try instead of if
        subprocess.run(['powershell', '-ExecutionPolicy', 'Bypass', '-Command', command], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the PowerShell command: {e}")

while True:  #loop forever
    print("\nSelect an option:")
    print("[1] Check if your computer is connected to the internet")
    print("[2] Show static IP")
    print("[3] Show network adapters details on your computer")
    print("[4] Show ipconfig data on your computer")
    print("[5] Show TCP IP config values etc")
    print("[6] Show all of the stuff connected to your computer")
    print("[7] Show the maximum network speed available for your network adapter")
    print("[8] Internet speed test")
    print("[9] Show current ipv4(s) on your computer")
    print("[10] Exit")
#may add more to this!
    choice = input("Enter the number corresponding to what you want to do: ")

    if choice == "1":
        run_powershell(checkifcomputerconnectedtointernet)
    elif choice == "2":
        run_powershell(ips)
    elif choice == "3":
        run_powershell(shownetworkadapterdetailsonyourcomputer)
    elif choice == "4":
        run_powershell(listingipconfigdata)
    elif choice == "5":
        run_powershell(showtcpipconfigvaluesetc)
    elif choice == "6":
        run_powershell(showallstuffconnectedtopc)
    elif choice == "7":
        run_powershell(showsmaxinternetspeedavailableforyou)
    elif choice == "8":
        webbrowser.open("https://www.speedtest.net/") #basically opens the link
    elif choice == "9":
        run_powershell(staticip)
    elif choice == "10":
        print("Exiting in 5 seconds...")
        print(""""
             
              
  ______  _____   _____  ______       ______  __   __ _______         
 |  ____ |     | |     | |     \      |_____]   \_/   |______         
 |_____| |_____| |_____| |_____/      |_____]    |    |______         
                                                                      
 _______ _     _ _______ __   _ _     _      __   __  _____  _     _  
    |    |_____| |_____| | \  | |____/         \_/   |     | |     |  
    |    |     | |     | |  \_| |    \_         |    |_____| |_____|  
                                                                      
 _______  _____   ______      _     _ _______ _____ __   _  ______    
 |______ |     | |_____/      |     | |______   |   | \  | |  ____    
 |       |_____| |    \_      |_____| ______| __|__ |  \_| |_____|    
                                                                      
 _______ _     _ _____ _______      _______  _____   _____           /
    |    |_____|   |   |______         |    |     | |     | |       / 
    |    |     | __|__ ______|         |    |_____| |_____| |_____ .  
                                                                                                         
                                                                           
                                                                           
              
              
              
              
                    
              """)
        time.sleep(5)#timer for 5 seconds
        sys.exit(0)#exits
    else:
        print("Select a number corresponding to what you want to do:")

""""if __name__ == "__main__":
    main() # this is essentially just something to put at the end of every code from now on, it stops it from ending basically. thats not what it is, but thats what it essentially does.
^I dont know why this wouldnt work to be honest, the code didnt stop running anyway when i ran it as an exe without this and it didnt really give me errors."""
