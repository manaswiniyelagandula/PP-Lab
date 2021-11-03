def linear_search(a, n, x):
    for i in range(n):
        if a[i] == x:
            return i
    return -1

n = int(input("Enter no.of elements: "))
a = list(map(int, input("Enter elements: ").split()))
key = int(input("Enter search element: "))

pos = linear_search(a, n, key)
if pos == -1:
    print("Element not found")
else:
    print("Element found at position", pos + 1)
        
