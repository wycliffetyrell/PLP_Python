# created an empty list
my_list=[]

# Appending numbers in the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# inserting 15 in the second position in the list
my_list.insert(1,15)

# extending
a = [50,60,70]
my_list.extend(a)

# Removing last element
del my_list[-1]

# sorting in ascending
my_list.sort()

# index of 30
index_30 = my_list.index(30)
print(index_30)
