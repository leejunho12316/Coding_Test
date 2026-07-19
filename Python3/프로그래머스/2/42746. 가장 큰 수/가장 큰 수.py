def func(string):
    string = (string*4)[:4]
    return string

def solution(numbers):
    
    numbers = [str(x) for x in numbers]
    
    numbers.sort(key = lambda x : func(x), reverse=True)
    
    answer = ''.join(numbers)
    answer = answer.lstrip('0')
    
    if answer == '':
        return '0'
    return answer
    
    