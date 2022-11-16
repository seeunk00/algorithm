n = int(input())
people = list(map(int, input().split()))

people.sort()

result = 0
r_people = []

for i in range(len(people)):
    result = result + people[i]
    r_people.append(result)

print(sum(r_people))