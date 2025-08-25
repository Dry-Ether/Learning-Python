heights=input("enter all heights separated by comma:")
height_list=heights.split(',')
count=0
for height in height_list:
    count=count+1
print("Total Person:"+str(count))
for i in range(0,count):
    height_list[i]=int(height_list[i])

total=0
for person in height_list:
    total+=person
avg= total/count
print("Avarage height is:"+str(round(avg)))