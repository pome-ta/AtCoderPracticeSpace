import sys
if sys.platform == 'ios':
  # todo: そもそも、問題文が存在するか確認した方がいいか
  from pathlib import Path
  question_path = Path('./input_file.txt')
  if not question_path.exists():
    import clipboard
    clipboard_text = clipboard.get()
    
  clipboard_text = clipboard_text.split('\n')
  text = '\n'.join(clipboard_text)
  with open('input_file.txt', 'w') as f:
    f.write(text)
  sys.stdin = open('input_file.txt')

