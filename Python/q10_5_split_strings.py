"""
一開始先判斷是否為奇數，若是則補 "_"。
使用 while 迴圈配合索引，每次取兩個字元 s[index:index+2] 加入結果陣列，
索引每次加 2。
"""


def solution(s):
    if len(s) % 2 != 0:
        s += "_"

    result = []
    index = 0

    while index < len(s):
        result.append(s[index : (index + 2)])
        index += 2

    return result
