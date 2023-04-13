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

score = 0
for i, c in enumerate(cards):
  score += c if (i % 2 == 0) else -c

print(score)

