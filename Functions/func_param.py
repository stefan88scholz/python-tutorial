# Function with parameters
def AddNum(a, b):
    print(a + b)


AddNum(5, 6)


# Function with default parameters
def AddNum2(a=10, b=340):
    print(a + b)


AddNum2()
AddNum2(100)
AddNum2(b=100)


# Function expects two int as parameters but does not throw an error.
# If type check is necessary than buildin function isInstance needs to be used
def AddNum3(a: int = 10, b: int = 340):
    if not isinstance(a, int):
        print("Wrong parameter")
        return
    print(a + b)


AddNum3(4.5, 5.5)
print(AddNum3.__annotations__)


# Function with return parameter string
def FullName(fname: str = "Max", lname: str = "Mustermann") -> str:
    return fname + ' ' + lname


print(FullName('Stefan', 'Scholz'))
print(FullName.__annotations__)
