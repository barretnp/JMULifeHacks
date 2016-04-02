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
import re
import string

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
    corpi = [post.text for post in d_session.query(HackCorpus).filter(HackCorpus.text != "" and HackCorpus.category==category).all()]
    bigtext = "\n".join(corpi)
    return bigtext

def get_instructions(big_corpus):
    recipe_pattern = re.compile(r'[1-9][)]*[.]*[)]*')
    my_pattern = recipe_pattern.split(big_corpus)
    if len(my_pattern) > 0:
        res = filter(lambda x: x[0].isdigit() if len(x) > 0 else False, my_pattern)
    else:
        res = "None"
    return res
    

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

def generate(model, n, seed=None, max_iterations=7, max_len=140):
  """Generates a list of tokens from information in model, using n as the
    length of n-grams in the model. Starts the generation with the n-gram
    given as seed. If more than max_iteration iterations are reached, the
    process is stopped. (This is to prevent infinite loops)"""
  sentence_starts = filter(lambda x: x[0][0].isupper(), model.keys())
  sentence_ends = filter(lambda x: x[n-1][0] in set(string.punctuation), model.keys())
  if seed is None:
    seed = random.choice(sentence_starts)
  output = list(seed)
  current = tuple(seed)
  for i in range(max_iterations):
    if current in model:
      possible_next_tokens = model[current]
      next_token = random.choice(possible_next_tokens)
      if next_token is None: break
      cur_len = 0
      for tok in output:
        cur_len += len(tok)
      if (cur_len + len(next_token)) > (max_len-15):
          next_token = random.choice(sentence_ends)
      output.append(next_token)
      if output[-1] in string.punctuation: break
      current = tuple(output[-n:])
  return output

def build_bad_advice(db_session, cat='lifehacks', cat2='shittylifehacks'):
    corpus = get_corpus(db_session, category=cat)
    bad_corpus = get_corpus(db_session, category=cat2)
    tokens = tokenize(corpus)
    bad_tokens = tokenize(bad_corpus)
    model = build_model(tokens, 2)
    bad_model = build_model(bad_tokens, 2)
    sentence = generate(model, 2, max_iterations=20)
    second_sentence = generate(bad_model, 2, max_iterations=20)
    out = ' '.join(sentence)
    out2 = ' '.join(second_sentence)
    return out + ' ' + out2


def main():
        print build_bad_advice(db_session, cat='foodhacks', cat2='budgetfood')
    

if __name__ == '__main__':
    main()
    
