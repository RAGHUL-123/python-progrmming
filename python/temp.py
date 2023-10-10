celsius=float(input("enter the temperature in celsius: "))
fahrenheit=(celsius*9/5)+32
print(f"temperature in celsius:{celsius}")
print(f"temperature in fahrenheit:{fahrenheit}")
if celsius>30:
    print("it is hot")
elif celsius<=20 and celsius<=30:
    print("it is modrate")