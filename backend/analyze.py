from __main__ import *
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk import tokenize

def extract_features(document, word_features):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


def analyze(summary):
	n_instances = 100

	# Get 100 objective and subjective sentences, each entry is the form  < "sentence":subj/obj >
	subj_docs = [(sent, 'subj') for sent in subjectivity.sents(categories='subj')[:n_instances]]
	obj_docs = [(sent, 'obj') for sent in subjectivity.sents(categories='obj')[:n_instances]]

	# Split into 80 trainging documents and 20 testing documents
	train_subj_docs = subj_docs[:80]
	test_subj_docs = subj_docs[80:100]
	train_obj_docs = obj_docs[:80]
	test_obj_docs = obj_docs[80:100]
	training_docs = train_subj_docs+train_obj_docs
	testing_docs = test_subj_docs+test_obj_docs

	# Retreives only the sentences from the training document
	# Those sentences are then split creating a long list of individual words
	sentim_analyzer = SentimentAnalyzer()
	all_words = sentim_analyzer.all_words([doc for doc in training_docs])

	# Retrieve most frequently occuring words from the word list
	unigram_feats = sentim_analyzer.unigram_word_feats(all_words, min_freq=4)

	#Add the default feature extractor
	sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=unigram_feats)

	# Extracts features from training docs, if a feature is found it is entered into a map
	# of the form < ({ contains(feature):true/false, contains(feature):true/false, contains(feature):true/false } : 'sub/obj' )>
	training_set = sentim_analyzer.apply_features(training_docs)
	test_set = sentim_analyzer.apply_features(testing_docs)

	#Train the classifier with data from the training set
	trainer = NaiveBayesClassifier.train
	classifier = sentim_analyzer.train(trainer, training_set)

	for key,value in sorted(sentim_analyzer.evaluate(test_set).items()):
		print('{0}: {1}'.format(key, value))

		
	#Classify the summary 
	return classifier.classify(extract_features(summary.split(), unigram_feats))
