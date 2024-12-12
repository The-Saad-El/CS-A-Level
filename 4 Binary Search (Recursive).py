# Recursive Binary Search


mylist = [1,2,3,4,5,6,7,8,9,10,11]
print(f'The List is {mylist}')

lowerbound = 0
upperbound = 10   # ie. len(mylist) - 1


def recursivebinarysearch(tosearch):
    
    global mylist
    global lowerbound
    global upperbound
    
    # basecase
    if lowerbound > upperbound:
        print(f"{tosearch} was not found in {mylist}.")
    
    else:  
        middle = int((lowerbound + upperbound) / 2)
        
        if mylist[middle] == tosearch:
            print(f"{tosearch} was found at index {middle}.")
        
        # generalcase
        elif mylist[middle] > tosearch:
            upperbound = middle - 1
            recursivebinarysearch(tosearch)
        else:
            lowerbound = middle + 1
            recursivebinarysearch(tosearch)


numtosearch = int(input('Enter the Number to Search For: '))
recursivebinarysearch(numtosearch)
