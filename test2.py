def solution(word):
    
    if len(word) != 5:
        word += "_"*(5-len(word))
        
    print(word)

solution('AAA')