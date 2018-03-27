def fibonacciRemainder(n, divisor):
    if n < 1:
        return n % divisor
    
    previous_to_last_value = 0 # F(0) = 0
    last_value = 1 # F(1) = 1

    ind = 2
    while ind < n+1:
        temp = last_value
        last_value = last_value + previous_to_last_value
        previous_to_last_value = temp
        ind += 1

    return last_value % divisor

if __name__ == '__main__':
    n, divisor = [int(num) for num in raw_input().split()]
    print fibonacciRemainder(n, divisor)
