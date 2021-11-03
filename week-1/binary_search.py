def binary_search(a, low, high, x):
    while(low <= high):
        mid = (low + high) // 2
        if a[mid] < x:
            low = mid + 1
        if a[mid] > x:
            high = mid - 1
        if a[mid] == x:
            return mid
    return -1

n = int(input("Enter no.of elements: "))
a = list(map(int, input("Enter elements: ").split()))
key = int(input("Enter search element: "))
l = 0
h = n - 1
pos = binary_search(a, l, h, key)
if pos == -1:
    print("Element not found")
else:
    print("Element found at position", pos + 1)
        
