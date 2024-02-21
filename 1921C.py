# https://codeforces.com/contest/1921/problem/C

for _ in range(int(input())):

    messages, charge, timeDrain, switchDrain = list(map(int, input().split()))
    moments = [0] + list(map(int, input().split()))

    for i in range(messages):

        # finding whether it's better to turn off or let it drain for the period in between
        charge -= min((moments[i+1] - moments[i])*timeDrain, switchDrain)

        if charge <= 0:
            print('No')
            break

    else:
        print('YES')
