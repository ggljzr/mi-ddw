# Text Mining

This task was to recongnize and classify [named entities](https://en.wikipedia.org/wiki/NER) in a given text (in this case article about [American revolution](https://simple.wikipedia.org/wiki/Americas) on Wikipedia).

Recognition was done with [nltk](http://www.nltk.org/) module, specificaly with `nltk.ne_chunk` function, and with custom NER function.

Aside from basic classification provided by `nltk.ne_chunk`, we implemented more specific classification using Wikipedia articles about found entities. Data from wikipedia were obtained with [wikipedia](https://pypi.python.org/pypi/wikipedia/) module.

## Implementation and results

Both implementation, comments, and results can be fount in IPython notebook [here](https://github.com/ggljzr/mi-ddw/blob/master/Task%203%20-%20Text%20Mining/task3.ipynb).

If you want to run notebook on your computer, you have to install [Jupyter](http://jupyter.org/).

## Issues, future improvements

As described in the notebook, I had some issues with finding suitable noun phrase in first sentence of the summary of Wikipedia article. I was able to fix this to some degree by switching between normal english and simple english Wikipedia.

Another issue is getting most common entities, which I think is not very effective and could use some improvement.

Entity recognition also sometimes mistakes common words with actual named entities, this issues however is common for both custom NER and `nltk.ne_chunk`.