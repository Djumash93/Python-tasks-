#getting an input in number of students
number_students = int(input('How many students registering for the exam? '))


for number in range(0,number_students): #in range of number off students
    with open('reg_form.txt', 'a') as f: # 'a' lets create, write and append at the end of files
        f.write('Student ID: '+ input(f'ID number for student number {number+1}: ') + '........................\n')
        
#output in the text file will have have the student ID as an intro, followed by the input text.