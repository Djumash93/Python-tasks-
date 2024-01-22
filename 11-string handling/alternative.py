initial_string = str(input('Please type your word or words: '))
new_string =""
index1=0
while index1<len(initial_string):
    if index1%2==0:
        new_string+=initial_string[index1].upper() #every odd letter to uppercase
    else:
        new_string+=initial_string[index1] 
    index1+=1    
    
print("\n" + new_string + "\n")    


####################################################################################
string_list = initial_string.split(" ")

final_list =[]
index2=0
while index2<len(string_list):
    if index2%2 !=0:
        final_list.append(string_list[index2].upper())   #Every second word to upper case
    else:
        final_list.append(string_list[index2])  
    index2+=1
print(" ".join(final_list)) 