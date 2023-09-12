#!/usr/bin/python3


def minOperations(n):
    if n < 2:
        return n

    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = float("inf")
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

        return dp[n] if dp[n] != float('inf') else 0

n = 4

print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12

print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

