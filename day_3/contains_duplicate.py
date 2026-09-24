num=[1,2,2,3,5,6]

for n in num:

    if num.count(n)>1:

        print(True)

        break

else:

    print(False)