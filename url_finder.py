import requests
import re
from bs4 import BeautifulSoup
from tkinter import *


# function to find all links on a webpage
def find_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = []
    for link in soup.find_all("a"):
        links.append(link.get("href"))
    return links


# function to find all links that are not indexed by search engines
def find_unindexed_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = []
    for link in soup.find_all("a"):
        href = link.get("href")
        if href and "http" not in href and href != "/" and href != "#" and ".pdf" not in href and ".jpg" not in href and ".jpeg" not in href and ".png" not in href and ".gif" not in href and ".mp3" not in href and ".mp4" not in href:
            new_url = url + href
            response = requests.get(new_url)
            if "noindex" in response.text:
                links.append(new_url)
    return links


# function to find admin and login pages
def find_admin_login_pages(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = []
    for link in soup.find_all("a"):
        href = link.get("href")
        if href and ("admin" in href.lower() or "login" in href.lower()):
            new_url = url + href
            links.append(new_url)
    return links


# function to create GUI
def create_gui():
    # function to handle search button click
    def search_button_click():
        # get input from text box
        url = url_text.get()
        # find all links on webpage
        all_links = find_links(url)
        # find unindexed links on webpage
        unindexed_links = find_unindexed_links(url)
        # find admin and login pages
        admin_login_pages = find_admin_login_pages(url)
        # create output message
        output_message = f"All Links on Webpage: {all_links}\nUnindexed Links: {unindexed_links}\nAdmin and Login Pages: {admin_login_pages}"
        # display output message in text box
        output_text.delete("1.0", END)
        output_text.insert("1.0", output_message)

    # create GUI window
    window = Tk()
    window.title("Web Crawler")
    # create input label and text box
    url_label = Label(window, text="Enter URL:")
    url_label.pack()
    url_text = Entry(window, width=50)
    url_text.pack()
    # create search button
    search_button = Button(window, text="Search", command=search_button_click)
    search_button.pack()
    # create output label and text box
    output_label = Label(window, text="Output:")
    output_label.pack()
    output_text = Text(window, height=10, width=50)
    output_text.pack()
    # start GUI loop
    window.mainloop()


# call create_gui function to start program
create_gui()
