#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import oauth2 as oauth
import urllib2 as urllib
import json

# See Assginment 6 instructions or README for how to get these credentials
access_token_key = "3373982026-NkvNfCHNZ86rhPDxSCxo8NczTSyZ1kYu58LidBW"
access_token_secret = "MolbdawuVXzhLo1vjgfVl1EJ1Yn4PmdqbotWbnp35vYOk"

consumer_key = "KyZCfxN575O0ZMRBCNHs3bGp7"   #api key
consumer_secret = "6B5NwX1Abhc1wleoqdzCsElfHiZeLFbl4fovuRBgQvUuuVq98c"   #api secret

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url,
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def fetchsamples():
  url = "https://stream.twitter.com/1/statuses/sample.json"
  #can change the url to the newer REST API v. 1.1 instead
  parameters = []
  response = twitterreq(url, "GET", parameters)
  for line in response:
    print line.strip()

"""
  #search_response = urllib.urlopen("http://twitter.com/search.json?q=microsoft")
  #test_response = urllib.urlopen("https://api.twitter.com/1.1/search/tweets.json?q=microsoft")

  #print search_response
  parameters = []
  search_response = twitterreq("http://twitter.com/search.json?q=microsoft", "POST", parameters)
  #print search_response
  for line in search_response:
    print line.strip()

  #test_pyresonse = json.load(search_response)

  #print test_pyresonse
"""

if __name__ == '__main__':

  fetchsamples()