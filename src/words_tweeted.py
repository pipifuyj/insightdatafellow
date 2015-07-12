# example of program that calculates the total number of times each word has been tweeted.
from collections import Counter
input_path="tweet_input/tweets.txt"
data=open(input_path)
words=list()
for i, line in enumerate(data):
	words.extend(line.split())
word_count=Counter(words)
keys=sorted(word_count.keys(), key=lambda str: [ord(ele) for ele in str])
output = open("tweet_output/ft1.txt", "w")
for idx, val in enumerate(keys):
	if idx < (len(keys)-1):
		output.write("%-28s%s\n" % (val, word_count[val]))
	else:
		output.write("%-28s%s" % (val, word_count[val]))