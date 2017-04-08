import nltk
import numpy as np
import wikipedia

def get_entity(entity):
    if isinstance(entity, tuple) and entity[1][:2] == 'NN':
        return entity
    if isinstance(entity, nltk.tree.Tree):
        text = ' '.join([word for word, tag in entity.leaves()])
        return (text, entity.label())
    return None

def extract_entities(chunk):
    data = []

    for entity in chunk:
        d = get_entity(entity)
        if d is not None:
            data.append(d)

    return data

text = None
with open('short_text', 'r') as f:
    text = f.read()

tokens = nltk.word_tokenize(text)
tagged = nltk.pos_tag(tokens)

# print(tagged)
ne_chunked = nltk.ne_chunk(tagged, binary=True)

ex = extract_entities(ne_chunked)

print(ex)