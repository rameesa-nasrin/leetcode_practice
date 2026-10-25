digits = [1,2,3]

num = int("".join(map(str,digits)))

num += 1

result = list(map(int,str(num)))

print(result)