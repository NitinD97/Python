"""
VOCABULARY AND MATCHING
(Phrase matching)
"""
import spacy
from spacy.matcher import PhraseMatcher


def show_found_matched(doc, found_matches):
    for match_id, start_idx, end_idx in found_matches:
        string_val = nlp.vocab.strings[match_id]
        print(string_val, start_idx, end_idx, match_id, doc[start_idx:end_idx])
    print()


if __name__ == '__main__':
    nlp = spacy.load('en_core_web_sm')

    matcher = PhraseMatcher(nlp.vocab)
    with open('./txtFiles/008_reaganomics.txt', encoding='utf-8') as f:
        doc = nlp(f.read())

    phrase_list = ['voodoo economics', 'supply-side economics', 'trickle-down economics', 'free-market economics']
    phrase_patterns = [nlp(text) for text in phrase_list]

    matcher.add('econ_matcher', None, *phrase_patterns)
    found_matches = matcher(doc)
    show_found_matched(doc, found_matches)

