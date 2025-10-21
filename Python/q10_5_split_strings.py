def solution(s):
    if len(s) % 2 != 0:
        s += "_"

    result = []
    index = 0

    while index < len(s):
        result.append(s[index : (index + 2)])
        index += 2

    return result
