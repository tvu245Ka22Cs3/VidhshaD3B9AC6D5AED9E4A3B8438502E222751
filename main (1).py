#1.1 implement a recursion function to calculate the factorial of a given number
def factorial(n):
  if n == 0:
    return 1
  return n * factorial(n - 1)


num = 5
print("Factorial of", num, "is", factorial(num))
# leap year
print("enter the year:")
y = int(input())
if y % 4 == 0 and y % 100 != 0:
  print("/n it is a leap year")
elif y % 400 == 0:
  print("/n it is a leap year")
else:
  print("/n it is not a leap year")
