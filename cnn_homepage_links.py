from bs4 import BeautifulSoup
import requests
import sources

def scrape_links(source):
    response = requests.get(sources.sites[source])
    html = response.text
    soup = BeautifulSoup(html)
    print(soup)
    news_body = soup.find("div", {"class":"zn_containers"})
    print(news_body)
    # news_article_links = news_body.find_all("a")
    # i = 0
    
    # print("\n\n[ ] %s"%source)
    # while(i < 50):
    #     print(news_article_links[i]["href"])
    #     i+=1

