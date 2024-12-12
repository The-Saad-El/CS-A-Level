# Simple Queue

# works on the principle of FIFO
# uses two pointers: headpointer - pointing at the position of the first item & tailpointer - pointing at the first empty position
# has usually 2 methods: enqueue & dequeue


myqueue = ['','','','','']   # an arrray of length 5 (0-4)
headpointer = -1   # points at the postion of the 1st item. Is initialized to -1 as the queue is now empty
tailpointer = 0   # points at the first avaiable position in the queue

def enqueue():
    global myqueue
    global headpointer
    global tailpointer
    
    if tailpointer == 5:   # ie > 4 (> length of queue)
        print('The Queue is Full.')
    else:
        myqueue[tailpointer] = input('Enter the Element to Enqueue: ')
        tailpointer += 1
        print('The Element was Enqueqed.')
        
        if headpointer == -1:   # if the queue was initially totally empty, so headpointer would be at -1
            headpointer = 0   # hence now its value should change to 0 to point to the first item in the queue which is the element just enqueued
        
def dequeue():
    global myqueue
    global headpointer
    global tailpointer
            
    if headpointer == -1:
        print('The Queue is Empty.')
    else:
        myqueue[headpointer] = ''   # or could return/print the dequeqed value
        headpointer += 1
        print('The Last Element was Dequeqed.')
        if headpointer == tailpointer:   # only possible when the queue is empty and after dequeing
            headpointer = -1   # initializes their positions
            tailpointer = 0 
            
def main():
    while True:
        print('Possible Actions on the Stack: | 1. Enqueue | 2. Dequeue | 3. Display | 4. Pointers | 5. Exit |')
        answer = int(input('Enter your Choice (1,2,3,4,5): '))
        if answer == 1:
            enqueue()
        elif answer == 2:
            dequeue()
        elif answer == 3:
            print(f'The Queue is: {myqueue}')
        elif answer == 4:
            print(f'The HeadPointer is: {headpointer} | The TailPointer is: {tailpointer}')
        elif answer == 5:
            break
        else:
            print('Invalid Input: Enter an Integer among (1,2,3,4,5).')
        print()
             
        
main()
