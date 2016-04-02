import praw
from tweetahack.database import db_session
from tweetahack.models import HackCorpus
from functools import partial
from multiprocessing.pool import ThreadPool

def main():
    UA = 'Searching for food hacks'
    r = praw.Reddit(UA)
    pool = ThreadPool(4)
    subs = ['GetStudying', 'MusicForConcentration','homeworkhelp']
    partial_parse = partial(parse_subreddit, r)
    res = pool.map(partial_parse, subs)
    print res

def parse_subreddit(reddit_session, subreddit):
    cur_subreddit = reddit_session.get_subreddit(subreddit)
    for submission in cur_subreddit.get_hot(limit=1000):
        if str(cur_subreddit) in cur_subreddit.url and submission.selftext[:2000]:
	        db_session.add(HackCorpus(category=str(cur_subreddit), text=submission.selftext[:2000], url=submission.url))
    db_session.commit()
    return 'DONE!: ' + str(subreddit)


if __name__ == '__main__':
    main()
