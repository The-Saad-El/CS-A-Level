# Linear Search

# makes a list using inputs by user
# then searches for a number in the list 


def makelist(): 
    mylist = []
    while True:
        _ = int(input("Enter an Integer Input to the List (0 to terminate): "))
        if _ == 0:
            break
        else:
            mylist.append(_)
    print(f'Your List is: {mylist}')
    return mylist

def searchlist(mylist):
    x = 0
    y = []

    tosearch = int(input('Enter the Number to Search: '))

    for num in mylist:
        x += 1
        if num == tosearch:
            y.append(x)
        
    if y == []:
        print(f'{tosearch} was not found in the list {mylist}')
    else:
        print(f'{tosearch} was found at position(s) {y} in the list {mylist}')

mylist = makelist()
print("\n")
searchlist(mylist)
