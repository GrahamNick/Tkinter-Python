# Python Poll Average by Nick Graham
import ast
from tkinter import *
tk = Tk()
average1 = 0
average2=0
average3=0
average4=0
total=0
try:
  f = open('Data.txt','r')
  user = ast.literal_eval((f.read()))
  f.close()
except:
  user = {}

def addToDict(hour,pet,shoe,grade):
  user[name.get()] = {'Hours':hour, 'Pets':pet, 'Shoes':shoe, 'Grade':grade}
  f = open('Data.txt','w')
  f.write(str(user))
  f.close()
  name.delete(0,END)
  hours.delete(0,END)
  pets.delete(0,END)
  shoes.delete(0,END)
  grades.delete(0,END)
def callback():   #name.get() and hours.get()
  if name.get() in user:
    messagebox.showinfo('Error', name.get() + ' has already been used')
  elif name.get() == '':
    messagebox.showinfo('Error', 'please type your name')

  try:
    hour = float(hours.get())
  except:
    messagebox.showinfo('Error', hours.get() + ' is not acceptable')

  try:
    shoe = int(shoes.get())
  except:
    messagebox.showinfo('Error', shoes.get() + ' is not acceptable')

  try:
    pet = int(pets.get())
  except:
    messagebox.showinfo('Error', pets.get() + ' is not acceptable')

  try:
    grade = int(grades.get())
  except:
    messagebox.showinfo('Error', grades.get() + ' is not acceptable')


  try:
    addToDict(hour,pet,shoe,grade)
  except:
    pass
  
def showData(average1,average2,average3,average4,total):
  for i in user:
    average1 += user[i]['Hours']
    average2 += user[i]['Shoes']
    average3 += user[i]['Pets']
    average4 += user[i]['Grade']
    
  total = len(user)
  if len(user) > 0:
    messagebox.showinfo('Data', 'Out of ' + str(total) + ' answers' + '. The average amount of hours slept is: ' + str(round(average1,1)) + '. The average amount of pets oned is: ' + str(round(average3,0)) + '. The average amount of shoe pairs owned is: ' + str(round(average2,0)) + '. The average grade is: ' + str(round(average4,0)))
  
name = Entry(tk)
name.grid(row=0,column=2)
Label(tk, text='Name:').grid(row=0,column=1)

hours = Entry(tk)
hours.grid(row=1,column=2)
Label(tk, text='How many hours of sleep per night do you usually get when you have school the next day?:').grid(row=1,column=1)

shoes = Entry(tk)
shoes.grid(row=2,column=2)
Label(tk, text='How many pair of shoes do you own?:').grid(row=2,column=1)

pets = Entry(tk)
pets.grid(row=3,column=2)
Label(tk, text='How many pets do you own?:').grid(row=3,column=1)

grades = Entry(tk)
grades.grid(row=4,column=2)
Label(tk, text='What grade are you in?:').grid(row=4,column=1)

data = Button(tk, text='Show data', command= lambda: showData(average1,average2,average3,average4,total))
data.grid(row=5,column=2)

btn1 = Button(tk, text="Submit",command = lambda: callback())
btn1.grid(row=5,column=1)

btn4 = Button(tk, text='Quit', command=tk.destroy)
btn4.grid(row=5)

mainloop()
