#最大子列和问题
def max_sum(L):
    max = 0
    current = 0
    for item in L:
        current += item
        if current > max:
            max = current
        if current < 0:
            current = 0
    return max

if __name__ == "__main__":
    L = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
    item = 22
    result = insert_sort(L, item)
    print(result)
