#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import json
import pdb
#pdb.set_trace()

sentimentData = open(sys.argv[1])
#twitterData = open(sys.argv[2])
twitterfile = sys.argv[2]



def twitterDict(file):
    #print 'creating twitterDict: '
    twitterData = open(file, "r")

    twitter_list_dict = []
    #lines(tweet_file)
    for line in twitterData:
        twitter_list_dict.append( json.loads(line.decode('utf-8-sig')) )

    #print "length: " , len(twitter_list_dict)
    return twitter_list_dict


def sentimentDict( data ):
    #print 'creating sentimentDict: '

    #lines(sentimentData)
    scores = {} # initialize an empty dictionary

    for line in data:
      #term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      #term, score  = line.split("\\s")
      #scores[term] = int(score)  # Convert the score to an integer.
      #print "type of line: ", type(line)  # str
        l = line.split()
        #print "type of l: ", type(l)   # list
        #print "l= ", l
        #print "len(l)= ", len(l)

        if len(l) == 2:
            term, score = l[0], l[1]
            #print "len 2: term = ", term, "score = ", score
        else:
            """
            term = u''
            for i in range(len(l[:-1])):
                term.join(l[i]).encode('utf-8').strip()

            print term
            """

            term, score = l[:-1], l[-1]
            #score = l[-1]
            #print "len 3: term = ", term, "score = ", score


        scores[str(term)] = float(score)  # dict[list]

        #print "scores of term : ", term, scores["term"]

    #print "sentiment: "
    #print scores.keys(), scores.values(), 
    return scores

def newSentiDict( data):
    newdict = {}

    return newdict


def lines(fp):
    print str(len(fp.readlines()))


def tweetscore(dict, tweet):
    #print dict.keys()
    #print dict.values()

    score = 0.0
    current_score = 0.0
    if "text" in tweet.keys():
        for word in tweet["text"].split():   
            newword = word.encode('utf-8') 

            if newword in dict.keys():
                #print "newword= ", newword
                
                #print " type of dict[word]= ", type(dict[newword])
                #print dict[newword]
                
                current_score = float(dict[newword])
                score += current_score  # total score for input tweet 
                
    #if score > 0.0:
        #print "score= ", score

    return score


def construct_new_dict(tweets, dict):
    newdict = {}

    #print "len of tweets= ", len(tweets)

    for index in range(len(tweets)):
        tweet_score = 0.0
        tweet_score = tweetscore(dict, tweets[index])

        #print "score for this tweet= ", tweet_score

        if "text" in tweets[index].keys():
            for word in tweets[index]["text"].split():   
                newword = word.encode('utf-8') 
  
                # now, for all new words which not in sentiment dict, thus 0 score
                if newword not in dict.keys():
                    #handle new term
                    if newword not in newdict:
                    #print "adding: ", newword, " with tweet score= ",tweet_score

                        newdict[newword] = [ tweet_score ]
                    else:  # multiple exists for this new word
                    #print "already exist, append: ", newword, " with tweet score= ",tweet_score, "word has score= ", dict[newword]

                        newdict[newword].append(tweet_score)

    return newdict

def main():
    tweets = twitterDict(twitterfile)
    sentiment = sentimentDict(sentimentData) # old dict

    # reorder tweets due to sentiment weight

    # construct an initial dict
    
    # construc a new dict to store the new terms
    # the items are lists of integers, each of the integer suggesting the score of the sentence with the word in it

    """
    We will run your script on a file that contains strongly positive and strongly negative tweets and verify that the non-sentiment-carrying terms in the strongly positive tweets are assigned a higher score than the non-sentiment-carrying terms in negative tweets.
    """
    newdict = construct_new_dict(tweets, sentiment)

    #print newdict

    for newterm in newdict.keys():
        #import pdb
        #pdb.set_trace()
        
        #print newterm, newdict[newterm] 

        print newterm+" ", sum(newdict[newterm])/len(newdict[newterm])


    #print "point= ", sentiment["expands"]





if __name__ == '__main__':
    main()