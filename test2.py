from audioop import reverse


def solution(cap, n, deliveries, pickups):
    
    r_deliveries = deliveries[::-1]
    r_pickups = pickups[::-1]

    while sum(deliveries):
        for i,v in enumerate(r_deliveries):
            if v != 0:
                if v - cap > 0 
                r_deliveries[i] == v - cap 
                
    
    answer = -1
    return answer