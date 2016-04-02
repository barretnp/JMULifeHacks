from sklearn.feature_extraction.text import CountVectorizer
from nltk.util import ngrams
from nltk.tokenize.api import StringTokenizer
import nltk.data
from database import db_session
from models import HackCorpus
import cPickle
from itertools import chain, imap
import collections

def flatten(l):
    for el in l:
        if isinstance(el, collections.Iterable) and not isinstance(el, basestring):
            for sub in flatten(el):
                yield sub
        else:
	    yield el

def generate_ngrams(d_session):
    corpi = [post.text for post in d_session.query(HackCorpus).filter(HackCorpus.text != "").all()]
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    bigtext = "\n".join(corpi)
    #sentences = [sentence for sentence in sent_detector.tokenize(bigtext)]
    #print sentences[5]
    gen_ngrams = ngrams(bigtext.split(' '), 2)
    ngram_dict = {}
    for item in gen_ngrams:
        if item not in ngram_dict:
            ngram_dict[item]=1
        else:
            ngram_dict[item]+=1
    return ngram_dict

def main():
    ngrams_generated = generate_ngrams(db_session)
    for key in ngrams_generated.keys():
        print str(key) + ": " + str(ngrams_generated[key])

if __name__ == '__main__':
    main()
    
