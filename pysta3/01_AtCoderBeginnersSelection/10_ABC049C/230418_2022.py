import sys

if sys.platform == 'ios':
  from pathlib import Path
  import clipboard

  _path = Path('./input_file.txt')
  None if _path.exists() else _path.write_text(
    clipboard.get(), encoding='utf-8')
  sys.stdin = open(_path)

import re


# s, b
def _re_check_match(cmp: list, s: str, b: bool):
  print('t')
  #print(s)
  if s == '':
    return True
  if not (b):
    return False

  for c in cmp:
    print('m')
    print(c)
    m = re.match(c, s)
    print(m)
    if bool(m):
      e = m.end()
      s = s[e:]
      return _re_check_match(cmp, s, True)
  #print('e')
  return _re_check_match(cmp, s, False)


def check_match(cmp: list, s: str, b=True) -> bool:
  return _re_check_match(cmp, s, True)


S = input()

re_matches = [r'^dream', r'^dreamer', r'^erase', r'^eraser']
re_compile = list(map(re.compile, re_matches))

print(check_match(re_compile, S))

