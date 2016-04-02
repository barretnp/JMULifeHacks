import praw
from textblob.classifiers import NaiveBayesClassifier

UA = 'Trying to learn about food'
r = praw.Reddit(UA)
subreddit = r.get_subreddit('recipes')

train = []
test = []
count = 0

for submission in subreddit.get_hot(limit=100):
	if count <= 80:
		if str(subreddit) in subreddit.url and submission.selftext[:2000]:
			train.append((submission.selftext[:2000], 'food'))
	else:
		if str(subreddit) in subreddit.url and submission.selftext[:2000]:
			test.append((submission.selftext[:2000], 'food'))
	count += 1

subreddit = r.get_subreddit('lifehacks')
count = 0

for submission in subreddit.get_hot(limit=100):
	if count <= 80:
		if str(subreddit) in subreddit.url and submission.selftext[:2000]:
			train.append((submission.selftext[:2000], 'life'))
	else:
		if str(subreddit) in subreddit.url and submission.selftext[:2000]:
			test.append((submission.selftext[:2000], 'life'))
	count += 1

cl = NaiveBayesClassifier(train)
print str(cl.accuracy(test) * 100) + "%"
