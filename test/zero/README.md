`test.json` is the truncated version of `article2user.json`.  
`test.py` converts it to a df, i.e. `test.csv`.  
`zero.py` takes `test.csv` to create a matrix, `zero_text.txt`.  
`counter.py` takes `zero_test.txt` and converts it into a format suitable for election, and stores it in `count.json`.  
`counter_bloc.py` takes `zero_test.txt` and converts it into a format suitable for bloc voting, and stores it in `count_bloc.json`.  
`stv.py`, `sntv.py`, `k_borda_count.py` take `count.json` to provide election results.  
`bloc.py` takes `count_bloc.json` to provide its result.
