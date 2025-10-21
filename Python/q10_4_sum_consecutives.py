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
