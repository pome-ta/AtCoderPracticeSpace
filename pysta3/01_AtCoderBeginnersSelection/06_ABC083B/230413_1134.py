import sys

if sys.platform == 'ios':
  from pathlib import Path
  import clipboard

  _path = Path('./input_file.txt')
  None if _path.exists() else _path.write_text(
    clipboard.get(), encoding='utf-8')
  sys.stdin = open(_path)

# N 以下の整数
# A 以上、B 以下
# 

N, A, B = map(int, input().split(' '))
l = range(1, N + 1)

result = 0
for n in l:
  a = sum(map(int, list(str(n))))
  result += n if A <= a and a <= B else 0

print(result)
