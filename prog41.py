#!/usr/bin/env python
from multiprocessing.pool import ThreadPool
from time import time as timer
import urllib.request

urls = ["https://yahoo.com", "http://google.com","http://ibm.com", "http://apple.com"]

def fetch_url(url):
    try:
        response = urllib.request.urlopen(url)
        return url, response.read(), None
    except Exception as e:
        return url, None, e

start = timer()
for url in urls:
    url,response,NONE=fetch_url(url)
    print(response)
'''results = ThreadPool(20).imap_unordered(fetch_url, urls)
for url, html, error in results:
    if error is None:
        print("%r fetched in %ss" % (url, timer() - start))
    else:
        print("error fetching %r: %s" % (url, error))'''
print("Elapsed Time: %s" % (timer() - start,))
