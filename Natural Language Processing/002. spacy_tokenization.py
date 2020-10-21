"""
TOKENIZATION:
Tokens are the basic building blocks for some text.
Prefix: ${"(,
Suffix: .,km!,
Infix: -/,
Exception: let's U.S.
"""
from pathlib import Path

import spacy

if __name__ == '__main__':
    nlp = spacy.load('en_core_web_sm')
    text = u'"I\'m going home to U.S.!" Mail me the data at some.mail@mail.com or https://wesitePage.com/sendMail.'
    doc = nlp(text)
    # check the tokens carefully, it keeps the mail/website/U.S. intact
    print("Tokens in sentence: ")
    for token in doc:
        # all the tokens printed are joined using |
        print(token, end=' | ')
    print(f"\n\nNumber of tokens in the sentence: {len(doc)}", end='\n\n')

    # Tokens cannot be reassigned, i.e., doc[5] = 'test', will throw an error
    print(f'Getting single token: {doc[0]}')
    print(f'Getting slice of text tokens: {doc[0:5]}', end='\n\n')

    """
    Spacy can understand Named Entities, another layer of context, i.e., 
    some entites are organization / location names to relate to things like money/date
     -> doc.ents 
        contain the entities
    """

    text = u'I am Nitin Dhiman. I live in India. I am a Software Engineer at Yellow Messenger Pvt. Ltd.'
    doc = nlp(text)
    print(f'Entities in the sentence: "{text}"')
    # loop through entites using doc.ents
    for entity in doc.ents:
        # print each entity
        print(entity)

        # print each entity label
        print(f"Label: {entity.label_}")

        # Printing the description of each entity label
        print(f"Label Explaination: {str(spacy.explain(entity.label_))}", end='\n\n')

    """
    Spacy can also recognise noun chunks.
    -> doc.noun_chunks
        this contains noun and the words describing that noun
    """
    print(f'Nouns in the sentence: "{text}"')
    # parse through noun chunks using doc.noun_chunks
    for chunk in doc.noun_chunks:
        # prints each chunk of noun
        print(chunk)
