# pip install termcolor pyfiglet indirin

import random
import time
import pyfiglet
import os
from termcolor import colored

# Rastgele IP adresi oluşturma fonksiyonu
def generate_random_ip():
    return '.'.join(str(random.randint(0, 255)) for _ in range(4))

# 1000 tane rastgele IP oluşturma fonksiyonu
def generate_ip_list():
    return [generate_random_ip() for _ in range(1000)]

# Görsel ASCII sanatı oluşturma fonksiyonu
def print_ascii_art():
    ascii_art = pyfiglet.figlet_format("IPChanger by Y46")
    print(colored(ascii_art, 'red'))  # Başlık kırmızı renkte olacak
    print(colored("Press Enter to start...", 'blue'))  # Mavi renkte olacak

# IP'yi değiştiren ve 0.1 saniye bekleyen fonksiyon
def change_ip():
    ip_list = generate_ip_list()  # Her 1000 IP'lik küme için yeni liste oluştur
    while True:
        for ip in ip_list:
            os.system('cls' if os.name == 'nt' else 'clear')  # Ekranı temizle
            print(colored("IPChanger by Y46", 'red'))
            print(colored("Değişen IP:", 'cyan'), colored(ip, 'green'))
            time.sleep(0.1)  # 0.1 saniye bekle

# Başlangıç ekranı ve kullanıcıdan Enter tuşuna basılmasını istemek
def main():
    print_ascii_art()
    input("Press Enter to start...")
    change_ip()

# Ana fonksiyonu çalıştır
if __name__ == "__main__":
    main()