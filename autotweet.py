# https://developer.nytimes.com/

import tweepy
import logging
from config import create_api
import time
import requests
import time
from datetime import datetime
import json


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

dateNow = datetime.now()

curMonthDay = dateNow.strftime("%m%d")

tweetcount = 0

urls = []

def get_article(curMonthDay):
    logger.info("Retrieving articles")

    logger.info("Current Month day " + curMonthDay)

    fullDate = "2010" + curMonthDay

    requestUrl = "https://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date=" + fullDate + "&end_date=" +fullDate+ "&facet=false&facet_filter=false&q=technology&sort=relevance&api-key=[YOUR API KEY]"
    requestHeaders = {"Accept": "application/json"}

    request = requests.get(requestUrl, headers=requestHeaders)

    try:
        decoded = json.loads(request.text)
    
        response = decoded['response']

        for x in response['docs']:
            print (x["web_url"])
            urls.append(x["web_url"])

    
    except (ValueError, KeyError, TypeError) as e:
        print (e)
        logger.info(e)


def new_tweet(api,urls):
    global tweetcount

    logger.info("generating new tweet")
    tweet = urls[tweetcount]

    print(tweet)
    print(tweetcount)
    tweetcount = tweetcount + 1
    
    api.update_status(tweet)
    logger.info("Tweeted")

    return tweetcount


def main():

    while True:
        get_article(curMonthDay)
        api = create_api()
        new_tweet(api, urls)
        logger.info("Waiting...")
        time.sleep(7200)

    


if __name__ == "__main__":
    main()