# 1. write program to takes two numbers as input from the user, and then handles the
# ZeroDivisionError. if the second number is zero. The code should provide a
# meaningful error message.

val=int(input("enter the 1st number: "))
try:
  val2=int(input("enter the 2nd number: "))
  result=val/val2
  print(f"result={result}")
except ZeroDivisionError:
    print("zero is not valid")
print("Better luck next time")
