# Circular Queue

# works on the principle of FIFO
# uses two pointers: headpointer - pointing at the position of the first item & tailpointer - pointing at the first empty position
# has usually 2 methods: enqueue & dequeue
# after reaching the end, the pointers in circular queue wrap themselvees around


myqueue = ['','','','','']   # an arrray of length 5 (0-4)
headpointer = -1   # points at the postion of the 1st item. Is initialized to -1 as the queue is now empty. Could be 0 or any other value.
tailpointer = 0   # points at the first avaiable position in the queue
numberofitems = 0   # indicative of the number of elements in the queue

def enqueue():
    global myqueue
    global headpointer
    global tailpointer
    global numberofitems
    
    if numberofitems == 5:
        print('The Queue is Full.')
        
    else:   # the queue has empty space
        
        myqueue[tailpointer] = input('Enter the Element to Enqueue: ')
        print('The Element was Enqueqed.')
        
        if headpointer == -1:   # when the very first element is enqueued
            headpointer = 0
            
        if tailpointer == 4:   # tailpointer is at the very end (4) while the queue is not full
            tailpointer == 0   # wraps around to start of queue
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

    else:   # the queue is not empty
        myqueue[headpointer] = ''   # or could return/print the dequeqed value
        print('The Last Element was Dequeqed.')
        
        if headpointer == 4:
            headpointer = 0
        else:
            headpointer += 1
            
        numberofitems -= 1
            
def main():
    while True:
        print('Possible Actions on the Stack: | 1. Enqueue | 2. Dequeue | 3. Display Data | 4. Exit |')
        answer = int(input('Enter your Choice (1,2,3,4): '))
        if answer == 1:
            enqueue()
        elif answer == 2:
            dequeue()
        elif answer == 3:
            print(f'The Queue is: {myqueue}')
            print(f'The HeadPointer is: {headpointer} | The TailPointer is: {tailpointer} | The NumberofData is: {numberofitems}')
        elif answer == 4:
            break
        else:
            print('Invalid Input: Enter an Integer among (1,2,3,4).')
        print()
             
        
main()
