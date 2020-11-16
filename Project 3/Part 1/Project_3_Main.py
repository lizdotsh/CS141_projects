from Project_3 import *
import emoji
#Elizabeth Goodwin 

#Create a dictionary containing all of the emojis from the Tortoise data set. Be sure to assign a variable name to this dictionary.
tortoise_emojis = feature_extract('tortoise_tweets.txt', feature='emoji')
#print(tortoise_emojis)
#Create a dictionary containing all of the emojis from the Umbrella data set. Be sure to assign a variable name to the dictionary.
umbrealla_emojis = feature_extract('umbrella_tweets.txt', feature='emoji')
#print(umbrealla_emojis)
#Find all of the emojis that are shared by the two data sets (i.e. the emojis that can be found in both). Print these out.
shared_emojis = []
for key in list(umbrealla_emojis.keys()):  #separates keys, turns into its own list
    if key in list(tortoise_emojis.keys()): #ads to shared_emojis list if shared
        shared_emojis += [key] 
    else:
        pass

#print(list(umbrealla_emojis.keys()))
#print(list(tortoise_emojis.keys()))
print(shared_emojis)

#Find all of the emojis that are in the Tortoise data set but not the Umbrella data set. Print these out.
tortoise_unique_emojis = []
for key in list(tortoise_emojis.keys()): 
    if key not in list(umbrealla_emojis.keys()):
        tortoise_unique_emojis += [key]
    else:
        pass
print(tortoise_unique_emojis)

#Create a dictionary containing all of the hashtags from the Umbrella data set. Print this out. 
umbrella_hashtags = feature_extract('umbrella_tweets.txt', feature='#')
print(umbrella_hashtags)
#What is the most common hashtag? (You don’t have to write code to find it, just look at the data, and comment on it in your write-up.)
#it is #umbrellaacademy or #tvtime, tied for first. 