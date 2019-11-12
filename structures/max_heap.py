import random


class MaxHeap:

    def __init__(self):
        self._array = []

    def add(self, val):
        self._array.append(val)
        index = len(self._array) - 1
        while index > 0:
            parent_element = (index - 1) // 2
            if self._array[parent_element] < val:
                self._array[parent_element], self._array[index] = self._array[index], self._array[parent_element]
                index = parent_element
            else:
                break

    def pop(self):

        # Take note of the max val (heap root), del root
        to_return = self._array[0]
        self.del_index(0)
        return to_return

    def del_index(self, index):
        if index == len(self._array) - 1:
            self._array.pop()

        # Swap element with last appended to keep heap-shape
        self._array[index] = self._array.pop()
        while True:
            lchild_index = index * 2 + 1
            rchild_index = index * 2 + 2

            if rchild_index > len(self._array) - 1:
                break

            # If a child node is larger than the current one, swap them and update the index
            max_child = max(lchild_index, rchild_index, key=lambda x: self._array[x])
            if self._array[max_child] > self._array[index]:
                self._array[index], self._array[max_child] = self._array[max_child], self._array[index]
                index = max_child
            # If this node is larger than both children, we're done
            else:
                break

    def top(self):
        return self._array[0]


l = [random.randint(0, 10) for _ in range(10)]
mh = MaxHeap()

for i in l:
    mh.add(i)  # O(logN) (total: O(N*logN)

print(l)
print(mh._array)

print(max(l))  # O(n)
print(mh.top())  # O(1)

l.remove(max(l))  # O(n^2)
mh.pop()  # O(logN)

print(sorted(l) == sorted(mh._array))
