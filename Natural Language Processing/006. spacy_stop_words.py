"""
STOP WORDS
these are the words like 'is' , 'the' that does not have any meaning. But words like these can hurt your NLP model.
We mostly remove stop words.
"""

import spacy

if __name__ == '__main__':
    nlp = spacy.load('en_core_web_sm')
    # Set of stop words
    print('No of stop words?', len(nlp.Defaults.stop_words))
    print(nlp.Defaults.stop_words, end='\n\n')

    # check if a word is a stop word
    print('"is" Stop word?', nlp.vocab['is'].is_stop)
    print('"mystery" Stop word?', nlp.vocab['mystery'].is_stop, end='\n\n')

    # add a stop word to the list
    print('"btw" Stop word before adding to the list?', nlp.vocab['btw'].is_stop)
    nlp.Defaults.stop_words.add('btw')
    nlp.vocab['btw'].is_stop = True
    print('"btw" Stop word after adding to the list?', nlp.vocab['btw'].is_stop)
    print('No of stop words?', len(nlp.Defaults.stop_words), end='\n\n')

    # remove a stop word?
    print('"really" Stop word before removing from the list?', nlp.vocab['really'].is_stop)
    nlp.Defaults.stop_words.remove('really')
    nlp.vocab['really'].is_stop = False
    print('"really" Stop word after removing from the list?', nlp.vocab['really'].is_stop)
    print('No of stop words?', len(nlp.Defaults.stop_words))



