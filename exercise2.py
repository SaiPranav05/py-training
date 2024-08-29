#number of strings where len>2

input_strings = ['abc','aba','aa','bab','bb']
count = 0
for s in input_strings:
    if len(s) > 2:
        count += 1
print(count)
