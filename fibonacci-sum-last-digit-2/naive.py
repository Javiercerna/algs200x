def fibonacciSumLastDigit(m, n):
    if m < 2 and n < 2 and m != n:
        return m + n

    previous_last_digit = 0 # F(0) = 0
    last_digit = 1 # F(1) = 1
    sum_digit = 1 if m == 0 else 0

    dummy_ind = 2
    while dummy_ind <= n:    
        temp = last_digit
        last_digit = (last_digit + previous_last_digit) % 10
        previous_last_digit = temp
        if (dummy_ind >= m and dummy_ind <= n):
            sum_digit = (sum_digit + last_digit) % 10
        dummy_ind += 1
    return sum_digit

if __name__ == '__main__':
    m, n = [int(num) for num in raw_input().split()]
    print fibonacciSumLastDigit(m, n)
