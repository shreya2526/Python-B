
def checkleapyear(y): 
 return(((y % 4 == 0) and (y % 100 != 0)) or (y % 400 ==0));

#The above line Returns true if the year is a multiple of 4 and not a multiple of 100 OR the year is a multiple of 400 as mentioned per the syntax logic above.

y= int(input('enter a year: '))
if (checkleapyear(y)):
 print("The given year is leap year") 
else: 
 print("The given year is not a leap year")
