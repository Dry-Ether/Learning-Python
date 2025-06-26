#method 1
import random
l=["Heads","Tails"]
a=random.choice(l)
print(a)
#method 2
a=random.randint(0,1)
if a==0:
    print("heads")
else:
    print("tails")
