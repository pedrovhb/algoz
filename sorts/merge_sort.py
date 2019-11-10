import random
from collections import deque


def merge(l1, l2):
    merged_list = deque()

    if not l1:
        return l2
    if not l2:
        return l1

    crt_l1 = l1.popleft()
    crt_l2 = l2.popleft()
    while True:
        if crt_l1 < crt_l2:
            merged_list.append(crt_l1)
            if l1:
                crt_l1 = l1.popleft()
            else:
                merged_list.append(crt_l2)
                merged_list.extend(l2)
                return merged_list
        else:
            merged_list.append(crt_l2)
            if l2:
                crt_l2 = l2.popleft()
            else:
                merged_list.append(crt_l1)
                merged_list.extend(l1)
                return merged_list


def merge_sort(to_merge):
    if len(to_merge) == 1:
        return deque([to_merge])
    median = len(to_merge) // 2
    l, r = to_merge[:median], to_merge[median:]
    merged_l, merged_r = merge_sort(l), merge_sort(r)
    res = merge(merged_l, merged_r)
    return res


my_list = [random.randint(0, 10) for _ in range(12)]
print(my_list)  # [9, 2, 10, 1, 4, 5, 10, 5, 7, 2, 7, 3]
my_list = list(merge_sort(my_list))
print(my_list)  # [1, 2, 2, 3, 4, 5, 5, 7, 7, 9, 10, 10]
