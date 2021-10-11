import calendar 
print(">>>>>>>>>> Leap Year Calculator<<<<<<<<<<")
y1=int(input("enter first year: "))
y2=int(input("enter second yesr: "))
leaps=calendar.leapdays(y1,y2)
print("number of leap years between",y1,'and',y2,'is: ',leaps,'years')

year=int(input("enter the year to display: "))
print(calendar.prcal(year))
 
