# lists are ordered, mutable and allowed for duplicate values
mylist = ['dog', 'cat', 'mouse', 'dog', 'banana', 123423 ]


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


# check if an item is in a list
if "banana" in mylist:
    print('yes')
else:
    print('no')


# check length of a list
print(len(mylist))


# add something to a list
mylist.append('trees')


# remove the last item from a list
lastItem = mylist.pop()


# remove a specific element
# if value not in list, you will get a ValueError
item = mylist.remove('cat')


# remove everything from the list
mylist.clear()


# reverse the list
mylist.reverse()


# sort the list in place
mylist.sort()


# create a new sorted list
newList = sorted(mylist)


# create a new list with many of the same value
mylist = [0] * 5 


# append 2 lists
mylist = [1,2,3,4,5]
list2 = [10, 11, 12]

newList = mylist + list2


# slicing a list, get a part of a list. Last index is excluded
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = mylist [1:5]
print(a) # prints [2, 3, 4, 5]


# from beginning to 5
a = mylist[:5]


# from 5 to end
a = mylist[5:]


# step index: take every 2nd, 3rd...etc item
a = mylist[::2]


# if you assign one var to another list, it will assign by reference. just like javascript
list_org = ['berlin', 'stockholm', 'nairobi']
list_copy = list_org

list_copy.append('tokyo')

print(list_org)
print(list_copy)


# to make a separate copy of the list
list_org = ['berlin', 'stockholm', 'nairobi']
list_copy = list_org.copy()


# option 2
list_copy = list(list_org)


# option 3
list_copy = list_org[:]


# list comprehension, create new list from existing list in 1 line
a = [ 1, 2, 3, 4, 5 ]
b = [ i * i for i in a ]



