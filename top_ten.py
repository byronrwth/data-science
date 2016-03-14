#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import json
import operator

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
    #print twitter_list_dict
    return twitter_list_dict



def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweets = twitterDict(twitterfile)


    '''
    Your script should print output to stdout. Each line of output should contain a hashtag, followed by a space, followed by the frequency of that hashtag in the entire file. There should be one line per unique hashtag in the entire file. Each line should be in the format <hashtag:string> <frequency:float>
    '''

    hashtags = {}  # state, sentiment score


    for index in range(len(tweets)):
        if "entities" in tweets[index].keys():
            #print tweets[index]["entities"]

            if tweets[index]["entities"]["hashtags"] is not None : # != []
                #print tweets[index]["entities"]["hashtags"]
                for hashtag in tweets[index]["entities"]["hashtags"]:
                    if hashtag["text"] not in hashtags.keys():
                        hashtags[hashtag["text"]] = 1
                    else:
                        hashtags[hashtag["text"]] += 1

                    #print hashtag["text"], hashtags[hashtag["text"]]

    " return top 10 hashtags: hashtag frequency:float "
    #for item in hashtags.keys():
    #    print item, hashtags[item]


    # sort on values, not keys
    topten = sorted(hashtags.items(), key=operator.itemgetter(1), reverse=True)
    #print topten

    for i in range(10):
        #print topten[i], type(topten[i])  # tuple !!
        #print list(topten[i]), type(list(topten[i]))
        tag, count = list(topten[i])
        print tag, count

if __name__ == '__main__':
    main()