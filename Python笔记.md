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

### 列表元素的增加 

​	1.append()

​		在列表的末尾添加一个元素 

```python
lst=[10,20,30]

print('添加元素之前',lst,id(lst))

lst.append(100)

print('添加元素之后',lst,id(lst)) 
```

​	2.extend() 

​		在列表的末尾至少添加一个元素	

```python
lst2=['hello','world']

lst.extend(lst)

print(lst) 
```

​	3.insert() 

​		 在列表的任意位置添加一个元素

```python
lst.insert(1,90)

print(lst) 
```

​	4.切片

​		 在列表的任意位置至少添加一个元素

```python
lst3=[True,False,'hello']

lst[1:]=lst3

print(lst) 
```

### 列表元素的删除

​	1.remove()

​		一次删除一个元素，重复元素只删除第一个

```python
lst=[10,20,30,40,50,60,30]

lst.remove(30)

print(lst) 
#从列表中移除一个元素，如果有重复元素只移除第一个
```

​	2.pop()

​		删除一个指定索引位置上的元素，不指定索引则删除列表最后一个元素 

```python
lst.pop(1)

print(lst) 
```

​	3.切片

​		一次至少删除一个元素（会产生一个新的列表对象）

```python
new_list=lst[1:3]

print('原列表',lst)

print('切片后的列表',new_list) 
```

​	4.clear()

​		清空列表 

```python
lst.clear()

print(lst) 
```

​	5.del

​		删除列表

```python
del lst 
```

### 列表元素的修改 

​	1.为指定索引的元素赋予一个新值

```python
lst=[10,20,30,40]

lst[2]=100

print(lst) 
```

​	2.为指定的切片赋予一个新值

```python
lst[1:3]=[300,400,500,600]

print(lst) 
```

### 列表元素的排序

1.方法一：调用sort()，列中所有元素默认按照从小到大顺序（升序）排序，可以指定reverse=True进行降序排序

```python
lst=[20,40,10,98,54]

print('排序前的列表',lst)

#开始排序，默认升序

lst.sort()

print('排序后的列表',lst,id(lst))

#通过指定关键字参数，将列表元素降序排序

lst.sort(reverse=True) #T:降序；F:升序

print(lst)  
```

2.方法二：调用内置函数sorted()，可以指定reverse=True进行降序排序。该方法会产生新的列表对象，原列表不变

```python
lst=[20,40,10,98,54]

print('原列表',lst)

#开始排序，默认升序

new_list=sorted(lst)

print(lst)

print(new_list)

#通过指定关键字参数，将列表元素降序排序

desc_list=sorted(lst,reverse=True)

print(desc_list) 
```

### 列表生成式 

​	语法格式：
​		[i*i for i in range(1,10)] 

（i*i→表示列元素的表达式	i→自定义变量	range(1,10)→可迭代对象） 

```python
lst=[i*2 for i in range(1,11)]

print(lst)

#输出[2，4，6，8，10] 
```

## 字典

![](D:\Github\Python\image\字典.png)

- 内置数据结构之一，与列表同属可变序列
- 以键值对的方式存储数据，字典是无序序列 

### 字典基础操作

1.字典的创建

```python
#①大括号{}

	scores={'张三':100,'李四':98,'王五':45}

#②内置函数dict()

	scores=dict(name='jack',age=20)
```

2.字典中元素的获取

```python
#①[]

    scores['张三']

	print(scores['张三'])

#	（元素不存在将报错）

#②get()

	scores.get('张三')
    
	print(scores.get('张三'))     #输出结果None
	
    print(scores.get('张三',99))  #输出结果 99
#	（元素不存在将输出None） 
```

3.key的判断

```python
#①in

print('张三' in scores)

#②not in

print('张三' not in scores) 
```

4.字典元素的新增/修改

```python
scores['Jack']=90 
```

5.字典元素的删除

```python
del scores['张三'] 
```

### 获取字典视图

​	1.keys()

​		获取字典中所有key

```python
keys=scores.keys()

print(keys)

print(type(keys))

print(list(keys))  #将所有键转换为列表list
```

​	2.values()

​		获取字典中所有value

```python
values=scores.values()

print(values)

print(type(values))

print(list(values)) #将所有值转换为列表list
```

​	3.items()

​		获取字典中所有key,value对

```python
items=scores.items()

print(items)

print(list(items)) #将所有键值对转换为列表list
```

### 字典元素的遍历

for item in scores:
        print(item) 

```python
scores={'张三':100,'李四':98,'王五':45}

for item in scores:

  print(item,scores[item],scores.get(item)) 
```

### 字典生成式 

- 内置函数zip() 
- item.upper(): price for item,price in zip(items,prices)

```python
items=['Fruits','Book','Others']

prices=[96,78,85]

d={item. upper():price for item, price in zip(items,prices)}

print(d) 
```

![](D:\Github\Python\image\字典的特点（总结）.png)

## 元组

Python内置的数据结构之一，是一个不可变数列 

### 元组创建方式

​	1.小括号**()**

```python
t1=('Python','world',98)

print(t1)

print(type(t1))
```

​	2.内置函数**tuple()**

```python
t2=tuple(('Python','world',98))

print(t2)

print(type(t2))
```

- 只包含一个元组的元素需要使用逗号和小括号，否则会被误认为int,str等类型

```python
t3=('Python',)

print(t3)

print(type(t3))
```

### 元组对象是否可以引用

- 若元组中的对象本身是不可变对象，则不能再引用其他对象
- 若元组中的对象本身是可变对象，则可变对象的引用不允许改变，但数据可以改变

```python
t=(10,[20,30],9)

print(t)

print(type(t))

print(t[0],type(t[0]),id(t[0]))

print(t[1],type(t[1]),id(t[1]))

print(t[2],type(t[2]),id(t[2]))

#[1]=100 报错：SyntaxError: cannot assign to literal

t[1].append(100) #向列表中添加元素

print(t,id(t[1])) #列表内存地址不变
```

### 元组的遍历

​	1.方法一：索引

```python
t=('Python','world',98)

'''第一种获取元组元素的方式，索引'''

print(t[0])

print(t[1])

print(t[2])

#print(t[3]) IndexError: tuple index out of range
```

​	2.方法二：遍历

```python
'''第二种获取元组元素的方式，遍历元组'''

for item in t:

  print(item)
```

## 集合

![](D:\Github\Python\image\集合1.png)

![](D:\Github\Python\image\集合2.png)

### 集合的创建

​	1.使用**{}**

```python
s={2,3,4,5,5,6,7,7}

print(s) #不允许重复
```

​	2.使用内置函数**set()**

```python
s1=set(range(6))

print(s1,type(s1))

s2=set([1,2,4,5,5,5,6,6])

print(s2,type(s2))

s3=set((1,2,4,4,5,65)) #集合中的元素是无序的

print(s3,type(s3))

s4=set('Python')

print(s4,type(s4))
```

### 集合基础操作

​	1.判断

​		**①in/not in**

```python
s={10,20,30,405,60}

print(10 in s)

print(100 in s)

print(50 not in s)
```

​	2.新增

​		**①add()**

```python
s.add(80)

print(s)
```

​		**②update()**

```python
s.update({200,400,300})

print(s)

s.update([100,123,456])

s.update((12,52,48))

print(s)
```

​	3.删除

​		**①remove()**

​			一次删除一个指定元素，若指定元素不存在抛出KeyError

​		**②discard()**

​			一次删除一个指定元素，若指定元素不存在不抛异常

​		**③pop()**

​			一次删除一个任意元素

​		**④clear()**

​			清空集合

### 集合间关系判断

1.是否相等

- **==/!=**

```python
s={10,20,30,40}

s1={30,40,20,10}

print(s==s1) #True

print(s!=s1) #False
```

2.一个集合是否为另一个集合的子集

- **issubset**

```python
s1={10,20,30,40,50,60}

s2={10,20,30,40}

s3={10,20,90}

print(s2.issubset(s1)) #True

print(s3.issubset(s1)) #False
```

3.一个集合是否为另一个集合的超集（母集）

- **issuperset**

```python
print(s1.issuperset(s2)) #True

print(s1.issuperset(s3)) #False
```

4.两个集合是否没有交集

- **isdisjioint**

```python
print(s2.isdisjoint(s3)) #False

s4={100,200,300}

print(s2.isdisjoint(s4)) #True
```

### 集合的数学操作

- 示意图  **返回值都为Boolean类型**

![](D:\Github\Python\image\集合示意图.png)

1.交集

- **intersection / &**

```python
s1={10,20,30,40}

s2={20,30,40,50,60}

print(s1.intersection(s2))

print(s1 & s2)
```

2.并集

- **union / |**

```python
print(s1.union(s2))

print(s1 | s2) #union=|

print(s1)

print(s2)
```

3.差集

- **difference / -**

```python
print(s1.difference(s2))

print(s1-s2) #difference=-

print(s1)

print(s2)
```

4.对称差集

- **symmetric_difference / ^**

```python
print(s1.symmetric_difference(s2))

print(s1^s2) #symmetric_difference=^
```

### 集合生成式

- **{i\*i for i in range()}**
- 将列表生成式中的[]改为{}即可

```python
#列表生成式

lst=[i*i for i in range(10)]

print(lst)

#集合生成式

lst={i*i for i in range(10)}

print(lst)
```

## 四种数据类型的使用场景

 列表：

- 存储相同类型的数据。
- 通过迭代遍历，在循环体内部，针对列表中的每一项元素，执行相同的操作。

元组：

- 函数的参数和返回值。

- 格式化字符串，格式化字符串后面的（）本质上就是一个元祖。
- 让列表不可以修改，保护数据安全。

集合：

- 有序的列表   
- 使用集合做排行榜等类型的场景   

字典：

- 需要多个键值对，可作为某个事务的说明。
- 将多个字典放在一个列表中，再进行遍历，再循环体内针对每一个字典进行相同的处理。

![](D:\Github\Python\image\区别1.png)

![](D:\Github\Python\image\总结1.png)

## 字符串

![](D:\Github\Python\image\字符串1.png)

![字符串2](D:\Github\Python\image\字符串2.png)

![字符串3](D:\Github\Python\image\字符串3.png)

### 字符串的创建与滞留机制

- 驻留机制的几种情况：

1.字符串长度为0或1时

2.符合标识符的字符串（字母、数字、下划线）

3.字符串只在编译时驻留，运行时不会

4.[-5，256]之间的整数数字

### 字符串常用操作

#### 1.查询

①**index（）**

​	查找子串substr第一次出现的位置，如果查找的子串不存在时，则抛出ValueError

```python
s='hello,hello'

print(s.index('lo')) #3

print(s.find('lo')) #3

print(s.rindex('lo')) #9

print(s.rfind('lo')) #9
```

②**rindex（）**

​	查找子串substr最后一次出现的位置，如果查找的子串不存在时，则抛出ValueError

③**find()**

​	查找子串substr第一次出现的位置，如果查找的子串不存在时，则返回-1

④**rfind()**

​	查找子串substr最后一次出现的位置，如果查找的子串不存在时，则返回-1

#### 2.大小写转换

①**upper()**

​	把字符串中所有字符转成大写字母

```python
s='hello,python'

a=s.upper() #转成大写后，会产生一个新的字符串对象

print(a,id(a))

print(s,id(s))
```

②**lower()**

​	把字符串中所有字符转成小写字母

```python
b=s.lower() #转成小写后，会产生一个新的字符串对象

print(b,id(b))

print(s,id(s))

print(b==s)

print(b is s) #False
```

③**swapcase()**

​	把字符串中所有大写字母转成小写字母，小写字母转成大写字母

```python
s2='hello,Python'

print(s2.swapcase())
```

④**capitalize()**

​	把第一个字符转换为大写，把其余字符转成小写字母

```python
print(s2.capitalize())
```

⑤**title()**

​	把每个单词的第一个字符转换为大写，把每个单词的剩余字符转换为小写

```python
print(s2.title())
```

#### 3.对齐

①**center()**

​	居中对齐，第一个参数指定宽度，第二个参数指定填充符，第二个参数可选，默认空格，如果设置宽度小于实际宽度则返回原字符串

```python
s='hello,Python'

print(s.center(20,'*'))
```

②**ljust()**

​	左对齐，第一个参数指定宽度，第二个参数指定填充符，第二个参数可选，默认空格，如果设置宽度小于实际宽度则返回原字符串

```python
print(s.ljust(20,'*'))

print(s.ljust(10))
```

③**rjust()**

​	右对齐，第一个参数指定宽度，第二个参数指定填充符，第二个参数可选，默认空格，如果设置宽度小于实际宽度则返回原字符串

```python
print(s.rjust(20,'*'))

print(s.rjust(10))
```

④**zfill()**

​	右对齐，左边用0填充，该方法只接收一个参数，用于指定字符串的宽度，如果指定的宽度小于字符串的长度，则返回字符串本身

```python
print(s.zfill(20))

print(s.zfill(10))

print('-8910'.zfill(8))
```

#### 4.劈分

①**split()**

- 从字符串的左边开始劈分，默认的劈分字符是空格字符串，返回的值都是一个列表
- 以通过参数sep指定劈分字符串是的劈分符
- 通过参数maxsplit指定劈分字符串时的最大劈分次数，在经过最大次劈分之后，剩余的子串会单独做为一部分

```python
s='hello world Python'

lst=s.split()

print(lst) #未指定劈分字符，默认空格

s1='hello|world|Python'

print(s1.split(sep='|'))

print(s1.split(sep='|',maxsplit=1))
```

②**rsplit()**

- 从字符串的右边开始劈分，默认的劈分字符是空格字符串，返回的值都是一个列表
- 以通过参数sep指定劈分字符串是的劈分符
- 通过参数maxsplit指定劈分字符串时的最大劈分次数，在经过最大次劈分之后，剩余的子串会单独做为一部分

```python
print(s.rsplit())

print(s1.rsplit(sep='|'))

print(s1.rsplit(sep='|',maxsplit=1)) #产生区别
```

#### 5.判断

①**isidentifier()**

判断指定的字符串是不是合法的标识符

②**isspace()**

判断指定的字符串是否全部由空白字符组成(回车、换行，水平制表符)

③**isalpha()**

判断指定的字符串是否全部由字母组成

④**isdecimal()**

判断指定字符串是否全部由十进制的数字组成

⑤**isnumeric()**

判断指定的字符串是否全部由数字组成

⑥**isalnum()**

判断指定字符串是否全部由字母和数字组成

#### 6.替换

- **replace()**

第1个参数指定被替换的子串，第2个参数指定替换子串的字符串，该方法返回替换后得到的字符串，替换前的字符串不发生变化，调用该方法时可以通过第3个参数指定最大替换次数

```python
s='hello,Python'

print(s.replace('python','Java'))

s1='hello,Python,Python,Python'

print(s1.replace('Python','Java',2))
```

#### 7.合并

- **join()**

将列表或元组中的字符串合并成一个字符串

```python
lst=['hello','java','Python']

print('|'.join(lst))

print(''.join(lst))



t=('hello','Java','Python')

print(''.join(t))

print('*'.join('Python'))
```

### 字符串的比较操作

- 运算符：**>,>=,<,<=,==,!=**
- 比较规则

​	首先比较两个字符串中的第一个字符，如果相等则继续比较下一个字符，依次比较下去，直到两个字符串中的字符不相等时，其比较结果就是两个字符串的比较结果，两个字符串中的所有后续字符将不再被比较

- 比较原理

​	两上字符进行比较时，比较的是其ordinal value(原始值)，调用内置函数ord可以得到指定字符的ordinal value。与内置函数ord对应的是内置函数chr调用内置函数chr时指定ordinal value可以得到其对应的字符

```python
print('apple'>'app')

print('apple'>'banana')

print(ord('a'),ord('b'))

print(chr(97),chr(98))
```

### 字符串的切片操作

- 字符串是不可变类型；不具备增删改等操作；切片操作将产生新的对象

```python
s='hello,Python'

s1=s[:5] #未指定起始位置，从0开始切

s2=s[6:] #未指定结束位置，切到字符串最后一个元素

s3='!'

newstr=s1+s3+s2



print(s1)

print(s2)

print(newstr)

print(id(s))

print(id(s1))

print(id(s2))

print(id(newstr))



print(s[1:5:1]) #从1开始截到5（不含5），步长1（0→）

print(s[::-1]) #从字符串最后一个元素开始（←-1）
```

### 格式化字符串

1.**%**作占位符

![](D:\Github\Python\image\格式化字符串1.png)

```python
name='张三'

age=20

print('我叫%s,今年%d岁' % (name,age))
```

2.**{}**作占位符

![](D:\Github\Python\image\格式化字符串2.png)

```python
print('我叫{0},今年{1}岁'.format(name,age))
```

3.**f-string**

```python
print(f'我叫{name},今年{age}岁')



print('%10d' % 99) #10表示的是宽度

print('%.3f' % 3.1415926) #.3表示的是精度（小数点后几位）

print('%10.3f' % 3.1415926) #同时表示宽度和精度

print('{0:.3}'.format(3.1415926)) #此处.3表示一共三位有效数字

print('{0:.3f}'.format(3.1415926)) #此处，.3f表示小数点后三位

print('{:.3f}'.format(3.1415926)) #0表示占位符顺序，可省略
```

### 字符串的编码转换

- 编码：将字符串转换为二进制数据（bytes）
- 解码：将bytes类型的数据转换成字符串类型

![](D:\Github\Python\image\字符串编码.png)

```python
s='天涯共此时'

#编码

print(s.encode(encoding='GBK')) #在GBK这种编码格中，一个中文占两个字节

print(s.encode(encoding='UTF-8')) #在UFT-8这种编码格式中，一个中文占三个字节

#解码

byte=s.encode(encoding='GBK')

print(byte.decode(encoding='GBK'))
```

**函数**

