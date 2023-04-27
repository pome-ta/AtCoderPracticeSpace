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
'''
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
'''


def min_div(divs: list) -> int:
  order = []
  old_d = 0
  for d in divs:
    order.append(d - old_d)
    old_d = d
  return min(order)


N, L, K, *Ai = [
  int(i) for i in sum([l.split() for l in sys.stdin.readlines()], [])
]

cmbs = combinations(Ai, K)
cmbs_set = [[*c, L] for c in cmbs]

result_list = [min_div(cmb) for cmb in cmbs_set]

print(max(result_list))
