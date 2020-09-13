import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import json
import pudb
from tqdm import tqdm
import numpy as np
from nltk.stem.snowball import SnowballStemmer

ss = SnowballStemmer("norwegian")


f = open("article_text.json", "r")
dict_here = json.load(f)
f.close()

text_list = [dict_here[x]["text"] + ". " + dict_here[x]["lead"] + ". " + dict_here[x]["head"]+". " for x in dict_here]
text_all = ""
# pu.db
for t in text_list:
    text_all += t + " "

text_list = sent_tokenize(text_all)
words = word_tokenize(text_all)
words = [w.lower() for w in words]
words = list(set(words))
N = len(text_list)

labels = ["rød", "røde", "venstre", "Igjen","Arbeiderparti", "Støre", "Stoltenberg", "Sosialistisk", "Venstreparti", "Audun", "Lysbakken"]
labels = [l.lower() for l in labels]

word_dict = {}
label_dict = {}

for word in tqdm(words):
    count = 0
    for text in text_list:
        if word in text:
            count += 1
    word_dict[word] = count

for label in tqdm(labels):
    count = 0
    for text in text_list:
        if label in text:
            count += 1
    label_dict[label] = count

all_PMI = []
for i, label in tqdm(enumerate(labels)):
    all_PMI.append({})
    for word in words:
        count = 0
        for text in text_list:
            if word in text and label in text:
                count += 1
        try:
            all_PMI[i][label+"&_&"+word] = np.log(N * count / (word_dict[word] * label_dict[label]))
        except:
            all_PMI[i][label+"&_&"+word] = 0.0

    all_PMI[i] = {k: v for k, v in sorted(all_PMI[i].items(), key=lambda item: item[1], reverse=True)[:20]}

for i in range(len(all_PMI)):
    for each in all_PMI[i]:
        if all_PMI[i][each] > 0:
            print(each.replace("&_&",": "))
pu.db
