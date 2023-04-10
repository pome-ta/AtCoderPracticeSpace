import sys
if sys.platform == 'ios':
  import clipboard
  a = clipboard.get()
  a = a.split('\n')
  text = '\n'.join(a)
  with open('input_file.txt', 'w') as f:
    f.write(text)
  sys.stdin = open('input_file.txt')

