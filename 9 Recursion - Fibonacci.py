# Fibonacci Sequence


def fibseq(n):
    if (n<=1):   #base case
        return n
    else:
        return fibseq(n-1) + fibseq(n-2)   #general case
    
term = int(input("Enter Term Number: "))
print(f'At n = {term}, the term is {fibseq(term)}.')
print('(The Fibonacci Sequence is 0,1,1,2,3,5,8,13,21,34,55,...)')
