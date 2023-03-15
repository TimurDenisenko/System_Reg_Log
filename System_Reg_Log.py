from tkinter import * 

def stul(event):
    v=var.get()
    if v==1:
        win.destroy()
        reg=Tk()
        reg.geometry("600x600")
        reg.title("Registreerimine")

        lbl=Label(reg,text="Registreerimine",font="Arial 50",fg="Black")
        lblrename=Label(reg,text="Name: ",font="Arial 20",fg="Black")
        entrename=Entry(reg,font="Arial 20")
        lblrepass=Label(reg,text="Password: ",font="Arial 20",fg="Black")
        entrepass=Entry(reg,show="*",font="Arial 20")
        lblconfrepass=Label(reg,text="Confirm password: ",font="Arial 20",fg="Black")
        entconfrepass=Entry(reg,show="*",font="Arial 20")

        lst=[lbl,lblrename,entrename,lblrepass,entrepass,lblconfrepass,entconfrepass]
        for i in range(len(lst)):
            lst[i].pack(pady=50) if i==0 else lst[i].pack()

        reg.mainloop()

win=Tk()
win.geometry("900x900")
win.title("System")

var=IntVar()

lbl=Label(win,text="LilleTool",font="Arial 50",fg="Black")
rbreg=Radiobutton(win,text="Registreerimine",font="Arial 30",fg="Green",variable=var,value=1)
rblog=Radiobutton(win,text="Autoriseerimine",font="Arial 30",fg="Blue",variable=var,value=2)
rbmut=Radiobutton(win,text="Nime või parooli muutmine",font="Arial 30",fg="Orange",variable=var,value=3)
rbun=Radiobutton(win,text="Unustanud parooli taastamine",font="Arial 30",fg="Orange",variable=var,value=4)
btngo=Button(win,text="Alusta",font="Arial 30",fg="Black",bg="Green")
btnlop=Button(win,text="Lõpetamine",font="Arial 30",fg="Black",bg="Red")

btngo.bind("<Button-1>",stul)

lst=[lbl,rblog,rbreg,rbmut,rbun,btnlop,btngo]
for i in range(len(lst)):
    lst[i].pack(pady=50) if i==0 else (lst[i].pack(side=RIGHT,pady=200,padx=120) if i in [5,6] else lst[i].pack())

win.mainloop()
