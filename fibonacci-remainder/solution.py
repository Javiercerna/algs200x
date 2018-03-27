import math

def fibonacci(n):
    if n < 1:
        return n

    previous_to_last_value = 0 # F(0) = 0
    last_value = 1 # F(1) = 1
    for ind in range(2, n+1):
        temp = last_value
        last_value = last_value + previous_to_last_value
        previous_to_last_value = temp
    return last_value

def findPisanoPeriod(divisor):
    if divisor < 2:
        return 2

    # Special case: 10**n where n >= 3
    special_case = math.log(divisor,10)
    if special_case >= 3 and special_case == int(special_case):
        return int(15*(10**(special_case-1)))
        
    period = 3
    previous_to_last_value = 2
    last_value = 3
    while True:
        if previous_to_last_value % divisor == 0 and \
           last_value % divisor == 1:
            break
        temp = last_value
        last_value = last_value + previous_to_last_value
        previous_to_last_value = temp
        period += 1
    return period

def fibonacciRemainder(n, divisor):
    if n < 1:
        return n % divisor
    period = findPisanoPeriod(divisor)
    equivalent_n = n
    while equivalent_n > period:
        equivalent_n = equivalent_n % period
        #print 'Equivalent n (original=%s): %s' % (n, equivalent_n)
    return fibonacci(equivalent_n) % divisor

if __name__ == '__main__':
    n, divisor = [int(num) for num in raw_input().split()]
    print fibonacciRemainder(n, divisor)
