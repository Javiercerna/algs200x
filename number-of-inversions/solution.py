def merge(left_half, right_half):
    merged_nums = []
    left = list(left_half)
    right = list(right_half)
    count_inversions = 0
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            merged_nums.append(left.pop(0))
        else:
            count_inversions += len(left)
            merged_nums.append(right.pop(0))
    return merged_nums + left + right, count_inversions

def mergeSort(nums):
    if len(nums) == 1:
        return nums, 0
    
    half = len(nums)/2
    left_half, left_inversions = mergeSort(nums[:half])
    right_half, right_inversions = mergeSort(nums[half:])
    sorted_nums, merge_inversions = merge(left_half, right_half)
    return sorted_nums, (left_inversions + right_inversions + merge_inversions)

def numberOfInversions(nums):
    sorted_nums, total_inversions = mergeSort(nums)
    return total_inversions

if __name__ == '__main__':
    n = int(raw_input())
    nums = [int(num) for num in raw_input().split()]
    print numberOfInversions(nums)
