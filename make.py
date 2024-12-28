# 1로 만들기

def min_operations_to_one(n):      # DP 테이블 초기화
    dp = [0] * (n + 1)

    # Bottom-Up 방식으로 DP 테이블 채우기
    for i in range(2, n + 1):
        # 현재 숫자에서 1을 뺀 경우
        dp[i] = dp[i - 1] + 1

        # 2로 나누어 떨어지면 최소 연산 횟수 갱신
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)

        # 3으로 나누어 떨어지면 최소 연산 횟수 갱신
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    return dp[n]

# 입력
n = int(input())
# 출력
print(min_operations_to_one(n))
