import requests
import json
import logging

logging.basicConfig(filename="app_url_check.log", format='%(asctime)s %(message)s', filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

with open('article2user.json', 'r') as f_in:
    data = json.load(f_in)

urls = data.keys()

count = 0
for url in urls:
    status = requests.get(url).status_code
    if status == 404:
        count += 1
        print(f'INFO: URL {url} not available')
        logger.info(f'INFO: URL {url} not available')

print(f'INFO: No URL available for {count}')
logger.info(f'INFO: No URL available for {count}')
