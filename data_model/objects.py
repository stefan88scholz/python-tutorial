# Objects are Python's abstraction for data. All data in a Python program is
# represented by objects or by relations between objects.
# https://docs.python.org/release/3.13.5/reference/datamodel.html
from numbers import Number
from types import NoneType

# Every object has an identity, a type and value. An object's identity (address) never changes once
# it has been created. The is operator compares the identity of two objects; the id() function returns
# an integer representing its identity.
obj_a = 5
obj_b = 'Hello'
obj_c = obj_a
print(obj_a is obj_a) #True
print(obj_a is obj_b) #False
print(obj_a is obj_c) #True
print('Identity of obj_a:' + hex(id(obj_a)).__str__())
print('Identity of obj_b:' + hex(id(obj_b)).__str__())
print('Identity of obj_b:' + hex(id(obj_c)).__str__())

# ++++++++++++++++++++++ #
# Type None ++++++++++++ #
# ++++++++++++++++++++++ #
# This type is a single value, there is a single object with this value. This object is access through the
# built-in name None. It is used to signify the absence of a value in many situations, e.g., it is returned
# from functions that don’t explicitly return anything. Its truth value is false.
obj_none = None
print(obj_none)
print(type(obj_none))
print('Is obj_none of type NoneType? ' + str(isinstance(obj_none,NoneType)))
print('------------------------------')
# ++++++++++++++++++++++++++++++++ #
# Type NotImplemented ++++++++++++ #
# ++++++++++++++++++++++++++++++++ #
# This type has a single value. There is a single object with this value. This object is accessed through
# the built-in name NotImplemented. Numeric methods and rich comparison methods should return this value
# if they do not implement the operation for the operands provided.
obj_notImplemented = NotImplemented
print(obj_notImplemented)
print(type(obj_notImplemented))
print('Is obj_notImplemented of type NonImplementedType? ' + str(isinstance(obj_notImplemented,type(obj_notImplemented))))
print('------------------------------')
# ++++++++++++++++++++++++++++++++ #
# Type Ellipsis ++++++++++++++++++ #
# ++++++++++++++++++++++++++++++++ #
# This type has a single value. There is a single object with this value. This object is accessed through
# the literal ... or the built-in name Ellipsis. Its truth value is true.
myList = [0,1,...,6]
print(myList)
obj_ellipsis = Ellipsis
print(obj_ellipsis)
print(type(obj_ellipsis))
print('Is obj_ellipsis of type ellipsis? ' + str(isinstance(obj_ellipsis,type(obj_ellipsis))))
print('------------------------------')
# ++++++++++++++++++++++++++++++++ #
# Type numbers.Number ++++++++++++ #
# ++++++++++++++++++++++++++++++++ #
#The root of the numeric hierarchy. If you just want to check if an argument x is a number, without caring
# what kind, use isinstance(x, Number).
obj_num = 5
print('Is obj_num of type Number? ' + str(isinstance(obj_num,Number)))
print('------------------------------')
# These are created by numeric literals and returned as results by arithmetic operators and arithmetic
# built-in functions. Numeric objects are immutable; once created their value never changes. Python numbers
# are of course strongly related to mathematical numbers, but subject to the limitations of numerical
# representation in computers.
# The string representations of the numeric classes, computed by __repr__() and __str__(), have the following
# properties:
# They are valid numeric literals which, when passed to their class constructor, produce an object having the
# value of the original numeric.
# The representation is in base 10, when possible.
# Leading zeros, possibly excepting a single zero before a decimal point, are not shown.
# Trailing zeros, possibly excepting a single zero after a decimal point, are not shown.
# A sign is shown only when the number is negative. #Python distinguishes between integers, floating-point numbers,
# and complex numbers:
obj_num2 = obj_num.__repr__()
print('obj_num2.__repr__(): ' + obj_num2.__str__())
print('Type of obj_num2: ' + str(type(obj_num2)))
print('------------------------------')
# ++++++++++++++++++++++++++++++++++ #
# Type numbers.Integral ++++++++++++ #
# ++++++++++++++++++++++++++++++++++ #
# These represent elements from the mathematical set of integers (positive and negative).
# There are two types of integers:
# Integers (int)
#    These represent numbers in an unlimited range, subject to available (virtual) memory only.
#    For the purpose of shift and mask operations, a binary representation is assumed, and negative
#    numbers are represented in a variant of 2’s complement which gives the illusion of an infinite string
#    of sign bits extending to the left.
# Booleans (bool)
#    These represent the truth values False and True. The two objects representing the values False and True
#    are the only Boolean objects. The Boolean type is a subtype of the integer type, and Boolean values behave
#    like the values 0 and 1, respectively, in almost all contexts, the exception being that when converted to a
#    string, the strings "False" or "True" are returned, respectively.
obj_integer = 10
print(obj_integer.__repr__())
print('Type of obj_integer: ' + str(type(obj_integer)))
obj_boolean = True
print(obj_boolean)
print('Type of obj_integer: ' + str(type(obj_boolean)))
print('Is obj_boolean of type Number? ' + str(isinstance(obj_num,Number)))
print('------------------------------')
# +++++++++++++++++++++++++++++++++++++ #
# Type numbers.Real(float) ++++++++++++ #
# +++++++++++++++++++++++++++++++++++++ #
# These represent machine-level double precision floating-point numbers.
obj_real = 3.456
print('Type of obj_real: ' + str(type(obj_real)))
print('Is obj_real of type Number? ' + str(isinstance(obj_real,Number)))
print('------------------------------')
# ++++++++++++++++++++++++++++++++++++++++++ #
# Type numbers.Complex(complex) ++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++ #
obj_complex01 = complex(4,5)
obj_complex02 = complex(3.456)
obj_complex03 = complex('-4.5j')
print(obj_complex01)
print(obj_complex02)
print(obj_complex03)
print(obj_complex03.real)
print(' --------------------------------------------------')
# ++++++++++++++++++++++++++++++++++++++++++ #
# Type Sequences +++++++++++++++++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++ #
# These represent finite ordered sets indexed by non-negative numbers. The built-in function len() returns the
# number of items of a sequence. When the length of a sequence is n, the index set contains the numbers 0, 1, …, n-1.
# Item i of sequence a is selected by a[i]. Some sequences, including built-in sequences, interpret negative
# subscripts by adding the sequence length. For example, a[-2] equals a[n-2], the second to last item of sequence
# a with length n.
# Sequences also support slicing: a[i:j] selects all items with index k such that i <= k < j. When used as an
# expression, a slice is a sequence of the same type. The comment above about negative indexes also applies to
# negative slice positions.
# Some sequences also support “extended slicing” with a third “step” parameter: a[i:j:k] selects all items of a
# with index x where x = i + n*k, n >= 0 and i <= x < j.
# Sequences are distinguished according to their mutability:
# Immutable sequences: Strings, Tuples, Bytes
# An object of an immutable sequence type cannot change once it is created

# Mutable sequences: Lists, Byte Arrays
print(' Mutable sequences: Lists')
# Lists are mutable sequences, typically used to store collections of homogeneous items
# (where the precise degree of similarity will vary by application).
obj_list_01 = [ -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
print('obj_list_01: ' + obj_list_01.__str__())
print('Length of obj_list_01: ' + len(obj_list_01).__str__())
print('obj_list_01[2]: ' + obj_list_01[2].__str__())
print('obj_list_01[2:3]: ' + obj_list_01[2:3].__str__())
print('obj_list_01[2:4]: ' + obj_list_01[2:4].__str__())
print('obj_list_01[3:9:1]: ' + obj_list_01[3:9:1].__str__())
print('obj_list_01[3:9:2]: ' + obj_list_01[3:9:2].__str__())
print('obj_list_01[-2]: ' + obj_list_01[-2].__str__())
print('list((1,2,3))' + list((1,2,3)).__str__())
obj_list_01.sort(reverse=True)
print(obj_list_01)
obj_list_01.sort(reverse=False)
print(obj_list_01)
obj_list_02 = ['Stefan', 'Beate', 'Hannah', 'Philipp']
obj_list_02.sort()
print('Sort by alphabet obj_list_02.sort(): ' + obj_list_02.__str__())
obj_list_02.sort(reverse=True)
print('Sort by alphabet reverse obj_list_02.sort(reverse=True): ' + obj_list_02.__str__())