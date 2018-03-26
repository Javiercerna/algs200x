def LCM(a, b):
    dividend = 2
    while dividend < a * b:
        if dividend % a == 0 and dividend % b == 0:
            return dividend
        dividend += 1
    return dividend

if __name__ == '__main__':
    a, b = [int(num) for num in raw_input().split()]
    print LCM(a, b)
