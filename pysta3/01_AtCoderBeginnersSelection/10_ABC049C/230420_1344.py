import sys

if sys.platform == 'ios':
  from pathlib import Path
  import clipboard

  _path = Path('./input_file.txt')
  None if _path.exists() else _path.write_text(
    clipboard.get(), encoding='utf-8')
  sys.stdin = open(_path)

import re

S = input()
pattern = r'(dream|dreamer|erase|eraser)*'
result = re.fullmatch(pattern, S)
print('YES' if bool(result) else 'NO')

