import random


class MinKHeap:

    def __init__(self, max_k):
        self._array = []
        self.max_k = max_k
        self._max_array_size = 2 ** self.max_k

    def add(self, val):
        self._array.append(val)

        index = len(self._array) - 1
        while index > 0:
            parent_index = (index - 1) // 2
            if self._array[parent_index] > val:
                self._array[parent_index], self._array[index] = self._array[index], self._array[parent_index]
                index = parent_index
            else:
                break

        if len(self._array) > self._max_array_size:
            self._array.pop()

    def low(self):
        return self._array[0]


l = [random.randint(0, 10000) for _ in range(3000)]

mkh = MinKHeap(5)
for num in l:
    mkh.add(num)

print('Min 5 MinKHeap:', sorted(mkh._array)[:5])
print('Min 5 list:', sorted(l)[:5])
print('Length of MinKHeap', len(mkh._array))
print('Length of list:', len(l))
