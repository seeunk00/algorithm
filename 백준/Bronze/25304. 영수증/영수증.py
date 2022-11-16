total_price = int(input())
count = int(input())

sum = []

result = 0

for i in range(count):
  price, c = map(int, input().split()) 
  sum.append(price*c)

for j in sum:
  result = result + j

if total_price == result:
  print('Yes')
else:
  print('No')