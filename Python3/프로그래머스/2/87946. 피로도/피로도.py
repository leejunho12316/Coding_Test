from itertools import permutations

def solution(k, dungeons):
    answer_lst = []
    
    for dungeon_lst in list(permutations(dungeons, len(dungeons))):
        cur_k = k
        result = 0
        
        # 처음부터 끝까지 돌기
        for dungeon in dungeon_lst:
            # cur_k가 최소 필요 피로도 미만 or 소모 피로도 미만이면 끝.
            if cur_k < dungeon[0] or cur_k < dungeon[1] : 
                break
            
            # 아니라면 성공
            result += 1
            cur_k -= dungeon[1]
            
        # 끝났으면 돈 던전 개수 추가.
        answer_lst.append(result)
    
    
    return max(answer_lst)