# 카드 구매하기

def max_card_price(n, prices):      # DP 테이블 초기화
    dp = [0] * (n + 1)

    for i in range(1, n + 1):  # 카드 개수
        for j in range(1, i + 1):  # 현재 카드팩의 크기
            dp[i] = max(dp[i], dp[i - j] + prices[j - 1])  # 가격을 갱신

    return dp[n]

n = int(input())
prices = list(map(int, input().split()))
print(max_card_price(n, prices))
