if sys.platform == 'ios':
  import sys
  input_text: str = ''
  # todo: そもそも、input text が存在するか確認した方がいいか
  from pathlib import Path
  question_path = Path('./input_file.txt')
  if question_path.exists():
    input_text = question_path.read_text()
  else:
    import clipboard
    input_text = clipboard.get()
    question_path.write_text(input_text, encoding='utf-8')

  sys.stdin = input_text

