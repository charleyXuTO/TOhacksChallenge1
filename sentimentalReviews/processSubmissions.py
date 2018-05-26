import matplotlib as mpl
mpl.use('tkagg')
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import numpy as np


print(mReview.objects.all())

businessReviews = [" the waiter was rude and mean but he was also pretty."]

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

x_pos = np.arange(len(objects))



totalScores = [neutralScores, positiveScores, negativeScores]


figure = plt.figure()
colors = ['b','g','r']
plt.pie(totalScores, labels = objects, autopct = '%1.1f%%', startangle = 140, colors = colors)



plt.title("Reviews")



figure.show()
plt.show()
