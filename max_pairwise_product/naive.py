def computeMaxPairwiseProduct(integers):
    product = 0
    
    for i in range(len(integers)):
        for j in range(i+1, len(integers)):
            if product < integers[i]*integers[j]:
                product = integers[i]*integers[j]
    
    return product

if __name__ == '__main__':
    total_nums = int(raw_input())
    integers = [int(num) for num in raw_input().split()]
    assert(len(integers) == total_nums)
    print computeMaxPairwiseProduct(integers)
