# write a program of factorial using recursive function 
def fact(n):
   if n == 1:
       return 1
   else:
       return n*fact(n-1)
num = int(input("enter the number:"))
if num < 0:
   print("factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", fact(num))

