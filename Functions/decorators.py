# https://book.pythontips.com/en/latest/decorators.html
# 7.1. Everything in Python is an object
def hi(fname = "Stefan"):
    print(f'Hello {fname}')
    print('Hello {first_name}'.format(first_name=fname))

print('01 --------------------------------')
print(hi)
hi()
print('02 --------------------------------')
greet = hi
print(greet)
greet()
print('03 --------------------------------')
del hi
# print(hi()) NameError: name 'hi' is not defined
print('04 --------------------------------')
print(greet)
greet()

del greet

# 7.2. Defining functions within functions:
print('05 --------------------------------')
def hi(fname = "Stefan"):
    print('You are inside function hi')
    print(f'Hello {fname}')

    def greet():
        print('You are in function greet')

    def welcome():
        print('You are in function welcome')

    greet()
    welcome()
    print('Now you are back in function hi')

hi()
#greet() #NameError. name 'greet is not defined. Outside namespace
del hi

# 7.3. Returning functions from within functions
print('06 --------------------------------')
def hi(name="Stefan"):
    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    if name == "Stefan":
        return greet
    else:
        return welcome

a = hi()
print(a)

#This clearly shows that `a` now points to the greet() function in hi()
#Now try this
print(a())
#outputs: now you are in the greet() function

# 7.4. Giving a function as an argument to another function
print('07 --------------------------------')
def hi():
    return "Hi Stefan!"

def doSomethingBeforeHi(func):
    print("I am doing some boring work before executing hi()")
    print(func())

doSomethingBeforeHi(hi)

# 7.5. Writing your first decorator:
print('08 --------------------------------')
def a_new_decorator(a_func):

    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")

        a_func()

        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction

def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")

print(a_function_requiring_decoration)
a_function_requiring_decoration()
#outputs: "I am the function which needs some decoration to remove my foul smell"

a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
#now a_function_requiring_decoration is wrapped by wrapTheFunction()
print('09 --------------------------------')
print(a_function_requiring_decoration)
a_function_requiring_decoration()
#outputs:I am doing some boring work before executing a_func()
#        I am the function which needs some decoration to remove my foul smell
#        I am doing some boring work after executing a_func()
print('10 --------------------------------')
@a_new_decorator
def a_second_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")

a_second_function_requiring_decoration()
print(a_second_function_requiring_decoration.__name__)
del a_new_decorator
del a_function_requiring_decoration
del a_second_function_requiring_decoration

print('11 --------------------------------')
from functools import wraps
def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")
    return wrapTheFunction

@a_new_decorator
def a_function_requiring_decoration():
    """Hey yo! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")

print(a_function_requiring_decoration.__name__)
# Output: a_function_requiring_decoration
del a_new_decorator
del a_function_requiring_decoration
print('12 --------------------------------')
from functools import wraps
def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)
    return decorated

@decorator_name
def func():
    return("Function is running")

can_run = True
print(func())
print(func)
print(func.__name__)
# Output: Function is running

can_run = False
print(func())
# Output: Function will not run


# Logging
print('13 --------------------------------')
from functools import wraps

def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logit
def addition_func(x):
   """Do some math."""
   return x + x


result = addition_func(4)
print(result)
# Output: addition_func was called

# 7.6.1. Nesting a Decorator Within a Function
print('14 --------------------------------')
from functools import wraps

def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # Open the logfile and append
            with open(logfile, 'a') as opened_file:
                # Now we log to the specified logfile
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)
        return wrapped_function
    return logging_decorator

@logit()
def myfunc1():
    pass

myfunc1()
# Output: myfunc1 was called
# A file called out.log now exists, with the above string

@logit(logfile='func2.log')
def myfunc2():
    pass

myfunc2()
# Output: myfunc2 was called
# A file called func2.log now exists, with the above string

print('15--------------------------------')
class logit(object):

    _logfile = 'out.log'

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        log_string = self.func.__name__ + " was called"
        print(log_string)
        # Open the logfile and append
        with open(self._logfile, 'a') as opened_file:
            # Now we log to the specified logfile
            opened_file.write(log_string + '\n')
        # Now, send a notification
        self.notify()

        # return base func
        return self.func(*args)

    def notify(self):
        # logit only logs, no more
        pass

logit._logfile = 'out2.log' # if change log file
@logit
def myfunc1():
    pass

myfunc1()
# Output: myfunc1 was called





