"""
We can visualize tokenization.
displacy is built in visualizer
"""
from pathlib import Path
import spacy
from spacy import displacy

if __name__ == '__main__':
    nlp = spacy.load('en_core_web_sm')
    text = u'I am Nitin Dhiman. I live in India. I am a Software Engineer at Yellow Messenger Pvt. Ltd.'
    doc = nlp(text)

    # "dep" stands for syntactic dependency
    html = displacy.render(doc, style="dep", options={'distance': 110}, page=True, minify=True)
    output_path = Path("./generatedFiles/003. syntactic_dep.html")
    output_path.open("w", encoding="utf-8").write(html)

    # spacy can also visualize entities
    text = u'Apple sold nearly 5k iPhones worth $6 million in last 6 months.'
    doc = nlp(text)
    # "ent" stands for entity
    html = displacy.render(doc, style="ent", options={'distance': 110}, page=True, minify=True)
    output_path = Path("./generatedFiles/003. entity.html")
    output_path.open("w", encoding="utf-8").write(html)