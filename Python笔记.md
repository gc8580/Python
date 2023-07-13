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

### 		换行\n,回车\r,水平制表符\t,退格\b

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

