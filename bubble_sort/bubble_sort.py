def bubble_sort(unsorted_list):
    """
    Sorts a list of elements in ascending order using the Bubble Sort algorithm.
    The sorting is done in-place.

    Parameters:
        unsorted_list (list): The list of elements to sort.

    Returns:
        None
    """
    n = len(unsorted_list)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
                swapped = True
        if not swapped:
            break


if __name__ == "__main__":
    # Example usage
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", arr)
    bubble_sort(arr)
    print("Sorted list:", arr)
