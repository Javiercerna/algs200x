def fibonacciSumLastDigit(n):
    if n < 2:
        return n

    previous_last_digit = 0 # F(0) = 0
    last_digit = 1 # F(1) = 1
    sum_digit = 1

    dummy_ind = 2
    while dummy_ind <= n:    
        temp = last_digit
        last_digit = (last_digit + previous_last_digit) % 10
        previous_last_digit = temp
        sum_digit = (sum_digit + last_digit) % 10
        dummy_ind += 1
    return sum_digit

if __name__ == '__main__':
    n = int(raw_input())
    print fibonacciSumLastDigit(n)
