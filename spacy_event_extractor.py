import spacy
from spacy import displacy
from collections import Counter
from pprint import pprint
import en_core_web_sm
nlp = en_core_web_sm.load()
# doc = nlp('European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices')
# pprint([(X.text, X.label_) for X in doc.ents])

from bs4 import BeautifulSoup
import requests
import re
def url_to_string(url):
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'html5lib')
    for script in soup(["script", "style", 'aside']):
        script.extract()
    return " ".join(re.split(r'[\n\t]+', soup.get_text()))
ny_bb = url_to_string('https://www.nytimes.com/2018/08/13/us/politics/peter-strzok-fired-fbi.html?hp&action=click&pgtype=Homepage&clickSource=story-heading&module=first-column-region&region=top-news&WT.nav=top-news')
article = nlp(ny_bb)
# print(len(article.ents))
# pprint([(X.text, X.label_) for X in article.ents])
labels = [x.label_ for x in article.ents]
print(Counter(labels))
items = [x.text for x in article.ents]
print(Counter(items).most_common(3))
sentences = [x for x in article.sents]
print(sentences[20])
displacy.render(nlp(str(sentences[20])), jupyter=True, style='ent')
# pprint([(X, X.ent_iob_, X.ent_type_) for X in doc])
