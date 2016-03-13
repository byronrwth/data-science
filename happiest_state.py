#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import json

sentimentData = open(sys.argv[1])
#twitterData = open(sys.argv[2])
twitterfile = sys.argv[2]

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

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

        
        scores[str(term)] = int(score)  # dict[list]
        
        #print "scores of term : ", term, scores["term"]

    #print scores.keys()
    return scores


def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweets = twitterDict(twitterfile)
    sentiment = sentimentDict(sentimentData)

    # 3 ways for location detection :
    '''
    Use the coordinates field (a part of the place object, if it exists), to geocode the tweet. This method gives the most reliable location information, but unfortunately this field is not always available and you must figure out some way of translating the coordinates into a state.


    Use the other metadata in the place field. Much of this information is hand-entered by the twitter user and may not always be present or reliable, and may not typically contain a state name.


    Use the user field to determine the twitter user's home city and state. This location does not necessarily correspond to the location where the tweet was posted, but it's reasonable to use it as a proxy.

    '''

    happiness = {}  # state, sentiment score
    maxscore = 0
    happinest_state = None

    for index in range(len(tweets)):
        for k in ("text","place","user","coordinates") :
            if k in tweets[index].keys():
                
                #if "user" == k and tweets[index]["user"] is not None and tweets[index]["user"]["location"] is not None:
                #    print "location: ", tweets[index]["user"]["location"]

                if "place" == k and tweets[index]["place"] is not None :
                    if ( (tweets[index]["place"]["country_code"] == "US") or ( tweets[index]["place"]["country"]== "United States") ): # is not None:
                        #print "place: country_code: ", tweets[index]["place"]["country_code"]

                        #print "place: country: ", tweets[index]["place"]["country"]
                        
                        #print "location: ", tweets[index]["user"]["location"]
                        if tweets[index]["user"] is not None and tweets[index]["user"]["location"] is not None:
                            location = tweets[index]["user"]["location"].split()

                            if len(location) == 2:
                                if location[1] in states.keys():
                                    this_state = location[1] 

                                    if this_state not in happiness.keys():
                                        happiness[this_state] = [0.0, 0]

                                    #print "location: ", tweets[index]["user"]["location"], location[1], happiness["this_state"]


                #if "coordinates" == k and tweets[index]["coordinates"] is not None and tweets[index]["coordinates"]["coordinates"] is not None:
                #    print "coordinates: ", tweets[index]["coordinates"]["coordinates"]  # e.g. coordinates:  [-87.9535534, 41.8397865]

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

                                    #print score
                                    happiness[this_state][0] += score
                                    happiness[this_state][1] += 1
                                    #print this_state, happiness[this_state]


    " return highest average tweet sentiment "
    average = 0.0

    for item in happiness.keys():
        #print item, happiness[item]
        if happiness[item][1] > 0 and happiness[item][0] > 0:
            #print happiness[item]
            average = float( happiness[item][0]) / int( happiness[item][1] )
            #print average
            if average > maxscore:
                maxscore, happinest_state = average, item


    print happinest_state


if __name__ == '__main__':
    main()