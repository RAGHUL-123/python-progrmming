num1=int(input("enter the starting value: "))
num2=int(input("enter the stop value: "))
sum=0
temp=num1
while num1<=num2:
    if num1%2==0:
        sum+=num1;
    num1+=1
print("the sum of %d to %d is %d" % (num2,temp,sum))