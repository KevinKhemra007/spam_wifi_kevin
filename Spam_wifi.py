import os
import time
import sys
import pyfiglet
import random

# Banner function
def banner():
    hacker_art = """
     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
     ⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⠿⠿⠿⢷⣦⡀⠀⠀⠀⠀⠀⠀
     ⠀⠀⠀⠀⣠⣾⠟⠉⠀⠀⠀⠀⠀⠀⠙⢷⡀⠀⠀⠀⠀⠀
     ⠀⠀⠀⣴⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⠀⠀⠀⠀⠀
     ⠀⠀⢸⡇⠀⠀⢀⡀⠀⠀⠀⠀⣀⠀⠀⠀⣿⠀⠀⠀⠀⠀
     ⠀⠀⢻⡀⠀⢰⣿⡟⠀⠀⠀⢻⣿⡆⠀⢠⡟⠀⠀⠀⠀⠀
     ⠀⠀⠘⣷⡀⠘⠉⠀⠀⠀⠀⠀⠉⠁⢀⣾⠃⠀⠀⠀⠀⠀
     ⠀⠀⠀⠘⢿⡄⠀⠀⠀⠀⠀⠀⠀⣠⡿⠃⠀⠀⠀⠀⠀⠀
     ⠀⠀⠀⠀⠈⠻⣦⡀⠀⠀⠀⢀⣴⠟⠀⠀⠀⠀⠀⠀⠀⠀
     ⠀⠀⠀⠀⠀⠀⠈⠻⣦⡀⢠⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
     ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """
    print("\033[1;31m" + hacker_art + "\033[0m")  # Red color

    print("\033[1;34m" + pyfiglet.figlet_format("Hacker Tool", font="slant") + "\033[0m")
    print("\033[1;32m[1] Start wlan0")
    print("[2] Spam WiFi APs (Random)")
    print("[3] Clone & Spam WiFi")
    print("[4] Stop wlan0")
    print("[5] Exit\033[0m")
    print("\033[1;33m-------------------------------------------\033[0m")
    print("\033[1;36mCreated by Khemra \033[0m")
    print("\033[1;35mGitHub: https://github.com/khemra007 \033[0m")
    print("\033[1;35mTelegram: https://t.me/Kevin_Tech007 \033[0m")
    print("\033[1;33m-------------------------------------------\033[0m")

# Start wlan0
def start_wlan0():
    print("\033[1;33mStarting wlan0...\033[0m")
    os.system("sudo airmon-ng start wlan0")
    print("\033[1;32mWlan0 started successfully!\033[0m")

# Stop wlan0
def stop_wlan0():
    print("\033[1;31mStopping wlan0...\033[0m")
    os.system("sudo airmon-ng stop wlan0mon")
    os.system("sudo systemctl restart NetworkManager")
    print("\033[1;32mWlan0 stopped successfully!\033[0m")

# Function to get correct interface (wlan0mon or wlan0)
def get_interface():
    if os.system("iwconfig wlan0mon > /dev/null 2>&1") == 0:
        return "wlan0mon"
    else:
        return "wlan0"

# Spam WiFi APs (Random Names)
def spam_wifi():
    num_ssid = int(input("\033[1;34mEnter number of random fake WiFi names: \033[0m"))
    words = ["Hacker", "Virus", "FreeWiFi", "DarkNet", "NoInternet", "Ghost", "Anonymous", "Cyber", "Hidden"]
    
    ssid_list = []
    for _ in range(num_ssid):
        random_name = random.choice(words) + str(random.randint(1000, 9999))
        ssid_list.append(random_name)

    with open("wifi_list.txt", "w") as f:
        for ssid in ssid_list:
            f.write(ssid + "\n")

    interface = get_interface()
    print(f"\033[1;33mStarting WiFi spamming on {interface}...\033[0m")
    os.system(f"sudo mdk3 {interface} b -f wifi_list.txt -c 6")
    print("\033[1;32mWiFi spamming started!\033[0m")

# Clone WiFi and spam
def clone_wifi():
    target_wifi = input("\033[1;34mEnter target WiFi name to clone: \033[0m")
    cloned_wifi = target_wifi + "_FREE"
    print(f"\033[1;33mCloning {target_wifi} as {cloned_wifi} and spamming...\033[0m")

    with open("wifi_clone.txt", "w") as f:
        f.write(cloned_wifi + "\n")

    interface = get_interface()
    os.system(f"sudo mdk3 {interface} b -f wifi_clone.txt -c 6")

    print("\033[1;32mCloned WiFi and spamming started!\033[0m")

# Main Menu
while True:
    try:
        banner()
        choice = input("\033[1;36mSelect an option: \033[0m")

        if choice == "1":
            start_wlan0()
        elif choice == "2":
            spam_wifi()
        elif choice == "3":
            clone_wifi()
        elif choice == "4":
            stop_wlan0()
        elif choice == "5":
            print("\033[1;31mExiting tool...\033[0m")
            sys.exit()
        else:
            print("\033[1;31mInvalid choice, please try again!\033[0m")
    
    except KeyboardInterrupt:
        print("\n\033[1;31m[!] Exiting due to user interrupt (Ctrl+C)\033[0m")
        sys.exit()
