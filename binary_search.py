

data = [1,2,4,5,6,7,8,11,15,17,19,21]

def binary_search(data, target, low, high):

    mid = (high + low)//2
    if low>high:
        return False

    if data[mid] == target:
        return mid

    elif target > data[mid]:
        
        return binary_search(data, target, mid+1, high)
    else:
        return binary_search(data, target, low, mid - 1)

print(binary_search(data, 12, 0, len(data)))
