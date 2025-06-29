list1=[[1,1,1],[1,1,1],[1,1,1]]
print(f"{list1[0]}\n{list1[1]}\n{list1[2]}")
colum=int(input("Select a Colum Between 1-3:"))
row=int(input("Select a Row Between 1-3:"))
list1[colum-1][row-1]='x'
print(f"{list1[0]}\n{list1[1]}\n{list1[2]}")
