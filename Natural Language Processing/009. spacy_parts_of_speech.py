"""
PARTS OF SPEECH
Its common for rare words to mean exactly same in a sentence.
Its also common, when the order of words are reversed, the meaning of the sentence change entirely.
So we need to take into account the part of speech around the word, not just the word itself.
It is better to add linguistic knowledge to add useful info, instead of using raw words to solve problems.
i.e. is to know a NOUN, VERB, ADJECTIVE.
"""

import spacy

if __name__ == '__main__':
    nlp = spacy.load('en_core_web_lg')
    text = u"The quick brown fox jumped over a lazy dog's back."
    doc = nlp(text)

    print(f'| {"Token":{10}} | {"POS_":{10}} | {"Definition of POS_":{25}} | {"TAG_":{10}} | {"Definition of TAG_":{50}} |')
    print('-' * 121)
    for token in doc:
        print(f'| {token.text:{10}} | {token.pos_:{10}} | {spacy.explain(token.pos_):{25}} | {token.tag_:{10}} | {spacy.explain(token.tag_):{50}} |')
    print()

    # en_core_web_lg can pick up the differences in the sentences
    print('Difference bw context, and spacy\'s capability')
    text = u'I read books on NLP.'
    doc = nlp(text)
    token = doc[1]
    print(
        f'| {token.text:{10}} | {token.pos_:{10}} | {spacy.explain(token.pos_):{25}} | {token.tag_:{10}} | {spacy.explain(token.tag_):{50}} |')

    text = u'I read a book on NLP.'
    doc = nlp(text)
    token = doc[1]
    print(
        f'| {token.text:{10}} | {token.pos_:{10}} | {spacy.explain(token.pos_):{25}} | {token.tag_:{10}} | {spacy.explain(token.tag_):{50}} |')
    print()

    # count POS frequency
    text = u"The quick brown fox jumped over a lazy dog's back."
    doc = nlp(text)
    pos_count = doc.count_by(spacy.attrs.POS)
    print(f'Parts of Speech count: {pos_count}')
    for pos in sorted(pos_count.keys()):
        print(f'| {pos} | {doc.vocab[pos].text:{7}} | {pos_count[pos]}')
    print()

    # similarly we can count tags frequency
    tag_count = doc.count_by(spacy.attrs.TAG)
    print(f'Tags count: {tag_count}')
    for tag in sorted(tag_count.keys()):
        print(f'| {tag:<{20}} | {doc.vocab[tag].text:{10}} | {tag_count[tag]}')
    print()

    # we can also count syntactical dependency(def) frequency
    dep_count = doc.count_by(spacy.attrs.DEP)
    print(f'Syntactical depencency count: {dep_count}')
    for dep in sorted(dep_count.keys()):
        print(f'| {dep:<{20}} | {doc.vocab[dep].text:{10}} | {dep_count[dep]}')
    print()





