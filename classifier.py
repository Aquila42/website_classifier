__author__ = 'Aquila'

import urllib2
import os, sys, re, nltk, enchant, random
import simplejson as json
import xml.etree.ElementTree as ET
from nltk.corpus import nps_chat
from nltk.classify.naivebayes import NaiveBayesClassifier as learner
from bs4 import BeautifulSoup

english = enchant.Dict("en_US")
SUBJECT_CHARS = 50

class CategoryClassifier:
    """Classify text based on the formality of the formatting and content"""

    def build_classifier(self):

        #print "Creating a list of labels. If this is done, the previous init doesn't have to be"
        labels = ['arts','business','computers','home','recreation','science','shopping','knowledge']

        self.labeled_features = []
        for label in labels:
            print label.upper()
            self.labeled_features.extend(self.build_data_set(label))
            print self.labeled_features

        print self.labeled_features

        print "Labeled Features: ",self.labeled_features
        classifier = learner.train(self.labeled_features)
        classifier.show_most_informative_features()
        return classifier


    def build_data_set(self,label):
        #print "Train classifier with label 'arts' in build_data_set"
        urls = "subset/"+label+"_urls"
        #print "Open arts_urls - this is what has to be classified"
        f = open(urls,'r')
        #Got the URLs from file

        #print "Fetch data from each URL"
        for url in f:
            try:
                valid_url = urllib2.urlopen(url,None,1)
                #get html from URL
                html = valid_url.read()
                print url
            except:
                continue
            soup = BeautifulSoup(html, 'html.parser')
            #like gettine msg
            raw = soup.get_text().strip()
            builder = raw.encode("ascii","ignore")
            labeled_sets = []
            labeled_sets.append((self.extract_features(builder), label))
        return labeled_sets

    def test_self(self):
        correct = 0
        for (example, label) in self.labeled_features:
            if self.classifier.classify(example) == label:
                correct += 1
        print correct, " / ", len(self.labeled_features)

    def get_classifier(self):
        return self.classifier

    def get_true_value(self):
        return self.formal_label

    def file_to_dict(self, filename):
        lines_dict = {}
        for line in file(filename).readlines():
            temp = line.strip().split()
            lines_dict[temp[0]] = int(temp[1])
        return lines_dict

    def classification_format(self, raw):
        msg = nltk.clean_html(raw)
        fs = self.extract_features(msg)
        return fs

    def classify(self, raw):
        return self.classifier.classify(self.classification_format(raw))

    def prob_classify(self, raw):
        dist = self.classifier.prob_classify(self.classification_format(raw))
        return dist.prob(dist.max())

    def extract_features(self, msg):
        # features:
        # 	portion of words capitalized properly
        # 	occurrence of swear words, emoticons, and
        # 	number of misspelled words (real but not spelled correctly)

        #print "Get words from the webpage. This includes html"
        words = nltk.word_tokenize(msg)
        counts = {}
        features = {}
        counts["agriculture"] = 0
        counts["animals"] = 0
        counts["animation"] = 0
        counts["architecture"] = 0
        counts["astronomy"] = 0
        #counts["science"] = 0
        counts["books"] = 0
        counts["chemistry"] = 0
        counts["commerce"] = 0
        counts["crafts"] = 0
        counts["current"] = 0
        counts["economy"] = 0
        counts["education"] = 0
        counts["films"] = 0
        counts["games"] = 0
        counts["government"] = 0
        counts["history"] = 0
        counts["hobbies"] = 0
        counts["household"] = 0
        counts["manufacturing"] = 0
        counts["medical"] = 0
        counts["music"] = 0
        counts["reference"] = 0
        counts["services"] = 0
        counts["society"] = 0
        counts["sports"] = 0
        counts["technology"] = 0
        counts["travel"] = 0
        for word in words:
            word.lower()
            if word in self.agriculture.keys():
                counts["agriculture"] += 1/float(self.agriculture[word])
                print "agriculture ",word
            if word in self.animals.keys():
                counts["animals"] += 1/float(self.animals[word])
                print "animals ",word
            if word in self.animation.keys():
                counts["animation"] += 1/float(self.animation[word])
                print "animation ",word
            if word in self.architecture.keys():
                counts["architecture"] += 1/float(self.architecture[word])
                print "architecture ",word
            if word in self.astronomy.keys():
                counts["astronomy"] += 1/float(self.astronomy[word])
                print "astronomy ",word
            if word in self.books.keys():
                counts["books"] += 1/float(self.books[word])
                print "books ",word
            if word in self.chemistry.keys():
                counts["chemistry"] += 1/float(self.chemistry[word])
                print "chemistry ",word
            if word in self.commerce.keys():
                counts["commerce"] += 1/float(self.commerce[word])
                print "commerce ",word
            if word in self.crafts.keys():
                counts["crafts"] += 1/float(self.crafts[word])
                print "crafts ",word
            if word in self.current.keys():
                counts["current"] += 1/float(self.current[word])
                print "current ",word
            if word in self.economy.keys():
                counts["economy"] += 1/float(self.economy[word])
                print "economy ",word
            if word in self.education.keys():
                counts["education"] += 1/float(self.education[word])
                print "education ",word
            if word in self.films.keys():
                counts["films"] += 1/float(self.films[word])
                print "films ",word
            if word in self.games.keys():
                counts["games"] += 1/float(self.games[word])
                print "games ",word
            if word in self.government.keys():
                counts["government"] += 1/float(self.government[word])
                print "government ",word
            if word in self.history.keys():
                counts["history"] += 1/float(self.history[word])
                print "history ",word
            if word in self.hobbies.keys():
                counts["hobbies"] += 1/float(self.hobbies[word])
                print "hobbies ",word
            if word in self.household.keys():
                counts["household"] += 1/float(self.household[word])
                print "household ",word
            if word in self.manufacturing.keys():
                counts["manufacturing"] += 1/float(self.manufacturing[word])
                print "manufacturing ",word
            if word in self.medical.keys():
                counts["medical"] += 1/float(self.medical[word])
                print "medical ",word
            if word in self.music.keys():
                counts["music"] += 1/float(self.music[word])
                print "music ",word
            if word in self.reference.keys():
                counts["reference"] += 1/float(self.reference[word])
                print "reference ",word
            if word in self.services.keys():
                counts["services"] += 1/float(self.services[word])
                print "services ",word
            if word in self.society.keys():
                counts["society"] += 1/float(self.society[word])
                print "society ",word
            if word in self.sports.keys():
                counts["sports"] += 1/float(self.sports[word])
                print "sports ",word
            if word in self.technology.keys():
                counts["technology"] += 1/float(self.technology[word])
                print "technology ",word
            if word in self.travel.keys():
                counts["travel"] += 1/float(self.travel[word])
                print "travel ",word

        print "\n\n"
        features["agriculture"] = (counts["agriculture"] > 50)
        features["animals"] = (counts["animals"] > 50)
        features["animation"] = (counts["animation"] > 50)
        features["architecture"] = (counts["architecture"] > 50)
        features["astronomy"] = (counts["astronomy"] > 50)
        #features["science"] = (counts["science"] > 100)
        features["books"] = (counts["books"] > 50)
        features["chemistry"] = (counts["chemistry"] > 50)
        features["commerce"] = (counts["commerce"] > 40)
        features["crafts"] = (counts["crafts"] > 50)
        features["current"] = (counts["current"] > 50)
        features["economy"] = (counts["economy"] > 50)
        features["education"] = (counts["education"] > 50)
        features["films"] = (counts["films"] > 50)
        features["games"] = (counts["games"] > 50)
        features["government"] = (counts["government"] > 60)
        features["history"] = (counts["history"] > 50)
        features["hobbies"] = (counts["hobbies"] > 50)
        features["household"] = (counts["household"] > 50)
        features["manufacturing"] = (counts["manufacturing"] > 50)
        features["medical"] = (counts["medical"] > 50)
        features["music"] = (counts["music"] > 50)
        features["reference"] = (counts["reference"] > 40)
        features["services"] = (counts["services"] > 50)
        features["society"] = (counts["society"] > 50)
        features["sports"] = (counts["sports"] > 50)
        features["technology"] = (counts["technology"] > 50)
        features["travel"] = (counts["travel"] > 40)

        print counts

        return features

    def __init__(self):
        self.curdir = os.path.dirname(os.path.realpath(__file__))

        #print "Defining paths to category files for similarity matching"
        path = "features/"
        self.agriculture = self.file_to_dict(path+"agriculture_freq")
        self.animals = self.file_to_dict(path+"animals_freq")
        self.animation = self.file_to_dict(path+"animation_freq")
        self.architecture = self.file_to_dict(path+"architecture_freq")
        self.astronomy = self.file_to_dict(path+"astronomy_freq")
        self.books = self.file_to_dict(path+"books_freq")
        self.chemistry = self.file_to_dict(path+"chemistry_freq")
        self.commerce = self.file_to_dict(path+"commerce_freq")
        self.crafts = self.file_to_dict(path+"crafts_freq")
        self.current = self.file_to_dict(path+"current_freq")
        self.economy = self.file_to_dict(path+"economy_freq")
        self.education = self.file_to_dict(path+"education_freq")
        self.films = self.file_to_dict(path+"films_freq")
        self.games = self.file_to_dict(path+"games_freq")
        self.government = self.file_to_dict(path+"government_freq")
        self.history = self.file_to_dict(path+"history_freq")
        self.hobbies = self.file_to_dict(path+"hobbies_freq")
        self.household = self.file_to_dict(path+"household_freq")
        self.manufacturing = self.file_to_dict(path+"manufacturing_freq")
        self.medical = self.file_to_dict(path+"medical_freq")
        self.music = self.file_to_dict(path+"music_freq")
        self.reference = self.file_to_dict(path+"reference_freq")
        self.services = self.file_to_dict(path+"services_freq")
        self.society = self.file_to_dict(path+"society_freq")
        self.sports = self.file_to_dict(path+"sports_freq")
        self.technology = self.file_to_dict(path+"technology_freq")
        self.travel = self.file_to_dict(path+"travel_freq")

        print "Calling build_classifier to train classifier"
        self.classifier = self.build_classifier()
        self.test_self() #Check trained classifier


def main():
    f = CategoryClassifier()
    classifier = f.get_classifier()
    print "Training done"
    file_pointer = open("subset/test",'r')
    for url in file_pointer:
        try:
            valid_url = urllib2.urlopen(url,None,1)
            html = valid_url.read()
        except:
            continue
        soup = BeautifulSoup(html, 'html.parser')
        raw = soup.get_text().strip()
        builder = raw.encode("ascii","ignore")
        featureset = f.extract_features(builder.strip())
        predicted_label = classifier.classify(featureset)
        print url,predicted_label

if __name__ == "__main__":
    main()
