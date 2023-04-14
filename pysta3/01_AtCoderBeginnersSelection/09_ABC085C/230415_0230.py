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

from itertools import product

N, Y = map(int, input().split(' '))

ip = list(product(range(N + 1), repeat=3))

result = [-1, -1, -1]
for y in ip:
  num = sum(y)
  value = (y[0] * 10000) + (y[1] * 5000) + (y[2] * 1000)
  if (num < N) and (value == Y):
    result = y
    break

print(result)

