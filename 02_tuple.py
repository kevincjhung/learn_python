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