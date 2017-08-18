import sys
sum = []
arr=[]
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)


for i in range(len(arr)-2):
    for j in range(len(arr)-2):
        sum.append(arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
print(max(sum))








#Congratulations, you passed the sample test case.
#Click the Submit Code button to run your code against all the test cases.

#Input (stdin)
#1 1 1 0 0 0
#0 1 0 0 0 0
#1 1 1 0 0 0
#0 9 2 -4 -4 0
#0 0 0 -2 0 0
#0 0 -1 -2 -4 0
#Your Output (stdout)
#13
#Expected Output
#13