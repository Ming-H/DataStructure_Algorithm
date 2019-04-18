# -*- coding:utf-8 -*-

def maxmin(l, low, high):
    #   判断列表分到最后只剩下一个或者两个数时就比较
    #   返回的是一个列表[max,min]，第一个最大值，第二个最小值
    if high - low <= 1:
        if l[low] < l[high]:
            return [l[high], l[low]]
        else:
            return [l[low], l[high]]
    # 选取分治的中点
    mid = (low + high) // 2
    # 调用递归
    left_list = maxmin(l, low, mid)
    right_list = maxmin(l, mid + 1, high)
    # 将左边的最大值和右边的最大值比较
    if left_list[0] > right_list[0]:
        # 将左边的最小值和右边最小值比较
        if left_list[1] > right_list[1]:
            # 返回列表[max,min]
            return [left_list[0], right_list[1]]
        else:
            return [left_list[0], left_list[1]]
    else:
        if left_list[1] > right_list[1]:
            return [right_list[0], right_list[1]]
        else:
            return [right_list[0], left_list[1]]
 
if __name__ == "__main__":
    test_list = [1, 5, 7, 15, 8, 6, 4, 2, 0, 20]
    num = maxmin(test_list, 0, len(test_list) - 1)
    print("最大值：%d,最小值%d" % (num[0], num[1]))


# 参考文献： https://blog.csdn.net/weixin_41498948/article/details/81411017
