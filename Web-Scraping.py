import requests
import re
import os
import socket

def menu():
    print("1- Web Scraping")
    print("2- Site Analysis")
    print("3- Back Door Control")
    print("4- Certificate Check")
    print("5- Link Analysis")
    print("6- SQL Injection")
    print("7- Port Scan")
    print("8- Exit")

def web_scraping():
    url = input("Enter the URL of the website: ")
    r = requests.get(url)
    content = r.text
    print(content)

def site_analizi():
    url = input("Enter the URL of the website: ")
    r = requests.get(url)
    status = r.status_code
    headers = r.headers
    print("Durum Kodu:", status)
    print("Başlıklar:")
    for header in headers:
        print(header + ":", headers[header])

def arka_kapi_kontrol():
    url = input("Enter the URL of the website: ")
    if "admin" in url:
        print("Available")
    else:
        print("Unavailable")

def sertifika_kontrol():
    url = input("Enter the URL of the website: ")
    r = requests.get(url)
    cert = r.connection.sock.getpeercert()
    if cert:
        print("There is a certificate")
    else:
        print("No certificate")

def link_analizi():
    url = input("Enter the URL of the website: ")
    r = requests.get(url)
    content = r.text
    pattern = re.compile(r'href="(.*?)"')
    links = pattern.findall(content)
    print("Linkler:")
    for link in links:
        print(link)

def sql_enjeksiyonu():
    url = input("Enter the URL of the website: ")
    payload = input("Enter SQL Injection Payload: ")
    r = requests.get(url + payload)
    content = r.text
    if "syntax" in content:
        print("This site is open to SQL injection")
    else:
        print("This site is closed to SQL injection")

def port_taramasi():
    ip = input("Enter IP address: ")
    for port in range(1, 65536):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((ip, port))
        if result == 0:
            print("Port", port, "open")
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
        print("Invalid selection")

input("Press any key to exit...")
#01Kevin01
