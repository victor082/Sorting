# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for i in range(cur_index, len(arr)):
            if arr[i] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr


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
