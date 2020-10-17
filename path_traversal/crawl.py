import requests
import re
import sys

if (len(sys.argv) != 2):
    print("usage: py crawl.py [url to crawl]")
    exit()

globalEntrypoint = sys.argv[1]
f = open("results.txt", "w")

#cache = 
#def cache(url):


def crawl(entrypoint):
    response = requests.get(entrypoint)
    regex = "<a href=\"(?!\.\.)(.*)\">"
    matches = re.findall(regex, response.text)

    for match in matches:
        if match == 'README':
            matchResponse = requests.get(entrypoint + match)
            f.write(matchResponse.text + ' ' + entrypoint+match + '\n')
            #print(requests.get(entrypoint+match).text)
        else:
           # print('crawling...  ', entrypoint+match)
            crawl(entrypoint+match)

crawl(globalEntrypoint)
f.close()
