import matplotlib.pyplot as plt; plt.rcdefaults()

from nltk.sentiment.vader import SentimentIntensityAnalyzer

import numpy as np

businessReviews = [" the waiter was rude and mean."]

sid = SentimentIntensityAnalyzer()

positiveScores = 0
negativeScores = 0
neutralScores = 0

objects = ('Neutral', 'Positive', 'Negative')

#analyse sentiments
for sentence in businessReviews :
    print("Sentence: " + sentence + "\n")

    score = sid.polarity_scores(sentence)

    neutralScore = score['neu']
    positiveScore = score['pos']
    negativeScore = score['neg']

    positiveScores += positiveScore
    negativeScores += negativeScore
    neutralScores += neutralScore


    print("Neutral Score: {} Positive Score: {} Negative Score: {}  ".format(neutralScore, positiveScore, negativeScore))

objects = ('Neutral', 'Positive', 'Negative')

y_pos = np.arrange()
totalScores = [neutralScores, positiveScores, negativeScores]


plt.bar(totalScores, )
