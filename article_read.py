from bs4 import BeautifulSoup
import requests
import pprint
import sources
import fox_homepage_links as fox
import cnn_homepage_links as cnn
import reddit_news_links as reddit

def get_homepage_articles(news_sites):
    for source in sources.sites:
        if(source == "infowars"):
            continue
        elif(source == "msnbc"):
            continue
        elif(source == "cnn"):
            # cnn.scrape_links(source)
            break
        elif(source == "reddit"):
            reddit.scrape_links(source)
        elif(source == "foxnews"):
            # fox.scrape_links(source)
            break

get_homepage_articles(sources)






