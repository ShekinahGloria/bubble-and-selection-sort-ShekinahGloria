def selection_sort(unsorted_list):
    """
    Returns a new list that is sorted in ascending order using Selection Sort.
    """
    lst = unsorted_list.copy()  # avoid modifying the original list
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst


if __name__ == "__main__":
    # Example usage
    arr = [50, 18, 25, 45, 71]
    print("Original list:", arr)
    print("Sorted list:", selection_sort(arr))
