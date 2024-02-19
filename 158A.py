# https://codeforces.com/contest/158/problem/A

n, k = list(map(int, input().split()))
scores = list(map(int, input().split()))
place = scores[k-1]  # getting score of at the qualifying index

# finding the amount of scores that qualify
scores.reverse()
tot = (n - scores.index(place))

# getting rid of zeros if the qualifying score is zero
print(tot if place != 0 else tot-scores.count(0))
