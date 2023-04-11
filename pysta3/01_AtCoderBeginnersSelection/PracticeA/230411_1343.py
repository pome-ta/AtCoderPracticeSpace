import sys
if sys.platform == 'ios':
  from pathlib import Path
  # todo: そもそも、input text が存在するか確認した方がいいか
  input_text: str = ''
  question_path = Path('./input_file.txt')

  if question_path.exists():
    input_text = question_path.read_text()
  else:
    import clipboard
    input_text = clipboard.get()
    question_path.write_text(input_text, encoding='utf-8')

  sys.stdin = input_text

a = input()
