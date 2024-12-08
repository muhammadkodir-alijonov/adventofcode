import bisect

def maxValue(events):
    events.sort(key=lambda x: x[1])

    n = len(events)

    dp = [0] * n
    dp[0] = events[0][2]

    for i in range(1, n):
        dp[i] = max(dp[i-1], events[i][2])  

    def find_last_non_overlapping(i):
        low, high = 0, i-1
        while low <= high:
            mid = (low + high) // 2
            if events[mid][1] < events[i][0]:
                low = mid + 1
            else:
                high = mid - 1
        return high

    max_sum = dp[-1] 

    for i in range(1, n):
        prev_index = find_last_non_overlapping(i)
        if prev_index >= 0:
            max_sum = max(max_sum, dp[prev_index] + events[i][2])

    return max_sum