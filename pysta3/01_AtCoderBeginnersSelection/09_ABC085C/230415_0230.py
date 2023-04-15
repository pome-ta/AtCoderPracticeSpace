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

N, Y = map(int, input().split(' '))
ratio = [10000, 5000, 1000]
M, G, S = [(int(Y / y) if int(Y / y) < N else N) + 1 for y in ratio]

result = [-1, -1, -1]

for m in range(M):
  for g in range(G):
    for s in range(S):
      num = sum([m, g, s])
      value = sum([r * y for r, y in zip(ratio, [m, g, s])])
      if (num < N) and (value == Y):
        result = [m, g, s]
        break

print(result[0], result[1], result[2])

