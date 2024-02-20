
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#Functions to be performed below. 

###################################################


#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass


with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['id']=task_components[2] #adding id
    curr_t['description'] = task_components[3]
    curr_t['due_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[5], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[6] == "Yes" else False
   
    task_list.append(curr_t)





# function to write to file

def write_to_file():
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['id'],  #adding ID to be written out in the file
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
# 1) Registering a user

def reg_user():
        '''Add a new user to the user.txt file'''
        # - Request input of a new username
        new_username = input("New Username: ")
        if new_username in username_password.keys(): #avoiding duplicate usernames
            print('Username already exists')
            return
        # - Request input of a new password
        new_password = input("New Password: ")

        # - Request input of password confirmation.
        confirm_password = input("Confirm Password: ")

        # - Check if the new password and confirmed password are the same.
        if new_password == confirm_password:
            # - If they are the same, add them to the user.txt file,
            print("New user added")
            username_password[new_username] = new_password
            
            with open("user.txt", "w") as out_file:
                user_data = []
                for k in username_password:
                    user_data.append(f"{k};{username_password[k]}")
                out_file.write("\n".join(user_data))

        # - Otherwise you present a relevant message.
        else:
            print("Passwords do no match")

####################################################

#2) Adding a new task

def add_task():
   
    task_username = input("Name of person assigned to task: ")
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        return    #changing continue to return to break out of the function in the loop below
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")
    if len(task_list)==0: #if length of task data = 0 then adding the first task id = 1
        task_id =1
    else:        
        for index, new_task in enumerate(task_list, start=1):
          task_id = index+1 #adding id as an ordered index number after looping through task_l
          #this is so that the user doesnt have to manually add it, and id is ordered

    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "id":str(task_id), #turning into string
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False,
        
       
    }
    
    task_list.append(new_task)
    write_to_file()
    print("Task successfully added.")

###################################################

#3) view all the tasks
def view_all():
    
    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Task ID: \t {t['id']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)
        
#############################################       

#3) View user's specific task assigned to them
def view_mine():
    
    option = input('Would you like to choose a specific task? Yes/No or -1 to return to Main Menu: ')
    if option.lower() == 'yes':
        temp_id = input('Please enter the ID number: ') #getting the specific task by ID
        for t in task_list:
            if t['id'] == temp_id and t['username'] == curr_user:  #checking the id and username match
             disp_str = f"Task: \t\t {t['title']}\n"
             disp_str += f"ID Number: \t {t['id']}\n"
             disp_str += f"Assigned to: \t {t['username']}\n"
             disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
             disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
             disp_str += f"Task Description: \n {t['description']}\n"
             print(disp_str) 
             complete_option = input('Would you like to mark this task as completed? Yes/No :') #giving the option to complete the task
             if complete_option.lower() == 'yes':
               t['completed'] = True
             edit_option = input('Would you like to edit you task? Yes/No: ')
             if edit_option.lower()=='yes': 
               t['due_date'] = datetime.strptime(input('What is the due date? YYYY-MM-DD '), DATETIME_STRING_FORMAT) #keeping the date format
               t['username'] = input('Who is this task assigned to? Please choose from established usernames ')    
               #editing only the username and due date
        write_to_file() #see above function for writing to file
        print("Task successfully edited.")     
    elif option.lower()=='no':
        for t in task_list:
            if t['username']==curr_user:
             disp_str = f"Task: \t\t {t['title']}\n"
             disp_str += f"ID Number: \t {t['id']}\n"
             disp_str += f"Assigned to: \t {t['username']}\n"
             disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
             disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
             disp_str += f"Task Description: \n {t['description']}\n"
             print(disp_str) 
    elif option =='-1': #return option to main menu
        return     
    
    
   


#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

#Getting User_List
user_list = username_password.keys() #getting the list of users from user.txt file

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        reg_user()

    elif menu == 'a':
        '''Allow a user to add a new task to task.txt file
            Prompt a user for the following: 
             - A username of the person whom the task is assigned to,
             - A title of a task,
             - A description of the task and 
             - the due date of the task.'''
        add_task()


    elif menu == 'va':
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling) 
        '''

        view_all()    


    elif menu == 'vm':
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling)
        '''
        view_mine()
                
    
    elif menu == 'ds' and curr_user == 'admin': 
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
            
        with open("user.txt", 'a+') as user_file_admin: #a+ will let you read files without destroying original and create them if they don't yet exist 
            user_file_admin.seek(0)
            user_data_lines = user_file_admin.readlines()  #each line is a new user
        
        num_users = len(user_data_lines)
        
        with open("tasks.txt", 'a+') as task_file_admin:
            task_file_admin.seek(0)
            task_data_lines = task_file_admin.readlines()  #each line is a new task
        num_tasks = len(task_data_lines)

        print("-----------------------------------")
        print(f"Total number of users: \t\t {num_users}")
        print(f"Total number of tasks: \t\t {num_tasks}")
        print("-----------------------------------")    

    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    elif menu == 'gr':
        count_complete = 0
        count_overdue = 0
        with open("task_overview.txt", "w") as task_overview_file:
            task_overview_to_write = []
            for t in task_list: #calculating tasks and dates
                if t['completed'] == True: #completed tasks
                    count_complete = count_complete+1     
                if datetime.now() > t['due_date'] and t['completed'] == 'No': #if the date is overdue and task incomplete
                    count_overdue = count_overdue+1  
            task_overview_to_write.append(f'Amount of tasks generated;{len(task_list)}') #tasks generated
            task_overview_to_write.append(f'Tasks completed;{str(count_complete)}') #completed tasks
            task_overview_to_write.append(f'Incomplete tasks;{str(len(task_list)-count_complete)}') #incomplete tasks
            task_overview_to_write.append(f'Incomplete overdue tasks;{str(count_overdue)}')
            task_overview_to_write.append(f'Percentage of incomplete tasks;{str((len(task_list)-count_complete)/len(task_list)*100)}')
            task_overview_to_write.append(f'Percentage of overdue incomplete tasks;{str(count_overdue/len(task_list)*100)}') #percentage of incomplete tasks
       
            task_overview_file.write("\n".join(task_overview_to_write))
        with open('user_overview.txt', "w") as user_overview_file:
            user_overview_to_write =[]
            user_line_count =0
            with open("user.txt", 'r') as user_file: #reopening user.txt to read the file line by line
                for line in user_file: #user_file is the file open at top of login section for users.
                    user_line_count +=1  #each line represents a new user
            user_overview_to_write.append(f'Amount of users registerd;{str(user_line_count)}')
            user_overview_to_write.append(f'Amount of tasks generated;{str(len(task_list))}')
            for user in user_list: #getting every user from user_list and matching to task_list. user_list at line 223
                user_task_count =0
                user_completed_count =0
                count_user_overdue =0
                for t in task_list: 
                    if user == t['username']: #matching username from user_data file to username in task list object
                        user_task_count+=1
                    if user == t['username'] and t['completed'] == True:  #condition for calculating completed tasks for specific user
                        user_completed_count+=1  
                    if user == t['username'] and datetime.now() > t['due_date'] and t['completed'] == 'No':   
                        count_user_overdue+=1 
                user_overview_to_write.append(f'Number of tasks assigned to {user};{str(user_task_count)}')      
                user_overview_to_write.append(f'Overall percentage of tasks assigned to {user};{str((user_task_count/len(task_list))*100)}')
                
                if user_task_count!=0:  #avoiding a divison by 0 Error      
                    assigned_tasks_percentage_complete = (user_completed_count/user_task_count)*100
                    assigned_tasks_percentage_incomplete = (user_task_count-user_completed_count)/user_task_count*100
                    assigned_tasks_percentage_incomplete_overdue = (count_user_overdue/user_task_count)*100
                else:
                    assigned_tasks_percentage_complete =0
                    assigned_tasks_percentage_incomplete =0
                    assigned_tasks_percentage_incomplete_overdue =0
                        
                user_overview_to_write.append(f'Percentage of the assigned tasks to "{user}" that have been COMPLETED;{str(assigned_tasks_percentage_complete)}') #Percentage of tasks specific to the user, not overall task number
                user_overview_to_write.append(f'Percentage of the assigned tasks to "{user}" that are INCOMPLETE;{str(assigned_tasks_percentage_incomplete)}')#percentage of tasks specific to user
                user_overview_to_write.append(f'Percentage of the assigned tasks to "{user}" that are INCOMPLETE and OVERDUE;{str(assigned_tasks_percentage_incomplete_overdue)}')
            user_overview_file.write("\n".join(user_overview_to_write))    
    else:
        print("You have made a wrong choice, Please Try again")
       
        
 