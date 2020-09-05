from nltk import ngrams, FreqDist
import pudb
import json

f = open("sample_text", "r")
lines = f.readlines()
text = ""
for line in lines:
    text += line.strip() + " "
f.close()

all_counts_1 = dict()
for size in 1, 2, 3:
    all_counts_1[size] = FreqDist(ngrams(text.split(), size))

f = open("sample_text_2", "r")
text = ""
for line in lines:
    text += line.strip() + " "
f.close()

all_counts_2 = dict()
for size in 1, 2, 3:
    all_counts_2[size] = FreqDist(ngrams(text.split(), size))

all_counts = {}

all_counts[1] = [x[0] for x in all_counts_1[1].most_common(10)]
all_counts[1].extend([x[0] for x in all_counts_2[1].most_common(10)])


all_counts[2] = [x[0] for x in all_counts_1[2].most_common(10)]
all_counts[2].extend([x[0] for x in all_counts_2[2].most_common(10)])


all_counts[3] = [x[0] for x in all_counts_1[3].most_common(10)]
all_counts[3].extend([x[0] for x in all_counts_2[3].most_common(10)])
f = open("samples.json", "w")
json.dump(all_counts, f, indent=4)
f.close()
