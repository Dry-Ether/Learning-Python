'''count=1
while count<=10:
    print(count)
    count+=1
    print("Hi")
    if count==7:
        break
    
print("Out of Loop")'''


'''list1=["hi","hello","welcome"]
names=["krisna","Ram","Madhav"]
for item in list1:
    for name in names:
        print(item,name)
        if item=="hello" and name=="Ram":
            break
    print("out of inner loop")
print("out from outer loop")'''

'''list1=["hi","hello","welcome"]
names=["krisna","Ram","Madhav"]
for item in list1:
    for name in names:
        
        if item=="hello" and name=="Ram":
            continue
        print(item,name)
    print("out of inner loop")
print("out from outer loop")'''

for i in range(1,11):
    pass