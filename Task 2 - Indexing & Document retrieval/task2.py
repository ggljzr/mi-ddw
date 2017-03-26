
# import
from sklearn.metrics.pairwise import cosine_similarity, pairwise_distances
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import numpy as np

def get_top_n(matrix, n=10):
	return np.array([ matrix[i].argsort()[-n:][::-1]+1 for i in range(225)])

def get_precision(query_index, top_retrieved):
	relevant = []
	with open('cranfield/r/{}.txt'.format(query_index)) as f:
		for line in f:
			relevant.append(int(line))

	tp = 0
	fn = 0
	fp = 0

	for doc in relevant:
		if doc in retrieved:
			tp += 1
		else:
			fn += 1 

	for doc in retrieved:
		if doc not in relevant:
			fp += 1

	p = tp / (tp + fp)
	r = tp / (tp + fn)
	f = 2 * ((p * r)/(p + r))

	return p, r, f

# prepare corpus
corpus = []

for d in range(1400):
    f = open("cranfield/d/"+str(d+1)+".txt")
    corpus.append(f.read())
    f.close()
# add query to corpus
for q in range(225):
    f = open("cranfield/q/"+str(q+1)+".txt")
    corpus.append(f.read())
    f.close()

# init vectorizer
tfidf_vectorizer = TfidfVectorizer()
count_vectorizer = CountVectorizer()
binary_vectorizer = CountVectorizer(binary=True)
 
# prepare matrix
#matice obsahujici hodnoty pro dvojice (dokument, term)
#tj kazdy policko je tfidf hodnota termu v danym dokumentu (radek)
tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)

#to samy akorat counts (tj pocet vyskytu termu v danym dokumentu) misto tfidf (doufam)
count_matrix = count_vectorizer.fit_transform(corpus)

#a nakonec jen {0,1} jestli tam term neni/je
bin_matrix = binary_vectorizer.fit_transform(corpus)

r_tfdif_cos = np.array(cosine_similarity(tfidf_matrix[1400:], tfidf_matrix[:1400]))
r_tfdif_euc = np.array(pairwise_distances(tfidf_matrix[1400:], tfidf_matrix[:1400]))

r_count_cos = np.array(cosine_similarity(count_matrix[1400:], count_matrix[:1400]))
r_count_euc = np.array(pairwise_distances(count_matrix[1400:], count_matrix[:1400]))

r_bin_cos = np.array(cosine_similarity(bin_matrix[1400:], bin_matrix[:1400]))
r_bin_euc = np.array(pairwise_distances(bin_matrix[1400:], bin_matrix[:1400]))

#matice (225, 10), pro kazdy query top 10 dokumentu podle tfdif score, cos sim
top_relevant_tfdif_cos = get_top_n(r_tfdif_cos)
top_relevant_tfdif_euc = get_top_n(r_tfdif_euc)

top_relevant_count_cos = get_top_n(r_count_cos)
top_relevant_count_euc = get_top_n(r_count_euc)

top_relevant_bin_cos = get_top_n(r_bin_cos)
top_relevant_bin_euc = get_top_n(r_bin_euc)


