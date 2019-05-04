from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords

import requests

# getting text document from Internet
# text = requests.get('http://rare-technologies.com/the_matrix_synopsis.txt').text


# getting text document from file
# fname="C:\\Users\\TextRank-master\\wikipedia_deep_learning.txt"
# with open(fname, 'r') as myfile:
#       text=myfile.read()


#getting text document from web, below function based from 3
from bs4 import BeautifulSoup
from urllib.request import urlopen

# def get_only_text(url):
#  """
#   return the title and the text of the article
#   at the specified url
#  """
#  page = urlopen(url)
#  soup = BeautifulSoup(page, "lxml")
#  text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
#  return soup.title.text, text
#
# url="https://en.wikipedia.org/wiki/Deep_learning"
# text = get_only_text(url)

# print ('Summary:')
# print (summarize(text, ratio=0.01))
#
# print ('\nKeywords:')
# print (keywords(text, ratio=0.01))

#
#

text = """
An argument over bursting of crackers led to an altercation between two groups in Thane, the police said on Tuesday.At least 15 people have been booked in connection with the incident, a police spokesperson said. According to one of the complainants, a Dalit woman who is a former corporator, her minor son was bursting crackers in Kalyan to celebrate the Indian Air Force’s air strike on February 26 when he asked a man, who was passing by, to be careful.
This led to an argument between the two after which the man allegedly slapped the boy and ran away, the official said. Later, when the woman confronted the man, he along with some of his associates allegedly thrashed the mother-son duo on Sunday and threatened them with dire consequences, the spokesperson said.The woman approached the police who booked the man and his seven aides under various sections of the Indian Penal Code (IPC), including rioting, harassment and criminal intimidation, and the Scheduled Castes and Scheduled Tribes (Prevention of Atrocities) Act, the official said.The man in turn lodged a cross-complaint against the woman and her son. Based on his complaint, the police registered offences against the woman, her son and five others under various IPC sections, the official said. No arrest has been made as of now , but investigations are under way, police officials said.
"""
print ('Summary:')
print (summarize(text, ratio=0.2))

print ('\nKeywords:')

# higher ratio => more keywords
print (keywords(str(text), ratio=0.2))
