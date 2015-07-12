# example of program that calculates the median number of unique words per tweet.
input_path="tweet_input/tweets.txt"
data=open(input_path)
words=list()
count=list()
median=list()
for idx, line in enumerate(data):
	count.append(len(set(line.split())))
sumup=0
length=0
for idx, val in enumerate(count):
	#l=count[0:(idx+1)]
	#m=sum(l)/float(len(l)) 
	sumup=sumup+val
	length=length+1
	m=sumup/float(length)
	median.append(m)
output = open("tweet_output/ft2.txt", "w")
for idx, val in enumerate(median):
	if idx < (len(median)-1):
		output.write("%s\n" % val)
	else:
		output.write("%s" % val)
