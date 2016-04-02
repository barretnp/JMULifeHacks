import praw
import pickle
from textblob.classifiers import NaiveBayesClassifier

UA = 'Trying to learn about food'
r = praw.Reddit(UA)
subreddit = r.get_subreddit('recipes')

train = []
test = []
count = 0

for submission in subreddit.get_hot(limit=200):
	if count <= 150:
		if str(subreddit) in subreddit.url and submission.selftext[:2000]:
			train.append((submission.selftext[:2000], 'food'))
	else:
		if str(subreddit) in subreddit.url and submission.selftext[:2000]:
			test.append((submission.selftext[:2000], 'food'))
	count += 1

subreddit = r.get_subreddit('lifehacks')
count = 0

for submission in subreddit.get_hot(limit=200):
	if count <= 150:
		if str(subreddit) in subreddit.url and submission.selftext[:2000]:
			train.append((submission.selftext[:2000], 'life'))
	else:
		if str(subreddit) in subreddit.url and submission.selftext[:2000]:
			test.append((submission.selftext[:2000], 'life'))
	count += 1

subreddit = r.get_subreddit('GetStudying')
count = 0

for submission in subreddit.get_hot(limit=200):
	if count <= 150:
		if str(subreddit) in subreddit.url and submission.selftext[:2000]:
			train.append((submission.selftext[:2000], 'study'))
	else:
		if str(subreddit) in subreddit.url and submission.selftext[:2000]:
			test.append((submission.selftext[:2000], 'study'))
	count += 1

subreddit = r.get_subreddit('outdoor')
count = 0

for submission in subreddit.get_hot(limit=200):
	if count <= 150:
		if str(subreddit) in subreddit.url and submission.selftext[:2000]:
			train.append((submission.selftext[:2000], 'events'))
	else:
		if str(subreddit) in subreddit.url and submission.selftext[:2000]:
			test.append((submission.selftext[:2000], 'events'))
	count += 1

f = open('myclassifier.pickle', 'wb')
cl = NaiveBayesClassifier(train)
pickle.dump(cl, f)
f.close()
print str(cl.accuracy(test) * 100) + "%"
cl.show_informative_features(10)

