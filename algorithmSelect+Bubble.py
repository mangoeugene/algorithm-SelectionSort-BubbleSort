import time
import random


def selection_sort(arr):
    """選擇排序"""
    n = len(arr)
    for i in range(n):
        # 找出最小值索引
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # 交換當前位置和最小值的位置
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def bubble_sort(arr):
    """泡沫排序"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# 分別測試兩種方法並記錄下時間
def test_sorting_methods(nums):
    print("Original array:", nums)

    # 選擇排序
    start_time = time.perf_counter()
    selection_sorted = selection_sort(nums.copy())
    selection_time = time.perf_counter() - start_time
    print(f"Selection Sort time: {selection_time:.6f} seconds")
    print("Selection Sorted array:", selection_sorted)

    # 泡沫排序
    start_time = time.perf_counter()
    bubble_sorted = bubble_sort(nums.copy())
    bubble_time = time.perf_counter() - start_time
    print(f"Bubble Sort time: {bubble_time:.6f} seconds")
    print("Bubble Sorted array:", bubble_sorted)


# 示例
nums = [427, 2542, 5039, 5903, 7109, 9711, 8722, 2234, 5214, 1179]
test_sorting_methods(nums)
