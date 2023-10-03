def heapify(num, n, i):
    largest = i  # Initialize the largest element as the root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # If the left child is greater than the root
    if left < n and num[left] > num[largest]:
        largest = left

    # If the right child is greater than the largest 
    if right < n and num[right] > num[largest]:
        largest = right

    # If the largest element is not the root, then swap 
    if largest != i:
        num[i], num[largest] = num[largest], num[i]
        # Recursively heapify the affected subtree
        heapify(num, n, largest)

def heap_sort(num):
    n = len(num)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(num, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Swap the current root (maximum element) with the last element
        num[i], num[0] = num[0], num[i]
        # Call max heapify on the reduced heap
        heapify(num, i, 0)

# Example:
if __name__ == "__main__":
    arr = [13, 12, 13, 15, 6, 9]
    heap_sort(arr)
    print("Sorted array is:", arr)
