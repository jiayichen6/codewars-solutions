"""
使用 current_num 記住前一個數字，且從第二個數字開始比對的方式
在前後數字相同時計數 count + 1，不同時將數字乘上 count 並加進 result
最後重置 current_num 和 count。
"""


def sum_consecutives(lst):
    result = []
    current_num = lst[0]
    count = 1
    for num in lst[1:]:
        if num == current_num:
            count += 1
        else:
            result.append(current_num * count)
            current_num = num
            count = 1

    result.append(current_num * count)
    return result
