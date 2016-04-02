import pickle


def classify(self, tweet):
    f = open('my_classifier.pickle', 'rb')
    classifier = pickle.load(f)

    category = classifier.classify(tweet)

    f.close()
    return category
