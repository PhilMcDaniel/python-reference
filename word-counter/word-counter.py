import requests as re
from bs4 import BeautifulSoup
import pandas as pd

#get text from url
url = 'https://www.congress.gov/bill/114th-congress/house-bill/1493/text?overview=closed'
full_html = re.get(url)
soup = BeautifulSoup(full_html.text, 'html.parser')
text = soup.find(id='billTextContainer')

#get text by reading file

#add words to dict to keep track of count
words = {}
for string in soup.stripped_strings:
    word_list = string.split(' ')
    for word in word_list:
        #ignore certain words/strings
        if word in ['',' ','\n']:
            pass
        else:
            #update dict with count
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

#load to df to explore results
df = pd.DataFrame.from_dict(words,orient='index',columns=['count']).reset_index()
df.sort_values(by='count',ascending=False).head(50)