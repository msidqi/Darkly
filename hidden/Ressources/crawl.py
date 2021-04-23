import requests
import re
import sys

if (len(sys.argv) != 2):
    print("usage: python3 crawl.py [url to crawl]")
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
            flag = re.match("[a-z\d]+", matchResponse.text)
            if flag:
                print("Flag: " + flag.group())
                f.write("Flag: " + flag.group())
        else:
            crawl(entrypoint+match)

print('crawling...  ' + globalEntrypoint)
crawl(globalEntrypoint)
f.close()
