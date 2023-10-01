#https://codeforces.com/contest/266/problem/B

spots, time = input().split()
spots, time = int(spots), int(time)
line  = [*input()]

for i in range(time):
    changed = False
    for j in range(spots-1):
        if changed == True: #checking if the boy had just switched
            changed = False
            continue
        else:
            if line[j] == "B" and line[j+1] == "G":
                changed = True
                line[j], line[j+1] = 'G', 'B'
            else:
                pass
            
print(''.join(line))