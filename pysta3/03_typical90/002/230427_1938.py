import sys

if sys.platform == 'ios':
  from pathlib import Path
  import clipboard

  _path = Path('./input_file.txt')
  None if _path.exists() else _path.write_text(
    clipboard.get(), encoding='utf-8')
  sys.stdin = open(_path)


def get_bracket(n: int) -> str:
  return ('(' * n) + (')' * n)


N = int(input())

is_possible = True if N % 2 == 0 or N else False

result = ''

if is_possible:
  loop = N // 2
  #s = ('(' * loop) + (')' * loop)
  s_list = []
  for b in range(2):
    if b:
      for l in range(loop):
        s_list.append('()' * l + get_bracket(loop - l))
    else:
      for l in range(loop):
        s_list.append(get_bracket(loop - l) + '()' * l)

#print(result)
'''

((((()))))
 (((()
((((()))))
()(((())))
()()((()))
'''

