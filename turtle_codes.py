Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t = turtle.Pen()
>>> t.shape('turtle')
>>> t.forward(200)
>>> t.left(90)
>>> t.forward(200)
>>> t.left(90)
>>> t.forward(200)
>>> t.left(90)
>>> t.forward(200)
>>> t.left(90)
>>> 
>>> t.reset()
>>> for i in range(4):
	t.forward(200)
	t.left(90)

	
>>> t.reset()
>>> for i in range(40):
	t.forward(5 * i)
	t.left(45)

	
>>> t.reset()
>>> t.speed(0)
>>> for i in range(200):
	t.forward(2 * i)
	t.left(45)

	
>>> t.reset()
>>> for i in range(40):
	t.circle(2 * i)
	t.left(45)

	
Traceback (most recent call last):
  File "<pyshell#26>", line 2, in <module>
    t.circle(2 * i)
  File "C:\Python38\lib\turtle.py", line 1990, in circle
    self.speed(speed)
  File "C:\Python38\lib\turtle.py", line 2174, in speed
    self.pen(speed=speed)
  File "C:\Python38\lib\turtle.py", line 2459, in pen
    self._update()
  File "C:\Python38\lib\turtle.py", line 2663, in _update
    screen._delay(screen._delayvalue) # TurtleScreenBase
  File "C:\Python38\lib\turtle.py", line 566, in _delay
    self.cv.after(delay)
  File "C:\Python38\lib\tkinter\__init__.py", line 799, in after
    self.tk.call('after', ms)
KeyboardInterrupt
>>> t.reset()
>>> t.speed(0)
>>> for i in range(100):
	t.circle(2 * i)
	t.left(45)

	
>>> t.reset()
>>> t.color('red')
>>> for i in range(50):
	t.circle(2 * i)
	t.left(45)

	
Traceback (most recent call last):
  File "<pyshell#34>", line 2, in <module>
    t.circle(2 * i)
  File "C:\Python38\lib\turtle.py", line 1990, in circle
    self.speed(speed)
  File "C:\Python38\lib\turtle.py", line 2174, in speed
    self.pen(speed=speed)
  File "C:\Python38\lib\turtle.py", line 2459, in pen
    self._update()
  File "C:\Python38\lib\turtle.py", line 2663, in _update
    screen._delay(screen._delayvalue) # TurtleScreenBase
  File "C:\Python38\lib\turtle.py", line 566, in _delay
    self.cv.after(delay)
  File "C:\Python38\lib\tkinter\__init__.py", line 799, in after
    self.tk.call('after', ms)
KeyboardInterrupt
>>> import random
>>> colors = ['red','blue','green','black']
>>> import random
>>> t.reset()
>>> t.speed(0)
>>> for i in range(100):
	t.color(random.choice(colors))
	t.circle(2 * i)
	t.left(45)

	
>>> 