import re

MODES = ['postfix', 'prefix', 'infix']
MODE_DEFAULT = 'postfix'
ALL_OPS = ['+', '-', '*', '/', '^', 'sqrt', '%']
HP_OPS = ['*', '/', '^', 'sqrt', '%']
LP_OPS = ['+', '-']
PRE_GROUP_TOKEN = '('
POST_GROUP_TOKEN = ')'


def display_help():
    print('OPS:')
    print('quit - exit the program')
    print('exit - exit the program')
    print('mode - postfix/prefix/infix')
    print('')


def display_output(input_string):
    print(input_string)
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

        case '^':
            op2 = stack.pop()
            op1 = stack.pop()
            value = op1 ** op2

        case 'sqrt':
            op1 = stack.pop()
            value = op1 ** 0.5

        case '%':
            op2 = stack.pop()
            op1 = stack.pop()
            value = op1 % op2

        case _:
            raise ValueError("Operation is invalid: " + operation)

    return value


def get_calculated_value_postfix(tokens):
    stack = []

    while len(tokens) > 0:
        token = tokens.pop(0)

        if (token.isnumeric()):
            stack.append(float(token))
        elif (token in ALL_OPS):
            stack.append(perform_arithmetic(stack, token))
        elif (token == PRE_GROUP_TOKEN):
            stack.append(get_calculated_value_postfix(tokens))
        elif (token == POST_GROUP_TOKEN):
            break
        else:
            raise ValueError("Invalid character in input: " + token)

    return stack.pop()


def get_calculated_value_prefix(input_string):
    raise ValueError("not implemented")


def get_calculated_value_infix(input_string):
    raise ValueError("not implemented")


def tokenizer(input_string):
    return re.split('\s+', input_string)


def get_calculated_value(input_string, mode):
    match mode:
        case 'postfix':
            tokens = tokenizer(input_string)
            value = get_calculated_value_postfix(tokens)

        case 'prefix':
            value = get_calculated_value_prefix(input_string)

        case 'infix':
            value = get_calculated_value_infix(input_string)

        case _:
            display_output('Invalid mode: ' + mode)

    return value


def clean_string(input):
    input = input.strip()
    return input


def get_new_mode(old_mode):
    mode = clean_string(input('Enter a mode> '))
    if mode in MODES:
        display_output('Entering mode: ' + mode)
    else:
        display_output('Invalid mode: ' + new_mode)
        mode = old_mode

    return mode


if __name__ == '__main__':
    display_help()
    mode = MODE_DEFAULT

    while True:
        # input_string = clean_string(input('Enter an operation> '))
        # input_string = '( 1 2 * 5 + ) 5 + 2 *'
        # input_string = '2 2 ^'
        # input_string = '5 sqrt 5 %'
        # input_string = '4 3 %'
        input_string = '( 1 2 * 5 + ) 5 + 2 * 2 sqrt *'

        match input_string:
            case 'exit':
                break

            case 'quit':
                break

            case 'help':
                display_help()

            case 'mode':
                mode = get_new_mode(mode)

            case _:
                display_output(f'Calculating: ' + input_string)
                value = get_calculated_value(input_string, mode)
                display_output(f'Value: {value}')

        break
