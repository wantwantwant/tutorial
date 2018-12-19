resu= str(input('请输入：'))

def is_Chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False
print(is_Chinese("resu"))


def is_number(word):
    """判断一个unicode是否是数字"""
    for number in word:
        if number >= u'\u0030' and number <= u'\u0039':
            return True
        else:
            return False
print(is_number("resu"))


def is_alphabet(word):
    """判断一个unicode是否是英文字母"""
    for en in word:
        if (en >= u'\u0041' and en <= u'\u005a') or (en >= u'\u0061' and en <= u'\u007a'):
           return '是英文'
        else:
           return '不是英文'
print(is_alphabet("resu"))

