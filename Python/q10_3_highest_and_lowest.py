"""
先將字串用 split() 分割，再用推導式將字串每個元素轉換成數字，
接著用 max, min 取得最大值最小值組成字串。
"""


def high_and_low(numbers):
    num_list = [int(num) for num in numbers.split()]
    return f"{max(num_list)} {min(num_list)}"
