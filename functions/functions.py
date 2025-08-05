# A function definition is an executable statement. Its execution binds the function name in the current
# local namespace to a function object (a wrapper around the executable code for the function). This function
# object contains a reference to the current global namespace as the global namespace to be used when the function
# is called.
# https://docs.python.org/3/reference/compound_stmts.html#function

def myFirstFunction():
    """Function without parameters"""
    print("My first function without parameters and return value")


def printName(first_name, last_name):
    print(first_name + ' ' + last_name)


# If you do not know how many arguments that will be passed into your function, add a * before the
# parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:
def SetFirstNameKids(*kidsFName):
    print(type(kidsFName))
    print(len(kidsFName))
    print(kidsFName)


# If you do not know how many keyword arguments that will be passed into your function, add two
# asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly
def SetDataKids(**kidsData):
    print(kidsData['fname'] + kidsData['lname'] + str(kidsData['age']))


def LearnInnerFunction():
    num_a = 10
    num_b = 20

    def addNum(num_1, num_2):
        print(num_1 + num_2)

    addNum(num_a, num_b)
    addNum.type = 'int'
    print(type(addNum))
    print(type(addNum.type))
    return addNum.type


LearnInnerFunction.help = "Help"
LearnInnerFunction.Count = 5

if __name__ == '__main__':
    """Learning functions"""
    print(myFirstFunction.__doc__)
    myFirstFunction()
    printName("Stefan", "Scholz")
    SetFirstNameKids("Hannah", "Philipp", "Leah", "Annika")
    SetDataKids(fname="Hannah", lname="Fehler", age=4)
    print('Add :' + LearnInnerFunction())
    print(LearnInnerFunction.__class__)
    print(LearnInnerFunction.__dict__)
    print(dir(LearnInnerFunction))
