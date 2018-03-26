def LCM(a, b):
    lcm = 1
    divisor = 2
    while a != 1 or b != 1:
        if a % divisor != 0 and b % divisor != 0:
            divisor += 1
            continue
        else:
            lcm *= divisor
        
        if a % divisor == 0:
            a /= divisor
        if b % divisor == 0:
            b /= divisor
    return lcm

if __name__ == '__main__':
    a, b = [int(num) for num in raw_input().split()]
    print LCM(a, b)
