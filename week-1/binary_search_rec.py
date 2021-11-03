def binary_search(a, low, high, x):
    mid = (low + high) // 2
    if a[mid] == x:
        return mid
    if (low <= high):
        if a[mid] < x:
            return binary_search(a, mid + 1, high, x)
        if a[mid] > x:
            return binary_search(a, low, mid - 1, x)
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
        
