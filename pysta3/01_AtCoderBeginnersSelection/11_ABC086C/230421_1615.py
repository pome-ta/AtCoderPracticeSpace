import sys

if sys.platform == 'ios':
  from pathlib import Path
  import clipboard

  _path = Path('./input_file.txt')
  None if _path.exists() else _path.write_text(
    clipboard.get(), encoding='utf-8')
  sys.stdin = open(_path)


def dis(x0, y0, x1, y1):
  return abs(x0 - x1) + abs(y0 - y1)


N = int(input())

_t, _x, _y = 0, 0, 0

for _ in range(N):
  n, x, y = map(int, input().split())

  d = dis(x, y, _x, _y)
  t = n - _t
  _t, _x, _y = n, x, y
  is_flag = False if t < d else False if t % 2 != d % 2 else True

print('Yes' if is_flag else 'No')

