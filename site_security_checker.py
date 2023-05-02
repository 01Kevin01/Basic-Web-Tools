import tkinter as tk
import requests
from bs4 import BeautifulSoup

def check_site():
    # Get the URL from the user input
    url = url_entry.get()
    
    # Send a GET request to the URL and get the status code
    try:
        response = requests.get(url)
        status_code = response.status_code
    except:
        status_code = "Error"
    
    # Check if the site is vulnerable to SQL injection
    try:
        # Send a GET request to the URL with a SQL injection payload
        response = requests.get(url + "'")
        
        # Check if the response contains a MySQL error message
        soup = BeautifulSoup(response.text, 'html.parser')
        error_messages = soup.find_all('p', class_='errormessage')
        
        if any("You have an error in your SQL syntax" in str(error) for error in error_messages):
            sql_injection = "Vulnerable"
        else:
            sql_injection = "Not vulnerable"
    except:
        sql_injection = "Error"
    
    # Check if the site is vulnerable to cross-site scripting (XSS)
    try:
        # Send a GET request to the URL with an XSS payload
        response = requests.get(url + '"<script>alert("XSS");</script>')
        
        # Check if the payload is reflected in the response
        if "<script>alert(\"XSS\");</script>" in response.text:
            xss = "Vulnerable"
        else:
            xss = "Not vulnerable"
    except:
        xss = "Error"
    
    # Display the results in the output label
    output_label.config(text=f"Status code: {status_code}\nSQL injection: {sql_injection}\nXSS: {xss}")

# Create the GUI
root = tk.Tk()
root.title("Site Security Checker")

# Create the URL label and entry
url_label = tk.Label(root, text="URL:")
url_label.pack(side="left")
url_entry = tk.Entry(root)
url_entry.pack(side="left")

# Create the check button
check_button = tk.Button(root, text="Check", command=check_site)
check_button.pack(side="left")

# Create the output label
output_label = tk.Label(root, text="")
output_label.pack(side="left")

root.mainloop()
