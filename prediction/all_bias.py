left_list = [
    "motstandernes", 
    "røde", 
    "djevlene", 
    "møter", 
    "motstander", 
    "problem", 
    "motstand", 
    "scorer", 
    "møte", 
    "sjef", 
    "oftest", 
    "smadret", 
    "kontret", 
    "scoringslisten", 
    "balanse", 
    "maktet", 
    "igjen", 
    "rød", 
]

right_list = [
    "bakgrunnen",
    "grunn",
    "etablerte",
    "opprettelsen",
    "døpt",
    "alternativ",
    "offensivt",
    "defensiv",
    "innrømmer",
    "offensive",
    "balanse",
    "offensiv",
    "uttrykk",
    "assisterende",
    "renter",
    "tilværelsen",
    "anslår",
    "eventyret",
    "høyre",
    "erna",
    "siv",
    "hans",
]

import json
import pudb
from tqdm import tqdm
import pandas as pd

f = open("article2user.json", "r")
all_links = json.load(f)
f.close()

f = open("article_text_all.json", "r")
all_text = json.load(f)
f.close()

final_dict = {"left": 0, "right": 0}

for i, each_link in tqdm(enumerate(all_links)):
    time = 0
    for each in all_links[each_link]:
        time += sum(all_links[each_link][each])
    try:
        text_here = all_text[str(i)]["text"] + all_text[str(i)]["head"] + all_text[str(i)]["lead"]
    except:
        continue
    assert each_link == all_text[str(i)]["article"]
    left_count, right_count = 0, 0
    for l in left_list:
        # if l in text_here:
        #     left_count += 1
        left_count += text_here.count(l)
    for r in right_list:
        # if r in text_here:
        #     right_count += 1
        right_count += text_here.count(r)
    # left_count /= len(left_list)
    # right_count /= len(right_list)
    if left_count < 0.1 and right_count < 0.1:
        continue
    elif left_count > right_count:
        final_dict["left"] += time
    elif left_count < right_count:
        final_dict["right"] += time

df = pd.read_csv("election_results.csv")

final_bias = {}
for i, row in tqdm(df.iterrows()):
    row = list(row)
    e_type = row[0]
    values = row[1:11]
    text_here = ""
    for val in values:
        try:
            text_here += all_text[str(val)]["text"] + all_text[str(val)]["head"] + all_text[str(val)]["lead"]
        except:
            continue
    left_count, right_count = 0, 0
    for l in left_list:
        left_count += text_here.count(l)
    for r in right_list:
        right_count += text_here.count(r)
    final_bias[e_type] = (-left_count + (final_dict["left"]/final_dict["right"]) * right_count) / (left_count + (final_dict["left"]/final_dict["right"]) * right_count)


