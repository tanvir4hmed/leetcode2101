# class Solution(object):
#     def plusOne(self, digits):
#         end = len(digits) - 1
#         digits[end] = digits[end] + 1
#         while digits[end] >= 10:
#             reminder = digits[end] % 10
#             digits.append(reminder)
#             digits[end] = int(digits[end] / 10)
#         start = end+1
#         end = len(digits) - 1
#         while start < end:
#             temp = digits[start]
#             digits[start] = digits[end]
#             digits[end] = temp
#             start = start + 1
#             end = end - 1
#         return digits


digits = [9,9]
end = len(digits) - 1
digits[end] = digits[end] + 1
while digits[end] >= 10:
    reminder = digits[end] % 10
    digits.append(reminder)
    digits[end] = int(digits[end] / 10)
start = end+1
end = len(digits) - 1
while start < end:
    temp = digits[start]
    digits[start] = digits[end]
    digits[end] = temp
    start = start + 1
    end = end - 1
print(digits)