#Problem: https://codeforces.com/problemset/problem/1855/B

'''
Learned:
--Only even numbers can have streak of divisors longer than 1
--The longest streak of divisors must start at 1, because even if 
    there is a streak starting in the middle of the number list, the
    length 'n' streak will guarantee a length 'n' streak starting at 1,
    because if n = 18, then out of the 18 number streak, one number is divisible by 18, 
    since every 18th number is a multiple of 18, the same with, 17, 16, so on, all the way to 1 
'''

for x in range(int(input())):
    
    num = int(input())
    if num%2 != 0:
        print(1)
        continue
    else:
        count = 0
        for i in range(1,num+1):
            if num%i == 0:
                count +=1
            else:
                break
        print(count)
        
