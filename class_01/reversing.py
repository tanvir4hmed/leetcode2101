
# ## Reversing the list with time complexity O(n) and memory complexity O(n)
# a = [1, 2, 3, 4]
# result = []
# start = len(a) - 1
# end = 0
# while start >= 0:
#     result.append(a[start])
#     start -= 1
#
# print(result)


### Reversing the list with time complexity O(n) and memory complexity O(1)
a = [1, 2, 3, 4]
start = 0
end = len(a) - 1
while start < end:
    temp = a[start]
    a[start] = a[end]
    a[end] = temp
    start += 1
    end -= 1

print(a)
