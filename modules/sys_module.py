import sys

def current_fn_name(parent_idx=0):
    # depth is 1 bc this is already a fn, so we need the caller
    return sys._getframe(1 + parent_idx).f_code.co_name

def userData(fname: str, lname: str, city: str, birthplace: str):
    print('----------------------------------------------------------------------------------------------------------')
    print(f'Inside function {current_fn_name()}')
    data = f'{fname} {lname} ; {city} ; {birthplace}'
    print(f'Value of sys._getframe(0) in function userData: {sys._getframe(0)}')
    print(f'Value of sys._getframe(1) in function userData: {sys._getframe(1)}')
    print('Function name: ' + current_fn_name())
    print(f'Function name of parent_idx=1 : {current_fn_name(1)}')
    print(f'Function name of parent_idx=2 : {current_fn_name(2)}')
    print('Function parameters vars(): ' + vars().__str__())
    print(f'userData.__dict__: {userData.__dict__}')
    print(f'End of function {current_fn_name()}')
    print('----------------------------------------------------------------------------------------------------------')
    return data

def main():
    print('----------------------------------------------------------------------------------------------------------')
    print('*****************************')
    print('******* sys._getframe *******')
    print('*****************************')
    print(f'Inside function {current_fn_name()}')
    print(f'Return type of sys_getframe: {type(sys._getframe(0))}')
    print(f'Value of sys._getframe(0) in function main: {sys._getframe(0)}')
    print(f'Value of sys._getframe(1) in function main: {sys._getframe(1)}')
    ret_user_data = userData('Max','Mustermann','Musterstadt','Geburtsstadt')
    print(f'Inside function {current_fn_name()}')
    print(f'Return value of function userData: {ret_user_data}')
    print(f'Function name of current_fn_name(-1): {current_fn_name(-1)}')
    print('----------------------------------------------------------------------------------------------------------')

if __name__ == '__main__':
    main()