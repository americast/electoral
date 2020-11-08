import os
import json
import logging

logging.basicConfig(filename="app_extract.log", format='%(asctime)s %(message)s', filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

DATA_PATH = "../one_week"

print('INFO: Reading input directory')
logger.info('INFO: Reading Input directory ')
# Listing the directories in the folder
files = os.listdir(DATA_PATH)

map_user2article = {}
map_article2user = {}

count_html = 0
all_articles_set = set() # unique collection of all articles

for file in files:
    f = open(DATA_PATH + "/" + file).read()
    # Each line determines a data point in the form of a JSON data
    fs = f.split("\n")
    logger.info(f"INFO: Reading for file {file}")
    print(f"INFO: Reading for file {file}")
    for each_f in fs:
        try:
            # Converting a string data point into JSON form for parsing
            data = json.loads(each_f)
            # Executing first level sanity checks
            if "profile" not in data:
                if "userId" in data and "activeTime" in data and "url" in data:
                    all_articles_set.add(data['url'])
                    if not str(data['url']).endswith(".html"):
                        continue
                    count_html += 1
                    logger.info(f"INFO: Working for count {count_html} with data {data['url']} {data['userId']} ")
                    print(f"INFO: Working for count {count_html} with data {data['url']} {data['userId']} ")

                    # Processing for the user. Forming the user wise JSON file
                    if data["userId"] not in map_user2article:
                        map_user2article[data["userId"]] = {}
                    if data["url"] not in map_user2article[data["userId"]]:
                        map_user2article[data["userId"]][data["url"]] = []
                    map_user2article[data["userId"]][data["url"]].append(data["activeTime"])

                    # Processing for the URL. Forming the URL wise JSON file
                    if data["url"] not in map_article2user:
                        map_article2user[data["url"]] = {}
                    if data["userId"] not in map_article2user[data["url"]]:
                        map_article2user[data["url"]][data["userId"]] = []
                    map_article2user[data["url"]][data["userId"]].append(data["activeTime"])
        except:
            pass

logger.info(f'INFO: Final all count {len(all_articles_set)} ')
print(f'INFO: Final all count {len(all_articles_set)} ')

logger.info(f'INFO: Final HTML count {count_html} Saving files ...')
print(f'INFO: Final HTML count {count_html} Saving files ...')

f_user2article = open("user2article.json", "w")
f_article2user = open("article2user.json", "w")

f_user2article.write(json.dumps(map_user2article, indent=4))
f_article2user.write(json.dumps(map_article2user, indent=4))

with open('all_articles.txt', 'w') as f:
    for item in all_articles_set:
        f.write("%s\n" % item)