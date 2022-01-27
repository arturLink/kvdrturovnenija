from tkinter import *
k=0
def klikker(event):
    global k
    k+=1
    nupp.config(text=k)
def klikker_(event):
    global k
    k-=1
    nupp.config(text=k)
def txt_to_lbl(event):
    t=txt.get()
    lbl.configure(text=t)
    txt.delete(0,END)#start=0, stop=viimane
def valimine():
    valik=var.get()
    lbl.configure(text=valik)
    txt.insert(0,valik)
aken=Tk()
aken.title("Akna nimetus")
aken.geometry("800x500")

nupp=Button(aken,text="Mina olen nupp",font="Arial 20",width=20,bg="#FF6347",fg="#000080",relief=RAISED)
nupp.pack()#place(x=280,y=220)#side=LEFT
nupp.bind("<Button-1>",klikker)
nupp.bind("<Button-3>",klikker_)

lbl=Label(aken,text="...",height=3,width=20,font="Arial 20",fg="green",bg="lightblue",relief="solid")
lbl.pack()

txt=Entry(aken,width=20,font="Arial 20",fg="blue",bg="lightblue", justify=CENTER)
txt.pack()
txt.bind("<Return>",txt_to_lbl)#Enter
