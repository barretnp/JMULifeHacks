import praw
import re

def main():
    UA = 'Searching generically'
    r = praw.Reddit(UA)
    subreddit = r.get_subreddit('foodhacks+outdoors+lifehacks')
    for submission in subreddit.get_hot(limit=500):
        if re.search("pizza", submission.title, re.IGNORECASE) or re.search("pizza", submission.selftext, re.IGNORECASE):
	        print (submission.selftext[:2000], submission.title)

if __name__ == '__main__':
    main()
