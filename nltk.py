# chap 1
import nltk
# nltk.download()

# tokenize -- word tokenizer, sentence tokenizer
# corpora: plural of corpus, body of text
# lexicon: words and meanings, different according to context
# 

from ntlk.tokenize import sent_tokenize, word_tokenize

EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."

print(sent_tokenize(EXAMPLE_TEXT))

print(word_tokenize(EXAMPLE_TEXT))


######## chap 2: stop words
# NLTK is really pre-processing data, NOT generate any insights for u
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence = "This is an exmaple showing off stop word filtration"
stop_words = set(stopwords.words("english"))

print(stop_words)