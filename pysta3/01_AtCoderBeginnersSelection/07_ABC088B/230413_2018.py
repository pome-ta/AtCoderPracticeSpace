import sys

if sys.platform == 'ios':
  from pathlib import Path
  import clipboard

  _path = Path('./input_file.txt')
  None if _path.exists() else _path.write_text(
    clipboard.get(), encoding='utf-8')
  sys.stdin = open(_path)

# N 枚のカード

N = int(input())
cards = sorted(map(int, input().split(' ')), reverse=True)

for i, c in enumerate(cards):
  if not i:
    score = c
  else:
    if (i % 2 == 0):
      score += c
    else:
      score -= c

print(score)
