from bisect import bisect_left, bisect_right


def count_by_value(a,left_val,right_val):
    """
    정렬된 배열 a 에서, left_val 이상, right_val 이하인 값들의 개수를 반환
    """
    left_index = bisect_left(a,left_val)
    right_index = bisect_right(a,right_val)
    return right_index-left_index

a = [1,2,3,3,3,3,4,4,8,9]
print(count_by_value(a,4,4))

print(count_by_value(a,-1,3))

