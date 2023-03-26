# rotating-proxy-scraper-bot
This is is still being developed but currently I have gotten it to print proxy lists from api with proxy_scraper, and use fiver scraper modular.py to load a proxy and complete login and button clicks on posts that fit specification. This has been written as a learning exercise and nothing more, please follow terms of service.  

03/26/2023-

This script is designed to scrape data from the website Fiverr using a list of proxies. If a proxy fails to connect, it is removed from the list and the script continues running until all proxies have been exhausted or there are no more proxies left in the list.
Installation

To run this script, you must have Python 3.8 or higher installed on your system. You will also need to install the urllib3 and proxy_scraper modules. You can do this using the following command:

pip install urllib3 proxy_scraper

Usage

Before running the script, you must have a file named proxy_list.txt in the same directory as the script. This file should contain a list of proxies in the following format:

makefile

ip_address:port

To run the script, simply execute the following command in your terminal:

python fiver_scraper.py

The script will load the list of proxies from the proxy_list.txt file and begin scraping data from Fiverr using a random proxy from the list. If a proxy fails to connect, it will be removed from the list and the script will continue running until all proxies have been exhausted or there are no more proxies left in the list. Once the script has finished running, it will print the number of removed proxies and delete the proxy_list.txt file.
License

This code is licensed under the MIT License.
