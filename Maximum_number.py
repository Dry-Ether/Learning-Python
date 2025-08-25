number= input("Enter list of number:")
number_list=number.split()
count=0
for numbers in number_list:
    count+=1
print(f"The length of the list is: {count}")
for i in range(count):
    number_list[i]=int(number_list[i])
maximum_number=number_list[0]
for a in number_list:
    if a>maximum_number:
        maximum_number=a
print(f"The Maximum number is:{maximum_number}")