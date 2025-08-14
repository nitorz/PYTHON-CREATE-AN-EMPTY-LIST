# Create an empty list
my_list = []
my_list += [10, 20, 30, 40]
my_list.insert(1, 15)
my_list.extend([50, 60, 70])
my_list.pop()
my_list.sort()
print("Final list:", my_list)
print("Index of 30:", my_list.index(30))
