number=int(input("Enter your number: "))
prime=True
for i in range(2,number-1):
    a=number%i
    i+=1
    if a==0:
        prime=False
        break

if number<2:
    print("Enter a number geater than 1")
elif prime==False:
    print("The number is not a prime number")
else:
    print("The number is prime number")