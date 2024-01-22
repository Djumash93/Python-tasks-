#calculating a user's total holiday cost
city_flight = str(input('Which city will you be flying to? : '))
num_nights = int(input('How many nights will you stay at the hotel? please enter a number: '))
rental_days = int(input('How many days will you hire a car for? Enter a number: '))

def hotel_cost(num_nights = num_nights ): #giving the parameter the same name as the function which I set as a default value
    hotel_price = 75
    total_price = num_nights*hotel_price
    return total_price

def plane_cost( city = city_flight.lower()): #to lower case so that cases in the input don't cause a logic bug
    if city == 'barcelona':
        flight_price = 100
    elif city == 'london':
         flight_price = 200
    elif city == 'new york':
        flight_price =300      
    else:
        flight_price =  50
    
    return flight_price

def car_rental(rent_days = rental_days): 
    daily_cost = 50
    total_cost = daily_cost*rent_days
    return total_cost

def holiday_cost(hotel_cost = hotel_cost, plane_cost = plane_cost, car_rental = car_rental):
    total_cost = hotel_cost()+plane_cost()+car_rental() #invoking all default values for the functions from before 
    return total_cost
       
print(f'The total cost for the hotel is £{hotel_cost()}. The flight was £{plane_cost()} each way.')
print(f'The car cost £{car_rental()} for {rental_days} days and the total cost of the holiday is £{holiday_cost()}.')
# two print functions instead of \n to keep the code tidy