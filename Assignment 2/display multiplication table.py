numtable = int(input("Enter the number whose multiplication table you want to display: "))

for i in range(1, 11):
   print(numtable, 'x', i, '=', numtable*i)