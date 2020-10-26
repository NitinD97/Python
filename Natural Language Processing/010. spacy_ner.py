"""
NAMED ENTITY RECOGNITION (NER)
This means to get the names of the organisation, person, location, currency, quantity, time expressions etc.
We can add our own custom entities using spacy.
"""

import spacy


def show_entities(doc):
    print('>>> TEXT: ', doc.text)

    if doc.ents:
        for ent in doc.ents:
            print(f'{ent.text:{30}} | {ent.label_:{10}} | {spacy.explain(ent.label_):{20}}')
    else:
        print('No entites found!')
    print()


if __name__ == '__main__':
    nlp = spacy.load('en_core_web_sm')

    text = u'Hi, how are you?'
    doc = nlp(text)
    show_entities(doc)

    text = u'May I go to Washington, DC next May to see the Washington Monument?'
    doc = nlp(text)
    show_entities(doc)

    text = u'Can I please have 500 dollars of Microsoft stock?'
    doc = nlp(text)
    show_entities(doc)

    text = u'Can I please have 500 dollars of Microsoft stock?'
    doc = nlp(text)
    show_entities(doc)

    text = u'Money View to build a U.K. factory for $6 million'
    doc = nlp(text)
    show_entities(doc)

    print('Here spacy was unable to tell that Tesla was a NOUN/ORG.')

    # Adding a custom entity in the vocab
    from spacy.tokens import Span

    ORG = nlp.vocab.strings[u'ORG']
    print(ORG, end='\n\n')

    new_entity = Span(doc, 0, 2, label=ORG)
    doc.ents = list(doc.ents) + [new_entity]
    show_entities(doc)

    # adding multiple entities in the vocab
    # BEFORE ADDING MULTIPLE CUSTOM ENTITIES
    print('BEFORE ADDING MULTIPLE CUSTOM ENTITIES:')
    text = u'Our company created a brand new vacuum cleaner. This new vacuum-cleaner is the best in show. Apple ' \
           u'launched a new iphone'
    doc = nlp(text)
    show_entities(doc)

    # AFTER ADDING MULTIPLE ENTITES
    print('AFTER ADDING MULTIPLE CUSTOM ENTITIES:')
    from spacy.matcher import PhraseMatcher

    matcher = PhraseMatcher(nlp.vocab)
    phrase_list = ['vacuum cleaner', 'vacuum-cleaner', 'iphone']
    phrase_patterns = [nlp(text) for text in phrase_list]
    matcher.add('newProducts', None, *phrase_patterns)
    found_matches = matcher(doc)

    # finding the PRODUCT
    PRODUCT = nlp.vocab.strings[u'PRODUCT']

    # creating a list of entity Span using all the matches found in the doc
    new_entities = [Span(doc, match[1], match[2], label=PRODUCT) for match in found_matches]
    doc.ents = list(doc.ents) + new_entities
    show_entities(doc)

    print('CHECKING HOW MANY TIMES MONEY ENTITY WAS USED IN A SENTENCE: ')
    text = u'Originally I paid $29.95 for this car, but now it is marked down by 10 dollars, bringing its value to ' \
           u'19.95 dollars.'
    doc = nlp(text)
    print('>>> TEXT:', doc.text)
    print(len([ent for ent in doc.ents if ent.label_ == 'MONEY']) ,end='\n\n')

    # spacy can also visualize entities
    from spacy import displacy
    from pathlib import Path

    text = u'Apple sold nearly 5k iPhones worth $6 million in last 6 months. Sony on the other hand sold' \
           u' a million TV sets and headphones. These both tech giants are in a competition.'
    doc = nlp(text)
    sent_list = []
    for sent in doc.sents:
        new_doc = nlp(sent.text)
        print(f'{str(new_doc.ents):{60}} | {new_doc.text}')
        if new_doc.ents:
            sent_list.append(new_doc)
    html = displacy.render(sent_list, style="ent", options={'distance': 110}, page=True, minify=True)
    output_path = Path("./generatedFiles/010. ner_visualization.html")
    output_path.open("w", encoding="utf-8").write(html)


