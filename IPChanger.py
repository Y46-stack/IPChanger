import requests
import random
import time
from termcolor import colored
import pyfiglet

# IP değiştirmek için kullanılacak proxy listesi
proxy_list = [
    "http://123.456.789.101:8080",
    "http://234.567.890.123:8080",
    "http://345.678.901.234:8080",
    "http://456.789.012.345:8080",
    "http://567.890.123.456:8080",
    # Buraya daha fazla proxy ekleyebilirsiniz (1000'e kadar).
]

# Yazıyı renkli olarak göstermek için pyfiglet kullanıyoruz
ascii_banner = pyfiglet.figlet_format("IPChanger by Y46")
print(colored(ascii_banner, "red"))
print(colored("Press Enter to Start", "yellow"))

input()

# 1000 defa IP değiştirme
for i in range(1000):
    # Random olarak bir proxy seçiyoruz
    proxy = random.choice(proxy_list)
    print(colored(f"Using Proxy: {proxy}", "green"))
    
    # Proxy ayarları
    proxies = {
        "http": proxy,
        "https": proxy,
    }
    
    try:
        # İstek göndererek IP değiştirme (örneğin bir web sitesine bağlanma)
        response = requests.get("http://httpbin.org/ip", proxies=proxies, timeout=5)
        if response.status_code == 200:
            ip_info = response.json()
            ip_address = ip_info.get('origin')
            print(colored(f"New IP: {ip_address}", "yellow"))
        else:
            print(colored("Failed to connect using the proxy!", "red"))
    except requests.exceptions.RequestException as e:
        print(colored(f"Error: {e}", "red"))
    
    # 1 saniye bekle
    time.sleep(1)

print(colored("Completed 1000 IP changes!", "blue"))