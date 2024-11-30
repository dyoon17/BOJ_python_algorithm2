#1748. 수 이어 쓰기 1

result = 0  # 자릿수의 총합
digit = 1   # 현재 자릿수
start = 1   # 현재 자릿수 범위의 시작 값 (1, 10, 100, ...)

N = int(input())

while start <= N:	# 자릿수 계산
    end = min(start * 10 - 1, N)  # 현재 자릿수에서 마지막 숫자와 N 중 작은 값
    result += (end - start + 1) * digit		# 현재 자릿수 범위의 숫자 개수 계산 후 다음 자릿수로 이동
    start *= 10  # 다음 자릿수의 시작 값
    digit += 1   # 자릿수 증가

print(result)	# 새로운 수의 자릿수 출력
