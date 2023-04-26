import sys

if sys.platform == 'ios':
  from pathlib import Path
  import clipboard

  _path = Path('./input_file.txt')
  None if _path.exists() else _path.write_text(
    clipboard.get(), encoding='utf-8')
  sys.stdin = open(_path)

# N 個の切れ目
# 左右の長さが L [cm]
# 左から i 番目の切れ目
# 左から A i​ [cm] の位置
# N 個の切れ目のうち K 個
# K+1 個のピースに分割

from itertools import combinations


def combination(arrays: list, k: int) -> list:
  result_list = []
  if len(arrays) < k:
    return []
  if k == 1:
    result_list = [[i] for i in arrays]
  else:
    for i in range(len(arrays) - k + 1):
      for r in combination(arrays[i + 1:], k - 1):
        result_list.append([arrays[i], *r])
  return result_list


# 階乗
def frct(num: int) -> int:
  return 1 if num == 0 else num * frct(num - 1)


def cmbntn(n: int, r: int) -> int:
  pass


def comb(l: list, n: int) -> list:
  c = []
  _p = [[i for i in range(len(l))] for _ in range(n)]
  for x in range(len(l)):
    for y in range(n):
      c.append([x, y])

  return c


N, L, K, *Ai = [
  int(i) for i in sum([l.split() for l in sys.stdin.readlines()], [])
]

cmb = list(combinations(Ai, K))
c = comb(Ai, K)
cc = combination(Ai, K)

a = []
for i in range(len(Ai)):
  print(i)

