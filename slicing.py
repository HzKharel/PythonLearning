my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1
# You can use positive or negative index ie my_list[9] and my_list[-1] return the same value
# You can also use a range of index, in this format list[start (inclusive):end (non-inclusive): step]
# The step can also go in the negative direction

print(my_list[0::2])

##### String Slicing
sample = 'This is a simple string'
print(sample)

# Reversed string
print(sample[::-1])

#Reversing the words
words = sample.split(' ') #Using space as a break point
print(' '.join(words[-1::-1]))
