import sys

if sys.platform == 'ios':
  from pathlib import Path
  import clipboard

  _path = Path('./input_file.txt')
  None if _path.exists() else _path.write_text(
    clipboard.get(), encoding='utf-8')
  sys.stdin = open(_path)

import re


def check_match(_s, _p):
  for p in _p:
    if not(_s):
      break
    m = re.match(p, _s)
    x=1
    if bool(m):
      e = m.end()
      _s = _s[e:]
      check_match(_s, _p)
  
  return 'NO' if _s else 'YES'


s = input()
result = 'NO'
re_matches = [r'^dream', r'^dreamer', r'^erase', r'^eraser']
compile = map(re.compile, re_matches)

print(check_match(s, compile))

