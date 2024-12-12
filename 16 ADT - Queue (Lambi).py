# Circular (Lambi) Queue


myqueue = []
headpointer = -1
tailpointer = 0
numberofitems = 0

def makequeue():
    global myqueue
    myqueue = []
    length = int(input('Enter the Length of the Queue: '))
    for index in range(length):
        myqueue.append('')

def enqueue():
    global myqueue
    global headpointer
    global tailpointer
    global numberofitems
    
    if numberofitems == len(myqueue):
        print('The Queue is Full.')
        
    else:
        
        myqueue[tailpointer] = input('Enter the Element to Enqueue: ')
        print('The Element was Enqueqed.')
        
        if headpointer == -1:
            headpointer = 0
            
        if tailpointer == 4:
            tailpointer == 0
        else:
            tailpointer += 1
        
        numberofitems += 1
            
def dequeue():
    global myqueue
    global headpointer
    global tailpointer
    global numberofitems
            
    if numberofitems == 0:
        print('The Queue is Empty.')

    else:
        myqueue[headpointer] = ''
        print('The Last Element was Dequeqed.')
        
        if headpointer == (len(myqueue) - 1):
            headpointer = 0
        else:
            headpointer += 1
            
        numberofitems -= 1
        
def display():
    # best for queue with max length of 10 (due to asthetic reasons)
    print("--------------")
    for index, element in enumerate(myqueue):
        print(f'|{index}|{element.center(10)}|')
    print("--------------")
    print(f'The HeadPointer is: {headpointer} | The TailPointer is: {tailpointer} | The NumberofData is: {numberofitems}')   # i wanna make it so that the pointers themselves indicate on the graphic queue itself laikin (bohot) lambi hojaye gi

def view():
    print(f'The Queue is: {myqueue}')
    print(f'The HeadPointer is: {headpointer} | The TailPointer is: {tailpointer} | The NumberofData is: {numberofitems}')

def reset():
    global headpointer
    global tailpointer
    global numberofitems
    
    makequeue()
    headpointer = -1
    tailpointer = 0
    numberofitems = 0
    print('The Data was Reset.')
        
            
def main():
    x = 0
    makequeue()
    print()
    
    while True:
        x += 1
        print(f'[{x}]')
        
        print('Possible Actions on the Queue: | 1. Enqueue | 2. Dequeue | 3. View Data | 4. Display Data | 5. Reset | 6. Exit |')
        answer = int(input('Enter your Choice (1,2,3,4,5,6): '))
        if answer == 1:
            enqueue()
        elif answer == 2:
            dequeue()
        elif answer == 3:
            view()
        elif answer == 4:
            display()
        elif answer == 5:
            reset()
        elif answer == 6:
            break
        else:
            print('Invalid Input: Enter an Integer among (1,2,3,4,5,6).')
        print()
             
        
main()
