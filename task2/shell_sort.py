def shell_sort(arr):
    # Get the length of the array
    n = len(arr)
    # Initialize the gap to half of the length of the array
    gap = n // 2

    # Start with a big gap, then reduce the gap
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            # Sort the elements with the current gap
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        # Reduce the gap for the next element
        gap //= 2
        
    return arr


if __name__ == "__main__":
    print("===== Shell Sort Demo =====")
    print("Original array: [9, 8, 3, 7, 5, 6, 4, 1]")

    print("Sorted array:", shell_sort([9,8,3,7,5,6,4,1]))
