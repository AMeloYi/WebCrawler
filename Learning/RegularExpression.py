# -------------------------------------------------------------------
# 正则表达式
# 资料来源： http://www.runoob.com/python/python-reg-expressions.html
# -------------------------------------------------------------------

import re

# -----How to use re.match-------------------------------------------
print("--- How to use re.match -------------------")
# re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None
# Example 1
print("---- Example 1 ----")
print(re.match('www','www.runoob.com').span())  # 在起始位置匹配
print(re.match('com','www.runoob.com'))         # 不在起始位置匹配

# Examle 2
print("---- Example 2----")
line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!")

# -----How to use re.search-----------------------------------------
print("--- How to use re.search ------------------")
# re.search 匹配整个字符串，直到找到一个匹配
# Example

line = "Cats are smarter than dogs"

matchObj = re.match(r'dogs', line, re.M|re.I)
if matchObj:
    print("match --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")

matchObj = re.search(r'dogs', line, re.M|re.I)
if matchObj:
    print("match --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")

# -----How to use re.sub--------------------------------------------
print("--- How to use re.sub ---------------------")
# re.sub 替换字符串中的匹配项 检索和替换
# -- re.sub(pattern, repl, string, count=0, flags=0)
# -- pattern: 正则中的模式字符串
# -- repl: 替换的字符串，也可以为一个函数
# -- string: 要被查找替换的原始字符串
# -- count: 模式匹配后替换的最大次数， 默认0表示替换所有的匹配

# Example 1
print("---- Example 1 ----")
phone = "2004-959-559 # 这是一个国外电话号码"

# 删除字符串中的 Python注释
num = re.sub(r'#.*$', "", phone)
print("电话号码是: ", num)

# 删除非数字(-)的字符串
num = re.sub(r'\D', "", phone)
print("电话号码是: ", num)

# Example 2 将字符串中的匹配的数字乘以2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)

s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))  # ?P<name> 带命名的分组