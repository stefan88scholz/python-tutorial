from enum import Enum

class Weekdays(Enum):
    MONDAY = 'Monday'
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

print(f'type(Weekdays): {type(Weekdays)}')
print(f'type(Weekdays.MONDAY): {type(Weekdays.MONDAY)}')
print(f'Weekdays.MONDAY: {Weekdays.MONDAY}')
print(f'Weekdays.MONDAY.name: {Weekdays.MONDAY.name}')
print(f'Weekdays.MONDAY.value: {Weekdays.MONDAY.value}')
print(f'Weekdays(\'Monday\'): {Weekdays('Monday')}')
print(f'Weekdays.TUESDAY.name: {Weekdays.TUESDAY.name}')
print(f'Weekdays.TUESDAY.value: {Weekdays.TUESDAY.value}')
print(f'Weekdays(2): {Weekdays(2)}')
print(f'Weekdays.TUESDAY.__repr__(): {Weekdays.TUESDAY.__repr__()}')


