def str_to_datetime_changer(str_datetime):
    year = int(str_datetime[:4])
    month = int(str_datetime[5:7])
    day = int(str_datetime[8:])
    
    return year * 12* 28 + 28*month + day



def solution(today, terms, privacies):
    
    #오늘
    today = str_to_datetime_changer(today)
    
    print("today :",today)
    
    #terms
    terms_dict = {}
    for i in terms:
        terms_dict[i[0]] = int(i[2:])
    
    
    #privacies
    privacies_list = []
    for i in privacies:
        day = str_to_datetime_changer(i[:-2]) + terms_dict[i[-1]] * 28 -1

            
                
        privacies_list.append(day)

    print("privacies_list :",privacies_list)
        
    answer = []
    for i,v in enumerate(privacies_list):
        if today > v:
            answer.append(i+1)

    return answer



#실행
#case1
# today,terms,privacies = "2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

#case2
today,terms,privacies = "2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]

# case3
# today,terms,privacies = "2022.05.19", ["A 6", "B 12", "C 3","D 1"], ["2014.12.03 D", "2015.07.01 B", "2015.02.19 C", "2015.02.20 C"]

result = solution(today,terms,privacies)
print(result)