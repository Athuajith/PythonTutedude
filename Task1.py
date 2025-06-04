n=int(input("Enter a number:"))
def factorial(n):
   if n < 0:
     return "Entered number is negative"
   elif n < 2:
       return 1
   else:
      return  n * (factorial(n - 1))

result=factorial(n)

print(f"Factorial of {n} is: {result}")
