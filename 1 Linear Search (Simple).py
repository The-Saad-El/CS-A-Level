# Linear Search (Simple Version)


mylist = [1,2,3,3,3,4,5,5,6]
print(f'The List is {mylist}')

tosearch = int(input('Enter the Number to Search For: '))

for num in mylist:
    if num == tosearch:
        print(f'The Number {tosearch} was found in the list {mylist}')
        break
else: 
    print(f'The Number {tosearch} was not found in the list {mylist}')


# issay ziada aur simple nahi kar sakta :(