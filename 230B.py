# https://codeforces.com/contest/230/problem/B

'''
Learned:
The square of a prime number will have exactly 3 divisors
'''

# sieve of Eratosthenes
# does not have to go up to 1E12, because these number will be squared, (1E6 squared == 1E12)
n = 1000001
nums = [True] * n
x = 2
while x*x <= n:
    if nums[x] is True:
        for i in range(x*x, n, x):
            nums[i] = False

    x += 1

# putting the square of every prime number into a set (set is hashed)
allPrimes = set()
for i in range(2, n):  # start at 2, because 0 and 1 aren't prime
    if nums[i] is True:
        allPrimes.add(i**2)


input()  # unnecessary input

# going through each number and checking if it's in the set
nums = (list(map(int, input().split())))
for i in nums:
    if i in allPrimes:
        print('YES')
    else:
        print('NO')
