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
  if t == 'd':
    if len(s) >= 7:
      dreamer = s[:7] if s[:7] == 'dreamer' else None
      if dreamer:
        c = s[7:]
        if c[0] == 'e' or c[0] == 'd' or c == '':
          return str_check(c)
    if len(s) >= 5:
      dream = s[:5] if s[:5] == 'dream' else None
      if dream:
        c = s[5:]
        if c == '' or (len(c) > 3 and c[2] != 'a'):
          return str_check(c)

  if t == 'e':
    if len(s) >= 6:
      eraser = s[:6] if s[:6] == 'eraser' else None
      if eraser:
        c = s[6:]
        if c[0] == 'e' or c[0] == 'd' or c[0] == '':
          return str_check(c)
    if len(s) >= 5:
      erase = s[:5] if s[:5] == 'erase' else None
      if erase:
        c = s[5:]
        if c[0] == 'e' or c[0] == 'd' or c[0] == '':
          return str_check(c)
  return False


S = input()
print('YES' if str_check(S) else 'NO')

