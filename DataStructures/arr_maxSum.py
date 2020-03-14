# A = input("input: ")
arr = [1,2,5,-1,10,90,-2,100,5]

arr_len = len(arr)
max_temp = 0
max_sum = 0
temp1=[]
temp2=[]


for i in range(arr_len):
    if arr[i] >= 0:
        max_sum += arr[i]
        temp1.append(arr[i])
    else:
        if max_temp <= max_sum:
            max_temp = max_sum
            temp2 = temp1[:]
        temp1 = []
        max_sum = 0
if max_sum > max_temp:
    print(temp1)
else:
    print(temp2)


# ### Solution1:
# tempSum = 0
# maxSum = 0
# maxLength = 0
# mark = 0
# start = 0
# end = 0
# for i, val in enumerate(A):
#     if (val < 0):
#         mark = i + 1
#         tempSum = 0
#         continue
#
#     tempSum += val
#
#     if (tempSum > maxSum or tempSum == maxSum and (i + 1 - mark) > maxLength):
#         start = mark
#         end = i + 1
#         maxLength = (i + 1 - mark)
#         maxSum = tempSum
#
# print(A[start:end])
