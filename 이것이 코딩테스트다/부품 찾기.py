n = int(input())

store_array = list(map(int, input().split()))

m = int(input())

customer_array = list(map(int, input().split()))

for i in customer_array:
  if i in store_array:
    print('yes', end=' ')
  else:
    print('no', end=' ')