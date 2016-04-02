from sklearn.feature_extraction.text import CountVectorizer
from nltk.util import ngrams
from nltk.tokenize import TweetTokenizer
import nltk.data
from database import db_session
from models import HackCorpus
import cPickle
from itertools import chain, imap
import collections
import random

def flatten(l):
    for el in l:
        if isinstance(el, collections.Iterable) and not isinstance(el, basestring):
            for sub in flatten(el):
                yield sub
        else:
	    yield el

def get_corpus(d_session, category=None, size=None):
    """
    generate a corpus of traning text from DB
    """
    corpi = [post.text for post in d_session.query(HackCorpus).filter(HackCorpus.text != "" and HackCorpus.category=='lifehacks').all()]
    bigtext = "\n".join(corpi)
    return bigtext

def tokenize(big_text):
    tknzer = TweetTokenizer()
    tokens = tknzer.tokenize(big_text)
    return tokens

def build_model(tokens, n):
  "Builds a Markov model from the list of tokens, using n-grams of length n."
  model = dict()
  if len(tokens) < n:
    return model
  for i in range(len(tokens) - n):
    gram = tuple(tokens[i:i+n])
    next_token = tokens[i+n]
    if gram in model:
      model[gram].append(next_token)
    else:
      model[gram] = [next_token]
  final_gram = tuple(tokens[len(tokens)-n:])
  if final_gram in model:
    model[final_gram].append(None)
  else:
    model[final_gram] = [None]
  return model

def generate(model, n, seed=None, max_iterations=100):
  """Generates a list of tokens from information in model, using n as the
    length of n-grams in the model. Starts the generation with the n-gram
    given as seed. If more than max_iteration iterations are reached, the
    process is stopped. (This is to prevent infinite loops)"""
  if seed is None:
    seed = random.choice(model.keys())
  output = list(seed)
  current = tuple(seed)
  for i in range(max_iterations):
    if current in model:
      possible_next_tokens = model[current]
      next_token = random.choice(possible_next_tokens)
      if next_token is None: break
      output.append(next_token)
      current = tuple(output[-n:])
    else:
      break
  return output



def main():
    corpus = get_corpus(db_session)
    tokens = tokenize(corpus)
    model = build_model(tokens, 2)
    sentence = generate(model, 2, max_iterations=20)
    print ' '.join(sentence)
    

if __name__ == '__main__':
    main()
    
