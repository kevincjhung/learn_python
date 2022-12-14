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

# https://www.youtube.com/watch?v=HGOBQPFzWKo&t=2725s