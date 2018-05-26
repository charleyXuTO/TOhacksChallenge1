from django.core.management.base import BaseCommand
from submission.models import review as mReview
import matplotlib as mpl
mpl.use('tkagg')
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import numpy as np

class Command(BaseCommand):
    help = 'Prints the titles of all Posts'

    def handle(self, *args, **options):




        businessReviews = []

        for review in mReview.objects.all():
            businessReviews.append((str(review)))



        sid = SentimentIntensityAnalyzer()

        positiveScores = 0
        negativeScores = 0
        neutralScores = 0

        objects = ('Neutral', 'Positive', 'Negative')

        # analyse sentiments
        for sentence in businessReviews:
            print("Sentence: " + sentence + "\n")

            score = sid.polarity_scores(sentence)

            neutralScore = score['neu']
            positiveScore = score['pos']
            negativeScore = score['neg']

            positiveScores += positiveScore
            negativeScores += negativeScore
            neutralScores += neutralScore

            print("Neutral Score: {} Positive Score: {} Negative Score: {}  ".format(neutralScore, positiveScore,
                                                                                     negativeScore))

        print("\nTotals: Neutral: {} Positive: {} Negative: {} ".format(neutralScores, positiveScores, negativeScores))
        objects = ('Neutral', 'Positive', 'Negative')

        x_pos = np.arange(len(objects))

        totalScores = [neutralScores, positiveScores, negativeScores]

        figure = plt.figure()
        colors = ['b', 'g', 'r']
        plt.pie(totalScores, labels=objects, autopct='%1.1f%%', startangle=140, colors=colors)

        plt.title("Reviews")

        figure.show()
        plt.show()

