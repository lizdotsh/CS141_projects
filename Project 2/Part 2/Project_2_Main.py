from Project_2 import *
import random

#Generate 5 random phone numbers using the full list of area codes (AREA_CODES)
#Using a period as the separator
#These numbers should be stored in a list. After the full list is generated, print it.
fivelist = []
for i in range(5):
    fivelist += [make_phone_number(sep = '.')]
print(fivelist)
    


#Generate 10 random phone numbers for the area code 503 only. Use the default separator.
#These should be stored in a list. 
#After the full list is generated, print it.
tenlist = []
for i in range(10):
    tenlist += [make_phone_number(area_codes = ['503'])]
print(tenlist)
