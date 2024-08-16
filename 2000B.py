# https://codeforces.com/contest/2000/problem/B

for _ in range(int(input())):

    input()  # unused input
    passengers = list(map(int, input().split()))
    seated = set()
    seated.add(passengers[0])  # adding the first passenger

    for i in range(1, len(passengers)):

        # checking if the seat is valid
        if ((passengers[i] - 1) in seated) or ((passengers[i] + 1) in seated):
            seated.add(passengers[i])

        # if not, break the loop
        else:
            print('NO')
            break

    # if loop naturally ends (all seatings valid)
    else:
        print('YES')
