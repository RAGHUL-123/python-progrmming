year=int(input("enter the year: "))
if year%4==0:
    print("its leap year")
elif year%100==0:
    print("it is not a leap year")
elif year%400==0:
    print("it leap year")
else:
    print("it is not a leap year")