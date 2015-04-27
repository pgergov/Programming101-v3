import requests
from bs4 import BeautifulSoup

response = requests.get("http://register.start.bg/")

soup = BeautifulSoup(response.text)
with open("links.txt", 'w') as f:
    for element in soup.find_all("a"):
        if isinstance(element.get("href"), str) and element.get(
                "href").startswith("link.php"):
            f.write(element.get("href") + "\n")

headers = {}
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36\
 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
with open("links.txt", 'r') as f:
    content = f.read().split()
with open("servers.txt", 'w') as f:
    for link in content:
        try:
            response = requests.get(
                "http://register.start.bg/" + link, headers=headers, timeout=10)
            f.write(response.headers["server"] + "\n")
            print(response.headers["server"])
        except:
            pass

with open("servers.txt", 'r') as f:
    content = f.read().split("\n")
with open("bg_servers.txt", 'w') as f:
    for server in content:
        try:
            f.write(server[:server.index("/")] + "\n")
        except:
            f.write(server + "\n")
