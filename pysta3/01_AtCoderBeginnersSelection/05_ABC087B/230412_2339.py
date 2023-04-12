import sys

if sys.platform == 'ios':
  from pathlib import Path
  import clipboard

  _path = Path('./input_file.txt')
  None if _path.exists() else _path.write_text(
    clipboard.get(), encoding='utf-8')
  sys.stdin = open(_path)

# 500 円玉 A 枚
# 100 円玉 B 枚
#  50 円玉 C 枚
# 合計 X 円
# X 円は、何通り

ratio = [500, 100, 50]
abcs = [y for row in [[r] * int(input()) for r in ratio] for y in row]
x = input()




