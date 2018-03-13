def computeMaxPairwiseProduct(integers):
    numbers = list(integers)
    product = 1
    for dummy_ind in range(2):
        max_index = numbers.index(max(numbers))
        max_number = numbers.pop(max_index)
        product *= max_number
    
    return product

if __name__ == '__main__':
    total_nums = int(raw_input())
    integers = [int(num) for num in raw_input().split()]
    assert(len(integers) == total_nums)
    print computeMaxPairwiseProduct(integers)
