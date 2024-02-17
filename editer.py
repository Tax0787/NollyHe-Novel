from tkinter import *
from tkinter.messagebox import showerror as err
from tkinter.messagebox import showinfo as info
from tkinter.filedialog import askopenfilename as select_file
from mn_format import encoding, decoding


class Data:

  def __init__(self, html, length):
    self.html = html
    self.length = length


data = None


class fun1:

  def __init__(self):
    global data
    if data == None:
      err('StateError', 'No File is opend')
      del self
    else:
      self.__line = Tk()
      self.__line.title('HTML SRC')
      self.__ent = Entry(self.__line)
      self.__ent.place(width=1000, height=1414)
      self.__btn = Button(self.__line, text="OK", command=self.__exit)
      self.__btn.pack()
      self.__line.mainloop()

  def __exit(self):
    global data
    data.HTML = int(self.__ent.get())
    self.__line.destroy()


class fun2:

  def __init__(self):
    global data
    if data == None:
      err('StateError', 'No File is opend')
      del self
    else:
      self.__line = Tk()
      self.__line.title('input length of line')
      self.__ent = Entry(self.__line)
      self.__ent.pack()
      self.__btn = Button(self.__line, text="OK", command=self.__exit)
      self.__btn.pack()
      self.__line.mainloop()

  def __exit(self):
    global data
    data.length = int(self.__ent.get())
    self.__line.destroy()


def fun4():
  global data
  if data == None:
    data = Data(None, None)
  with open(select_file()) as f:
    html, length = decoding(f.read())
  data.html = html
  data.length = length


def fun3():
  global data
  if data == None:
    return err('StateError', 'No File is opend')
  with open(select_file(), 'w') as f:
    f.write(encoding(data.html, data.length))


def fun5():
  y = select_file()
  with open(y, 'w') as f:
    f.write("")
    info("File Generated", f"file {y} is successfully generated")


win = Tk()
win.title("Editor")

btn1 = Button(win, text="HTML", command=fun1)
btn1.pack()
btn2 = Button(win, text="line-length", command=fun2)
btn2.pack()
btn3 = Button(win, text="SaveFile", command=fun3)
btn3.pack()
btn4 = Button(win, text="LoadFile", command=fun4)
btn4.pack()
btn5 = Button(win, text="WriteFile", command=fun5)
btn5.pack()

win.mainloop()
