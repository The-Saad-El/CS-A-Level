# Abstract Data Type: Stacks
# with thori lambi


def MakeStack():  
    mystack = []
    length = int(input('Enter the Length of the Stack: '))
    for index in range(length):
        mystack.append('')
    return mystack

def Display(mystack):
    # best for stack with max length of 10 (due to asthetic reasons)
    index = 0
    print("--------------")
    for element in mystack:
        print(f'|{index}|{element.center(10)}|')
        index += 1
    print("--------------")
    print('____________________________________________________________')

def Push(mystack, toppointer):
    if toppointer > len(mystack)-1:
        print('The Stack is Full')
    else:
        valuetopush = input('Enter the Value to Push: ')
        mystack[toppointer] = valuetopush
        toppointer += 1
        return toppointer

def Pop(mystack, toppointer):
    if toppointer == 0:
        print('The Stack is Empty')
    else:
        toppointer -= 1
        print(f'{mystack[toppointer]} was Popped')
        mystack[toppointer] = ''
        return toppointer

def Main():
    toppointer = 0
    mystack = MakeStack()
    while True:
        print('Possible Actions on the Stack: | 1. Push Data | 2. Pop Data | 3. Display Stack | 4. Top Pointer | 5. Exit |')
        answer = int(input('Choose Your Action (1,2,3,4,5): '))
        if answer == 1:
            toppointer = Push(mystack, toppointer)
        elif answer == 2:
            toppointer = Pop(mystack, toppointer)
        elif answer == 3:
            Display(mystack)
        elif answer == 4:
            print(f'The Top-Pointer is at: {toppointer}')
        elif answer == 5:
            break
        else:
            print('Invalid Input: Enter an Integer among (1,2,3,4,5).')

print('Let the Show Begin.')
Main()
