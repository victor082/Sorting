# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        current_index = i
        smallest_index = current_index
        for j in range(current_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[smallest_index], arr[current_index] = arr[current_index], arr[smallest_index]

    return arr
    # Divide the array into sorted and unsorted
    # loop through each element
    # Find the smallest element in the unsorted
    # Put the smallest element at the end of the sorted
    # Swap the first element of unsorted with the smallest element

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        # Walk through each elementt in the array
        for i in range(0, len(arr) - 1):
            # If the element is out of order from the neighbor...
            if arr[i] > arr[i+1]:
                # Swap
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
    return arr
# While swap is true, it goes to false which then runs the for loop.
# if the arr[i] is greater than arr[i+1] it then swaps.
# then the swap goes back to true and repeats the loop.

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
