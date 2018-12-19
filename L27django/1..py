# word= str(input('请输入：'))
#
# if word.encode('UTF-8').isdigit():
#     print('是数字')
# if  word.encode( 'UTF-8' ).isalpha():
#     print('shiyingwen')
# else:
#     False
#

resu= str(input('请输入：'))

def is_what(word):
  for ch in word:
     if '\u4e00' <= ch <= '\u9fff':
        return '是中文'
     if ch >= u'\u0030' and ch <= u'\u0039':
        return '是数字'
     if (ch >= u'\u0041' and ch <= u'\u005a') or (ch >= u'\u0061' and ch <= u'\u007a'):
        return '是英文'
     else:
        return False
print(is_what("resu"))