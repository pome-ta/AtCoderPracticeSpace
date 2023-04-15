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

#20 196000

#1000 1234000
# 1234
#14 27 959


N, Y = map(int, input().split(' '))
result = [-1, -1, -1]

ratio = [10000, 5000, 1000]
y = int(Y / ratio[2])

# N = m + g + s
# Y = (m * 10) + (g * 5) + (s * 1)

#print(result)

