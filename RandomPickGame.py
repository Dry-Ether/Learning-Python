import random
a=input("Enter each name with space:")
split=a.split(" ")
print(split)
length=len(split)
b=random.randint(0,length-1)
print(split[b])