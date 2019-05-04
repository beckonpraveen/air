import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
stopwords = list(STOP_WORDS)
document1 ="""
An argument over bursting of crackers led to an altercation between two groups in Thane, the police said on Tuesday.At least 15 people have been booked in connection with the incident, a police spokesperson said. According to one of the complainants, a Dalit woman who is a former corporator, her minor son was bursting crackers in Kalyan to celebrate the Indian Air Force’s air strike on February 26 when he asked a man, who was passing by, to be careful.
This led to an argument between the two after which the man allegedly slapped the boy and ran away, the official said. Later, when the woman confronted the man, he along with some of his associates allegedly thrashed the mother-son duo on Sunday and threatened them with dire consequences, the spokesperson said.The woman approached the police who booked the man and his seven aides under various sections of the Indian Penal Code (IPC), including rioting, harassment and criminal intimidation, and the Scheduled Castes and Scheduled Tribes (Prevention of Atrocities) Act, the official said.The man in turn lodged a cross-complaint against the woman and her son. Based on his complaint, the police registered offences against the woman, her son and five others under various IPC sections, the official said. No arrest has been made as of now , but investigations are under way, police officials said.
"""
nlp = spacy.load('en_core_web_sm')
docx = nlp(document1)
mytokens = [token.text for token in docx]
word_frequencies = {}
for word in docx:
    if word.text not in stopwords:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1

# print(word_frequencies)
maximum_frequency = max(word_frequencies.values())
for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word]/maximum_frequency)
# word_frequencies
sentence_list = [ sentence for sentence in docx.sents ]
sentence_scores = {}
for sent in sentence_list:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if len(sent.text.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent] += word_frequencies[word.text.lower()]
# print(sentence_scores)
from heapq import nlargest
summarized_sentences = nlargest(3, sentence_scores, key=sentence_scores.get)
# summarized_sentences
# for w in summarized_sentences:
#     print(w.text)
final_sentences = [ w.text for w in summarized_sentences ]
summary = ' '.join(final_sentences)
print(summary)
