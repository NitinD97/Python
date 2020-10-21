import spacy

if __name__ == '__main__':

    # Download model using "python3 -m spacy download en_core_web_sm"
    # 'en_core_web_sm' this is a small english model ~12MB
    # 'en_core_web_lg' this is a larger version of english model ~790MB

    # Here we load a model that we downloaded
    # small english model is enough for basic usecases
    nlp = spacy.load("en_core_web_sm")

    text = u"Tesla is looking at buying a U.S. startup for $6 million. Let's see what they do."
    doc = nlp(text)

    print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
    print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

    # in a pipeline, spacy does many task, mainly tagging, parsing and NER(Name Entity Recognition)
    nlp_pipeline = nlp.pipeline
    print(*nlp_pipeline, sep='\n')