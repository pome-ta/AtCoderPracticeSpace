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


def min_div(divs: list, min_value: int=0) -> int:
  order = []
  old_d = 0
  for d in divs:
    o = d - old_d
    if o == min_value:
      return o
    order.append(o)
    old_d = d
  return min(order)


N, L, K, *Ai = [
  int(i) for i in sum([l.split() for l in sys.stdin.readlines()], [])
]

min_val = min_div([*Ai, L])

cmbs = combinations(Ai, K)
cmbs_set = [[*c, L] for c in cmbs]

result_list = [min_div(cmb, min_val) for cmb in cmbs_set]

print(max(result_list))

