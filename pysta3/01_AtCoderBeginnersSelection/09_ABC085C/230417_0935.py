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

# N = m + g + s
# y = (m * 10) + (g * 5) + (s * 1)

N, Y = map(int, input().split(' '))  # 9
y = int(Y / 1000)  # 45

v = [-1, -1, -1]

for m in range(N + 1):
  for g in range(N + 1 - m):
    if (m * 10) + (g * 5) + (N - m - g) == y:
      v = [m, g, N - m - g]
      break

print(v[0], v[1], v[2])

