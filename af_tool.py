import requests, os, time, json
from urllib.parse import urlparse

def banner():
    os.system("clear")
    print("""
\033[1;32m
 █████╗ ███████╗    ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔══██╗██╔════╝   ██╔════╝██║  ██║██╔════╝██╔════╝██║  ██║██╔════╝██╔══██╗
███████║█████╗     ██║     ███████║█████╗  ██║     ███████║█████╗  ██████╔╝
██╔══██║██╔══╝     ██║     ██╔══██║██╔══╝  ██║     ██╔══██║██╔══╝  ██╔══██╗
██║  ██║██║         ╚██████╗██║  ██║███████╗╚██████╗██║  ██║███████╗██║  ██║
╚═╝  ╚═╝╚═╝         ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                            
\033[1;37m🔥 AF CHECKER – Proxy Tools + Security Scanner
💻 Developer: Ali Hamza AF
❤️ Powered by AF Cyber Force
======================================================================
""")

def fetch_proxies():
    print("[*] Generating real proxies from ProxyScrape...")
    try:
        url = "https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&protocol=http&timeout=10000&country=all&proxy_format=ipport&format=text"
        res = requests.get(url, timeout=30)
        proxies = [p.strip() for p in res.text.splitlines() if p.strip()]
        
        with open("proxies.txt", "w") as f:
            f.write("\n".join(proxies))
            
        print(f"[✓] {len(proxies)} live proxies saved to proxies.txt\n")
        return True
    except Exception as e:
        print(f"[!] Error fetching proxies: {e}")
        return False

def check_my_ip():
    try:
        print("[*] Checking your IP address...")
        response = requests.get("https://ipinfo.io/json", timeout=10)
        ip_data = response.json()
        print("\n[✓] Your IP Information:")
        print(f"IP: {ip_data.get('ip', 'N/A')}")
        print(f"Location: {ip_data.get('city', 'N/A')}, {ip_data.get('region', 'N/A')}")
        print(f"ISP: {ip_data.get('org', 'N/A')}")
        print(f"Country: {ip_data.get('country', 'N/A')}\n")
    except Exception as e:
        print(f"[!] Failed to fetch IP info: {e}\n")

def check_proxy_ip():
    if not os.path.exists("proxies.txt"):
        print("[!] No proxies found. Generate proxies first.\n")
        return
        
    try:
        with open("proxies.txt", "r") as f:
            proxies = [line.strip() for line in f.readlines() if line.strip()]
            
        if not proxies:
            print("[!] Proxy file is empty. Generate new proxies.\n")
            return
            
        proxy = proxies[0]
        print(f"[*] Testing first proxy: {proxy}")
        
        proxies_dict = {
            "http": f"http://{proxy}",
            "https": f"http://{proxy}"
        }
        
        start_time = time.time()
        response = requests.get(
            "https://ipinfo.io/json",
            proxies=proxies_dict,
            timeout=15
        )
        response_time = time.time() - start_time
        
        if response.status_code == 200:
            ip_data = response.json()
            print("\n[✓] Proxy Connection Successful!")
            print(f"Proxy IP: {ip_data.get('ip', 'N/A')}")
            print(f"Response Time: {response_time:.2f} seconds")
            print(f"Location: {ip_data.get('city', 'N/A')}, {ip_data.get('country', 'N/A')}\n")
        else:
            print(f"[!] Proxy connection failed (Status: {response.status_code})\n")
    except Exception as e:
        print(f"[!] Proxy test failed: {str(e)}\n")

def scan_link():
    try:
        url = input("\n🔗 Enter URL to scan: ").strip()
        if not url:
            print("[!] URL cannot be empty\n")
            return
            
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
            
        print(f"[*] Scanning: {url}")
        
        parsed = urlparse(url)
        if not parsed.netloc:
            print("[!] Invalid URL format\n")
            return
            
        start_time = time.time()
        response = requests.get(url, timeout=15, allow_redirects=True)
        response_time = time.time() - start_time
        
        print("\n[✓] Link Scan Results:")
        print(f"Status Code: {response.status_code}")
        print(f"Response Time: {response_time:.2f} seconds")
        print(f"Content Length: {len(response.content)} bytes")
        print(f"Final URL: {response.url}")
        
        if response.status_code == 200:
            print("Status: ✅ Safe and Reachable")
        elif response.status_code in (301, 302):
            print("Status: ⚠️ Redirect detected")
        else:
            print("Status: ⚠️ Unexpected response")
        print()
    except requests.exceptions.SSLError:
        print("[!] SSL Certificate Error - Potential security risk\n")
    except Exception as e:
        print(f"[!] Scan failed: {str(e)}\n")

def show_menu():
    print("""
[1] 🔁 Generate Proxies
[2] 🌐 Check My IP
[3] 🛡️  Check Proxy IP
[4] 🔍 Scan Link Safety
[5] 📺 Open YouTube
[6] 💬 Open WhatsApp
[7] 🚪 Exit Tool
""")

if __name__ == "__main__":
    banner()
    while True:
        show_menu()
        choice = input("📥 Select Option: ").strip()
        
        if choice == "1":
            fetch_proxies()
        elif choice == "2":
            check_my_ip()
        elif choice == "3":
            check_proxy_ip()
        elif choice == "4":
            scan_link()
        elif choice == "5":
            print("[*] Opening YouTube channel...")
            os.system("xdg-open 'https://youtube.com/@AliHamzaAF' > /dev/null 2>&1")
            print("[✓] Done\n")
        elif choice == "6":
            print("[*] Opening WhatsApp channel...")
            os.system("xdg-open 'https://whatsapp.com/channel/0029VaU5UfBBVJl2sqYwbJ1t' > /dev/null 2>&1")
            print("[✓] Done\n")
        elif choice == "7":
            print("\n👋 Exiting... AF Cyber Force Zindabad! 💥")
            break
        else:
            print("[!] Invalid option. Try again.\n")
        time.sleep(1)
