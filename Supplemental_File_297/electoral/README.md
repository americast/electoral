# Two-Sided Fairness in Non-Personalised Recommendations

## File descriptions
This is a collaborative effort of Aadi Swadipto Mondal, Sayan Sinha, Rakesh Bal and Gourab Patro for exploring fairness in recommender systems. We have analysed two specific fairness concerns -- _User fairness_ and _Organisational fairness_. This repository contains all the necessary codes used during the analysis. The methodological details can be found in the paper. All codes have been implemented in Python.

### Data Extraction

The data for this analysis can be downloaded from [this](http://reclab.idi.ntnu.no/dataset/) link. After downloading, set the data path in variable `DATA_PATH` of `extract.py`. This script will re-organise the data in JSON format. Two files are produced: one is ordered with respect to the users and the other with respect to the articles. Along with them, article links are also stored in a separate file. 

### Data Modelling

The script `modelling.py` is used for calculating the score of an article with respect to the user. As explained in the paper, the score is a linearly scaled number ranging from 1 to 10 based on the active time. This script calculates the active time for each user and article from the JSON files produced during data extraction. Finally, it determines the score matrix and stores in the `modelling.csv` file.

### Non-Negative Matrix Factorisation

As explained in the paper, the script `NMF.py` performs the non-negative matrix factorisation. At each step, we perform gradient descent and monitor the Root-Mean Square Error (RMSE). The maximum number of iterations performed is 5000. However, we require less no of iterations than that. After executing the required number of iterations, the predicted matrix is stored in the file `predicted_nmf_text_numpy.txt`.

### Election Simulation

We simulate six election methods. The files that perform the simulations are listed below. To execute the simulations, run the assister file of the corresponding election method followed by the main file. Each assister file takes the `predicted_nmf_text_numpy.txt` as the input. The main file saves the election results with a file name same as that of the election method name.

- **SNTV** : `SNTV.py` assisted by `counter.py` 
- **Borda** : `k_borda_count.py` assisted by `counter.py`
- **Bloc** : `bloc.py` assisted by `counter_bloc.py`
- **STV** : `stv.py` assisted by `counter.py`
- **CC** : `chamberlin.py` assisted by `counter_chamberlin.py`
- **Monroe** : `chamberlin.py` assisted by `counter_monroe.py`


### Article Scraping

- `scraper_article.py` : This script reads one by one the article links from the JSON (generated in Data Extraction section) by data extraction. Using a wrapper of python-requests which can simulate browser environments, the script scrapes the body, heading and other important section of all the articles and stores the data in JSON format. Similar to this `winner_scraper.py` scrapes only the articles for the winners of the election.

- `check_urls.py` : This script makes python-requests and checks if the URL is valid is not. 


## Code flow
### Dependencies
Both Python 3 and Python 2 have been used in this project. Python package dependencies can be installed using:

```
pip3 install -r req3
pip2 install -r req2
```

Extract the dataset and code folder in the same directory, otherwise set the data path as mentioned earlier in `extract.py`. Then this will be the flow of the code execution:  
```
python3 extract.py
cd prediction
python3 modelling.py && python3 NMF.py
python3 counter.py && python3 counter_bloc.py && python3 counter_chamberlin.py
python3 bloc.py && python3 chamberlin.py && python3 k_borda_count.py && python3 sntv.py
python3 counter_monroe.py && python3 chamberlin.py # chamberlin.py also runs monroe election method when succeeded by counter_monroe.py 
python2 stv.py 
cd ..
```
Copy all the result files in a folder named `election_results`. One can also modify `RESULTS_PATH` if required. Along with that, change the `TEST_CSV_PATH` if required. Next part is to scrape the articles. 

```
python3 scraper_article.py
```
This will generate `article_text.json`, which needs to be placed in the directory `PMI/`.

### User Fairness
Prepare a JSON file with election method name as the key, and the set of corresponding winners in respective lists (each winner is represented by the user no, which is an integer). Save the JSON file as `results.json` in the `prediction/` folder. The satisfaction values for the respective election methods can be obtained using:  

```
cd prediction
python3 satisfaction.py
cd ..
```

### Organisational Fairness
Organisational Fairness is measured using Pointwise Mutual Information (PMI). The results, just like the one created in the previous method, is saved in the `PMI` folder. The format, however, is CSV. It is saved as `election_results.csv`. Then, the following commands are executed:

```
cd PMI
python3 PMI_left.py
python3 PMI_right.py
python3 all_bias.py
```

Sample result files (`results.json` and `election_results.csv`) have been provided in this repository for reference.
