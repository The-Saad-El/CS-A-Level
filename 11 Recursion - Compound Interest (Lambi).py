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


principal = int(input("Enter the Principal Amount: "))
rate = int(input("Enter the Rate of Interest: "))
rate = 1 + rate/100
timeperiod =int(input("Enter the Time-Period of Compounding: "))

print('\n')

print(f'The Total Amount after Compounding will be: {compint(principal, rate, timeperiod)}.')
print(f'(Principal: Rs.{principal}, Rate: {rate}x, Time-Period: {timeperiod} Years)')


# inputs ki waja say ziada lambi hogayi