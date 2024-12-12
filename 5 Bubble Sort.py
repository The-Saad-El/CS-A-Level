# Bubble Sort


def bubblesort(somelist):
    swap = True
    top = len(somelist) - 1   # the index of the last term

    while swap and (top != 0):   # continues if there has been a swapping and the top index is not 0 (lesser than 1) (so there are still atleast 2 values which can be compared)
        swap = False
        for index in range(top):            
            if somelist[index] > somelist[index + 1]:
                # temp = somelist[index + 1]
                # somelist[index + 1] = somelist[index]    
                # somelist[index] = temp
                somelist[index], somelist[index + 1] = somelist[index + 1], somelist[index]   # :)
                swap = True
        top -= 1   # no need to recheck the lastmost number since it will already be sorted

    print(f'The  Sorted  List is {somelist}')

mylist = [230,43,8,101,5,100,9879,3,56]
print(f'The Original List is {mylist}')
bubblesort(mylist)
