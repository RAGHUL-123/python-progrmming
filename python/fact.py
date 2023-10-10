num=7
fact=1
num
if num<0:
     print("the factorial does not exists for negagive number")
elif num==0:
     print("the factorial of 0 is 1")
else:
    for i in range(1, num + 1):
       fact = fact * i
       print("the  factorial of", num, "is", fact)