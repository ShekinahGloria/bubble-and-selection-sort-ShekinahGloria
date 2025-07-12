def bubble_sort(unsorted_list):
    """
    Returns a new list that is sorted in ascending order using Bubble Sort.
    """
    lst = unsorted_list.copy()  # to avoid modifying original
    n = len(lst)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst


if __name__ == "__main__":
    # Example usage
    arr = [54, 28, 45, 62, 31, 18, 98]
    print("Original list:", arr)
    print("Sorted list:", bubble_sort(arr))
