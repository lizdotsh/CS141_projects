import unittest
import emoji
from Project3_Part2 import *


class Functions_Tester(unittest.TestCase):


  def test_prune_tweet_tokens_emoji(self):
    print('\n\nTest prune emoji')
    try:
      tokens = ['why', 'is', 'everything', 'so', 'expensive', '😭', 'im', 'broke', 'okay', 'i', 'dont', 'have', 'money', '😭', '😭', 'i', 'ordered', 'food', 'for', 'my', 'guinea', 'pig', '😍']
      new_tokens = prune_tweet_tokens(tokens)
      print('Input was:', tokens)
      print('Return value was:', new_tokens)
      result_pred = ['why', 'is', 'everything', 'so', 'expensive', 'im', 'broke', 'okay', 'i', 'dont', 'have', 'money', 'i', 'ordered', 'food', 'for', 'my', 'guinea', 'pig']
      print('Expected',result_pred)
      self.assertEqual(new_tokens, result_pred)
    except BaseException as e:
      print(e)
      print('Testing failed.')


  def test_prune_tweet_tokens_mentions(self):
    print('\n\nTest prune mentions')
    try:
      tokens = ['@tomfolanmd', '@jonathanstea', '@drrobbietee', 'i', 'volunteer', 'to', 'be', 'a', 'guinea', 'pig', '@ryanmarino', 'for', 'the', 'study']
      new_tokens = prune_tweet_tokens(tokens)
      print('Input was:', tokens)
      print('Return value was:', new_tokens)
      result_pred = ['i', 'volunteer', 'to', 'be', 'a', 'guinea', 'pig', 'for', 'the', 'study']
      print('Expected',result_pred)
      self.assertEqual(new_tokens, result_pred)
    except BaseException as e:
      print(e)
      print('Testing failed.')
      

  def test_prune_tweet_tokens_hashtags(self):
    print('\n\nTest prune hashtags')
    try:
      tokens = ['this', 'tweet', 'has', 'a', 'lot', 'of', '#hashtags', '#really', '#close', '#together', 'and', 'one', 'that', 'is', '#separate']
      new_tokens = prune_tweet_tokens(tokens)
      print('Input was:', tokens)
      print('Return value was:', new_tokens)
      result_pred = ['this', 'tweet', 'has', 'a', 'lot', 'of', 'and', 'one', 'that', 'is']
      print('Expected',result_pred)
      self.assertEqual(new_tokens, result_pred)
    except BaseException as e:
      print(e)
      print('Testing failed.')

  def test_prune_tweet_tokens_punctuation(self):
    print('\n\nTest prune hashtags')
    try:
      tokens = ['this', 'tweet', ',', 'has', 'a', 'lot', 'of', 'punctuation', ':', 'in', 'it', '!', 'and', ';', "there's", "didn't", 'more', '?']      
      new_tokens = prune_tweet_tokens(tokens)
      print('Input was:', tokens)
      print('Return value was:', new_tokens)
      result_pred = ['this', 'tweet', 'has', 'a', 'lot', 'of', 'punctuation', 'in', 'it', 'and', "there's", "didn't", 'more']
      print('Expected',result_pred)
      self.assertEqual(new_tokens, result_pred)
    except BaseException as e:
      print(e)
      print('Testing failed.')

  def test_prune_tweet_tokens_stops(self):
    print('\n\nTest prune stops')
    try:
      stops = {'the','turtle','and'}
      tokens = ['sometimes', 'there', 'are', 'examples', 'that', 'just', 'have', 'a', 'turtle', 'sometimes', 'the', 'example', 'has', 'turtle', 'and', 'potato']
      print('Input was:', tokens, '\nUsing stopwords:', stops)
      new_tokens = prune_tweet_tokens(tokens, stops)
      print('Return value was:', new_tokens)
      result_pred = ['sometimes', 'there', 'are', 'examples', 'that', 'just', 'have', 'a', 'sometimes', 'example', 'has', 'potato']
      print('Expected',result_pred)
      self.assertEqual(new_tokens, result_pred)
    except BaseException as e:
      print(e)
      print('Testing failed.')

#analysis each branch
#non default values vs default values
#no stopwords vs stopwords
  def test_analysis_freq_defaults(self):
    print('\n\nTest analyze frequency defaults')
    try:
      print('Using file Obama_1.txt with default parameters')
      frequencies = analyze('Obama_1.txt')
      print('Return value was:', frequencies)
      result_pred = [('the', 130), ('and', 114), ('of', 82), ('to', 70), ('our', 67), ('we', 62), ('that', 50), ('a', 48), ('is', 36), ('in', 25)]
      print('Expected',result_pred)
      self.assertEqual(frequencies, result_pred)
    except BaseException as e:
      print(e)
      print('Testing failed.')
  
  def test_analysis_freq_stops(self):
    print('\n\nTest analyze frequency stops')
    try:
      print('Using file Obama_1.txt with stopwords: the, and, of, to, our , we, that, a')
      frequencies = analyze('Obama_1.txt', stops = ['the','and','of','to','our','we','that','a'])
      print('Return value was:', frequencies)
      result_pred = [('is', 36), ('in', 25), ('this', 24), ('us', 23), ('for', 23), ('are', 22), ('but', 20), ('will', 19), ('it', 18), ('on', 17)]      
      print('Expected',result_pred)
      self.assertEqual(frequencies, result_pred)
    except BaseException as e:
      print(e)
      print('Testing failed.')


  def test_analysis_freq_number(self):
    print('\n\nTest analyze frequency number')
    try:
      print('Using file Obama_1.txt with number = 5')
      frequencies = analyze('Obama_1.txt', number = 5)
      print('Return value was:', frequencies)
      result_pred = [('the', 130), ('and', 114), ('of', 82), ('to', 70), ('our', 67)]
      print('Expected',result_pred)
      self.assertEqual(frequencies, result_pred)
    except BaseException as e:
      print(e)
      print('Testing failed.')

  def test_analysis_concordance_default(self):
    print('\n\nTest analyze concordance default')
    try:
      print('Using file Obama_1.txt with word = great')
      frequencies = analyze('Obama_1.txt', 'concordance', word = 'great')
      print('Return value was:', frequencies)
      result_pred = None
      print('Expected',result_pred)
      self.assertEqual(frequencies, result_pred)
    except BaseException as e:
      print(e)
      print('Testing failed.')
  
  def test_analysis_collocations_default(self):
    print('\n\nTest analyze collocations default')
    try:
      print('Using file Obama_1.txt')
      frequencies = analyze('Obama_1.txt', 'collocations')
      print('Return value was:', frequencies)
      result_pred = None
      print('Expected',result_pred)
      self.assertEqual(frequencies, result_pred)
    except BaseException as e:
      print(e)
      print('Testing failed.')



if __name__ == '__main__':
  unittest.main()
  