# https://codeforces.com/contest/1907/problem/C

a = ord('a')  # unicode representation of the letter 'a'

for _ in range(int(input())):

    n = int(input())

    word = input()

    count = [0] * 26

    # counting how many times each character showed up
    for letter in word:
        count[ord(letter) - a] += 1

    # will be the number of letters mod 2 unless more than half are the same number
    print(max(n % 2, (2*max(count))-n))
