#Use for, .split(), and if to create a Statement that will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'

for word in st.split():
    if word[0] == 's':
        print(word)


#Use range() to print all the even numbers from 0 to 10.
print(list(range(0,11,2)))
#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3
print([x for x in range(1,51) if x%3 == 0])
#Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
for x in st.split():
    if len(x) % 2 == 0:
        print(x + ' even')

#FizzBuzz 1 to 100

for x in range(1,100):
    if x%3 == 0 and x%5 == 0:
        print('FizzBuzz')
    elif x%3 == 0:
        print('Fizz')
    elif x%5 == 0:
        print('Buzz')
    else:
        print(x)

#Use List Comprehension to create a list of the first letters of every word in the string below
st = 'Create a list of the first letters of every word in this string'
print(word[0] for word in st.split())