#https://codeforces.com/contest/734/problem/A

times = int(input())
games = input()
Anton = games.count('A')

#Not using >= or <= operators
if times/2 < Anton:
    print('Anton')
elif times/2 > Anton:
    print('Danik')
else:
    print('Friendship')