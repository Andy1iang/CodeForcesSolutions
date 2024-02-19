# https://codeforces.com/problemset/problem/230/A

strength, numDragons = list(map(int, input().split()))

dragons = []

for _ in range(numDragons):
    dragons.append(list(map(int, input().split())))

dragons.sort()  # sorting the dragons by strengths

# each loop checks whether current strength is larger than the dragon's
for dragon in dragons:
    if strength <= dragon[0]:
        print('NO')
        break
    else:
        strength += dragon[1]

else:  # executes if loop ended naturally (without break statement)
    print('YES')
