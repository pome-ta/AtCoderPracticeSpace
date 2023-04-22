import sys

if sys.platform == 'ios':
  from pathlib import Path
  import clipboard

  _path = Path('./input_file.txt')
  None if _path.exists() else _path.write_text(
    clipboard.get(), encoding='utf-8')
  sys.stdin = open(_path)

#s = list(map(lambda i: i.split() if isinstance(i, list) else i, sys.stdin.readlines()))

a, b, c, s = []

