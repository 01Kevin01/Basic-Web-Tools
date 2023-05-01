import requests
import re
import os
import socket

def menu():
    print("1- Web Scraping")
    print("2- Site Analizi")
    print("3- Arka Kapı Kontrolü")
    print("4- Sertifika Kontrolü")
    print("5- Link Analizi")
    print("6- SQL Enjeksiyonu")
    print("7- Port Taraması")
    print("8- Çıkış")

def web_scraping():
    url = input("Web sitesinin URL'sini girin: ")
    r = requests.get(url)
    content = r.text
    print(content)

def site_analizi():
    url = input("Web sitesinin URL'sini girin: ")
    r = requests.get(url)
    status = r.status_code
    headers = r.headers
    print("Durum Kodu:", status)
    print("Başlıklar:")
    for header in headers:
        print(header + ":", headers[header])

def arka_kapi_kontrol():
    url = input("Web sitesinin URL'sini girin: ")
    if "admin" in url:
        print("Var")
    else:
        print("Yok")

def sertifika_kontrol():
    url = input("Web sitesinin URL'sini girin: ")
    r = requests.get(url)
    cert = r.connection.sock.getpeercert()
    if cert:
        print("Sertifika var")
    else:
        print("Sertifika yok")

def link_analizi():
    url = input("Web sitesinin URL'sini girin: ")
    r = requests.get(url)
    content = r.text
    pattern = re.compile(r'href="(.*?)"')
    links = pattern.findall(content)
    print("Linkler:")
    for link in links:
        print(link)

def sql_enjeksiyonu():
    url = input("Web sitesinin URL'sini girin: ")
    payload = input("SQL Enjeksiyon Payload'u girin: ")
    r = requests.get(url + payload)
    content = r.text
    if "syntax" in content:
        print("Bu site SQL enjeksiyonuna açık")
    else:
        print("Bu site SQL enjeksiyonuna kapalı")

def port_taramasi():
    ip = input("IP adresi girin: ")
    for port in range(1, 65536):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((ip, port))
        if result == 0:
            print("Port", port, "açık")
        s.close()

while True:
    menu()
    secim = input("Seçiminiz: ")
    if secim == "1":
        web_scraping()
    elif secim == "2":
        site_analizi()
    elif secim == "3":
        arka_kapi_kontrol()
    elif secim == "4":
        sertifika_kontrol()
    elif secim == "5":
        link_analizi()
    elif secim == "6":
        sql_enjeksiyonu()
    elif secim == "7":
        port_taramasi()
    elif secim == "8":
        break
    else:
        print("Geçersiz seçim")

input("Çıkmak için bir tuşa basın...")
#01Kevin01
