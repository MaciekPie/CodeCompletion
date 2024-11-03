def binary_search(Test_arr, low, high, k):
    if high >= low:
        Mid = (low + high) // 2
        if Test_arr[Mid] < k:
            return binary_search(Test_arr, Mid + 1, high, k)
        elif Test_arr[Mid] > k:
            return binary_search(Test_arr, low, Mid - 1, k)
        else:
            return Mid
    else:
        return low


def bubble_sort(list):
    for iter_num in range(len(list) - 1, 0, -1):
        for idx in range(iter_num):
            if list[idx] > list[idx + 1]:
                temp = list[idx]
                list[idx] = list[idx + 1]
                list[idx + 1] = temp


def bogo_sort(collection):
    import random

    def is_sorted(collection):
        for i in range(len(collection) - 1):
            if collection[i] > collection[i + 1]:
                return False
        return True

    while not is_sorted(collection):
        random.shuffle(collection)
    return collection


def bead_sort(sequence):
    if any(not isinstance(x, int) or x < 0 for x in sequence):
        raise TypeError("Sequence must be list of non-negative integers")
    for _ in range(len(sequence)):
        for i, (rod_upper, rod_lower) in enumerate(zip(sequence, sequence[1:])):
            if rod_upper > rod_lower:
                sequence[i] -= rod_upper - rod_lower
                sequence[i + 1] += rod_upper - rod_lower
    return sequence


def binary_insertion_sort(collection):
    n = len(collection)
    for i in range(1, n):
        value_to_insert = collection[i]
        low = 0
        high = i - 1

        while low <= high:
            mid = (low + high) // 2
            if value_to_insert < collection[mid]:
                high = mid - 1
            else:
                low = mid + 1
        for j in range(i, low, -1):
            collection[j] = collection[j - 1]
        collection[low] = value_to_insert
    return collection


def comb_sort(data):
    shrink_factor = 1.3
    gap = len(data)
    completed = False

    while not completed:
        gap = int(gap / shrink_factor)
        if gap <= 1:
            completed = True

        index = 0
        while index + gap < len(data):
            if data[index] > data[index + gap]:
                # Swap values
                data[index], data[index + gap] = data[index + gap], data[index]
                completed = False
            index += 1

    return data


def quick_sort(collection):
    from random import randrange

    if len(collection) < 2:
        return collection

    pivot_index = randrange(len(collection))
    pivot = collection.pop(pivot_index)

    lesser = [item for item in collection if item <= pivot]
    greater = [item for item in collection if item > pivot]

    return [*quick_sort(lesser), pivot, *quick_sort(greater)]


def column_based_sort(array, column=0):
    return sorted(array, key=lambda x: x[column])


def longest_subsequence(array):
    array_length = len(array)
    if array_length <= 1:
        return array
    pivot = array[0]
    is_found = False
    i = 1
    longest_subseq: list[int] = []
    while not is_found and i < array_length:
        if array[i] < pivot:
            is_found = True
            temp_array = [element for element in array[i:] if element >= array[i]]
            temp_array = longest_subsequence(temp_array)
            if len(temp_array) > len(longest_subseq):
                longest_subseq = temp_array
        else:
            i += 1

    temp_array = [element for element in array[1:] if element >= pivot]
    temp_array = [pivot, *longest_subsequence(temp_array)]
    if len(temp_array) > len(longest_subseq):
        return temp_array
    else:
        return longest_subseq


def longest_common_substring(text1, text2):
    if not (isinstance(text1, str) and isinstance(text2, str)):
        raise ValueError("longest_common_substring() takes two strings for inputs")

    text1_length = len(text1)
    text2_length = len(text2)

    dp = [[0] * (text2_length + 1) for _ in range(text1_length + 1)]
    ans_index = 0
    ans_length = 0

    for i in range(1, text1_length + 1):
        for j in range(1, text2_length + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                if dp[i][j] > ans_length:
                    ans_index = i
                    ans_length = dp[i][j]

    return text1[ans_index - ans_length : ans_index]


def longest_palindromic_subsequence(input_string):
    n = len(input_string)
    rev = input_string[::-1]
    m = len(rev)
    dp = [[-1] * (m + 1) for i in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 0
    for i in range(m + 1):
        dp[0][i] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if input_string[i - 1] == rev[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]
