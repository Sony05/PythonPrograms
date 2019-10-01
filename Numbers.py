# Python has "int" , "float", "complex" numeric types in Python.

#int
a = 1
b = 12345
c = -12345
print(type(a))
print(type(b))
print(type(c))

'''
float
'''
m = 2.8
n = -7.6
o = 9.0
p = 34e56
q = 3E45
r = -45.8e34
print(type(m))
print(type(n))
print(type(o))
print(type(p))
print(type(q))
print(type(r))

"""complex
"""
x = 6j
y = -4j
z = 2+4j

print(type(x))
print(type(y))
print(type(z))

d = complex(c)
print(type(d))

#Complex Numbers cannot be converted to any other type. This is wrong syntax
f = int(x)
