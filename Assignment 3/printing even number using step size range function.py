low=int(input("enter lower bound: ")) 
high = int(input("enter upper bound: "))

for num in range(low, high + 1):
 
 # checking condition
 if num % 2 == 0:
  print(num, end = " ")

