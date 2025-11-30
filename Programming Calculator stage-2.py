history_list = []

def add(a,b): return a+b
def subtract(a,b): return a-b
def multiply(a,b): return a*b
def divide(a,b):
    try:
        return a/b
    except Exception as e:
        print(e)
def power(a,b): return a**b
def remainder(a,b): return a%b

def select_op(choice):
    if choice == '#':
        return -1
    elif choice == '$':
        history_list.clear()
        print("History cleared")
        return 0
    elif choice == '?':
        if history_list:
            for h in history_list:
                print(h)
        else:
            print("No past calculations to show")
        return 0

    elif choice in ('+','-','*','/','^','%'):

        while True:
            num1s = input("Enter first number: ")
            print(num1s)
            if num1s.endswith('$'): return 0
            if num1s.endswith('#'): return -1
            try:
                num1 = float(num1s)
                break
            except:
                print("Not a valid number,please enter again")

        while True:
            num2s = input("Enter second number: ")
            print(num2s)
            if num2s.endswith('$'): return 0
            if num2s.endswith('#'): return -1
            try:
                num2 = float(num2s)
                break
            except:
                print("Not a valid number,please enter again")

        if choice == '+': result = add(num1, num2)
        elif choice == '-': result = subtract(num1, num2)
        elif choice == '*': result = multiply(num1, num2)
        elif choice == '/': result = divide(num1, num2)
        elif choice == '^': result = power(num1, num2)
        elif choice == '%': result = remainder(num1, num2)

        line = f"{num1} {choice} {num2} = {result}"
        history_list.append(line)
        print(line)
        return 0

    else:
        print("Unrecognized operation")
        return 0


while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")
    print("8.History  : ? ")
    
    choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
    print(choice)
    
    if select_op(choice) == -1:
        print("Done. Terminating")
        break
