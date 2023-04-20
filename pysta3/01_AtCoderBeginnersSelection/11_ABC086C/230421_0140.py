import sys

if sys.platform == 'ios':
  from pathlib import Path
  import clipboard

  _path = Path('./input_file.txt')
  None if _path.exists() else _path.write_text(
    clipboard.get(), encoding='utf-8')
  sys.stdin = open(_path)


def position(t, pxy, axy) -> bool:
  trgt = sum(pxy)
  if t + sum(axy) < trgt:
    return False
  tmod = True if t % 2 == 0 else False
  pmod = True if trgt % 2 == 0 else False
  return True if tmod == pmod else False


N = int(input())

a = [0, 0]
for s in range(N):
  n, _x, _y = map(int, input().split(' '))
  p = [_x, _y]
  result = position(n, p, a)
  if result:
    a = p
  else:
    break

print('Yes' if result else 'No')

