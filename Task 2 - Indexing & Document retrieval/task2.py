
# import
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import numpy as np
 
# prepare corpus
document_corpus = []
query_corpus = []

for d in range(1400):
    f = open("cranfield/d/"+str(d+1)+".txt")
    document_corpus.append(f.read())
# add query to corpus
for q in range(225):
    f = open("cranfield/q/"+str(q+1)+".txt")
    query_corpus.append(f.read())

# init vectorizer
tfidf_vectorizer = TfidfVectorizer()
count_vectorizer = CountVectorizer()
 
# prepare matrix
#matice obsahujici hodnoty pro dvojice (dokument, term)
#tj kazdy policko je tfidf hodnota termu v danym dokumentu (radek)
tfidf_matrix = tfidf_vectorizer.fit_transform(document_corpus)

#to samy akorat counts (tj pocet vyskytu termu v danym dokumentu) misto tfidf (doufam)
count_matrix = count_vectorizer.fit_transform(document_corpus)

print(tfidf_matrix.shape)
print(count_matrix.shape)

print(tfidf_matrix[0].shape) #hodnota tfidf kazdyho termu v dokumentu 0
print(count_matrix[0].shape) #pocet kazdyho termu v dokumentu 0

#pak tady to samy s tim query corpusem

