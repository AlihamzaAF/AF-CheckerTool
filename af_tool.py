import requests
from bs4 import BeautifulSoup
import os

def banner():
    os.system("clear")
    print("""
\033[1;32m
███████╗ ██████╗      ██████╗██╗  ██╗███████╗ ██████╗███████╗████████╗
██╔════╝██╔═══██╗    ██╔════╝██║  ██║██╔════╝██╔════╝██╔════╝╚══██╔══╝
███████╗██║   ██║    ██║     ███████║█████╗  ██║     █████╗     ██║   
╚════██║██║   ██║    ██║     ██╔══██║██╔══╝  ██║     ██╔══╝     ██║   
███████║╚██████╔╝    ╚██████╗██║  ██║███████╗╚██████╗███████╗   ██║   
╚══════╝ ╚═════╝      ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚══════╝   ╚═╝   
                                                                      
\033[1;37m
🔥 JANI PROXY – Proxy Generator + Checker
💻 Developer: Ali Hamza AF
❤️ Powered by AF Cyber Force
======================================================================
""")

def fetch_proxies():
    print("[*] Fetching proxies from ProxyScrape.com...")
    try:
        url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=1000&country=all&ssl=all&anonymity=all"
        r = requests.get(url)
        proxies = r.text.strip().split('\n')
        with open("proxies.txt", "a") as f:
            for p in proxies:
                f.write(p + "\n")
        print(f"[✓] {len(proxies)} proxies added to proxies.txt\n")
    except Exception as e:
        print(f"[!] Failed to fetch proxies: {e}")

def check_my_ip():
    try:
        ip = requests.get("https://ipinfo.io/json").json()
        print(f"[✓] Your Real IP Info:\n{ip}\n")
    except:
        print("[!] Failed to fetch your IP.")

def check_proxy_ip():
    try:
        proxy = open("proxies.txt").readlines()[0].strip()
        proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
        ip = requests.get("https://ipinfo.io/json", proxies=proxies, timeout=7).json()
        print(f"[✓] IP via Proxy:\n{ip}\n")
    except:
        print("[!] Proxy Failed or Not Working. Try generating new proxies.")

def scan_link():
    link = input("🔗 Enter URL to scan: ")
    try:
        r = requests.get(link, timeout=10)
        if r.status_code == 200:
            print("[✓] Link is reachable and likely safe.")
        else:
            print(f"[!] Link returned unusual status: {r.status_code}")
    except:
        print("[!] Link seems broken or potentially dangerous.")

def show_menu():
    print("""
[1] 🔁 Generate Proxies (JANI PROXY)
[2] 🌐 Check My IP
[3] 🛡️  Check IP Using First Proxy
[4] 🔍 Scan Any Link (Safe or Not)
[5] 📺 Open YouTube Channel
[6] 💬 Open WhatsApp Channel
[7] 🚪 Exit Tool
""")

if __name__ == "__main__":
    banner()
    while True:
        show_menu()
        choice = input("📥 Select Option: ")
        if choice == "1":
            fetch_proxies()
        elif choice == "2":
            check_my_ip()
        elif choice == "3":
            check_proxy_ip()
        elif choice == "4":
            scan_link()
        elif choice == "5":
            os.system("xdg-open https://youtube.com/@AliHamzaAF")
        elif choice == "6":
            os.system("xdg-open https://whatsapp.com/channel/0029VaU5UfBBVJl2sqYwbJ1t")
        elif choice == "7":
            print("👋 Exiting... Respect karo or karwao 💥")
            break
        else:
            print("[!] Invalid choice. Try again.\n")
