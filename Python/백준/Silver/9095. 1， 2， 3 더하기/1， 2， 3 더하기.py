T = int(input())
n_list=[]
for _ in range(T):
    n_list.append(int(input()))

# max(n_list)에 의해 만들어진 빈 배열이 dp_list[1],dp_list[2],dp_list[3]으로 직접 참조할 수 없을만큼 짧으면 인덱스 에러
# dp_list = [None] * (max(n_list) + 1)
# dp_list[1], dp_list[2], dp_list[3] = 1, 2, 4

def make_123(n):

    if n==1: return 1
    elif n==2: return 2
    elif n==3: return 4

    dp_list = [None] * (max(n_list) + 1)
    dp_list[1], dp_list[2], dp_list[3] = 1, 2, 4

    for i in range(4,n+1):
        dp_list[i] = dp_list[i-1] + dp_list[i-2] + dp_list[i-3]

    return dp_list[n]


for n in n_list:
    print(make_123(n))