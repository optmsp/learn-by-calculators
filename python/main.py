import re

MODES = ['postfix', 'prefix', 'infix']
MODE_DEFAULT = 'postfix'
OPERATIONS = ['+', '-', '*', '/']

WHITESPACE = [' ', "\n", "\t"]
PRE_GROUP = ['(']
POST_GROUP = [')']


def display_help():
    print('Operations:')
    print('quit - exit the program')
    print('exit - exit the program')
    print('mode - postfix/prefix/infix')
    print('')


def output_to_user(str):
    print(str)
    print('')


def perform_arithmetic(stack, operation):
    value = 0
    match operation:
        case '+':
            op2 = stack.pop()
            op1 = stack.pop()
            value = op1 + op2

        case '-':
            op2 = stack.pop()
            op1 = stack.pop()
            value = op1 - op2

        case '*':
            op2 = stack.pop()
            op1 = stack.pop()
            value = op1 * op2

        case '/':
            op2 = stack.pop()
            op1 = stack.pop()
            value = op1 / op2

        case _:
            raise ValueError("Operation is invalid: " + operation)

    return value


def get_calculated_value_postfix(tokens):
    stack = []

    while len(tokens) > 0:
        token = tokens.pop(0)

        if (token.isnumeric()):
            stack.append(float(token))
        elif (token in OPERATIONS):
            stack.append(perform_arithmetic(stack, token))
        elif (token in PRE_GROUP):
            stack.append(get_calculated_value_postfix(tokens))
        elif (token in POST_GROUP):
            break
        else:
            raise ValueError("Invalid character in input: " + token)

    if (len(stack) != 1):
        raise ValueError("stack is wrong len: ", len(stack))

    return stack.pop()


def get_calculated_value_prefix(str):
    raise ValueError("not implemented")


def get_calculated_value_infix(str):
    raise ValueError("not implemented")


def tokenizer(input):
    return re.split('\s+', input)


def get_calculated_value(str, mode):
    match mode:
        case 'postfix':
            tokens = tokenizer(str)
            value = get_calculated_value_postfix(tokens)

        case 'prefix':
            value = get_calculated_value_prefix(str)

        case 'infix':
            value = get_calculated_value_infix(str)

        case _:
            output_to_user('Invalid mode: ' + mode)

    return value


def clean_string(input):
    input = input.strip()
    return input


def get_new_mode(old_mode):
    mode = clean_string(input('Enter a mode> '))
    if mode in MODES:
        output_to_user('Entering mode: ' + mode)
    else:
        output_to_user('Invalid mode: ' + new_mode)
        mode = old_mode

    return mode


if __name__ == '__main__':
    display_help()
    mode = MODE_DEFAULT

    while True:
        # str = clean_string(input('Enter an operation> '))
        # str = '1 1 + 2 * 3 /'
        str = '( 1 2 * ) 2 + ( 3 2 / ) *'
        match str:
            case 'exit':
                break

            case 'quit':
                break

            case 'help':
                display_help()

            case 'mode':
                mode = get_new_mode(mode)

            case _:
                output_to_user(f'Calculating: ' + str)
                value = get_calculated_value(str, mode)
                output_to_user(f'Value: {value}')

        break
