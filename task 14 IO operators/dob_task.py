#with open('task 14 IO operators/DOB.txt', 'r+') as file: 
#Above file directory needed to be used to work on my own laptop

temp_list = [] #creating a temp list to store each line in a nested list, to index and rearrange

with open('DOB.txt', 'r+') as file:
    for line in file:
       temp_list.append(line.split(' ')) #appending each word into a nested list
        
print('Name \n')
for names in temp_list:
    print (names[0]+' ' +[1]) #getting each index number

print('\nBirthdate\n') 
for dates in temp_list:
    print(dates[2]+' '+dates[3]+' '+dates[4], end ='') #getting the birthdate, adding end ='' so that there is no a line gap after printed.