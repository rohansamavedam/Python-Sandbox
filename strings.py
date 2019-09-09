# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods
name = 'Rohan'
age = 20

#Concatenate
print('Hello I am ' + name + ' and I am ' + str(age))

# String Formatting

# Arguments by Position
print('{}, {}, {}'.format('a', 'b', 'c'))
print('{1}, {2}, {0}'.format('a', 'b', 'c'))

# Arguments by Name
print('My name is {name} and I am {age}'.format(name = name, age = age))

# F Strings only in Python 3.6+
print(f'My name is {name} and I am {age}')

# String Methods
s = 'hello there world'

# Make all upper
print(s.upper())

# Make all lower
print(s.lower())

# Get the length, same method also used for lists and dicts
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count 
sub = 'h'
print(s.count(sub))

# there are similar methods are there for spilt, starts with, ends with, is alpha numberic, is alphabhetic, is numeric.
