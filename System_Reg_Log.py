from tkinter import * 

def ispas(x):
    x=list(x)
    lst=[] 
    sym="~!#¤%&/()=?@£$€{[]}*-+.;:_"
    for i in x:
        if i.isdigit(): 
            lst.append(True)
            break 
    for i in x: 
        if i.isupper():
            lst.append(True)
            break 
    for i in x:
        if i.islower():
            lst.append(True)
            break 
    for i in x:
        if i in sym:
            lst.append(True)
            break 
    if len(lst)!=4:
        return False 
    else:
        return all(lst)

def fulk(p,n,s):
    p=p.get()
    p=ispas(p) 
    n=n.get() 
    s=s.get()
    if len(n)==0 or len(s)==0 or p==False:
        return False
    else:
        return True

def kontrol(x,y,z,i,reg):
    p1=x.get()
    p2=y.get()
    n=z.get()
    s=i.get()
    if ispas(p1)==False:
        x.configure(bg="Red")
    else:
        x.configure(bg="White") 
    if p1!=p2:
        y.configure(bg="Red")
    else:
        y.configure(bg="White") 
    if len(n)==0:
        z.configure(bg="Red")
    else:
        z.configure(bg="White") 
    if len(s)==0:
        i.configure(bg="Red")
    else:
        i.configure(bg="White") 
    c=fulk(x,y,z)
    if c==True:
        a=p1+","+n+","+","+s+"\n"
        with open("Sys.txt","a",encoding="utf-8-sig") as f:
            f.write(a)
        reg.destroy()

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
        entrepass=Entry(reg,show="*",font="Arial 20",bg="White")
        lblconfrepass=Label(reg,text="Confirm password: ",font="Arial 20",fg="Black")
        entconfrepass=Entry(reg,show="*",font="Arial 20",bg="White")
        lblsec=Label(reg,text="Salajane sõna: ",font="Arial 20",fg="Black")
        entsec=Entry(reg,font="Arial 20",bg="White")
        btnval=Button(reg,text="Valmis",font="Arial 20",fg="Black",bg="Gray",command=lambda: kontrol(entrepass,entconfrepass,entrename,entsec,reg))

        lst=[lbl,lblrename,entrename,lblrepass,entrepass,lblconfrepass,entconfrepass,lblsec,entsec,btnval]
        for i in range(len(lst)):
            lst[i].pack(pady=50) if i==0 else (lst[i].pack() if i!=9 else lst[i].pack(pady=20))

        reg.mainloop()

    if v==2 or i==1:
        win.destroy()
        log=Tk()
        log.geometry("600x600")
        log.title("Autoriseerimine")
        lbl=Label(log,text="Autoriseerimine",font="Arial 50",fg="Black")
        lblrename=Label(log,text="Name: ",font="Arial 20",fg="Black")
        entrename=Entry(log,font="Arial 20")
        lblrepass=Label(log,text="Password: ",font="Arial 20",fg="Black")
        entrepass=Entry(log,show="*",font="Arial 20")
        btnval=Button(log,text="Valmis",font="Arial 20",fg="Black",bg="Gray")
        lst=[lbl,lblrename,entrename,lblrepass,entrepass,btnval]
        for i in range(len(lst)):
            lst[i].pack(pady=50) if i==0 else (lst[i].pack() if i!=5 else lst[i].pack(pady=20))
        log.mainloop()

    if v==3:
        win.destroy()
        mut=Tk()
        mut.geometry("1200x600")
        mut.title("Nime või parooli muutmine")
        lbl=Label(mut,text="Nime või parooli muutmine",font="Arial 50",fg="Black")
        lblrename=Label(mut,text="Name: ",font="Arial 20",fg="Black")
        entrename=Entry(mut,font="Arial 20")
        lblrepass=Label(mut,text="Password: ",font="Arial 20",fg="Black")
        entrepass=Entry(mut,show="*",font="Arial 20")
        btnval=Button(mut,text="Valmis muutmine",font="Arial 20",fg="Black",bg="Gray")
        lst=[lbl,lblrename,entrename,lblrepass,entrepass,btnval]
        for i in range(len(lst)):
            lst[i].pack(pady=50) if i==0 else (lst[i].pack() if i!=5 else lst[i].pack(pady=20))
        mut.mainloop()
    if v==4:
        win.destroy()

def lop(event):
    win.destroy()

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
btnlop.bind("<Button-1>",lop)

lst=[lbl,rblog,rbreg,rbmut,rbun,btnlop,btngo]
for i in range(len(lst)):
    lst[i].pack(pady=50) if i==0 else (lst[i].pack(side=RIGHT,pady=200,padx=120) if i in [5,6] else lst[i].pack())

win.mainloop()
