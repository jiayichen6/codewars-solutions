"""
使用 range 方法，定義開始、結束數字和中間間隔，再使用 sum() 進行加總。
"""


def sequence_sum(begin_number, end_number, step):
    return sum(range(begin_number, end_number + 1, step))
