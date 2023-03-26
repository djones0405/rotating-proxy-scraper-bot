import requests
import random
import urllib3
from urllib.request import Request, urlopen
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ua = UserAgent()
proxies = []

# Main function
def main():
    # Retrieve latest proxies
    api_key = "API Key"
    api_url = f"https://api.proxylist.to/socks4?key={api_key}"

    response = requests.get(api_url, verify=False)

    if response.status_code == 200:
        proxies_doc = response.text.split('\n')
        with open('proxy_list.txt', 'w') as f:
            for proxy in proxies_doc:
                f.write(proxy + '\n')
    else:
        print(f"Error retrieving proxies: {response.status_code}")
        return
        # Choose a random proxy
        proxy_index = random_proxy()
        proxy = proxies[proxy_index]

        for n in range(1, 100):
            req = Request('https://proxylist.to/api/')
            req.set_proxy(proxy['ip'] + ':' + proxy['port'], 'http')

            # Every 10 requests, generate a new proxy
            if n % 10 == 0:
                proxy_index = random_proxy()
                proxy = proxies[http.txt]

            # Make the call
            try:
                my_ip = urlopen(req).read().decode('utf8')
                print('#' + str(n) + ': ' + my_ip)
            except: # If error, delete this proxy and find another one
                del proxies[proxy_index]
                print('Proxy ' + proxy['ip'] + ':' + proxy['port'] + ' deleted.')
                proxy_index = random_proxy()
                proxy = proxies[proxy_index]
            else:
                print(f"Error retrieving proxies: {response.status_code}")
            return

# Retrieve a random index proxy (we need the index to delete it if not working)
def random_proxy():
    return random.randint(0, len(proxies) - 1)

def scrape_proxies(proxy_file):
    proxy_list = []
    for i in range(1, 11):
        url = f"http://www.freeproxylists.net/?page={i}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', attrs={'class': 'DataGrid'})
        rows = table.findAll('tr')
        for row in rows[1:]:
            cols = row.findAll('td')
            ip = cols[0].text.strip()
            port = cols[1].text.strip()
            proxy_list.append(ip + ":" + port)
    with open(proxy_file, "w") as f:
        f.write("\n".join(proxy_list))
if __name__ == '__main__':
    main()
