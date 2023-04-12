import sys

if sys.platform == 'ios':
  from pathlib import Path
  import clipboard
  input_example_path = Path('./input_file.txt')
  None if input_example_path.exists() else input_example_path.write_text(
    clipboard.get(), encoding='utf-8')

  sys.stdin = open(input_example_path)

# n 分整数あり
# 全部偶数だと、2で割れる
# 何回計算したか


def counter(nums, c=0):
  if all([bool(i % 2 == 0) for i in nums]):
    n = [i / 2 for i in nums]
    c = counter(n, c + 1)
  return c


_ = input()
print(counter([int(i) for i in input().split(' ')]))

