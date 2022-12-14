import sys

# a tuple is a collection data type that is ordered and immutable
# often used for objects that belong together

# declaration 
myTuple = ('max', 28, 'boston')
print(myTuple)


# the parentheses are optional, this is also valid
myTuple = 'max', 28, 'boston'


# this is not a tuple
mytuple = ('max')


# this is how you write a tuple of 1
mytuple = ('max',)


# turning a list into a tuple 
mytuple = tuple(['max', 28, 'boston'])


# you can access an element in a tuple by index
# negative indices start from the end
item = myTuple[1]


# iterate through tuple
for i in mytuple:
    print(i)


# check if something is inside a tuple
if 'max' in myTuple:
    print('yes')
else:
    print('no')

# get the length of a tuple
print(len(myTuple))


# count how many of a thing there is
myTuple = ('a', 'b', 'c')
print(myTuple.count('a'))


# get the index of the first occurence
print(myTuple.index('a'))


# convert a tuple to and from a list
myList = list(myTuple)
print(myList)

myTuple2 = tuple(myList)
print(myTuple2)


# Slicing a tuple
a  = (1,2,3,4,5,6,7,8,9,10)
b = a[2:5]
print(b) # last index is not included


# step argument
a  = (1,2,3,4,5,6,7,8,9,10)
b = a[2::2] # takes every second element


# reverse a tuple
a  = (1,2,3,4,5,6,7,8,9,10)
b = a[::-1]

print(b)


# unpacking, aka destructuring. 
myTuple = "max", 28, 'Boston'

name, age, city = myTuple # must have the correct number of variables
print(name, age, city)

myTuple = (0,1,2,3,4)

i1, *i2, i3  = myTuple
print(i1)
print(i2) # all elements in between 
print(i3)


# comparisons between a tuple and a list
# because a tuple is unmutable, python can do some optimizations 
# that make it more efficient than a list
# tuples take less space and take less time to iterate through

my_list = [0,1,2,'hello', True]
my_tuple = (0,1,2,'hello', True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")



import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]"),  number=1000000)
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)"),  number=1000000)

