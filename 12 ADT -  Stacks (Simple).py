# Abstract Data Type: Stacks

# Stacks work on the principle of LIFO
# They support operations such as Push() & Pop()


mystack = ['','','','','']   # an array with 5 elements
toppointer = 0   # indicative of the first available position in the stack


def Push(ValuetoPush):   # adds an value to the first available position in the stack
    
    global mystack  # both are optional
    global toppointer
    
    if toppointer > 4:   # if the stack is completely full, the toppointer will hold 5 (>4)
        print('The Stack is Full')
        
    else:
        mystack[toppointer] = ValuetoPush
        toppointer += 1   # increments its value
        print(mystack)


def Pop():   # removes and returns the last value entered in the stack
    
    global mystack
    global toppointer
    
    if toppointer == 0:   # if the stack is empty, the toppointer will point at 0, indicating that the stack is totally empty
        print('The Stack is Empty')
        
    else:
        toppointer -= 1   # decrements its value
        mystack[toppointer] = ''   # the data is not actually removed since there still is something there
        print(mystack)   # or could print/return the Popped value


Push('Me')
Push('You')
Push('Us')
Pop()
Push('Our')
Push('They')
Push('Them')
Push('Their')