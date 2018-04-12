'''
We need to make sure that we have equal number of data points for each label.
We will label a review `useful` if it has received 1 or more `useful` votes,
and those with votes lesser than 1 as *not useful*.

The following snippet randomly samples for a predefined number (defined by `SAMPLE_SIZE`)
of *useful* and *not useful* reviews. The dataframes are then concatenated together and
the resulting df is then shuffled.
'''
import pandas as pd

THRESHOLD = 1
SAMPLE_SIZE = 5000

reviews = pd.read_csv('dataset/review.csv', usecols=['text', 'useful', 'cool', 'funny'])

useful_reviews = reviews.loc[reviews['useful'] >= THRESHOLD].sample(SAMPLE_SIZE)
not_useful_reviews = reviews.loc[reviews['useful'] < THRESHOLD].sample(SAMPLE_SIZE)
print("useful_reviews shape: ", useful_reviews.shape)
print("not_useful_reviews shape: ", not_useful_reviews.shape)

reviews = shuffle(pd.concat([useful_reviews, not_useful_reviews]))

reviews.to_csv('dataset/review.csv')