# Lists are mutable sequences, typically used to store collections of homogeneous items
# (where the precise degree of similarity will vary by application).
# https://docs.python.org/3/library/stdtypes.html#list


print('01 Create empty list using square brackets')
empty_list_01 = []
#print(empty_list_01)
print('---------------------------------------------------------')


print('02 Create a list using square brackets')
filled_list_01 = ['Januar', 'Februar', 'Maerz', 'April', 'Mai']
print(filled_list_01)
filled_list_02 = [0, 1, 2, 11, 22, 33, 44, 55, -1, -2, 5, 8]
print(filled_list_02)
print('---------------------------------------------------------')
print('02 Create a list comprehension')
obj_str = "Whether is great!"
compr_list_01 = [str(obj_str) for x in "12345"]
print(compr_list_01)
compr_list_02 = [str(6) for x in "12345"]
print(compr_list_02)



print('03 Use type constructor to create empty list: ')
empty_list_02 = list()
print(empty_list_02)
print('---------------------------------------------------------')



print('04 Type constructor with iterable list(iterable)')
print(list("12345"))
print(list([12,15,36]))
print('---------------------------------------------------------')



print('05 List implements all common sequence operations')
# https://docs.python.org/3/library/stdtypes.html#typesseq-common

print('(x in s) True if an item of s is equal to x, else False')
print('5 in filled_list_02: ', end="")
print(5 in filled_list_02)
print('5 in filled_list_01: ', end="")
print(5 in filled_list_01)
print('(x not in s) False if an item of s is equal to x, else True')
print('5 not in filled_list_02: ', end="")
print(5 not in filled_list_02)
print('5 not in filled_list_01: ', end="")
print(5 not in filled_list_01)
print('Concatenation of two strings: filled_list_01 + filled_list_02')
print(filled_list_01 + filled_list_02)
print('Adding list to itself n times: filled_list_03 = filled_list_02*4')
filled_list_03 = filled_list_02*4
print(filled_list_03)
print('Slice of s from i to j: filled_list_03[5:8]')
print(filled_list_03[5:8])
print('Sice of s from i to j with step k: filled_list_03[5:8:2]')
print(filled_list_03[5:20:2])
print('Length of list: len(filled_list_03)')
print(len(filled_list_03))
print('Smallest item of list: min(filled_list_03)')
print(min(filled_list_03))
print('Largest item of list: max(filled_list_03)')
print(max(filled_list_03))
print('Index of the first occurrence of x in list (at or after index i and before index j)')
print(filled_list_03.index(55))
print('Total number of occurrences of x in list')
print(filled_list_03.count(55))

print('---------------------------------------------------------')
# List implements all Mutable sequence operations
# https://docs.python.org/3/library/stdtypes.html#typesseq-mutable