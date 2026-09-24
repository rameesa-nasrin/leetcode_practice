prices=[7,6,4,3,1]

profit=0

buy=prices[0]

for p in prices:

    buy=min(buy,p)

    profit=max(profit,p-buy)

print(profit)

