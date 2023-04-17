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

r = [10, 5, 1]
v = [-1, -1, -1]

M, G, S = [N if y / i > N else int(y / i) for i in r]


for s in range(S + 1):
  if s > N:
    continue
  for g in range(G + 1):
    if g + s > N:
      continue
    for m in range(M + 1):
      cont = sum([m, g, s])
      if cont > N:
        continue
      value = (m * r[0]) + (g * r[1]) + (s)
      if cont == N and value == y:
        v = [m, g, s]
        break

print(v[0], v[1], v[2])

