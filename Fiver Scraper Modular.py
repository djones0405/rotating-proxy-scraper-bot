import os
import random
import urllib3
from urllib.request import Request, urlopen
import subprocess
from proxy_scraper import scrape_proxies


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

PROXY_FILE = "proxy_list.txt"
if not os.path.isfile(PROXY_FILE):
    subprocess.run(["/usr/bin/python3.8", "proxy_scraper.py"], capture_output=True, text=True)

proxies = []


def load_proxies():
    global proxies
    try:
        with open(PROXY_FILE) as f:
            proxy_list = f.readlines()
            proxies = [{'ip': proxy.split(':')[0], 'port': proxy.split(':')[1]} for proxy in proxy_list if proxy.strip()]
    except FileNotFoundError:
        print("proxy_list.txt not found. Scraping proxies...")
        proxy_list = scrape_proxies()
        proxies = [{'ip': proxy.split(':')[0], 'port': proxy.split(':')[1]} for proxy in proxy_list if proxy.strip()]

def scrape_proxies():
    # Scrape proxies from website
    # ...
    return proxy_list

def random_proxy():
    return random.randint(0, len(proxies) - 1)

def main():
    load_proxies()
    proxy_index = random_proxy()
    proxy = proxies[proxy_index]

    # Scrape data using the proxy
    req = Request('https://fiver.com')
    req.set_proxy(proxy['ip'] + ':' + proxy['port'], 'http')

    try:
        my_ip = urlopen(req).read().decode('utf8')
        print(f"Using proxy {proxy['ip']}:{proxy['port']} to scrape data")
        print(f"My IP: {my_ip}")
    except:
        del proxies[proxy_index]
        print(f"Proxy {proxy['ip']}:{proxy['port']} failed. Removing it from list.")
        main()

if __name__ == '__main__':
    main()
