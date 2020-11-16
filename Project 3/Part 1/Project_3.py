import emoji 
#testfile = open('test_file.txt', 'r')
#text = testfile.read()
#testfile.close()
#print(text)
#Elizabeth Goodwin 

def process_text(text, punct = '.,;:"?!.'): #do not change def line
    addspace = {'@':' @', '#':' #', '-':' '}
    for item in list(punct): #adds punct to dictionary. 
        addspace[item] = ''
    #print(addspace)
    text_2 = text.translate(text.maketrans(addspace)).split() #converts addspace for translate and translates
    return text_2
    # I realize you could use the maketrans to delete all in punct, but you can't use addspace and that without using two 
    # sets of translate(maketrans()) so I just added it all to addspace

#text_list = process_text(text, punct = '.,;:"?!.')
#print(process_text("here is a tweet that is open-ended and contains one-time words"))

def get_emojis(text): #do not change def line

    return [item for item in list(text) if item in emoji.UNICODE_EMOJI]

#print(get_emojis(text))

def get_features(text_list, feature): #do not change def line
    #debug the line below - you must leave it as list comprehension
    return [item for item in text_list if feature in item]
    
#print(get_features(text_list,'@'))

def feature_extract(filename, feature = '#'): #do not change def line
    with open(filename,'r') as file:
        tweet = file.read()
    tweets = process_text(tweet) #processes text for def_features 
    if(feature == '#' or feature == '@'):
        tweets_2 = get_features(tweets, feature)
    elif feature == 'emoji':
        tweets_2 = get_emojis(tweet)
    tweets_3 = {}
    for item in tweets_2:#counts number of times each emoji/feature is counted for dictionary
        if item in tweets_3:
            tweets_3[item] += 1
        else:
            tweets_3[item] = 1
    return tweets_3

#print(feature_extract('test_file.txt', feature = 'emoji'))
    
    
    
