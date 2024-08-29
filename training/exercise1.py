#program to print uniques values from a list

mylist = [1,4,7,2,1,4,6,7,2]
unique_list = set(mylist)
sorted_unique_list = sorted(unique_list)
print(sorted_unique_list)



#with out using built-in functions
mylist1 = [1,4,7,2,1,4,6,7,2]
unique_list1 = []  #to remove duplicates
for item in mylist1:
    if item not in unique_list1:
        unique_list1.append(item) #loop items and add to unique list from original list if already not present

n = len(unique_list1)
for i in range(n): #use bubble sort to sort the list
    for j in range(0, n - i - 1):
        if unique_list1[j] > unique_list1[j + 1]:
#swap if element is found greater than the next element
            unique_list1[j], unique_list1[j + 1] = unique_list1[j +1], unique_list1[j]
print(unique_list1)
print(len(unique_list1))