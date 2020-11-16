# Written by Elizabeth Goodwin 
import datetime
import pandas as pd
import random
import numpy as np
from Forum_Page import *

#Do not change the lists below 
title_list = ['A Post', 'Final_Project', 'Potato_Recipe', 'Sea Turtle', 'The turtle moves']
post_text_list = ['This post is about nothing', 'You are working on the CSCI 140 Final Project', 'There \
are lots of ways to make potatoes', 'Sea Turtles migrate during different seasons', 'This is probably \
a Terry Pratchett reference']
#Write your main program code here

CSCI_140 = Forum_Page('CSCI_140')
for x in range(5): CSCI_140.add_post(title_list[x], post_text_list[x]) #Adds 5 posts with the titles and posts coming from lists above
for x in range(3): CSCI_140.vote_post('Final_Project') #upvotes 'Final_Project' three times
print(CSCI_140.top_voted()) #prints top voted posts
CSCI_140.delete_post('Potato_Recipe') #deletes post
print(CSCI_140.get_titles()) #prints list of all titles
print(CSCI_140)
#print(CSCI_140.checker()) #debug
