# Name: Jove
# Time: 2023-07-13 13:57
print(r'Hello111111111111111 World')

import keyword
print(keyword.kwlist)

name = 'Jove'
print(name)
print('标识',id(name))
print('类型',type(name))
print('值',name)
name  = 'Jan'
print('标识',id(name))


print('二进制',0b11111111)
print('八进制',0o1111)
print('十六进制',0x111)

n1 = 1.1
n2 = 2.1
print(n1 + n2)
from decimal import Decimal
print(Decimal('1.1') + Decimal('2.2'))

print(True + 1)

print("人生苦短，及时行乐")
print('''人生苦短，
及时行乐''')
s2 = '77.133'
# print(int(s2),type(int(s2)))

# a1 = int(input('第一个数为：'))
# a2 = int(input('第二个数为：'))
# print(a1 + a2)

print(n1 , n2)
n1,n2 = n2,n1
print(n1 , n2)
n1,n2,n3 = 10,20,30
print(n1,n2,n3)
n1 = 10
n4 = 10
print(n1 == n4)
print(n1 is n4)

w = 'helloworld'
print('h' not in w)


print("-----------")
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(None))
print(bool(''))
print(bool(""))
print(bool([]))
print(bool(list()))
print(bool(()))
print(bool(()))
print(bool(tuple()))
print(bool({}))

num = int(input('请输出一个整数：'))

if num % 2 == 0 :
    print(num,'是偶数')
else :
    print(num,'不是偶数')

answer = input('请问您是会员吗？y/n :')
if answer == 'y':
    pass
else :
    pass