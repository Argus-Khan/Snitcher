import json

with open('word_list.json') as wl:
		wordlist = json.load(wl)

def snitch(word):

	wrd = word.lower()
	wrdL = []
	wrdL.append(wrd)

	comparision = set(wordlist).intersection(wrdL)

	return comparision
	# print(wordlist)
