import urllib.request
from bs4 import BeautifulSoup
import re

# BASE URLs
whoSampledBaseUrl = "http://www.whosampled.com"

# QUERYING WHOSAMPLED FROM USER INPUT
whoSampledQuery = input(">>")
whoSampledQueryRefined = whoSampledQuery.replace(" ", "+")
whoSampledURL = urllib.request.urlopen("http://www.whosampled.com/search/?q="+whoSampledQueryRefined).read()
whoSampledSoup = BeautifulSoup(whoSampledURL, "html.parser")
whoSampledQueryResult = whoSampledSoup.findAll('a', {'class' : 'trackTitle'})[0]['href']

# OPENING URL OF QUERIED RESULT FROM USER INPUT
whoSampledSongPage = urllib.request.urlopen(whoSampledBaseUrl+whoSampledQueryResult).read()
whoSampledSoup2 = BeautifulSoup(whoSampledSongPage, "html.parser")

# FIND OUT HOW MANY SONGS THE QUERIED SONG HAS SAMPLED FROM
howManySamples = whoSampledSoup2.find('span', {'class' : 'section-header-title'})
howManySamplesString = howManySamples.contents[0]
howManySamplesInt = int(re.sub("\D", "", howManySamplesString))

# RETURNS LIST OF HTML OBJECTS FOR THE AMOUNT OF SAMPLED SONGS THERE ARE
sampledSongsListSouped = whoSampledSoup2.findAll('a', {'class' : 'trackName playIcon'})[0:howManySamplesInt]

# MAKE LIST OF ONLY TITLE ATTRIBUTE FROM SOUPED RESULT
sampledSongsListTitles = []
for result in sampledSongsListSouped:
    sampledSongsListTitles.append(result["title"])
