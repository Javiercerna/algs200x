def GCD(a, b):
    if a == 0:
        return b
    if b == 0:
        return a

    if a < b:
        b = b % a
    else:
        a = a % b
    return GCD(a, b)

if __name__ == '__main__':
    a, b = [int(num) for num in raw_input().split()]
    print GCD(a, b)
        
