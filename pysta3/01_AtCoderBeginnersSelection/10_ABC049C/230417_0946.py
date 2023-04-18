import sys

if sys.platform == 'ios':
  from pathlib import Path
  import clipboard

  _path = Path('./input_file.txt')
  None if _path.exists() else _path.write_text(
    clipboard.get(), encoding='utf-8')
  sys.stdin = open(_path)

import re


def _out_str(_s, _p) -> str:
  pass


def check_match(_s, _p):
  print(_s)
  if _s == '':
    return 'YES'
  for p in _p:
    m = re.match(p, _s)
    x = 1
    print(m)
    if bool(m):
      e = m.end()
      _s = _s[e:]
      check_match(_s, _p)

  return 'NO'


s = input()

re_matches = [r'^dream', r'^dreamer', r'^erase', r'^eraser']
compile = map(re.compile, re_matches)

print(check_match(s, compile))

