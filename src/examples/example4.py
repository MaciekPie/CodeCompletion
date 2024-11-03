class fibonacci:
    def __init__(self) -> None:
        self.sequence = [0, 1]

    def get(self, index: int) -> list:
        if (difference := index - (len(self.sequence) - 2)) >= 1:
            for _ in range(difference):
                self.sequence.append(self.sequence[-1] + self.sequence[-2])
        return self.sequence[:index]


class prefix_sum:
    def __init__(self, array: list[int]) -> None:
        len_array = len(array)
        self.prefix_sum = [0] * len_array

        if len_array > 0:
            self.prefix_sum[0] = array[0]

        for i in range(1, len_array):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + array[i]

    def get_sum(self, start: int, end: int) -> int:
        if start == 0:
            return self.prefix_sum[end]

        return self.prefix_sum[end] - self.prefix_sum[start - 1]

    def contains_sum(self, target_sum: int) -> bool:
        sums = {0}
        for sum_item in self.prefix_sum:
            if sum_item - target_sum in sums:
                return True

            sums.add(sum_item)

        return False


def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    if not nums1 and not nums2:
        raise ValueError("Both input arrays are empty.")

    merged = sorted(nums1 + nums2)
    total = len(merged)

    if total % 2 == 1:
        return float(merged[total // 2])

    middle1 = merged[total // 2 - 1]
    middle2 = merged[total // 2]
    return (float(middle1) + float(middle2)) / 2.0


class CircularQueue:
    def __init__(self, n: int):
        self.n = n
        self.array = [None] * self.n
        self.front = 0  # index of the first element
        self.rear = 0
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return self.size == 0

    def first(self):
        return False if self.is_empty() else self.array[self.front]

    def enqueue(self, data):
        if self.size >= self.n:
            raise Exception("QUEUE IS FULL")

        self.array[self.rear] = data
        self.rear = (self.rear + 1) % self.n
        self.size += 1
        return self

    def dequeue(self):
        if self.size == 0:
            raise Exception("UNDERFLOW")

        temp = self.array[self.front]
        self.array[self.front] = None
        self.front = (self.front + 1) % self.n
        self.size -= 1
        return temp


def euclidean_distance_sqr(point1, point2):
    return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2
