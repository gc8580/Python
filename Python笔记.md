# Jove的Python笔记

## 	输出函数：

### 		格式 Print（）

```Python
#可输出数字、字符串
print('Hello World')
print('123')

#含有运算符的表达式
print(3+1)

#将数据输出文件中 注意点1.所指定的盘符存在；2.使用 file = 文件名对象
fp = open('D:/text.txt','a+') //a+ = 以读写的方式创建文件，如果文件不存在就创建，存在就在文件内容继续追加
print('Hello World',file = fp) //将Hello World输出到文件text当中
fp.close()

#不进行换行输出
print('Hello','World')


```

## 	转义字符

换行\n,回车\r,水平制表符\t,退格\b

​			①换行：\n (newline)

​			②回车：\r (return)

​			③水平制表符：\t (tab)——在不使用表格的情况下在垂直方向按列对齐文本。每8个字符可以看作一个水平制表符，如果遇到 \t 之				前未满8个字符，则 \t 就补空格直到满8个

​			④退格：\b (backspace)

```python
print('Hello\bWorld')  //输出效果：HellWorld （\b退一个格）
print('Hello111111111111111\rWorld') //输出效果：World （\r覆盖之前的内容）

print('\') //最后一个不能是反斜线，因为单引号为转义字符格式 会把引号转义
print('http:\\www.baidu.com')	输出效果：http:\www.baidu.com
print('http:\\\\www.baidu.com')	输出效果：http:\\www.baidu.com
print(r'Hello World') 输出效果：'Hello World'
```

## 二进制字符编码

```Python
print(chr(0b100111001011000))   //输出效果：乘
print(ord(乘))				   //输出效果：20056  十进制的100111001011000
```

## 关键字

```python
import keyword
print(keyword.kwlist)
//输出效果：['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

## 变量的定义和使用

```python
name = 'Jove'
print(name)
print('标识',id(name)) 		// 标识 1540154410800 地址空间
print('类型',type(name))		// 类型 <class 'str'>
print('值',name)				//	值 Jove
name  = 'Jan'				
print('标识',id(name))		// 标识 1540154410608 地址空间
```

## 常见的数据类型

1.整数类型-int (integer)-正数、负数和零

​	十进制——默认;

​	二进制——以0b开头;

​	八进制——以0o开头;

​	十六进制——以0x开头

2.浮点数类型-float-整数、小数

3.布尔类型bool

​		True=1, False=0

4.字符串类型-str (string) 

```python
print('二进制',0b11111111)
print('八进制',0o1111)
print('十六进制',0x111)

n1 = 1.1
n2 = 2.1
print(n1 + n2)  //输出结果 3.2
//因为计算机采用二进制存储数据有偶尔不精确情况，所以浮点型做计算的时候可以采用导入模块的方式。
from decimal import Decimal
print(Decimal('1.1') + Decimal('2.2'))  //输出结果 3.3

print(True + 1) //输出结果 2

print("人生苦短，及时行乐") // 单引号和双引号只能在一行使用
print('''人生苦短， 
及时行乐''') 	//三引号可以换行输出字符串

//类型转换

s2 = '77.133'
print(int(s2),type(int(s2))) 
//将String转成int类型时，字符串必须为数字串（整数），非数字串是不允许转换的

```

## 输入函数

​	格式：present = input('大圣想要什么礼物呢?')

```python
a1 = int(input('第一个数为：'))
a2 = int(input('第二个数为：'))
print(a1 + a2)
//输入的数据为str类型 所以需要用到强制类型转换
```

## 算术运算符

1.标准算术运算符

​	加+、减-、乘*、除/、整除//（向下取整）

2.取余运算符

​	%（9%4=1）

3.幂运算符

​	2**3 = 2的三次方

## 赋值运算符 

1.= (赋值符号)

​	支持链式赋值（执行顺序：右到左）

​	支持系列解包赋值（a,b,c=10,20,30）

​	支持参数赋值（+=,-=,*=,/=,//=,%=）

```python
//交换变量
print(n1 , n2)
n1,n2 = n2,n1
print(n1 , n2)

//多重赋值
n1,n2,n3 = 10,20,30
print(n1,n2,n3)
```

## 比较运算符 

1.<,>,<=,>=,!=

2.==

​	对象value的比较

3.is, is not

​	对象id的比较 

```python
n1 = 10
n4 = 10
print(n1 == n4) //True 比较的是值
print(n1 is n4) //True 比较的是标识及内存地址
print(n1 is not n4) //False
```

## 布尔运算符

​	and, or, not, in, 		

```Python
w = 'helloworld'
print('h' not in w)
//字母h确实存在于字符串W里 所以输出结果为False
```

## 位运算符

![位运算](D:\Github\Python\image\位运算.png)

## 对象布尔值

```Python
//以下结果都为Flase
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(None))
print(bool(''))
print(bool(""))
print(bool([])) 	#空列表
print(bool(list())) #空列表
print(bool(()))		#空元组
print(bool(tuple()))#空元组
print(bool({}))		#空字典
```

## 选择结构

![](D:\Github\Python\image\选择结构.png)

### 单分支结构

```python
#中文语义：如果……就……

#语法结构：if 条件表达式:
money=1000
s=int(input('请输入取款金额'))
if money>=s:
  money=money-s
  print('取款成功，余额为:',money)
else:
   print('取款失败，余额不足')


```

### 双分支结构

```Python
#语法结构：if 条件表达式：
#			 条件执行体1
#		else:
#			 条件执行体2 
```

### 多分支结构



```python
#中文语义:     ……是……？  不是
#             ……是……？  不是
#		  	  ……是……？  不是
#   		  ……是……？  是
 
#语法结构：
#if  条件表达式1：

#   条件执行体1

#elif 条件表达式2：

#   条件执行体2

#elif 条件表达式N：

#   条件执行体N

#else:

#   条件执行体N+1 
score=float(input('请输入一个成绩'))

if score>=90 and score<=100:

  print('A')

elif score>=80 and score<90:

  print ('B')

elif score>=70 and score<80:

  print('C')

elif score>=60 and score<70:

  print('D')

elif score>=0 and score<60:

  print('E')

else:

  print('成绩输入有误') 
```

### Pass语句 

```python
#语句什么都不做，只是一个占位符，用在需要语句的地方
#配套使用：
#if 语句的条件执行体
#for--in语句的循环体
#定义函数的函数体 
#pass语句的使用
answer = input('请问您是会员吗？y/n')
if answer == 'y':
    pass
else :
    pass    
```

## 循环结构

![](D:\Github\Python\image\循环结构.png)

### range函数的使用 

```python
#创建range（）的三种方式
range(stop)  #——创建一个以[0,stop)之间的整数序列，步长为1

r=range(10)

print(list(r)) 

range(start, stop)	#——创建一个(start, stop)之间的整数序列，步长为1

r=range(1, 10)

print(list(r)) 

range(start, stop, step)	#——创建一个(start, stop)之间的整数序列，步长为step

r=range(1,10,2)

print(list(r)) 
```

### while循环 

```python
#语法结构： 
#while 条件表达式:

#  条件执行体（循环体）

#四步循环法
#①初始化变量
#②条件判断
#③条件执行体（循环体）
#④改变变量
#计算0--4之间的累加和

sum=0 #初始变量为0

a=0 #条件判断

while a<5: #条件执行体（循环体）

  sum+=a #改变变量

  a+=1

print('和为',sum)

#1--100的偶数和

a=1

sum=0

while a<=100:

  if a%2==0:

    sum+=a

  a+=1

print('1到100间偶数之和为',sum) 
```

### for_in循环 

```python
#in 表达从（字符串、序列等）中依次取值，又称遍历
#for--in 遍历的对象必须是可迭代对象
#语法结构：
#for 自定义的变量 in 可迭代对象

#     循环体

#使用for循环，计算1到100之间的偶数和

sum=0

for item in range(1,101):

   if item%2==0:

     sum+=item

print(sum)


#100到999的水仙花数

for n in range(100,1000):

  sum=0

  for i in str(n):

    sum=sum+int(i)**3

  if sum==n:

    print(n) 
```

## 流程控制语句 break

```Python
#非正常结束循环 
for item in range(3):

  pwd=input('请输入密码:')

  if pwd=='8888':

    print('密码正确')

    break

  else:

    print('密码不正确') 
```

## 流程控制语句 continue 

```Python
#用于结束当前循环，进入下一次循环，通常与分支结构的if一起使用

#输出1-50之间所有5的倍数

#使用for_in语句

for item in range(1,51):

  if item % 5 == 0:

    print(item)

#使用continue语句

for item in range(1,51):

  if item % 5 != 0:

    continue

  print(item) 
```

## else语句	

①if else ——if 条件不成立，执行else

②while else—— 没有碰到break，执行else

③for else —— 没有碰到break，执行else 

```python
#③for else —— 没有碰到break，执行else 
for item in range(3):

  pwd=input('请输入密码')

  if pwd=='8888':

    print('密码正确')

    break

  else:

    print('密码不正确')

else:

  print('对不起，三次密码均输入错误')


#②while else—— 没有碰到break，执行else
a=0

while a<3:

  pwd = input('请输入密码')

  if pwd == '8888':

    print('密码正确')

    break

  else:

    print('密码不正确')

  a+=1

else:

  print('对不起，三次密码均输入错误') 
```

### 嵌套循环

循环结构中又嵌套了另外的完整循环结构，其中内层循环做为外层循环的循环体执行 

```python
#输出一个三行四列的矩形

for i in range(1,4): #行数，执行三次，一次一行

  for j in range(1,5):

    print('*',end='\t') #末尾换行改为水平制表符，避免换行

  print() #打行

# 9*9乘法表

for i in range(1,10): #行数

  for j in range(1,i+1):

    print(j,'*',i,'=',i*j,end='\t')

  print() 
```

## 二重循环中的 break 和 continue

```python
for i in range(5):

  for j in range(1,11):

    if j%2==0:

      continue #从step1重新开始循环

    print(j,end='\t')

  print() 
```

## 列表

![](D:\Github\Python\image\列表1.png)

![列表2](D:\Github\Python\image\列表2.png)

![列表3](D:\Github\Python\image\列表3.png)

![列表4](D:\Github\Python\image\列表4.png)

![列表5](D:\Github\Python\image\列表5.png)

### 列表的创建

```python
#方法一：[ ]
		lst1=['hello','world',98]

#方法二：使用内置函数list
		lst2=list(['hello','world',98])

#列表特点
#①列表元素按顺序有序排序

lst=['hello','world',98]

print(lst)

#②索引映射唯一个数据

lst=['hello','world',98]

print(lst[0],lst[-3])

#③列表可以存储重复数据

lst=['hello','world',98,'hello']

print(lst[0],lst[-4]) 
```

### 列表的查询操作

1.获取列表中指定元素的索引——index()

​	如查列表中存在N个相同元素，只返回相同元素中的第一个元素的指引
​	如果查询的元素不在列表中，会抛出ValueError
​	可以在指定的start和stop之间查找 

```python
lst=['hello','world',98,'hello']

print(lst.index('hello',0,4)) 
```

2.获取单个元素

- 正向索引从0到N-1

- 逆向索引从-N到-1
- 指定索引不存在，抛出IndexError

3.获取多个元素

​	语法结构：

​		列表名[start:stop:step] 

![](D:\Github\Python\image\列表0.png)

### 列表元素的判断及遍历 

①判断-语法结构： 

​	元素 in/not in 列表名

```python
lst=[10,20,'python','hello']

print(10 in lst)

print(100 in lst)

print(10 not in lst) 
```

