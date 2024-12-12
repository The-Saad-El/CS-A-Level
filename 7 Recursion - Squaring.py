# Squaring

def FindPower(base,exponent):
    if exponent == 0:   # basecase
        return 1
    else:
        return base * FindPower(base,exponent-1)   # generalcase
    
    
print(FindPower(5,5))