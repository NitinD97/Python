"""
Doc object format is a dictionary
Link to the docs:
https://spacy.io/api/doc

Doc = {
    ents: {...},
    sents: {...},
    text: {...},
    tokens: {...}
}
"""

import spacy
from spacy.attrs import POS

import json
from spacy.tokens import Doc
from spacy.vocab import Vocab

if __name__ == '__main__':
    nlp = spacy.load('en_core_web_sm')
    text = u'Today is a bright day. Listening to songs is bliss.'
    doc = nlp(text)
    doc_json = doc.to_json()
    doc_json = json.dumps(doc_json, indent=4)
    print(doc_json, end='\n\n')

    np_array = doc.to_array([POS])
    print(np_array)
    np_array = doc.from_array([POS], np_array)
    print(np_array, end='\n\n')

    # writes the state to disk
    doc.to_disk('./doc')

    # reads the state from disk
    doc = Doc(Vocab()).from_disk('./doc')
    print(doc.to_json())

