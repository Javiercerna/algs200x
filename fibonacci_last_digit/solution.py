def fibonacci_last_digit(n):
    previous_to_last_digit = 0 # F(0) = 0
    last_digit = 1 # F(1) = 1
    for ind in range(2,n+1):
        temp = last_digit
        last_digit = (last_digit + previous_to_last_digit) % 10
        previous_to_last_digit = temp
    return last_digit

if __name__ == '__main__':
    n = int(raw_input(n))
    print fibonacci_last_digit(n)
