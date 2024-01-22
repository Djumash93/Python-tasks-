#I will create a programme to read awards by calculating times in minutes
#Therefor minutes should be a numerical value ie an integer, as a float would add confusion
#It is possible to make a float but then we would have to multiply the value by 60 and measure in seconds
#which is not what we want. 

swimming_time_minutes = int(input('Enter the swimming time in minutes: '))
cycling_time_minutes = int(input('Enter the cycling time in minutes: '))
running_time_minutes = int(input('Enter the running time in minutes: '))

triathlon_total = swimming_time_minutes + cycling_time_minutes + running_time_minutes

if triathlon_total >=111:
    print('No award')
elif triathlon_total>=106:    
    print('Provincial Scroll')
elif triathlon_total >=101:
    print('Provincial Half Colours')
elif triathlon_total<=100:
    print('Provincial Colours')        