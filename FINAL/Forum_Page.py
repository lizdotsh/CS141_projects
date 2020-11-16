# Written by Elizabeth Goodwin 
import datetime
import pandas as pd
import random
import numpy as np

class Forum_Page:

    def __init__(self, name):
        self.__name = name
        self.__board = pd.DataFrame(columns = ['Title','Date', 'Author', 'Post', 'Votes'])
        self.__board.set_index('Title', inplace = True)
        self.__board['Votes'] = self.__board['Votes'].astype('int')
        self.__anon_words = self.__process('words.txt')
        
    
    def __process(self, filename):
        with open(filename,'r', encoding = 'UTF8') as file:
           result = [line.rstrip() for line in file]
        return result
        
    def __exists(self, title):
        return title in self.__board.index
    
    def checker(self):
        return self.__board.copy()
    
    def __generate_anon(self):
        n = 0
        while n == 0: 
            name = "_".join(random.sample(self.__anon_words, 2) + [(str(random.randint(0,9)) + str(random.randint(0,9)))]) #Generates random name
            if name in self.__board['Author'].unique(): pass # Checks if its an author already
            else: 
                n = 1
                return name
        
    def add_post(self, title, post, author = None):
        if author == None: author = self.__generate_anon() #Tests if an Author is given, if not it generates a random author
        if self.__exists(title) == False: self.__board.loc[title] = [str(datetime.date.today()), author, post, 0] # Tests if a post with the same title exists, and if so adds the post

    def delete_post(self, title):
        if self.__exists(title) == True: self.__board.loc[title, ['Post', 'Author']] = np.nan # If title exists, set the post and author columns at title row to NaN
    
    def vote_post(self, title, up = True):
        if (self.__exists(title) == True) and (self.__board.loc[title, ['Post', 'Author']].isnull().all() == False): #Tests if post exists and confinrms that it has not been deleted
            self.__board.loc[title, 'Votes'] += 1 if up == True else -1 # sets value of number added depending on if it is an up or down vote

    def top_voted(self): # Finds the item with the max amounts of votes and uses it inside of a function to find all other items with that vote count
        if self.__board.empty == False: return self.__board.loc[self.__board['Votes'].isin([self.__board['Votes'].max()])]
        
    def get_titles(self): return self.__board.index.tolist() #converts index into a list, returns said list
        
    def get_post_info(self, title): #checks if title exists, and if so returns a list of the Date, Author, Post, and Votes
        if self.__exists(title): return self.__board.loc[title].tolist()
    
    def get_name(self):
        return self.__name
        
    def __str__(self):
        active = self.__board[self.__board[['Post', 'Author']].notnull().all(1)] #creates a new dataframe that does not include anything with NaN in post/author, so no deleted ones. 
        return str(len(active)) + ' active posts on ' + self.get_name() #Returns the length of said dataframe in string format. 
        