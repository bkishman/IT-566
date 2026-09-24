def say_hi():
    print('Hi')
    print(f'Module Name: {__name__}')

# The defined functions here print the defined message with the called upper case/lower case functions
def print_message(message: str = 'Hello World')->None:
    print(f'Raw message: {message}')
    print(f'ALL CAPS: {message.upper()}')
    print(f'all lower case: {message.lower()}')
    print(f'Raw message: {message}')

def get_message_from_user()->str:
    user_input = input('Enter a message: ')
    return user_input

def get_number_from_user()->float:
    user_input = input('Enter a number: ')
    result = 0
    try:
        result = float(user_input)
    except Exception as e:
        print(f'You entered an invalid number. Setting result to zero.')

    return result