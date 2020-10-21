"""
LEMMATIZATION
It is not a reduction process, it does more than that.
It applies a morphological (relating to the form or structure of things.) analysis to words.
Ex: lemma of 'was' is 'be' and lemma of 'mice' is 'mouse'
More informative, looks at surrounding texts as well.
"""
import spacy


def show_lemmas(doc):
    # formatting the response
    for token in doc:
        print(f'{token.text:{12}} {token.pos_:{6}} {token.lemma:<{22}} {token.lemma_}')


if __name__ == '__main__':
    nlp = spacy.load('en_core_web_sm')
    text = u'I have been running in a race since I am a runner and I love to run. I ran a lot yesterday.'
    doc = nlp(text)
    show_lemmas(doc)
