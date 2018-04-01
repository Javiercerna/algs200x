def maxAdRevenue(profits_per_click, expected_clicks):
    profits = list(profits_per_click)
    clicks = list(expected_clicks)
    profits.sort()
    clicks.sort()
    return sum([profits[ind]*clicks[ind] for ind in range(len(clicks))])

if __name__ == '__main__':
    n = int(raw_input())
    profits_per_click = [int(num) for num in raw_input().split()]
    expected_clicks = [int(num) for num in raw_input().split()]
    print maxAdRevenue(profits_per_click, expected_clicks)
