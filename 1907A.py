#https://codeforces.com/contest/1907/problem/A

for i in range(int(input())):
  position = input()
  column = position[0]
  row = position[1] 
  for j in range(1,9):
    if str(j) != row:
      print(column+str(j))
  for letter in 'abcdefgh':
    if column != letter:
      print(letter+row)