import praw
from tweetahack.database import db_session
from tweetahack.models import HackCorpus
from functools import partial
from multiprocessing.pool import ThreadPool

result_list = []
def log_result(result):
    # This is called whenever foo_pool(i) returns a result.
    # result_list is modified only by the main process, not the pool workers.
    result_list.append(result)

def main():
    UA = 'Searching for life hacks'
    r = praw.Reddit(UA)
    pool = ThreadPool(4)
    subs = {'life':['lifehacks', 'actuallifehacks'],
            'food':['foodhacks', 'recipes', 'budgetfood'],
            'study':['GetStudying', 'MusicForConcentration', 'homeworkhelp' ],
            'outdoors':['outdoor', 'playgrounds', 'travel']}
    partial_parse = partial(parse_subreddit, r)
    for key, value in subs.iteritems():
        partial_2 = partial(partial_parse, key)
        res = pool.map(partial_2, value)
    pool.close()
    pool.join()
    print(result_list)


def parse_subreddit(reddit_session, category, subreddit_list):
    cur_subreddit = reddit_session.get_subreddit(subreddit_list)
    for submission in cur_subreddit.get_hot(limit=1000):
        if submission.is_self:
            db_session.add(HackCorpus(text=submission.selftext[:2000], url=submission.url, title=submission.title))
        else:
            db_session.add(HackCorpus(text=None, url=submission.url, title=submission.title))
    db_session.commit()
    return 'DONE!: ' + str(subreddit_list)


if __name__ == '__main__':
    main()
