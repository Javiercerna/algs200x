def merge(left_half, right_half):
    merged_nums = []
    left = list(left_half)
    right = list(right_half)
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            merged_nums.append(left.pop(0))
        else:
            merged_nums.append(right.pop(0))
    return merged_nums + left + right

def mergeSort(nums):
    if len(nums) == 1:
        return nums
    
    half = len(nums)/2
    left_half = mergeSort(nums[:half])
    right_half = mergeSort(nums[half:])
    return merge(left_half, right_half) 

if __name__ == '__main__':
    n = int(raw_input())
    nums = [int(num) for num in raw_input().split()]
    print mergeSort(nums)
    
