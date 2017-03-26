# Cranfield dataset processing

In this task we were processing [Cranfield collection](http://ir.dcs.gla.ac.uk/resources/test_collections/cran/). It contains sets of documents and queries, and lists of relevant documents for each query. 

Task was to create vector space model (using TF, [TFIDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) and binary methods), calculate relevance scores (using cosine similarity and euclidean distance) for each query and evaluate quality of these scores.

This implementation relies on [scikit-learn](http://scikit-learn.org/stable/) module.

## Usage

Both implementation, results, and comments can be found in notebook `task2.ipynb` [here](https://github.com/ggljzr/mi-ddw/blob/master/Task%202%20-%20Indexing%20%26%20Document%20retrieval/task2.ipynb). If you want to run notebook on your computer, you have to install [Jupyer](http://jupyter.org/).

## Relevance scores

Calculated relevance scores for each pair (query, document) can be found in `.csv` format in folder `relevance_scores` [here](https://github.com/ggljzr/mi-ddw/tree/master/Task%202%20-%20Indexing%20%26%20Document%20retrieval/relevance_scores).

## Results

The TFIDF vector space model had the best performance, as was expected. Other models (pure TF and binary model) had similar results, where binary model was ever so slightly better.

Results of every model were far worse when Euclidean distance was used instead of Cosine similarity.

## Issues with implementation, future improvements

Implementation was fairly straightforward, since `sklearn` module provides all necesary functions for this task.

Only issue is that I am not really sure if I used measuring with Euclidean distance
correctly, since it yields very poor results. This is what I would like to look into in the future.

Another thing that could use some improvement is visualisation of the results.