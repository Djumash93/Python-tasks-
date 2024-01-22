import math

###### FOR HYPERION DEV
# The task target has changed since I have submitted it. Originally there were no bonds involved, only interest
# 

finance_type = str(input(
    'investment - to calculate the amount of interest you\'ll earn on your investment\n'
    'bond - to calculate the amount you\'ll have to pay on a home loan\n'
    'Enter either \'investment\' or \'bond\' from the menu above to proceed: '
))



#############################INVESTMENT##################
#Let's get the amount on which the interest accrues
#This is followed by type of interest. Compound interest or simple interest
#Also lets keep in mind the compound interest formula A(1+rate/100)**time


if finance_type.lower() == 'investment':
   interest_type = input('Which type of interest is it? Choose between Simple or Compound interest: ')
   initial_amount_invested = float(input('What is the initial amount invested?: '))
   investment_length = float(input('What is the length of your investment term in years?: '))
   investment_rate = float(input('What is the investment percentage rate?: '))
   if "simple" in interest_type.lower():
      final_amount = initial_amount_invested + (initial_amount_invested/100*investment_rate*investment_length)
      print('________________')
      print(f"Investment Type: Simple Interest")
      print(f"Initial Deposit: {initial_amount_invested}")
      print(f"Investment length: {investment_length}")
      print(f"Investment rate in percentage: {investment_rate}")
      print(f"Amount after {investment_length} years: {round(final_amount,2)}")
      print('________________')
   elif "compound" in interest_type.lower():
      final_amount = initial_amount_invested*(1+(investment_rate/100))**(investment_length)
    #using math.pow would be: 
    #final_amount = initial_amount_invested*math.pow((1+(investment_rate/100)), investment_length)
      print('________________')
      print(f"Investment Type: Compound Interest")
      print(f"Initial Deposit: {initial_amount_invested}")
      print(f"Investment length: {investment_length}")
      print(f"Investment rate in percentage: {investment_rate}")
      print(f"Amount after {investment_length} years: {round(final_amount,2)}")
      print('________________')   
   else :    
      raise NameError('Please choose between "compound" or "simple" interest types')

######################BOND###################
elif finance_type.lower()=='bond':
    house_value = int(input('What is the value of the house? '))
    interest_rate = int(input('What is the interest rate?'))
    length_in_months = int(input('The number of months it will take you to repay the loan?'))
   #####final answer####
   ###formula: repayment = (i*P)/(1-(1+i)**(-n)). i = interest_rate/100/12
    repayment = ((interest_rate/100/12)*house_value)/(1-(1+(interest_rate/100/12))**(-length_in_months))
    print('___________BOND___________')
    print(f'House value: £{house_value}') 
    print(f'Interest rate: {interest_rate}%')
    print(f'Length in months: {length_in_months} months ') 
    print(f'Monthly repayment: £{round(repayment)} per month')  
    print('___________________________')
else:
    print('Please choose between \'investment\' or \'bond\' options')
    