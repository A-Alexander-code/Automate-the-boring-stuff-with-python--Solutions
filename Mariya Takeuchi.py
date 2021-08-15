#! python
# searchpypi.py - Opens several search results

import requests, sys, webbrowser, bs4
print("/|\m(owO)m/|\ - Searching...")     # display text while downloading the search result page
res = requests.get('https://google.com.ec/search?q=' 'https://pypi.org/search/?q='+' '.join(sys.argv[1:0]))
res.raise_for_status()

# TODO: Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text,'html.parser')
# TODO: Open a browser tab for each results
linkElems = soup.select('.package-snippet')
numOpen = min(5,len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://pypi.org'+linkElems[i].get('href')
    print('Opening',urlToOpen)
    webbrowser.open(urlToOpen)