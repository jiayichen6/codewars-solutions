"""
使用 prev_number 記住前一個數字，且從第二個數字開始比對的方式
在前後數字相同時計數 count + 1，不同時將數字乘上 count 並加進 result
最後重置 prev_number 和 count。
"""


def sum_consecutives(lst):
    result = []
    prev_num = lst[0]
    count = 1
    for num in lst[1:]:
        if num == prev_num:
            count += 1
        else:
            result.append(prev_num * count)
            prev_num = num
            count = 1

    result.append(prev_num * count)
    return result
