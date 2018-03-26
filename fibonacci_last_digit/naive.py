def fibonacci_last_digit(n):
    fibonacci_list = [0,1]
    for ind in range(2,n+1):
        fibonacci_list.append(fibonacci_list[ind-1] + fibonacci_list[ind-2])
    return fibonacci_list[n] % 10

if __name__ == '__main__':
    n = int(raw_input())
    print fibonacci_last_digit(n)
