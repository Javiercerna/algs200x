def numberOfInversions(nums):
    count = 0
    for first_ind, first_num in enumerate(nums):
        for second_ind, second_num in enumerate(nums[first_ind:]):
            if first_num > second_num:
                count += 1
    return count
    
if __name__ == '__main__':
    n = int(raw_input())
    nums = [int(num) for num in raw_input().split()]
    print numberOfInversions(nums)
