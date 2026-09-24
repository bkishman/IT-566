"""Implements Hello World demo."""

# imports hello_world.py
import hello_world

def main():
    message = hello_world.get_message_from_user()
    hello_world.print_message(message)
    number = hello_world.get_number_from_user()
    print(f'User entered: {number}')
    print('User entered: ' + str(number))
    #hello_world.say_hi()
    #hello_world.print_message()
    #hello_world.print_message('Oh, I love Python!')



# This is where the program actually begins, calling functions based on definitions above
if __name__ == '__main__':
    main()