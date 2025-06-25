name1=input("Enter Your Name:")
name2=input("Enter Your Partner Name:")

name3=(name1+name2)
name=name3.lower()

t= name.count('t')
r= name.count('r')
u= name.count('u')
e= name.count('e')

true = t+r+u+e

l= name.count('l')
o= name.count('o')
v= name.count('v')
e= name.count('e')

love = l+o+v+e

tl=int(str(true)+str(love))

if tl<10 or tl>90:
    print(f"Your love score is{tl}. you guys are made for each other")
elif tl<40 or tl>60:
    print(f"Your love score is {tl}.You are alright together")
else:
    print(f"Your love score is{tl}")