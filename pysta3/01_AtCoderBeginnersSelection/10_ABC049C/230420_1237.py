import sys

if sys.platform == 'ios':
  from pathlib import Path
  import clipboard

  _path = Path('./input_file.txt')
  None if _path.exists() else _path.write_text(
    clipboard.get(), encoding='utf-8')
  sys.stdin = open(_path)

import re


def check_match(cmp, s):
  if s == '':
    return 'YES'
  for c in cmp:
    m = re.match(c, s)
    if bool(m):
      e = m.end()
      _s = s[e:]
      if _s == '' or _s[0] == 'd' or _s[0] == 'e':
        return check_match(cmp, _s)
  return 'NO'


S = input()

re_matches = [r'^dreamer', r'^dream', r'^erase', r'^eraser']
compile = list(map(re.compile, re_matches))

print(check_match(compile, S))

