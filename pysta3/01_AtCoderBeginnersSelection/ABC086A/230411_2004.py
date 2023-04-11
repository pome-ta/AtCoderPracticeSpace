import sys

if sys.platform == 'ios':
  from pathlib import Path
  input_example_path = Path('./input_file.txt')

  if not input_example_path.exists():
    import clipboard
    input_text = clipboard.get()
    input_example_path.write_text(input_text, encoding='utf-8')
  sys.stdin = open(input_example_path)

a, b = map(int, sys.stdin.readline().split())

print('Even' if ((a * b) % 2 == 0) else 'Odd')

