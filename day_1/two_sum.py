arr=[3,4,2,8,7,2]

target=9

for num in arr:

    difference=target-num

    if difference in arr:

        print(arr.index(num),arr.index(difference))

        break




