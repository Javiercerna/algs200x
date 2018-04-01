import itertools

def maxAdRevenue(profits_per_click, expected_clicks):
    all_combinations = [list(zip(profits_per_click, p)) for
                        p in itertools.permutations(expected_clicks)]
    max_revenue = -1e11
    for combination in all_combinations:
        revenue = sum([el[0]*el[1] for el in combination])
        if revenue > max_revenue:
            max_revenue = revenue
    return max_revenue

if __name__ == '__main__':
    n = int(raw_input())
    profits_per_click = [int(num) for num in raw_input().split()]
    expected_clicks = [int(num) for num in raw_input().split()]
    print maxAdRevenue(profits_per_click, expected_clicks)
