#https://codeforces.com/contest/230/problem/B

'''
Learned:
The square of a prime number will have exactly 3 divisors
'''

n = 1000001 #does not have to go up to 1E12, because these number will be squared, (1E6 squared == 1E12)
nums = [True] * n
x = 2
#sieve of Eratosthenes 
while x*x<=n:
    if nums[x] is True:
        for i in range(x*x,n,x):
            nums[i] = False
                
    x+=1

#putting the square of every prime number into a set (checking if an item is in set is an O(1) operation in Python)
allPrimes = set()
for i in range(n):
    if nums[i] is True:
        allPrimes.add(i**2)
        
    
input()
nums = list(map(int,input().split())) 
for i in nums:
    if i in allPrimes and i!=1 and i!=0:
        print('YES')
    else:
        print('NO')