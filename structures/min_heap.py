import random


class MinKHeap:

    def __init__(self, max_k):
        self._array = []
        self.max_k = max_k

    def add(self, val):
        self._array.append(val)

        index = len(self._array) - 1
        while True:
            parent_index = (index - 1) // 2
            if self._array[parent_index] > val:
                self._array[parent_index], self._array[index] = self._array[index], self._array[parent_index]
                index = parent_index
            else:
                break

        if len(self._array) > 2 ** (self.max_k + 1):
            self._array = self._array[:2 ** (self.max_k + 1)]

    def low(self):
        return self._array[0]


l = [random.randint(0, 1000) for _ in range(3000)]

mkh = MinKHeap(5)
for num in l:
    mkh.add(num)

print(sorted(mkh._array)[:5])
print(sorted(l)[:5])

print(len(l), len(mkh._array))
