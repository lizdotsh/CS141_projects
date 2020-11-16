# Written by Elizabeth Goodwin

#User inputs original DNA sequence
oDNA = input('Enter sequence name: ' )
#print(oDNA)
#Renames DNA sequence in Variable nDNA, replaces machine header and changes format of read direction
nDNA = 'Seq' + oDNA[15:-2] + ':Read_' + oDNA[-1]
#Prints result
print('New name is', nDNA)
