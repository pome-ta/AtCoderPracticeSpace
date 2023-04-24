import sys

if sys.platform == 'ios':
  from pathlib import Path
  import clipboard

  _path = Path('./input_file.txt')
  None if _path.exists() else _path.write_text(
    clipboard.get(), encoding='utf-8')
  sys.stdin = open(_path)

# 左右の長さが L [cm]
# N 個の切れ目
# 左から i 番目の切れ目
# 左から A i​ [cm] の位置
# N 個の切れ目のうち K 個
# K+1 個のピースに分割

N, L, K, *As = [
  int(i) for i in sum([l.split() for l in sys.stdin.readlines()], [])
]

