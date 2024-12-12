# Binary Search

'''
about:
a binary search is more efficent if a list is already sorted. 
the value in of the middle item in the list is first tested to see if it matches the required item
the half of the list that does not contain the required item is discarded.
then the next item item tested is the middle item of the remaining half of the list. 
this is repeated unti the required item is found or there is nothing left to be tested.

performance:
considering a list with 1024 items
the maximum number of comparisons by a linear search would be 1024
while for binary search they would be only 16 (1024 = 2^16)
since it parses through the list by halving it each time

conditions for usage:
1) the list must already be sorted
2) the items in the list must be of the same datatype (else no comparisons can be made)
'''


mylist = [1,2,3,4,5,6,7,8,9,10,11]
print(f'The List is {mylist}')

tosearch = int(input('Enter the Number to Search For: '))

lowerbound = 0
upperbound = 10   # ie. len(mylist) - 1

while (lowerbound <= upperbound):
    index = int((upperbound + lowerbound) / 2)   # or: (upperbound + lowerbound) // 2 
    if tosearch == mylist[index]:
        print(f'The Number {tosearch} was found in the list {mylist}')
        break
    elif tosearch > mylist[index]: 
        lowerbound = index + 1
    else: 
        upperbound = index - 1
else: 
    print(f'The Number {tosearch} was not found in the list {mylist}')
    