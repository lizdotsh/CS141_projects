import emoji
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
#Elizabeth Goodwin
#test_file = open("test_file.txt","r")
#test = test_file.read()
#test_file.close()
#print(test)

def make_tokens(text): #do not change
    tt = TweetTokenizer(preserve_case=False) #do not change
    tokens = tt.tokenize(text) #do not change
    return tokens #do not change

#print(make_tokens(test))

#tokens = make_tokens(test)
def prune_tweet_tokens(tokens, stops = []): #do not change
    bad = ['@','#'] 
    stops = list(stops)
    stops += list('''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~''') + list(emoji.UNICODE_EMOJI.keys())
    #print(stops)
    f = [item for item in tokens if not any(ignore in item for ignore in bad)]
    return [it for it in f if it not in stops]
    

#print(prune_tweet_tokens(tokens))

def analyze(filename, analysis = 'frequency', stops = [], number = 10, word = ''): #do not change
    with open(filename,'r') as file: tokens = make_tokens(file.read()) # reads file
   # print(tokens)
    a = nltk.Text(prune_tweet_tokens(tokens, stops = stops)) # formats it for concordance and collocations 
   # print(prune_tweet_tokens(tokens, stops = stops))
    if analysis == 'frequency': return (nltk.FreqDist(prune_tweet_tokens(tokens, stops = stops))).most_common(number) #finds frequency using FreqDist and most_common
    elif analysis == 'concordance': a.concordance(word, lines = number) #finds concordance
    elif analysis == 'collocations': print(a.collocation_list(num = number))

#print(analyze('tortoise_tweets.txt', analysis = 'collocations', number = 10, word = 'tortoise'))
#__name__ = '__main__'

if __name__ == '__main__': #do not change
    stops = stopwords.words('english') + ['…', '’', '...']
    #print(stops)
    print(analyze('umbrella_tweets.txt', stops = stops, number = 15))
    print(analyze('tortoise_tweets.txt', stops = stops, number = 5))
    analyze('tortoise_tweets.txt', analysis = 'collocations', number = 5, stops = stops)
    analyze('umbrella_tweets.txt', analysis = 'concordance', number = 4, word = 'watch', stops = stops)
    #main program MUST BE indented or it will not run and will BREAK EVERYTHING

