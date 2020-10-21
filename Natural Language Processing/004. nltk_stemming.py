"""
STEMMING
Crude method of cataloging words. Can't be used everywhere, many exceptions.
Spacy does not include a stemmer, instead rely on lemmatization.
Stemming can be used for analysis.
"""
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer

if __name__ == '__main__':
    p_stemmer = PorterStemmer()
    # runner is a noun
    words = ['run', 'runner', 'ran', 'runs', 'running', 'easily', 'fairly', 'fairness']
    print('PORTER STEMMER:')
    for word in words:
        print(word + ' -> ' + p_stemmer.stem(word))

    print()
    print('SNOWBALL STEMMER:')
    s_stemmer = SnowballStemmer(language='english')
    for word in words:
        print(word + ' -> ' + s_stemmer.stem(word))

    words = ['generous', 'generation', 'generously', 'generate']
    for word in words:
        print(word + ' -> ' + s_stemmer.stem(word))

