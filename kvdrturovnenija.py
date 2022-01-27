from tkinter import *
from math import *

def KvUrov(event):
	D=b*b+4*a*c
	if D>0:
		x1=(-b+sqrt(D))/(2*a)
		x2=(-b-sqrt(D))/(2*a)
	elif D==0:
		x1=(-b+sqrt(D))/(2*a)
	else:
		x1="Нету x"



#Okno
window=Tk()
window.title("Квадратные уравнения")
window.geometry("600x400")

#Zagolovok
zglvk=Label(window,text="Решение квадратного уравнения",height=3,width=30,font="Arial 15",fg="green",bg="lightblue",relief="solid")
zglvk.place(x=137,y=10)
#Uravnenie
r1=Label(window,text="x**2+",height=2,width=7,font="Arial 12",fg="green",bg="white",relief="solid")
r1.place(x=130,y=110)
r2=Label(window,text="x+",height=2,width=4,font="Arial 12",fg="green",bg="white",relief="solid")
r2.place(x=240,y=110)
r3=Label(window,text="=0",height=2,width=4,font="Arial 12",fg="green",bg="white",relief="solid")
r3.place(x=321,y=110)
#Reshenie
lbl=Label(window,text="Решение",height=5,width=40,font="Arial 12",fg="black",bg="yellow",relief="solid")
lbl.place(x=117,y=220)

#A,B,C
a=Entry(window,width=4,font="Arial 12",fg="green",bg="lightblue", justify=CENTER)
a.place(height=43,x=90,y=110)
b=Entry(window,width=4,font="Arial 12",fg="green",bg="lightblue", justify=CENTER)
b.place(height=43,x=200,y=110)
c=Entry(window,width=4,font="Arial 12",fg="green",bg="lightblue", justify=CENTER)
c.place(height=43,x=281,y=110)

#Knopki
Reshit=Button(window,text="Решить",font="Arial 20",height=1,width=6,bg="darkgreen",fg="black",relief=RAISED)
Reshit.place(x=370,y=101)
Reshit.bind("<Button-1>",KvUrov)

window.mainloop()