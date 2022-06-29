def largest (arr, n):
    max = arr[0]
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max

def smallest(arr, n):
    min = arr[0]
    for i in range(1, n):
        if arr[i] < min:
            min = arr[i]
    return min

print("These are time from stop-watch in seconds")
arr = [10, 324, 45, 90, 980, 40]
n = len(arr)
ansLargest = largest(arr, n)
ansSmallest = smallest(arr, n)
print("Largest in given array is", ansLargest)
print("Smallest in given array is", ansSmallest)