def binarySearch(key, nums, low, high):
    if low > high:
        return -1
    mid = (low+high)/2
    if key == nums[mid]:
        return mid
    elif key < nums[mid]:
        return binarySearch(key, nums, low, mid-1)
    elif key > nums[mid]:
        return binarySearch(key, nums, mid+1, high)
    
if __name__ == '__main__':
    input_numbers = [int(num) for num in raw_input().split()]
    n = input_numbers[0]
    nums = input_numbers[1:]
    input_keys = [int(num) for num in raw_input().split()]
    n_keys = input_keys[0]
    keys = input_keys[1:]
    keys_indexes = []
    for key in keys:
        result = binarySearch(key, nums, 0, n-1)
        keys_indexes.append(result)
    print keys_indexes
    
        
    
