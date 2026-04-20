N = int(input())
result = 0

max_5 = N // 5

def algorithm(N):

    #5키로를 최대한 넣을 수 있는 개수 ~ 0개까지
    for i in range(max_5, -1, -1):
        left = N-i*5

        #3키로를 넣어서 0을 만들 수 있는지 확인. 있으면 바로 return
        if left % 3 == 0:
            return i + left//3

    return -1

print(algorithm(N))