import sys

if sys.platform == 'ios':
  from pathlib import Path
  import clipboard

  _path = Path('./input_file.txt')
  None if _path.exists() else _path.write_text(
    clipboard.get(), encoding='utf-8')
  sys.stdin = open(_path)

import re

# d, e => 
'''
dream
dreamer
erase
eraser
'''
'''
dream
dreamer
     erase
     eraser
d =>
  5 => ere, 
  7 => a

'''


def str_check(s):
  if s == '':
    return True
  t = s[0]
  if t == 'd':
    if len(s) > 7:
      dreamer = s[:7] if s[:7] == 'dreamer' else None
      if dreamer:
        c = s[7:]
        if c[0] == 'e' or c[0] == 'd' or c[0] == '':
          return str_check(c)
    if len(s) > 5:
      dream = s[:5] if s[:5] == 'dream' else None
      if dream:
        c = s[5:]
        if (len(c) > 3 and c[2] != 'a') or c[0] == '':
          return str_check(c)
  elif t == 'e':
    erase = s[:5]
    eraser = s[:6]
  else:
    return False


S = input()
re_matches = [r'^dream', r'^dreamer', r'^erase', r'^eraser']
re_compile = list(map(re.compile, re_matches))

a = list(range(10))
print(a)
print(a[:5])
print(a[5:])

#print('YES' if check_match(re_compile, S) else 'NO')

