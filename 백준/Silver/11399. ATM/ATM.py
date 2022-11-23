n = int(input())
people = list(map(int, input().split()))

people.sort()

middle = 0
result = 0
r_people = []

for i in range(len(people)):
    middle = middle + people[i]
    r_people.append(middle)

for i in range(len(r_people)):
    result = result + r_people[i]
    

print(result)