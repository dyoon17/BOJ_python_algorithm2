# 2×n 타일링

def tiling(n):      # DP 테이블 초기화
    dp = [0] * (n + 1)
    
    dp[1] = 1
    if n > 1:
        dp[2] = 2

    # Bottom-Up 방식으로 DP 테이블 채우기
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

    return dp[n]

n = int(input())
print(tiling(n))
