# https://docs.python.org/3/tutorial/classes.html
# https://www.w3schools.com/python/python_classes.asp
# https://www.w3schools.com/python/python_polymorphism.asp

class City:
    def __init__(self, name: str, country: str) -> None:
        self.name: str = name
        self.country: str = country

    def __str__(self) -> str:
        ret_str = f'Name of the city: {self.name} \nCountry of the city: {self.country}'
        return ret_str

    def __repr__(self) -> str:
        return f'{self.name} ({self.country})'

    def __format__(self, format_spec: str) -> str:
        match format_spec:
            case '!s':
                return self.__str__()
            case '!r':
                return self.__repr__()
            case '!a':
                return ascii(self.__repr__())
            case _:
                return super().__format__(format_spec)


    def __eq__(self, other) -> bool:
        return self.name == other.name and self.country == other.country

def str_and_repr() -> None:
    """
    1. Class does not define function __str__ nor __repr__
       -> __str__ returns None
       -> --repr__ return None
    2. Class defines __str__ but not __repr__
       -> __str__ returns result of __str__
       -> __repr__ returns string representation of the object
    3. Class defines no __str__ but __repr__
      -> __str__ returns result of __repr__ as built-in object implementation calls __repr__
      -> __repr__ returns result of __repr__
    4. Class defines __str__ and __repr__
      -> __str__ returns result of __str__
      -> __repr__ returns result of __repr__
    :return: None
    """
    munich = City(name='Munich', country='Germany')
    print(munich.__str__())
    print(City.__str__(munich))
    print(munich.__repr__())

def main() -> None:
    str_and_repr()

if __name__ == '__main__':
    main()
