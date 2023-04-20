import sys

if sys.platform == 'ios':
  from pathlib import Path
  import clipboard

  _path = Path('./input_file.txt')
  None if _path.exists() else _path.write_text(
    clipboard.get(), encoding='utf-8')
  sys.stdin = open(_path)


def str_check(s):
  if s == '':
    return True
  t = s[0]

  if t == 'e':
    if len(s) >= 6 and s[:6] == 'eraser':
      c = s[6:]
      if c == '' or c[0] == 'e' or c[0] == 'd':
        return str_check(c)
    if len(s) >= 5 and s[:5] == 'erase':
      c = s[5:]
      if c == '' or c[0] == 'e' or c[0] == 'd':
        return str_check(c)

  if t == 'd':
    if len(s) >= 7 and s[:7] == 'dreamer':
      c = s[7:]
      if c == '' or c[0] == 'e' or c[0] == 'd':
        return str_check(c)
    if len(s) >= 5 and s[:5] == 'dream':
      c = s[5:]
      if c == '' or c[0] == 'e' or c[0] == 'd':
        return str_check(c)

  return False


S = str(input()).replace(' ', '')
print('YES' if str_check(S) else 'NO')

