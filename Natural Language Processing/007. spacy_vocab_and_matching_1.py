"""
VOCABULARY AND MATCHING
(Rule based Matching)
It can be used as a powerful version of regexes.
Spacy offers a rule matching tool called matcher. Allows you to build a library of token patterns,
then match those patterns against a doc object to return a list of found matches.
https://spacy.io/usage/rule-based-matching
"""
import spacy
from spacy.matcher import Matcher


def show_found_matched(doc, found_matches):
    for match_id, start_idx, end_idx in found_matches:
        string_val = nlp.vocab.strings[match_id]
        print(string_val, start_idx, end_idx, match_id, doc[start_idx:end_idx])
    print()


if __name__ == '__main__':
    nlp = spacy.load('en_core_web_sm')
    matcher = Matcher(nlp.vocab)

    # pattern values can be found on the link provided in description.
    pattern1 = [{'LOWER': 'solarpower'}]  # SolarPower
    pattern2 = [{'LOWER': 'solar'}, {'IS_PUNCT': True}, {'LOWER': 'power'}]  # Solar-Power
    pattern3 = [{'LOWER': 'solar'}, {'LOWER': 'power'}]  # Solar Power

    # Name of the matcher is 'SolarPower', None is callback, then patterns
    matcher.add('SolarPower', None, pattern1, pattern2, pattern3)

    text = u'I use solar power at home. solarpower is free. solar-power can be obtained in the day'
    doc = nlp(text)
    found_matches = matcher(doc)
    show_found_matched(doc, found_matches)

    # if we want to remove from matcher, send the name of the matcher in remove function
    matcher.remove('SolarPower')

    pattern1 = [{'LOWER': 'solarpower'}]  # SolarPower
    # OP values can be found on the link provided in description.
    pattern2 = [{'LOWER': 'solar'}, {'IS_PUNCT': True, 'OP': '*'}, {'LOWER': 'power'}]  # Solar-Power, Solar--Power, Solar Power
    matcher.add('SolarPower', None, pattern1, pattern2)

    text = u'I use Solar power at home. solarpower is free. solar-power can be obtained in the day. i need solar--power'
    doc = nlp(text)
    found_matches = matcher(doc)
    show_found_matched(doc, found_matches)
