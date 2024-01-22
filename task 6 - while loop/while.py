#Enter -1 to stop running the programme

constant_number = 0
number_count =0
while constant_number >=0:
    input_number=int(input('Enter your number: '))
    if input_number == -1:
       break
    constant_number= input_number+constant_number
    number_count+=1

print(f'The average of all inputs is {constant_number/number_count}')    
    
    
 
  