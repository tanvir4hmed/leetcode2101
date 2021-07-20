### Search Time Complexity O(n) MC O(1)
a = [1, 8, 13, 5, 4]
target = 5
start = 0
end = len(a)
while start < end:
    if a[start] == target:
        print("Found in index ", start)
    start += 1
