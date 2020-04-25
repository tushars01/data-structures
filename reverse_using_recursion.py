#Implementing reverse of array using recursion

list = [1,2,3,4,5,6,3,5,7,8,4,2,6,4,2,4]
def reverse(list, start, end):

    if start<end-1:
        list[start], list[end-1] = list[end-1], list[start]
        start += 1; end -= 1
        reverse(list, start, end)
    return list

print(reverse(list, 0, len(list)))

