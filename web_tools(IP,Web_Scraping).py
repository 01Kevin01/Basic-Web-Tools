import requests
import socket
import tkinter as tk
from tkinter import scrolledtext


# Web scraping function
def scrape_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return "Error: Could not scrape website"
    except:
        return "Error: Could not scrape website"


# Function to get IP address from domain name
def get_ip_address(domain_name):
    try:
        return socket.gethostbyname(domain_name)
    except:
        return "Error: Could not get IP address"


# GUI code
window = tk.Tk()
window.title("Web Scraper")
window.geometry("800x600")

url_label = tk.Label(text="Enter website URL:")
url_label.pack()

url_entry = tk.Entry()
url_entry.pack()

scrape_button = tk.Button(text="Scrape Website", command=lambda: show_results(scrape_website(url_entry.get())))
scrape_button.pack()

ip_label = tk.Label(text="IP Address:")
ip_label.pack()

ip_text = scrolledtext.ScrolledText()
ip_text.pack()

def show_results(website_data):
    results_text.delete('1.0', tk.END)
    results_text.insert(tk.END, website_data)

    domain_name = url_entry.get().replace("https://", "").replace("http://", "").split("/")[0]
    ip_address = get_ip_address(domain_name)
    ip_text.delete('1.0', tk.END)
    ip_text.insert(tk.END, ip_address)

results_label = tk.Label(text="Scraped Website:")
results_label.pack()

results_text = scrolledtext.ScrolledText()
results_text.pack()

window.mainloop()






#01Kevin01