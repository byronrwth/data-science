#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import json
import pdb
#pdb.set_trace()


#twitterData = open(sys.argv[2])
twitterfile = sys.argv[1]



def twitterDict(file):
    #print 'creating twitterDict: '
    twitterData = open(file, "r")

    twitter_list_dict = []
    #lines(tweet_file)
    for line in twitterData:
        twitter_list_dict.append( json.loads(line.decode('utf-8-sig')) )

    #print "length: " , len(twitter_list_dict)
    return twitter_list_dict




def construct_dict(tweets, dict):


    #print "len of tweets= ", len(tweets)

    for index in range(len(tweets)):


        #print "score for this tweet= ", tweet_score

        if "text" in tweets[index].keys():
            for word in tweets[index]["text"].split():   
                newword = word.encode('utf-8') 
  
                if newword not in dict.keys():
                    # handle new term
                    #print "adding: ", newword, " with tweet score= ",tweet_score

                    dict[newword] = 1
                else:
                    #print "already exist, append: ", newword, " with tweet score= ",tweet_score

                    dict[newword] += 1

    return



def main():
    tweets = twitterDict(twitterfile)
    dict = {}

    # reorder tweets due to sentiment weight

    # construct an initial dict
    
    # construc a new dict to store the new terms
    # the items are lists of integers, each of the integer suggesting the score of the sentence with the word in it
    construct_dict(tweets, dict)

    #print newdict
    
    for term in dict.keys():
        #import pdb
        #pdb.set_trace()
        print term, "%.4f" %( float(dict[term])/len(dict) )

        #print newterm+" ", sum(newdict[newterm])/len(newdict[newterm])


    #print "point= ", sentiment["expands"]





if __name__ == '__main__':
    main()