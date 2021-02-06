#!/usr/bin/python3

# Answer code for testing purposes. Allows you to make use of the test/ folder.
# Anything outside of the starter/ and test/ folder is optional.


def InsertionSort(L):
    """Sort the array of integers in increasing order using insertion sort

    Args:
        array: An array of integers.
        
    Note: You are not supposed to use python's inbuilt sorting function
    """
    for j in range(1, len(L)):
        key = L[j]
        i = j - 1
        while i >= 0 and L[i] > key:
            L[i+1] = L[i]
            i = i - 1
        L[i+1] = key
    return L



def CountSwapsInInsertionSort(L):
    """Sort the array of integers (in increasing order) using insertion sort and count the total number of swaps required in the process
       see Figure 2.2 from the cormen book. Total number of swaps required for sorting the array 5,2,4,6,1,3 using insertion sort is 9 (total number of grey arrows)

    Args:
        array: An array of integers.
    """
    count = 0
    for j in range(1, len(L)):
        key = L[j]
        i = j - 1
        while i >= 0 and L[i] > key:
            L[i+1] = L[i]
            i = i - 1
            count = count + 1
        L[i+1] = key
    return count



def countNumberOfInversions(L):
    """Count total number of inversions in array, an inversion is defined as a pair with elements a_i and a_j at position index position i and j with the condintion that a_i > a_j and i < j
    Example: total number of inversions in the array 110, 105, 95, 85, 0 is 10 corresponding to (110, 105), (110, 95), (110, 85), (110, 0), (105, 95), (105, 85), (105, 0), (95, 85), (95, 0) and (85, 0)

    Args:
        array: An array of integers.
    """
    count = 0   
    for j in range(1, len(L)):
        key = L[j]
        i = j - 1
        while i >= 0 and L[i] > key:
            L[i+1] = L[i]
            i = i - 1
            count = count + 1
        L[i+1] = key
    return count
