from afinn import Afinn
import math
import re

af = Afinn()
from newsplease import NewsPlease
article = NewsPlease.from_url('https://www.indiatoday.in/elections/lok-sabha-2019/story/sabarimala-outfit-holds-namajapa-protest-in-kerala-1501155-2019-04-13')

finn = dict(map(lambda(w, s): (w, int(s)), [ 
            ws.strip().split('\t') for ws in open(article) ]))

# Word splitter pattern
pattern_split = re.compile(r"\W+")