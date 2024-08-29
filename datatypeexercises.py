#STRINGS
#Given the string 'hello' give an index command that returns 'e'. 

s = 'hello'
print(s[1])

#Reverse the string 'hello' using slicing:

print(s[::-1])

#Given the string hello, give two methods of producing the letter 'o' using indexing

print(s[-1])
print(s[4])

#LISTS
#Build this list [0,0,0] two separate ways

mylist = [0,0,0]
print(mylist)

print([0] * 3)

#Reassign 'hello' in this nested list to say 'goodbye' instead

mylist1 = [1,2,[3,4,'hello']]
mylist1[2][2] = 'goodbye'
print(mylist1)

#Sort the list below:

list1 = [5,3,4,6,1]
print(sorted(list1))

#DICTIONARIES

#Using keys and indexing, grab the 'hello' from the following dictionaries
d = {'simple_key':'hello'}
print(d['simple_key'])
d1 = {'k1':{'k2':'hello'}}
print(d1['k1']['k2'])
d2 =  {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d2['k1'][0]['nest_key'][1][0])
d3 = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d3['k1'][2]['k2'][1]['tough'][2][0])