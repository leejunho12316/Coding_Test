from itertools import product

def solution(word):
    
    l = ['A','E','I','O','U'] 
    
    # print(help(product))
    prod1 = list(product(l, repeat = 1))
    prod2 = list(product(l, repeat = 2))
    prod3 = list(product(l, repeat = 3))
    prod4 = list(product(l, repeat = 4))
    prod5 = list(product(l, repeat = 5))
    print(len(prod1), len(prod2), len(prod3), len(prod4), len(prod5))
    
    words = []
    
    for a in range(0,5):
        words.append(prod1[a])
        
        for b in range(5*a, 5*a+5):
            words.append(prod2[b])
            
            for c in range(5*b, 5*b+5):
                words.append(prod3[c])
                
                for d in range(5*c, 5*c+5):
                    words.append(prod4[d])
                    
                    for e in range(5*d, 5*d+5):
                        words.append(prod5[e])
    
    
    return words.index(tuple(word)) + 1
    