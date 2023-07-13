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

```python
num = int(input('请输出一个整数：'))
if num % 2 == 0 :
    print(num,'是偶数')
else :
    print(num,'不是偶数')
 
//多分枝语句格式如下：
if :

    elif:
       
    elif:
      . 
      .
      .
else:

#pass语句的使用
answer = input('请问您是会员吗？y/n')
if answer == 'y':
    pass
else :
    pass    
```

