import sys

if sys.platform == 'ios':
  from pathlib import Path
  import clipboard

  _path = Path('./input_file.txt')
  None if _path.exists() else _path.write_text(
    clipboard.get(), encoding='utf-8')
  sys.stdin = open(_path)

a, b, c, s = [
  int(j) if j.isdecimal() else j
  for j in sum([i.split() for i in sys.stdin.readlines()], [])
]

print(sum([a, b, c]), s)
