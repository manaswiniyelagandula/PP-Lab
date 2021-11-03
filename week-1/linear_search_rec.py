def linear_search(a, n, x):
    n = n - 1
    if a[n] == x:
        return n
    if n >= 0:
        return linear_search(a, n, x)
    return -1

n = int(input("Enter no.of elements: "))
a = list(map(int, input("Enter elements: ").split()))
key = int(input("Enter search element: "))

pos = linear_search(a, n, key)
if pos == -1:
    print("Element not found")
else:
    print("Element found at position", pos + 1)
        
