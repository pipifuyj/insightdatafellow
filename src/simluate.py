#example of simulate one hour data
import random
input_path="../tweet_input/tweets.txt"
lines=open(input_path).readlines()
output = open("../tweet_input/test.txt", "w")
num=100000000
for idx in range(num):
	output.write(lines[int(random.uniform(0, 2))])