from collections import deque

# How to use deque 队列

queue = deque(["Eric","John","Michael"])
queue.append("Terry")       #Terry入队
queue.append("Graham")      #Graham入队
print(queue.popleft())      #队首元素出队
#输出：'Eric'
print(queue.popleft())      #队首元素出队
#输出：'John'
print(queue)                #队列剩下元素
#输出：deque(['Michael','Terry','Graham'])


# How to use set 集合
# ---------------------------INFO-----------------------------------
# Python提供了set这种数据结构. set是一种无序的, 不包含重复元素的结构. 一般
# 用来测试是否已经包含了某元素, 或者用来对众多元素们去重. 与数学中的集合论同
# 样, 他支持的运算有交, 并, 差, 对称差.
# 创建一个set可以用 set() 函数或者花括号 {}. 但是创建一个空集是不能使用一个
# 花括号的, 只能用 set() 函数. 因为一个空的花括号创建的是一个字典数据结构.
# ------------------------------------------------------------------

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                       # 去重功能
print('orange' in basket)          # 快速判断元素是否在集合内
print('crabgrass' in basket)

# 两个集合间的运算
a = set('abracadabra')
b = set('alacazam')
print(a)        # 集合a中包含元素
print(a - b)    # 包含与a中但不包含在b中的元素
print(a | b)    # 集合a或b中包含的所有元素
print(a & b)    # 集合a或b中都包含了的元素
print(a ^ b)    # 不同时包含于a和b的元素

