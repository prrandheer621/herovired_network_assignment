import requests
from tabulate import tabulate
import time

subdomains = [
    "https://mail.google.com/", # Actual domain
    "https://mail2.google.com/", # Fake domain to test
    "https://photos.google.com/" #Actual domain
]

def getStatus(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return "Up"
        else:
            return "Down"
    except requests.ConnectionError:
        return "Down"
    except requests.Timeout:
        return "Timeout"

def monitor_subdomains():
    while True:
        results = []
        
        #Check for each subdomain, and store the result for printing in tabular form
        for subdomain in subdomains:
            status = getStatus(subdomain)
            results.append([subdomain, status])

        
        # Priting results in tabular format in pretty Format
        print(tabulate(results, headers=["Subdomain", "Status"], tablefmt="pretty"))

        # Infinite loop paused for 60 secs, before it will run again
        time.sleep(60)

if __name__ == "__main__":
    monitor_subdomains()
