import math
a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
operation=input("enter the operation(add,sub,mul,div):")
if operation=="add":
    result=a+b
elif operation=="sub":
       result=a-b
elif  operation=="mul":
      result=a*b
elif operation=="div":
     result=a/b
else:
    print("invalid number")
print("result ",result)