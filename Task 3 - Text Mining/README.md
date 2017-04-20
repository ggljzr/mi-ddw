# Text Mining

This task was to recongnize and classify [named entities](https://en.wikipedia.org/wiki/NER) in a given text (in this case article about [American revolution](https://simple.wikipedia.org/wiki/Americas) on Wikipedia).

Recognition was done with [nltk](http://www.nltk.org/) module, specificaly with `nltk.ne_chunk` function, and with custom NER function.

Aside from basic classification provided by `nltk.ne_chunk`, we implemented more specific classification using Wikipedia articles about found entities. Data from Wikipedia were obtained with [wikipedia](https://pypi.python.org/pypi/wikipedia/) module.

## Implementation and results

Both implementation, comments, and results can be fount in IPython notebook [here](https://github.com/ggljzr/mi-ddw/blob/master/Task%203%20-%20Text%20Mining/task3.ipynb).

If you want to run notebook on your computer, you have to install [Jupyter](http://jupyter.org/).

### Most common entities found by `nltk.ne_chunk`

| Entity              | Class Tag    | Count |
|:--------------------|:-------------|:-----:|
| British             | GPE          |  154  | 
| America             | GPE          |  145  | 
| American            | GPE          |  130  | 
| New                 | ORGANIZATION |   51  | 
| Loyalist            | GPE          |   46  | 
| Americans           | GPE          |   44  | 
| Britain             | GPE          |   40  | 
| Patriot             | GPE          |   38  | 
| Revolution          | ORGANIZATION |   38  | 
| Loyalists           | ORGANIZATION |   37  | 
| Congress            | ORGANIZATION |   35  | 
| Patriots            | GPE          |   29  | 
| Boston              | GPE          |   29  | 
| New York            | GPE          |   29  | 
| American Revolution | ORGANIZATION |   24  | 
| Parliament          | ORGANIZATION |   24  | 
| United States       | GPE          |   20  | 
| French              | GPE          |   19  | 
| Washington          | GPE          |   19  | 
| Continental         | ORGANIZATION |   18  | 

### Most common entites found by custom NER function

| Entity              | Count |
|:--------------------|:------|
| British             | 154   |
| America             | 145   |
| Loyalist            | 46    |
| Americans           | 44    |
| Britain             | 40    |
| Revolution          | 38    |
| Patriot             | 38    |
| Loyalists           | 37    |
| Congress            | 35    |
| Patriots            | 29    |
| Boston              | 29    |
| New York            | 29    |
| Parliament          | 24    |
| American Revolution | 24    |
| United States       | 20    |
| Washington          | 19    |
| French              | 19    |
| War                 | 18    |
| Act                 | 18    |
| King                | 17    |

### Classification with Wikipedia

Top 5 entities found by both `nltk.ne_chunk` and custom NER:

| Entity              | Description                                                                     |
|:--------------------|:--------------------------------------------------------------------------------|
| British             | sovereign country in western Europe                                             |
| America             | Thing*                                                                          |
| Loyalist            | individual allegiance toward established government political party sovereign   |
| Americans           | citizens of United States of America                                            |
| Britain             | sovereign country in western Europe                                             |

Entities found only by `nltk.ne_chunk`:

| Entity              | Description                          |
|:--------------------|:-------------------------------------|
| New                 | South Korean single-place paraglider |
| Continental         | one of several                       |

Entities found only by custom NER:

| Entity              | Description                          |
|:--------------------|:-------------------------------------|
| French              | country with territory in western Europe several overseas regions territories |
| War                 | state of armed conflict between societies                                     |
| Act                 | activity                                                                      |
| King                | electoral district in Australian state of New South Wales                     |

## Issues, future improvements

As described in the notebook, I had some issues with finding suitable noun phrase in first sentence of the summary of Wikipedia article. I was able to fix this to some degree by switching between normal english and simple english Wikipedia.

Another issue is getting most common entities, which I think is not very effective and could use some improvement.

Entity recognition also sometimes mistakes common words with actual named entities, this issues however is common for both custom NER and `nltk.ne_chunk`.