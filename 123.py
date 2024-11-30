#9095. 1, 2, 3 더하기

func = [0] * 12		# n은 양수이며 11보다 작음
func[1], func[2], func[3] = 1, 2, 4  # 초기값 설정

for i in range(4, 12):	# 4번째부터 ~
    func[i] = func[i - 1] + func[i - 2] + func[i - 3]

T = int(input())
for _ in range(T):
    n = int(input())
    print(func[n])
    
