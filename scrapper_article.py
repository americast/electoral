import json
from typing import Dict, List
import logging
import time

from requests_html import HTMLSession, Element
import requests_html

logging.basicConfig(filename="app_scrapper.log", format='%(asctime)s %(message)s', filemode='w')
logging.getLogger(requests_html.__name__).setLevel(logging.WARNING)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logger.info('INFO: Reading article file')
print('INFO: Reading article file')

with open('article2user.json', 'r') as f_in:
    data: Dict = json.load(f_in)

articles = list(data.keys())

logger.info(f'INFO: Found {len(articles)} articles')
print(f'INFO: Found {len(articles)} articles')

session = HTMLSession()
logger.info('INFO: Created session')
print('INFO: Created session')

text_collection = {}
count_error = 0

for index, article in enumerate(articles):
    try:
        r = session.get(str(article).strip(' \n'))
        try:
            r.html.render()
            print('INFO: HTML render successful')
            logger.info('INFO: HTML render successful')
        except:
            print('ERROR: Exception occurred for rendering. Retrying ...')
            logger.exception('ERROR: Exception occurred for rendering. Retrying ...')
            r.html.render()
            print('INFO: HTML render successful')
            logger.info('INFO: HTML render successful')
        lst: List[Element] = r.html.find('.body')
        lst_title: List[Element] = r.html.find('.title')
        lst_lead: List[Element] = r.html.find('.lead')
        if len(lst) != 0:
            text = str(lst[0].text).replace('\n', ' ')
        else:
            text = ""
            print(f'INFO: No body found for {article}')
            logger.info(f'INFO: No body found for {article}')
        if len(lst_title) != 0:
            head = str(lst_title[0].text).replace('\n', ' ')
        else:
            head = ""
            print(f'INFO: No head found for {article}')
            logger.info(f'INFO: No head found for {article}')
        if len(lst_lead) != 0:
            lead = str(lst_lead[0].text).replace('\n', ' ')
        else:
            lead = ""
            print(f'INFO: No lead found for {article}')
            logger.info(f'INFO: No lead found for {article}')
        text_collection[index] = {'text': text, 'head': head, 'lead': lead, 'article': article}

    except:
        print(f'ERROR: Exception occurred for {article}')
        logger.exception(f'ERROR: Exception occurred for {article}')
        count_error += 1

    if index % 50 == 0:
        print(f'INFO: Taking rest for 10s')
        logger.info(f'INFO: Taking rest for 10s')
        time.sleep(10)
        session = HTMLSession()
        logger.info('INFO: Created new session')
        print('INFO: Created new session')

logger.info(f'INFO: Articles not scraped count {count_error}')
print(f'INFO: Articles not scraped count {count_error}')

with open('article_text.json', 'w') as f_out:
    json.dump(text_collection, f_out)

logger.info('INFO: Articles text saved')
print('INFO: Articles text saved')
