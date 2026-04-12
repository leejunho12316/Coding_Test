s = int(input())

def fib(n):

    fibonacci = [None] * (n + 1)
    fibonacci[1], fibonacci[2] = 1, 1

    #3~n 까지 구하는 횟수
    for i in range(3, n+1):
        fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]

    return fibonacci[n],  n-2


#피보나치 수 재귀호출 의사 코드 실행 횟수는 피보나치 값과 같고
#피보나치 동적 프로그래밍 의사 코드 실행 횟수는 n-2와 같다.
num_rec, num_dp = fib(s)
print(num_rec, num_dp)
