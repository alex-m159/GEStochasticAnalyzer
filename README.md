# GEStochasticAnalyzer
This script will retrieve RuneScape pricing data for tradable items, and computes the stochastic oscillator value based on the past several weeks of price data.

# How To Use This Script
Download the GrandEx.py script and the RSCodes.txt file, saving both to the same directory.
Open a terminal window and move to the directory of GrandEx.py.
Run the following command to start the program:
```python
python GrandEx.py <search term1> [<search term2> ...]
```

The "search term" argument will be used to filter a list of RuneScape items down to those containing the search terms.
That list will be printed and you'll be prompted to enter an item code.
The program will make a call to the RuneScape API to get the pricing data; if it fails, then you'll be prompted to enter a code again. On success, it will print the stochastic oscillator value of the item based on the past 6 weeks (3 2-week intervals).

You can read more about the stochastic oscillator on Wikipedia:
https://en.wikipedia.org/wiki/Stochastic_oscillator
