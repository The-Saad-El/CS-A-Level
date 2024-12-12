# Compound Interest

# with:
# 1) principal amount
# 2) rate of interest
# 3) time period of compunding


def compint(principal, rate, timeperiod):
    if timeperiod == 0:   #basecase
        return principal
    else:
        return compint(principal*rate, rate, timeperiod-1)   #generalcase

x, y, z = 2000, 1.30, 5

print(f'The Total Amount after Compounding will be: {compint(x, y, z)}.')
print(f'(Principal: Rs.{x}, Rate: {y}x, Time-Period: {z} Years)')
