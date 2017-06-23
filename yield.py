Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
================= RESTART: F:\python\magic_function\yield.py =================
>>> class MyGen():
    print("生成器被执行")
    yield 1
    yield 2
    
SyntaxError: 'yield' outside function
>>> def MyGen():
    print("生成器被执行")
    yield 1
    yield 2

    
>>> myg= MyGen()
>>> next(myg)
生成器被执行
1
>>> next(myg)
2
>>> next(myg)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    next(myg)
StopIteration
>>> def Fibs()
SyntaxError: invalid syntax
>>> def Fibs():
	a=0
	b=1
	while True:
		a,b = b,a+b
		yield a

		
>>> for each in Fibs():
	if each >100:
		break
	print(each,end=" ")
