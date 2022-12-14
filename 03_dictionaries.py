# Dictionaries are key-value pairs, unordered and mutable

# Declaring dictionaries
myDict = {
    "name": "max",
    "age": 27,
    "city": "Berlin"
}
print(myDict)


# If you use the dict() you do not need the quotes around the key name
dict2 = dict(
    name = "John", 
    age = 25,
    city = "Amsterdam"
)


# getting the value using the key
city = dict2["city"]
print(city)


# Changing the value of a key
dict2["city"] = "Milan"
print(dict2)


# this works in js, but is not valid in python
# When you use dot notation, you indicate to Python that you want to either 
# run a particular operation on, or to access a particular property of, an object type.
donotdothis = ' dict2.city = "genoa" '


# Delete an item from dict
del dict2['city']
print(dict2)


# or you can use the pop method

mydict = {
    "name": "Sam",
    "age": 27,
    "city": "Berlin"
}


dict2.pop('name')
print(dict2)


# popitem()
# before python 3.7, this removes random pair
# 3.7 and after, this removes last inserted item
mydict.popitem() 


# Check if a key is inside a dict
if "name" in mydict:
    print(mydict["name"])
else:
    print('not in dict')


# try/except statements 
try:
    print(mydict["name"])
except:
    print('error')


# looping through a dictionary
for key in mydict:
    print(key)


# or you can do this
# the keys method returns a list with all the keys inside
for key in mydict.keys(): 
    print(key)


