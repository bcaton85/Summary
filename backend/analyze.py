from __main__ import *
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk import tokenize
import pickle

def extract_features(document, word_features):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

def analyze(summary):
	
	# Retrives only the sentences from the training document
	# Those sentences are then split creating a long list of individual words
	sentim_analyzer = SentimentAnalyzer()
	all_words = sentim_analyzer.all_words([summary])

	# Retrieve most frequently occuring words from the word list
	unigram_feats = sentim_analyzer.unigram_word_feats(all_words, min_freq=2)

	f = open('model.pickle', 'rb')
	classifier = pickle.load(f)
	f.close()

	#Classify the summary 
	return "Obj: "+ str(classifier.prob_classify(extract_features(summary.split(), unigram_feats)).prob('obj')) +" Sub:"+str(classifier.prob_classify(extract_features(summary.split(), unigram_feats)).prob('sub')) +summary

	