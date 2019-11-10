import random


# Average case is O(N^2)
def bubble_sort(l):
    # We'll repeat this loop until the array is sorted.
    # We know the array is sorted because we went through it
    # in its entirety and didn't swap values.
    while True:
        swapped = False

        # For each element in the list...
        for i in range(len(l)):

            # If it's not the last element, and if the next
            # element is smaller than the current one...
            if i < len(l) - 1 and l[i + 1] < l[i]:
                # Swap the current and next elements
                l[i + 1], l[i] = l[i], l[i + 1]

                # Set the swapped flag
                swapped = True

        # If the swapped flag hasn't been set in this iteration,
        # this means we went through the list without swapping;
        # it's sorted, so exit
        if not swapped:
            break


my_list = [random.randint(0, 10) for _ in range(12)]
print(my_list)  # [0, 2, 9, 6, 1, 4, 8, 5, 2, 8, 5, 7]
bubble_sort(my_list)
print(my_list)  # [0, 1, 2, 2, 4, 5, 5, 6, 7, 8, 8, 9]
