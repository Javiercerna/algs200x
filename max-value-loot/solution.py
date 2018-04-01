def sortItemsByValueWeightRatio(items):
    return sorted(items, key=lambda item: float(item[0])/item[1])

def maxValueOfLoot(knapsack_capacity, items):
    total_value = 0
    sorted_items = sortItemsByValueWeightRatio(items)
    while knapsack_capacity > 0:
        value, weight = sorted_items.pop()
        if knapsack_capacity >= weight:
            total_value += value
            knapsack_capacity -= weight
        else:
            total_value += (float(knapsack_capacity)/weight)*value
            knapsack_capacity = 0
    return total_value

if __name__ == '__main__':
    n_items, knapsack_capacity = [int(num) for num in raw_input().split()]
    items = []
    for dummy_ind in range(n_items):
        items.append(tuple(int(num) for num in raw_input().split()))
    print maxValueOfLoot(knapsack_capacity, items)
            
            
        
