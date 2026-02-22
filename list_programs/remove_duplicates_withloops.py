# Remove duplicates using loop

lst =[1,1,1,2,2,4,4,5,5,8,9,7,3,3]
new_list = []
for i in lst:
    if i not in new_list:
        new_list.append(i)
print("orginal list: ",lst)
print("List without duplicates:", new_list)