nums = [0,1,0,3,2]

arr=[]

for num in nums:

    if num!=0:

        arr.append(num)

while len(arr)<len(nums):

    arr.append(0)

print(arr)

