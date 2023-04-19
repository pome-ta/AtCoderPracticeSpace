import sys

if sys.platform == 'ios':
  from pathlib import Path
  import clipboard

  _path = Path('./input_file.txt')
  None if _path.exists() else _path.write_text(
    clipboard.get(), encoding='utf-8')
  sys.stdin = open(_path)

import re


def check_match(cmp: list, s: str) -> bool:
  if s == '':
    return True
  for c in cmp:
    m = re.match(c, s)
    if bool(m):
      _s = s[m.end():]
      if _s and _s[0] == 'r':  # eraser?
        #continue
        return check_match(list(reversed(cmp)), s)
      if len(_s) <= 4 and _s[:2] == 'er' and [2] != 'a':  # dreamer?
        #continue
        return check_match(list(reversed(cmp)), s)
      s = _s
      return check_match(cmp, _s)
  return False


S = input()

re_matches = [r'^dream', r'^dreamer', r'^erase', r'^eraser']
re_compile = list(map(re.compile, re_matches))

print('YES' if check_match(re_compile, S) else 'NO')

