from tkinter import * 

def ispas(x):
    lg=[]
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

def fulk(p,p1,n,s):
    lg=[]
    with open("Sys.txt","r",encoding="utf-8-sig") as f:
        for i in f:
            lg.append(i.strip().split(","))
    p=p.get()
    pu=ispas(p)
    p1=p1.get()
    n=n.get() 
    s=s.get()
    if p!=p1 or len(n)==0 or n in [j[0] for j in lg] or len(s)==0 or pu==False:
        return False
    else:
        return True

def mutfunc(x,y,m):
    lg=[]
    with open("Sys.txt","r",encoding="utf-8-sig") as f:
        for i in f:
            lg.append(i.strip().split(","))
    x1=x.get()
    y1=y.get()
    if x1 not in [j[0] for j in lg]:
        x.configure(bg="Red")
    else:
        x.configure(bg="White")
    if len(y1)==0 or y1==x1 or y1 in [j[m] for j in lg]:
        y.configure(bg="Red")
    else:
        y.configure(bg="White")
    if x1 in [j[m] for j in lg] and len(y1)!=0 and y1!=x1 and y1 not in [j[m] for j in lg]:
        ind=[j[m] for j in lg].index(x1) 
        lg[ind][m]=y1
        lg1=[]
        for i in lg:
            lg1.extend(i)
        for i in range(0,len(lg1)):
            lg1[i]+=","
        for i in range(0,len(lg1),3):
            if i!=0: lg1.insert(i,"\n")
        print(lg1)
        with open("Sys.txt","w",encoding="utf-8-sig") as f:
            f.writelines(lg1)

def mut():
    lg=[]
    with open("Sys.txt","r",encoding="utf-8-sig") as f:
        for i in f:
            lg.append(i.strip().split(","))
    global var
    nwin=Tk()
    nwin.geometry("600x600")
    nwin.title("Muuda nimi") 
    lblt=Label(nwin,text="Muuda nimi",font="Arial 20")
    lbln=Label(nwin,text="Kirjuta praegune nimi",font="Arial 20")
    entn=Entry(nwin,bg="White",fg="Black",font="Arial 20")
    lblnn=Label(nwin,text="Kirjuta uus nimi",font="Arial 20")
    entnn=Entry(nwin,bg="White",fg="Black",font="Arial 20") 
    btnv=Button(nwin,text="Muuda",bg="Gray",fg="Black",font="Arial 20", command=lambda: mutfunc(entn,entnn,0)) 
    lblt.pack(pady=50)
    lst=[lbln,entn,lblnn,entnn,btnv]
    for item in lst:
        item.pack()

    nwin.mainloop()

def mut1():
    lg=[]
    with open("Sys.txt","r",encoding="utf-8-sig") as f:
        for i in f:
            lg.append(i.strip().split(","))
    global var
    nwin=Tk()
    nwin.geometry("600x600")
    nwin.title("Muuda parool") 
    lblt=Label(nwin,text="Muuda parool",font="Arial 20")
    lbln=Label(nwin,text="Kirjuta praegune parool",font="Arial 20")
    entn=Entry(nwin,bg="White",fg="Black",font="Arial 20")
    lblnn=Label(nwin,text="Kirjuta uus parool",font="Arial 20")
    entnn=Entry(nwin,bg="White",fg="Black",font="Arial 20") 
    btnv=Button(nwin,text="Muuda",bg="Gray",fg="Black",font="Arial 20", command=lambda: mutfunc(entn,entnn,1)) 
    lblt.pack(pady=50)
    lst=[lbln,entn,lblnn,entnn,btnv]
    for item in lst:
        item.pack()
    nwin.mainloop()

def lug(lst,entx,enty,win,o):
    x=entx.get()
    y=enty.get()
    msx=[]
    msy=[]
    for i in lst: 
        msx.append(i[0])
    for i in lst:
        msy.append(i[1])
    if x in msx:
        entx.configure(bg="White")
    else:
        entx.configure(bg="Red")
    if y in msy:
        enty.configure(bg="White")
    else:
        enty.configure(bg="Red")
    if x in msx and y in msy and o==1: 
        win.destroy()
        sis=Tk()
        sis.geometry("500x500")
        sis.title("Welcome!")
        lblsis=Label(sis,text="Te olete süsteemis!",font="Arial 30")
        lblsis.pack(pady=100)
        sis.mainloop()
    elif x in msx and y in msy and o==0: 
        bt=Button(win,text="Muuda nimi",font="Arial 20",fg="Black",bg="Gray",command=mut)
        bt1=Button(win,text="Muuda parool",font="Arial 20",fg="Black",bg="Gray",command=mut1)
        bt.pack(side=LEFT)
        bt1.pack(side=LEFT)

def kontrol(x,y,z,i,btn):
    lg=[]
    with open("Sys.txt","r",encoding="utf-8-sig") as f:
        for o in f:
            lg.append(o.strip().split(","))
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
    if len(n)==0 or n in [j[0] for j in lg]:
        z.configure(bg="Red")
    else:
        z.configure(bg="White") 
    if len(s)==0:
        i.configure(bg="Red")
    else:
        i.configure(bg="White") 
    c=fulk(x,y,z,i)
    if c==True:
        btn.destroy()
        a=n+","+p1+","+s+"\n"
        with open("Sys.txt","a",encoding="utf-8-sig") as f:
            f.write(a)

def stul(win=None):
    if win: win.destroy()
    global var
    v=var.get() 
    lg=[]
    with open("Sys.txt","r",encoding="utf-8-sig") as f:
        for i in f:
            lg.append(i.strip().split(","))
    if v==1: 

        reg=Tk()
        reg.geometry("600x800")
        reg.title("Registreerimine")
        var=IntVar()
        lbl=Label(reg,text="Registreerimine",font="Arial 50",fg="Black")
        lblrename=Label(reg,text="Name: ",font="Arial 20",fg="Black")
        entrename=Entry(reg,font="Arial 20")
        lblrepass=Label(reg,text="Password: ",font="Arial 20",fg="Black")
        entrepass=Entry(reg,show="*",font="Arial 20",bg="White")
        lblconfrepass=Label(reg,text="Confirm password: ",font="Arial 20",fg="Black")
        entconfrepass=Entry(reg,show="*",font="Arial 20",bg="White")
        lblsec=Label(reg,text="Salajane sõna: ",font="Arial 20",fg="Black")
        entsec=Entry(reg,font="Arial 20",bg="White")
        btnval=Button(reg,text="Valmis",font="Arial 20",fg="Black",bg="Gray",command=lambda: kontrol(entrepass,entconfrepass,entrename,entsec,btnval))
        rlog=Radiobutton(reg,text="Autoriseerimine",font="Arial 20",fg="Blue",variable=var,value=2)
        blog=Button(reg,text="Autoriseerimine",font="Arial 20",fg="Blue",bg="Gray", command=lambda: stul(reg))

        lst=[lbl,lblrename,entrename,lblrepass,entrepass,lblconfrepass,entconfrepass,lblsec,entsec,btnval]
        for i in range(len(lst)):
            lst[i].pack(pady=50) if i==0 else (lst[i].pack() if i!=9 else lst[i].pack(pady=20))
        rlog.pack(side=LEFT)
        blog.pack(side=LEFT)
        reg.mainloop()

    if v==2:
        log=Tk()
        log.geometry("600x600")
        log.title("Autoriseerimine")
        lbl=Label(log,text="Autoriseerimine",font="Arial 50",fg="Black")
        lblloname=Label(log,text="Name: ",font="Arial 20",fg="Black")
        entloname=Entry(log,font="Arial 20")
        lbllopass=Label(log,text="Password: ",font="Arial 20",fg="Black")
        entlopass=Entry(log,show="*",font="Arial 20")
        btnval=Button(log,text="Valmis",font="Arial 20",fg="Black",bg="Gray", command=lambda: lug(lg,entloname,entlopass,log,1))
        lst=[lbl,lblloname,entloname,lbllopass,entlopass,btnval]
        for i in range(len(lst)):
            lst[i].pack(pady=50) if i==0 else (lst[i].pack() if i!=5 else lst[i].pack(pady=20))
        log.mainloop()

    if v==3:
        mut=Tk()
        mut.geometry("1200x600")
        mut.title("Nime või parooli muutmine")
        lbl=Label(mut,text="Nime või parooli muutmine",font="Arial 50",fg="Black")
        lblmuname=Label(mut,text="Name: ",font="Arial 20",fg="Black")
        entmuname=Entry(mut,font="Arial 20")
        lblmupass=Label(mut,text="Password: ",font="Arial 20",fg="Black")
        entmupass=Entry(mut,show="*",font="Arial 20")
        btnval=Button(mut,text="Kontrolli konto",font="Arial 20",fg="Black",bg="Gray",command=lambda: lug(lg,entmuname,entmupass,mut,0))
        lst=[lbl,lblmuname,entmuname,lblmupass,entmupass,btnval]
        for i in range(len(lst)):
            lst[i].pack(pady=50) if i==0 else (lst[i].pack() if i!=5 else lst[i].pack(pady=20))
        mut.mainloop()
    if v==4:
        print()

def lop(win):
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
btngo=Button(win,text="Alusta",font="Arial 30",fg="Black",bg="Green", command=lambda: stul(win))
btnlop=Button(win,text="Lõpetamine",font="Arial 30",fg="Black",bg="Red",command=lambda:lop(win))

lst=[lbl,rblog,rbreg,rbmut,rbun,btnlop,btngo]
for i in range(len(lst)):
    lst[i].pack(pady=50) if i==0 else (lst[i].pack(side=RIGHT,pady=200,padx=120) if i in [5,6] else lst[i].pack())

win.mainloop()
