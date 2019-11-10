import random


def selection_sort(l):
    sorted_l = []

    while l:
        min_element_position = 0
        for i in range(len(l)):
            if l[i] < l[min_element_position]:
                min_element_position = i
        sorted_l.append(l.pop(min_element_position))

    return sorted_l


my_list = [random.randint(0, 10) for _ in range(12)]
print(my_list)  # [9, 2, 10, 1, 4, 5, 10, 5, 7, 2, 7, 3]
my_list = selection_sort(my_list)
print(my_list)  # [1, 2, 2, 3, 4, 5, 5, 7, 7, 9, 10, 10]
