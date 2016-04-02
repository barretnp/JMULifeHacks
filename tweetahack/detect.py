import pickle


def classify(tweet):
    f = open('myclassifier.pickle', 'rb')
    classifier = pickle.load(f)

    category = classifier.classify(tweet)

    f.close()
    return category
