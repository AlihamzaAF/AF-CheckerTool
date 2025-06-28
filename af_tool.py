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
    url = "https://free-proxy-list.net/"
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    proxies = []
    for row in soup.select("table#proxylisttable tbody tr"):
        cols = row.find_all("td")
        if cols[6].text == "yes":
            proxies.append(f"{cols[0].text}:{cols[1].text}")
    with open("proxies.txt", "a") as f:
        for p in proxies:
            f.write(p + "\n")
    print(f"\n[✓] {len(proxies)} new proxies added to proxies.txt\n")

def show_menu():
    print("""
[1] 🔁 Generate Proxies (JANI PROXY)
[2] 🌐 Check My IP
[3] 🛡️  Check IP Using First Proxy
[4] 🔍 Scan Any Link (Safe or Not)
[5] 🚪 Exit Tool
""")

def check_my_ip():
    ip = requests.get("https://ipinfo.io/json").json()
    print(f"[✓] IP Info: {ip}\n")

def check_proxy_ip():
    try:
        proxy = open("proxies.txt").readlines()[0].strip()
        proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
        ip = requests.get("https://ipinfo.io/json", proxies=proxies, timeout=10).json()
        print(f"[✓] IP Info via Proxy: {ip}\n")
    except Exception as e:
        print("[!] Proxy Failed or Not Available\n")

def scan_link():
    link = input("🔗 Enter URL to scan: ")
    try:
        r = requests.get(link, timeout=10)
        if r.status_code == 200:
            print("[✓] Link appears reachable and safe.")
        else:
            print("[!] Link reachable but suspicious status:", r.status_code)
    except:
        print("[!] Link appears broken or dangerous.")

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
            print("👋 Exit. Thank you!")
            break
        else:
            print("[!] Invalid choice\n")
