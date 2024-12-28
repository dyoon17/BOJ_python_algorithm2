# 2×n 타일링 2

def tiling_with_2x2(n):      # 초기값 설정
    if n == 1:
        return 1
    if n == 2:
        return 3

    prev2, prev1 = 1, 3  # dp[1] = 1, dp[2] = 3      # 변수 초기화 (공간 최적화)

    # Bottom-Up 방식으로 계산
    for i in range(3, n + 1):
        current = (prev1 + 2 * prev2) % 10007
        prev2, prev1 = prev1, current

    return prev1

n = int(input())
print(tiling_with_2x2(n))
