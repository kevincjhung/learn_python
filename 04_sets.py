# sets unordered and mutable. they do no allow for duplicates
# they are declared with curly braces, single value pairs separated by a comma
# python will automatically sort the contents and remove duplicates
# you can put a tuple inside a set, but not dictionaries and lists

# declaring a set
set1 = {1,2,4,5,'airplane', (1,2,4), True, 3, 3}
print(set1)


# you can use the set() and pass in a list
myset = set([1,2,3])
print(myset)


# passing a string into set() will return a set with individual char
myset = set('hello world')
print(myset)



# creating an empty set
myset = set()


# adding things to a set
myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
myset.add(4)
myset.add(5)

print(myset)



# removing things from a set, if you try to remove an item that does not exist
# it will throw an error
myset.remove(5)
print(myset)


# remove element, if element does not exist, nothing happens
myset.discard(4)


# iterate through a set
for i in myset:
    print(i)

# check if an element is inside a set
if i in myset:
    print('yes')


# Union and intersection
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

# union combines both without duplication
u = odds.union(evens)
print(u)

# intersection 
i = odds.intersection(evens)

