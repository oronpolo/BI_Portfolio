#Merge two lists using the following condition
#Given two lists of numbers, write a Python code to create a new list such that the latest list should contain odd numbers from the first list and even numbers from the second list.

list1 = [5,4,3,2,1]
list2 = [6,7,8,9,10]
list3 = []

for i in range (len(list1)):
    if (list1[i] % 2 == 1):
        list3.append(list1[i])

for i in range (len(list2)):
    if (list2[i] % 2 == 0):
        list3.append(list2[i])

list3.sort()
print(list3)
