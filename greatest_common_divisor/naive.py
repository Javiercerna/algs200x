def GCD(a, b):
    gcd = 1
    divisor = 2
    while divisor < a or divisor < b:
        if a % divisor == 0 and b % divisor == 0:
            gcd *= divisor
            a /= divisor
            b /= divisor
        else:
            divisor += 1
    return gcd

if __name__ == '__main__':
    a, b = [int(num) for num in raw_input().split()]
    print GCD(a, b)
        
