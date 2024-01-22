# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program") #adding parentheses
print ("\n") #indentation correction and adding parentheses

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24" #indentation correction, getting rid of an equal sign as age_Str was not defined is not a parameter in an if else statement. Leaving numbers and getting rid of fletters to turn into int
age = int(age_Str) #indentation correction
print(f"I'm {age} years old.") #indentation correction. leaving spaces. syntax correction for placing int within str 

    # Variables declaring additional years and printing the total years of age
years_from_now = "3" #indentation correction
total_years = age + int(years_from_now) #indentation correction. turning years_from_now value to int to make the addition and not concatenate strings

print (f"The total number of years: {total_years}"  ) #indentation correction plus parentheses. syntax correction. adding curly braces {}. variable name correction: total_years

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12 #variable name correction: total_years not total
print (f"In 3 years and 6 months, I'll be {total_months + 6} months old") #parentheses. Syntax. Adding 6 months (3 years and 6 months)

#HINT, 330 months is the correct answer

