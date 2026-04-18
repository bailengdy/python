# DP
def rob(nums) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]
    prev2 = nums[0]
    prev1 = max(nums[0], nums[1])
    for i in range(2, n):
        curr = max(prev2 + nums[i], prev1)
        prev2 = prev1
        prev1 = curr
    return prev1

def rob_dp(nums) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, n):
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
    return dp[-1]


print(rob_dp([2,1,1,2])) #4