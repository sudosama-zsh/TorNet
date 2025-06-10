#!/usr/bin/env python3
import time
import requests
from stem import Signal
from stem.control import Controller
from colorama import Fore, Style
import pyfiglet

# =============================
# 🟢 Banner
# =============================
def show_banner():
    ascii_banner = pyfiglet.figlet_format("TorNet")
    print(Fore.RED + ascii_banner + Style.RESET_ALL)
    print(Fore.CYAN + "created by sudosama-zsh | may you stay anonymous\n" + Style.RESET_ALL)

# =============================
# 🌐 IP Display Function
# =============================
def get_current_ip():
    try:
        proxies = {
            'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050'
        }
        response = requests.get('https://ident.me', proxies=proxies, timeout=10)
        return response.text.strip()
    except Exception as e:
        return f"[!] Failed to Receive IP: {e}"

# =============================
# 🔁 Cycle Start
# =============================
def main():
    show_banner()

    while True:
        try:
            with Controller.from_port(port=9051) as controller:
                controller.authenticate(password='your_password_here')  # <-- Your Password Here
                controller.signal(Signal.NEWNYM)
                print(Fore.CYAN + "[*] IP Changed..." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"[!] Error: {e}" + Style.RESET_ALL)

        time.sleep(5) 

        new_ip = get_current_ip()
        print(Fore.RED + f"[+] New IP: {new_ip}\n" + Style.RESET_ALL)

        time.sleep(60) 

# =============================
# ▶️ Run
# =============================
if __name__ == "__main__":
    main()
# ==========================================================
# 🔁 Alternative IP-check services (if the default one fails)
# Replace the URL in requests.get(line 25) with any of these:
#
# https://api.ipify.org
# https://icanhazip.com
# https://ident.me
# https://checkip.amazonaws.com
# https://ifconfig.co/ip
# https://ipinfo.io/ip
# https://ipecho.net/plain
# https://wtfismyip.com/text
# https://myexternalip.com/raw
# https://bot.whatismyipaddress.com
# ==========================================================
# 🔧 Tor service control commands (Linux-based systems):
#
# Start Tor service:
#   sudo systemctl start tor
#
# Stop Tor service:
#   sudo systemctl stop tor
#
# Check Tor service status:
#   sudo systemctl status tor
#
# Restart Tor service:
#   sudo systemctl restart tor
#
# If your system uses tor@default instead, try:
#   sudo systemctl start tor@default
#   sudo systemctl stop tor@default
# ==========================================================

