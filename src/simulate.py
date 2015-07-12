#example of simulate one hour data
input_path="../tweet_input/tweets.txt"
lines=open(input_path).readlines()
output = open("tweet_input/test.txt", "w")
num=1000
for idx in range(num):
	output.write(lines[1])