import requests
import json
import pprint
import sys


def get_Kt(pt_days):
	Lt = min(pt_days)
	Ht = max(pt_days)
	C = pt_days[0]
	print "Lt"
	print Lt
	print "Ht"
	print Ht
	print "C"
	print C
	if Ht == Lt:
		K = 100*((C-Lt)/(1))
	else:
		K = 100*((C-Lt)/(Ht-Lt))
	return K

def sto_osc5(t_history, p_history_hash):
	# take slices 
	pt1 = [p_history_hash[t] for t in t_history[0:5]]
	pt2 = [p_history_hash[t] for t in t_history[5:10]]
	pt3 = [p_history_hash[t] for t in t_history[10:]]
	print "pt1 {}".format(pt1)
	print "pt2 {}".format(pt2)
	print "pt3 {}".format(pt3)
	K1 = get_Kt(pt1)
	K2 = get_Kt(pt2)
	K3 = get_Kt(pt3)
	print "K1 {}".format(K1)
	print "K2 {}".format(K2)
	print "K3 {}".format(K3)

	D = 100*(K1+K2+K3)/3
	return D

def sto_osc14(t_history, p_history_hash):
	# take slices 
	pt1 = [p_history_hash[t] for t in t_history[0:14]]
	pt2 = [p_history_hash[t] for t in t_history[14:28]]
	pt3 = [p_history_hash[t] for t in t_history[28:]]
	print "pt1 {}".format(pt1)
	print "pt2 {}".format(pt2)
	print "pt3 {}".format(pt3)
	K1 = get_Kt(pt1)
	K2 = get_Kt(pt2)
	K3 = get_Kt(pt3)
	print "K1 {}".format(K1)
	print "K2 {}".format(K2)
	print "K3 {}".format(K3)

	D = ((K1+K2+K3)/3)
	return D

def get_item_data(code):
	url_base = "http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item="

	try:
		item = requests.get(price_url_base + item_code).json()['item']['name']
#		item_name = item.json()['item']['name']
	
	except ValueError as v:
		return None
	else:
		print "Item: {}".format(item_name)
		history_url = "http://services.runescape.com/m=itemdb_rs/api/graph/"+ item_code +".json"
		daily_price_history = requests.get(history_url).json['daily']
#		price_history = price_history.json()['daily']



search_terms = sys.argv[1:]

with open("RScodes.txt", "r") as f_lines:
	for line in f_lines:
		if "Swap this note at any bank" not in line:
			for word in search_terms:
				if word.lower() in line.lower():
					print line,
					continue

item_code = raw_input("Runescape item code:")

t_hist = []
print p_hist
for k,v in p_hist.iteritems():
	t_hist.append(k)
#gets the previous 16 days of times
#will be used to access prices
t_hist = sorted(t_hist, reverse = True)[0:42]
for i in t_hist:
	print i

	
	print("Stochastic Oscillator over 5-day period: {}".format(sto_osc14(t_hist, p_hist)))
# %K = 100[(C - L14)/(H14 - L14)]
# %D = 3-period moving average of %K
#	where C is the most recent closing price
#	L14 is the low and H14 is the high of the previous 14 trading sessions (days)
# Wikipedia version:
#	%K = 100 *((Price-L5)/(H5-L5))
#   %D = 100*((K1+K2+K3)/3) 
