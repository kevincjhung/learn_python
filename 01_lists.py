# lists are ordered, mutable and allowed for duplicate values
mylist = ['dog', 'cat', 'mouse', 'dog']


# can also do it this way
list2 = list()
list2.append('dog') # append this way


# lists can have different data types
list3 = [12, 'a', 0.03424, True, ]


# accessing different elements
a = list3[2]


# iterating through an array 
for i in mylist:
    print(i)


# iterating through a string
for x in "banana":
    print(x)


# for loop, set number of times, this prints 0 to 5
for x in range(5):
    print(x)


# else in for loop. Will not be executed if the loop is stopped by a break statement
for x in range(6):
  print(x)
else:
  print("Finally finished!")


# nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

    