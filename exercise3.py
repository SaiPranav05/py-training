#.Python program to print even length words in a string

s1 = 'Python program to print even length words in a string'

for word in s1.split():
    if len(word) % 2 == 0:
        print(word)

#Python program to create a list of tuples from given list having number and its cube in each tuple

num_list = [1,3,5,7,9]

cubes_list = [(num,num**3) for num in num_list]
print(cubes_list)

#.Python program to sort list of dictionaries by values in Python

employees = [{'name':'nikhil', 'salary':50000},{'name':'shiva', 'salary':70000},
             {'name':'chaitanya', 'salary':90000},{'name':'tejo', 'salary':80000}]
    #sorting based on salary
sorted_employees = sorted(employees,key =lambda x:x['salary'])
print(sorted_employees)

#To check if two lists have at least one element in common in Python
def have_common_element(list1, list2):
    # Convert lists to sets
    set1 = set(list1)
    set2 = set(list2)
    
    # Use isdisjoint to check if sets have no elements in common
    return not set1.isdisjoint(set2)

list1 = [1, 2, 3, 4]
list2 = [4, 5, 6, 7]

if have_common_element(list1, list2):
    print("Lists have at least one element in common.")
else:
    print("Lists do not have any elements in common.")

#.Write a Python program to multiplies all the items in a list.

def multiply_list_items(list):
    result = 1
    for item in list:
        result *= item
    return result
list = [1,2,3,4]
print( 'the product of items in list are:',multiply_list_items(list))

#Write a Python program to check whether a given key already exists in a dictionary

def key_exists(dictionary,key):
    return key in dictionary
mydict = {'name':'jhayanth', 'age':21, 'sal':100000 }
key_to_check = 'age'
if key_exists(mydict,key_to_check):
    print(f"The key '{key_to_check}' exists" )
else:
    print(f"The Key '{key_to_check}' does not exist")  

#.Write a Python program to print all distinct values in a dictionary

def get_unique_values(mydict1):
    unique_values = set()
    for dictionary in mydict1:
        for value in dictionary.values():
            unique_values.add(value)
    return unique_values  
data = [
    {"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
    {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
    {"VIII": "S007"}
]

unique_values = get_unique_values(data)

print("Unique Values:", unique_values)

#.Write a Python program to find the maximum and minimum values in a set
def find_max_min(values_set):
    if not values_set:  
        return None, None  
    
    maximum_value = max(values_set)
    minimum_value = min(values_set)
    
    return maximum_value, minimum_value

values_set = {3, 7, 1, 9, 5}

max_value, min_value = find_max_min(values_set)

if max_value is not None and min_value is not None:
    print("Maximum Value:", max_value)
    print("Minimum Value:", min_value)
else:
    print("The set is empty, no maximum or minimum values.")

#Write a Python program to find the two numbers whose product is maximum among all the pairs in a given list of numbers. Use the Python set.

def find_max_product_pair(numbers):
    if len(numbers) < 2:
        raise ValueError("List must contain at least two numbers")
    
    max_product = float('-inf')
    max_pair = (None, None)

    pairs = set()

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            pair = (numbers[i], numbers[j])
            if pair not in pairs:
                pairs.add(pair)
                product = numbers[i] * numbers[j]
                if product > max_product:
                    max_product = product
                    max_pair = pair
    return max_pair, max_product
numbers = [1,2,3,4,5]
pair, product = find_max_product_pair(numbers)
print(f"The pair with the maximum product is {pair} with a product of {product}.")