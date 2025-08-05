# https://datascientest.com/de/python-lambda-funktionen-vorteile-und-verwendung
# https://docs.python.org/3/reference/expressions.html#lambda

# Lambda arguments: expression

# Lambda and sum Function
def sum_classic(a, b):
    return a + b


sum_lambda = lambda a, b: a + b
print(sum_lambda(5, 10))


# Lambda and Map Function
def doubler(x):
    return x * 2


results_def = list(map(doubler, [1, 2, 3, 4, 5]))
print(results_def)
print(list(map(lambda x: x * 2, [1, 2, 3, 4, 5])))


# Lambda and Filter Function
def est_pair(x):
    return x % 2 == 0


results_def = list(filter(est_pair, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(results_def)
print(list(filter(lambda x: x%2==0, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# Lambda and sorted function
def clee_tri(tuple):
    return tuple[1]
tuples = [(1, 5), (3, 2), (8, 10), (4, 7)]
results_def = sorted(tuples, key=clee_tri)
print(results_def)
print(sorted([(1, 5), (3, 2), (8, 10), (4, 7)], key=lambda x:x[1]))
