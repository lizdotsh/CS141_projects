import random
#Written by Elizabeth Goodwin
#Do not change the constant given below in any way
#Use it in your code
#If you are copying and pasting this list of area codes anywhere in your code, you are doing it wrong
AREA_CODES = ['205', '251', '256', '334', '659', '938', '907', '236', '250', '778', '480', '520', 
'602', '623', '928', '327', '479', '501', '870', '209', '213', '279', '310', '323', '341', '408', 
'415', '424', '442', '510', '530', '559', '562', '619', '626', '628', '650', '657', '661', '669', 
'707', '714', '747', '760', '805', '818', '820', '831', '840', '858', '909', '916', '925', '949', 
'951', '303', '719', '720', '970', '203', '475', '860', '959', '302', '202', '239', '305', '321', 
'352', '386', '407', '448', '561', '689', '727', '754', '772', '786', '813', '850', '863', '904', 
'941', '954', '229', '404', '470', '478', '678', '706', '762', '770', '912', '808', '208', '986', 
'217', '224', '309', '312', '331', '447', '464', '618', '630', '708', '730', '773', '779', '815', 
'847', '872', '219', '260', '317', '463', '574', '765', '812', '930', '319', '515', '563', '641', 
'712', '316', '620', '785', '913', '270', '364', '502', '606', '859', '225', '318', '337', '504', 
'985', '207', '227', '240', '301', '410', '443', '667', '339', '351', '413', '508', '617', '774',
'781', '857', '978', '231', '248', '269', '313', '517', '586', '616', '734', '810', '906', '947',
'989', '218', '320', '507', '612', '651', '763', '952', '228', '601', '662', '769', '314', '417', 
'573', '636', '660', '816', '406', '308', '402', '531', '702', '725', '775', '603', '201', '551', 
'609', '640', '732', '848', '856', '862', '908', '973', '505', '575', '212', '315', '332', '347', 
'516', '518', '585', '607', '631', '646', '680', '716', '718', '838', '845', '914', '917', '929', 
'934', '252', '336', '704', '743', '828', '910', '919', '980', '984', '701', '216', '220', '234', 
'326', '330', '380', '419', '440', '513', '567', '614', '740', '937', '405', '539', '572', '580', 
'918', '458', '503', '541', '971', '215', '223', '267', '272', '412', '445', '484', '570', '610', 
'717', '724', '814', '878', '401', '803', '839', '843', '854', '864', '605', '423', '615', '629', 
'731', '865', '901', '931', '210', '214', '254', '281', '325', '346', '361', '409', '430', '432', 
'469', '512', '682', '713', '726', '737', '806', '817', '830', '832', '903', '915', '936', '940', 
'945', '956', '972', '979', '385', '435', '801', '802', '276', '434', '540', '571', '703', '757', 
'804', '948', '206', '253', '360', '425', '509', '564', '304', '681', '262', '274', '414', '534', 
'608', '715', '920', '307'] #do not change or delete

#Write the first part of your program here: create a random valid prefix using conditionals
#You must use the two lines of code given to you
first = random.choice('0123456789') #do not change or delete
#print(first)
second = random.choice('0123456789') #do not change or delete
#print(second)
valid = False
while(valid == False):
    third = random.choice('0123456789')
    prefix = first + second + third
    #print(prefix)
    if(prefix == ('555' or '958' or '959') or prefix[1:] == '11'):
        pass
    else:
        valid = True

#print(prefix)
    
#Debug the second part of the program here: create a random suffix
#Do not add or delete lines
#Do not move lines
#Keep same general structure, i.e. use a while loop, use random.choices 
suffix = ''
i = 0
digits = random.choices([0,1,2,3,4,5,6,7,8,9], k=4)
#print(digits)
while i <= 3:
    suffix += str(digits[i]) 
    i += 1
    #print(i) #for debugging only, comment out when you turn in
#print(suffix) #for debugging only, comment out when you turn in


#Write the third part of your program here: randomly select an area code
#If this is more than one line, you might be doing it wrong
area = random.choice(AREA_CODES)
#print(area)

#Write the fourth part of your program here: put the area code, prefix, and suffix together
#to create a valid random phone number
#If this is more than one line, you might be doing it wrong
phone_number = area + '-' + prefix + '-' + suffix
#print the phone number at the end
#if you don't print it, you won't get results from the test program
#make sure it is stored in the correct variable name
print(phone_number) #do not change or delete
#the phone number at the end is the only thing that should be printed
#if you have other print lines, comment them out
