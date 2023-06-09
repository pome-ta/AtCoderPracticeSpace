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

N, Y = map(int, input().split(' '))
y = int(Y / 1000)
r = [-1, -1, -1]

for s in range(N + 1):
  for g in range(N + 1 - s):
    for m in range(N + 1 - s - g):
      if ((m * 10) + (g * 5) + (s) == y) and (m + g + s == N):
        r = [m, g, s]
        break

print(r[0], r[1], r[2])

