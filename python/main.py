MODES = ['postfix', 'prefix', 'infix']
MODE_DEFAULT = 'postfix'
OPERATIONS = ['+', '-', '*', '/']

def print_help():
    print ('Operations:')
    print ('quit - exit the program')
    print ('exit - exit the program')
    print('mode - postfix/prefix/infix')
    print ('')

def perform_operation(op1, op2, operation):
    if operation == '+':
        return op1 + op2
    elif operation == '-':
        return op1 - op2
    elif operation == '*':
        return op1 * op2
    elif operation == '/':
        return op1 / op2
    else:
        raise ValueError("Operation is invalid: " + operation)

def compute_value_postfix(userInput):
    stack = []
    for token in userInput.split(' '):
        if (token.isnumeric()):
            stack.append(token)
        elif (token.isalpha()):
            raise ValueError("Invalid character in input: " + token)
        else:
            if (len(stack) < 2):
                raise ValueError("Not enough operands")

            op2 = stack.pop()
            op1 = stack.pop()
            value = perform_operation(int(op1), int(op2), token)
            print("value: ", value)

def compute_value(userInput, mode):
    if mode == 'postfix':
        compute_value_postfix(userInput)
    elif mode == 'prefix':
        compute_value_prefix(userInput)
    elif mode == 'infix':
        compute_value_infix(userInput)
    else:
        print('Invalid mode: ' + mode)

if __name__ == '__main__':
    print_help()
    mode = MODE_DEFAULT

    while True:
        userInput = input('Enter an operation: ')
        if userInput == 'exit':
            break
        elif  userInput == 'quit':
            break
        elif userInput == 'mode':
            newMode = input('Enter a mode: ')
            if newMode in MODES:
                print('Entering mode: ' + newMode)
                print('')
                mode = newMode
            else:
                print('Invalid mode: ' + newMode)
                print('')
        else:
            compute_value(userInput, mode)
