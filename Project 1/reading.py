# Calculate average reading speed 
# Written by Elizabeth Goodwin
SEC_PER_MIN = 60
SEC_PER_HOUR = 3600
pages = int(input('Enter number of readable pages: '))
#print(pages)
reading_hours = float(input('Enter how long it took to read the book (in hours): '))
#print(reading_hours)
# reading pace = reading time in seconds / number of pages read
pace=(reading_hours*SEC_PER_HOUR)/(pages)
#print(pace)
print("Your average reading pace is",round((pace // SEC_PER_MIN)),'minutes',round((pace % SEC_PER_MIN)), 'seconds per page')


