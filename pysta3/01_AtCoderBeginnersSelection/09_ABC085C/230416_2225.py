import sys

if sys.platform == 'ios':
  from pathlib import Path
  import clipboard

  _path = Path('./input_file.txt')
  None if _path.exists() else _path.write_text(
    clipboard.get(), encoding='utf-8')
  sys.stdin = open(_path)

# N 枚のお札
# Y 円のお金

#20 196000

#1000 1234000
# 1234
#14 27 959

# N = m + g + s
# y = (m * 10) + (g * 5) + (s * 1)



N, Y = map(int, input().split(' '))  # 9

#N, Y = [20, 196000]
#N, Y = [1000, 1234000]
#N, Y = [2000, 20000000]

y = int(Y / 1000)  # 45

r = [-1, -1, -1]

#1000

m = N if y / 10 > N else y / 10
g = N if y / 5 > N else y / 5
s = N if y / 1 > N else y / 1
'''

m = y / 10
g = y / 5
s = y / 1
'''
aaa = [m, g, s]
print(sum(aaa))

