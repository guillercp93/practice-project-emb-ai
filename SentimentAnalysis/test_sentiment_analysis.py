from sentiment_analysis import sentiment_analyzer
import unittest


class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        result1 = sentiment_analyzer("I love working with Python")
        self.assertEqual(result1['documentSentiment']
                         ['label'], 'SENT_POSITIVE')

        result2 = sentiment_analyzer("I hate working with Pyhton")
        self.assertEqual(result2['documentSentiment']
                         ['label'], 'SENT_NEGATIVE')

        result3 = sentiment_analyzer("I am neutral on Python")
        self.assertEqual(result3['documentSentiment']['label'], 'SENT_NEUTRAL')


unittest.main()
