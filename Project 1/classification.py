#The data
results = [40, 10, 65, 15] #TP, FP, TN, FN
SPACE_5 = 5 * ' ' #Do not change, this line is correct
SPACE_10 = 10 * ' ' #Do not change, this line is correct
#Total positive tests
total_model_pos = results[0]+results[1]
#Total negative tests
total_model_neg = results[2]+results[3]
#Total positive individuals
total_real_pos = results[0] + results[3]
#Total negative individuals
total_real_neg = results[1] + results[2]

#Make the table
print(SPACE_10 + 'Model +'+ SPACE_5 + 'Model -' + SPACE_5 + 'Total') #Do not change, this line is correct
print('-' * 40) #Do not change, this line is correct
line1 = 'Real +' + SPACE_5 + str(results[0]) + SPACE_10 + str(results[3]) + SPACE_10 + str(total_real_pos)
print(line1 + '\n') #do not change, this line is correct
line2 = 'Real -' + SPACE_5 + str(results[1]) + SPACE_10 + str(results[2]) + SPACE_10 + str(total_real_neg)
print(line2) #do not change, this line is correct
print('-' * 40)#do not change, this line is correct
line3 = 'Total ' + SPACE_5 + str(total_model_pos) + SPACE_10 + str(total_model_neg) + SPACE_10 + str(sum(results))
print(line3) #do not change, this line is correct

#Calculate PPV and NPV
precision = results[0]/int(total_model_pos)
recall = results[0]/total_real_pos
print('\nPrecision: ' + str(precision) ) #leave the /n in, it creates the space after the table
print('Recall: '+ str(recall))