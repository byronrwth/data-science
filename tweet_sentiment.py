#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import json

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
            #term = u' '.join
            term, score = l[:-1], l[-1]
            #print "len 3: term = ", term, "score = ", score

        #print "type of term : ", type(term)  #list
        scores[str(term)] = int(score)  # dict[list]
        #print "scores of term : ", term, scores["term"]

    #print scores.keys()
    return scores


def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweets = twitterDict(twitterfile)
    sentiment = sentimentDict(sentimentData)

    # reorder tweets due to sentiment weight
    '''Create a method below that loops through each tweet in your twees_list.  For each individual tweet it should add up you sentiment
        score, based on the sent_dict.
    '''

    #print "point= ", sentiment["expands"]


    for index in range(len(tweets)):
        score = 0
        if "text" in tweets[index].keys():
            tweet_wordlist = tweets[index]["text"].split()

        #print tweet_wordlist

            for word in tweet_wordlist:
            #print "type of word: ", type(word)   #unicode
            #print word
                newword = word.encode('utf-8')
            #print newword
            #print "type of newword: ", type(newword)   #unicode


                if newword in sentiment.keys():
                    #print newword
                    #print "point= ", sentiment[newword]
                    score += sentiment[newword]


        print score


if __name__ == '__main__':
    main()