# Text Mining

This task was to recongnize and classify [named entities](https://en.wikipedia.org/wiki/NER) in a given text (in this case article about [American revolution](https://simple.wikipedia.org/wiki/Americas) on Wikipedia).

Recognition was done with [nltk](http://www.nltk.org/) module, specificaly with `nltk.ne_chunk` function, and with custom NER function.

Aside from basic classification provided by `nltk.ne_chunk`, we implemented more specific classification using Wikipedia articles about found entities. Data from Wikipedia were obtained with [wikipedia](https://pypi.python.org/pypi/wikipedia/) module.

## Implementation and results

Both implementation, comments, and results can be fount in IPython notebook [here](https://github.com/ggljzr/mi-ddw/blob/master/Task%203%20-%20Text%20Mining/task3.ipynb).

If you want to run notebook on your computer, you have to install [Jupyter](http://jupyter.org/).

### Most common entities found by `nltk.ne_chunk`


| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |       |

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

custom NER:
British count: 154
America count: 145
Loyalist count: 46
Americans count: 44
Britain count: 40
Revolution count: 38
Patriot count: 38
Loyalists count: 37
Congress count: 35
Patriots count: 29
Boston count: 29
New York count: 29
Parliament count: 24
American Revolution count: 24
United States count: 20
Washington count: 19
French count: 19
War count: 18
Act count: 18
King count: 17

## Issues, future improvements

As described in the notebook, I had some issues with finding suitable noun phrase in first sentence of the summary of Wikipedia article. I was able to fix this to some degree by switching between normal english and simple english Wikipedia.

Another issue is getting most common entities, which I think is not very effective and could use some improvement.

Entity recognition also sometimes mistakes common words with actual named entities, this issues however is common for both custom NER and `nltk.ne_chunk`.