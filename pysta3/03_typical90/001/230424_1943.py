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


def get_score(k, cuts, l):
  pass


def yokan_party():
  pass


def frct(num: int) -> int:
  l = reversed(range(1, num + 1))
  n = 1
  n = [ i for i in l]
  #for i in l:
  #  n *= i
  return n
  
  #for i in 


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

print(frct(5))

