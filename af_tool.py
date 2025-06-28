import os, requests
from bs4 import BeautifulSoup
import time

def banner():
    os.system("clear")
    print("""
\033[1;32m
████████╗███████╗███████╗████████╗███████╗██████╗ 
╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗
   ██║   █████╗  ███████╗   ██║   █████╗  ██████╔╝
   ██║   ██╔══╝  ╚════██║   ██║   ██╔══╝  ██╔═══╝ 
   ██║   ███████╗███████║   ██║   ███████╗██║     
   ╚═╝   ╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═╝     
\033[1;37m
 🌐 AF-BypassProxy | Dev: Ali Hamza AF
 🛡️ Powered By: AF Cyber Force | Termux Special
=================================================
""")


def fetch_proxies():
    print("\n[~] Fetching public HTTPS proxies...")
    url = "https://free-proxy-list.net/"
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    proxies = []
    for row in soup.select("table#proxylisttable tbody tr"):
        cols = row.find_all("td")
        if cols[6].text == "yes":
            proxies.append(f"{cols[0].text}:{cols[1].text}")
    with open("proxies.txt", "w") as f:
        for p in proxies:
            f.write(p + "\n")
    print(f"[✓] Total proxies saved: {len(proxies)} in proxies.txt\n")


def check_ip(proxy=None):
    try:
        if proxy:
            proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
            r = requests.get("https://api.myip.com", proxies=proxies, timeout=5)
        else:
            r = requests.get("https://api.myip.com", timeout=5)
        print(f"[✓] IP Info: {r.json()}")
    except Exception as e:
        print(f"[✘] Proxy Failed ({proxy}):", e)


def scan_link(link):
    print(f"\n[~] Scanning link: {link}")
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(link, headers=headers, timeout=6)
        if r.status_code in [200, 301, 302]:
            print(f"[✓] Link is reachable with status: {r.status_code}")
        else:
            print(f"[!] Warning: Unusual status code {r.status_code}")
    except Exception as e:
        print(f"[✘] Error reaching the link: {e}")


def menu():
    while True:
        banner()
        print("""\033[1;36m
[1] ✅ Fetch Fresh Proxies
[2] 🌐 Check My IP
[3] 🔁 Check IP Using First Proxy
[4] 🔍 Scan Any Link (Safe or Not)
[5] 🚪 Exit Tool
""")
        ch = input("Select Option ➤ ")
        if ch == '1':
            fetch_proxies()
            input("\nPress Enter to return to menu...")
        elif ch == '2':
            print("\n[✓] Your Original IP Info:")
            check_ip()
            input("\nPress Enter to return to menu...")
        elif ch == '3':
            try:
                with open("proxies.txt", "r") as f:
                    first = f.readline().strip()
                    print(f"\n[✓] Using Proxy: {first}")
                    check_ip(first)
            except:
                print("[✘] proxies.txt not found. Run option 1 first.")
            input("\nPress Enter to return to menu...")
        elif ch == '4':
            link = input("\n🔗 Enter link (include https://): ")
            scan_link(link)
            input("\nPress Enter to return to menu...")
        elif ch == '5':
            print("\n[✓] Exiting... Respect karo or karwao ✌️")
            break
        else:
            print("[✘] Invalid Option. Try Again.")
            time.sleep(2)

if __name__ == "__main__":
    menu()
