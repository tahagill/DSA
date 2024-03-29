# -*- coding: utf-8 -*-
"""smart_sort

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RU_2qNy159EKHGJC8MGtayx2LXtkZrB7
"""

from array import array

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def smart_sort(arr):
    if not isinstance(arr, array) or arr.typecode not in ['i', 'f']:
        raise TypeError("Input must be a compact array of int or float")

    if len(arr) < 2:
        return arr

    if len(arr) < 50:
        return selection_sort(arr)
    else:
        return quick_sort(arr)