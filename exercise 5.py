# store the days of the month 
def days_in_month():
    month_days={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

    # input the month number 
    month=int(input("enter a month number (1-12):"))

    # create a condition that will operate if it is a leap year 
    if month==2:
       leap_year=input("is it is a leap year? (yes/no):").strip().lower()
       print("days in month:", 29 if leap_year=="yes" else 28)

     # if it is not true, add another condition 
    elif month in month_days:  
        print("days in month:",month_days[month])
    # if it is not true then print 
    else:
        print("invalid month number") 