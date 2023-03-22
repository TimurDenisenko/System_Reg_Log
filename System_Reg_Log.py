from tkinter import *

def file():
    lg=[]
    with open("Sys.txt","r",encoding="utf-8-sig") as f:
        for i in f:
            lg.append(i.strip().split(","))
    return lg

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

def fulk(p,p1,n,s):
    lg=file()
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
    lg=file()
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
    lg=file()
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
    lg=file()
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

def lug(lst,entx,enty,win,o,but=None):
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
        if y in msy:
            enty.configure(bg="White")
        else:
            enty.configure(bg="Red")
    else:
        entx.configure(bg="Red")
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
        but.destroy()
        bt=Button(win,text="Muuda nimi",font="Arial 20",width=12,fg="white",bg="orange",command=mut)
        bt1=Button(win,text="Muuda parool",font="Arial 20",width=12,fg="white",bg="orange",command=mut1)
        bt.pack(side=LEFT,padx=65)
        bt1.pack(side=LEFT)

def kontrol(x,y,z,i,btn,win):
    lg=file()
    lg=lg
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
        file()
        log(win)

def regi(win=None):
    if win: win.destroy()
    reg=Tk()
    reg.iconbitmap("robot.ico")
    reg.geometry("600x800")
    reg.resizable(width=False,height=False)
    reg.title("Registreerimine")
    #imgr=PhotoImage(file="robot1.png")
    lbl=Label(reg,text="Registreerimine",font="Arial 40",fg="Black")
    #lblr=Label(reg,image=imgr) 
    lblrename=Label(reg,text="Name: ",font="Arial 20",fg="Black")
    entrename=Entry(reg,font="Arial 20")
    lblrepass=Label(reg,text="Password: ",font="Arial 20",fg="Black")
    entrepass=Entry(reg,show="*",font="Arial 20",bg="White")
    lblconfrepass=Label(reg,text="Confirm password: ",font="Arial 20",fg="Black")
    entconfrepass=Entry(reg,show="*",font="Arial 20",bg="White")
    lblsec=Label(reg,text="Salajane sõna: ",font="Arial 20",fg="Black")
    entsec=Entry(reg,font="Arial 20",bg="White")
    btnval=Button(reg,text="Valmis",font="Arial 20",width=19,fg="White",bg="Green",command=lambda: kontrol(entrepass,entconfrepass,entrename,entsec,btnval,reg))
    lst=[lbl,lblrename,entrename,lblrepass,entrepass,lblconfrepass,entconfrepass,lblsec,entsec,btnval]
    for i in range(len(lst)):
        lst[i].pack(pady=50) if i==0 else (lst[i].pack() if i!=9 else lst[i].pack(pady=20))
    

def log(win=None):
    if win: win.destroy()
    lg=file()
    log=Tk()
    log.iconbitmap("door.ico")
    log.geometry("600x800")
    log.title("Autoriseerimine")
    log.resizable(width=False,height=False)
    lbl=Label(log,text="Autoriseerimine",font="Arial 40",fg="Black")
    lblloname=Label(log,text="Name: ",font="Arial 20",fg="Black")
    entloname=Entry(log,font="Arial 20")
    lbllopass=Label(log,text="Password: ",font="Arial 20",fg="Black")
    entlopass=Entry(log,show="*",font="Arial 20")
    btnval=Button(log,text="Valmis",font="Arial 20",fg="White",bg="Blue",width=19, command=lambda: lug(lg,entloname,entlopass,log,1))
    lst=[lbl,lblloname,entloname,lbllopass,entlopass,btnval]
    for i in range(len(lst)):
        lst[i].pack(pady=50) if i==0 else (lst[i].pack() if i!=5 else lst[i].pack(pady=20))
    log.mainloop()

def nimparmut(win=None):
    lg=file()
    if win: win.destroy()
    mut=Tk()
    mut.resizable(width=False,height=False)
    mut.iconbitmap("gk.ico")
    mut.geometry("600x800")
    mut.title("Nime või parooli muutmine")
    lbl=Label(mut,text="Nime või parooli\n muutmine",font="Arial 40",fg="Black")
    lblmuname=Label(mut,text="Name: ",font="Arial 20",fg="Black")
    entmuname=Entry(mut,font="Arial 20")
    lblmupass=Label(mut,text="Password: ",font="Arial 20",fg="Black")
    entmupass=Entry(mut,show="*",font="Arial 20")
    btnval=Button(mut,text="Kontrolli konto",font="Arial 20",fg="White",bg="Orange",width=19,command=lambda: lug(lg,entmuname,entmupass,mut,0,btnval))
    lst=[lbl,lblmuname,entmuname,lblmupass,entmupass,btnval]
    for i in range(len(lst)):
        lst[i].pack(pady=50) if i==0 else (lst[i].pack() if i!=5 else lst[i].pack(pady=20))
    mut.mainloop()

def lop(win):
    win.destroy()

def lilletool(win=None):
    if win: win.destroy()
    win=Tk()
    win.resizable(width=False,height=False)
    win.iconbitmap("crocus.ico")
    win.geometry("900x900")
    win.title("System: LilleTool ")

    img=PhotoImage(file="2_8.png")
    img=img.subsample(5,5)
    imgrobot=PhotoImage(file="robot.png")
    imgrobot1=imgrobot.subsample(5,5)
    imgdor=PhotoImage(file="door.png")
    imgdor=imgdor.subsample(16,16)
    imggk=PhotoImage(file="gk.png")
    imggk=imggk.subsample(7,7)
    imgkr=PhotoImage(file="kubrub.png")
    imgkr=imgkr.subsample(5,5)
    imgredk=PhotoImage(file="redk.png")
    imgredk=imgredk.subsample(4,4)
    lbl=Label(win,text="LilleTool",font="Arial 50",fg="Black")
    lblimg2=Label(win,image=img)
    lblimg1=Label(win,image=img)
    lblrob=Label(win,image=imgrobot1)
    lbldor=Label(win,image=imgdor)
    lblgk=Label(win,image=imggk)
    lblkr=Label(win,image=imgkr)
    lblredk=Label(win,image=imgredk)
    btnreg=Button(win,text="Registreerimine",font="Arial 30",fg="White",bg="Green",width=25,command=lambda: regi(win))
    btnlog=Button(win,text="Autoriseerimine",font="Arial 30",bg="Blue",fg="White",width=25,command=lambda: log(win))
    btnmut=Button(win,text="Nime või parooli muutmine",font="Arial 30",fg="White",bg="Orange",width=25,command=lambda: nimparmut(win))
    btnun=Button(win,text="Unustanud parooli taastamine",font="Arial 30",fg="White",bg="Purple",width=25)
    btnlop=Button(win,text="Lõpetamine",font="Arial 30",fg="White",bg="Red",width=25,command=lambda:lop(win))
   
    lbl.place(x=325,y=40)
    lblimg1.place(x=580,y=25)
    lblimg2.place(x=220,y=25)
    btnreg.place(x=0,y=200)
    lblrob.place(x=600,y=185)
    btnlog.place(x=0,y=300)
    lbldor.place(x=600,y=290)
    btnmut.place(x=0,y=400)
    lblgk.place(x=600,y=400)
    btnun.place(x=0,y=500)
    lblkr.place(x=600,y=500)
    btnlop.place(x=0,y=600)
    lblredk.place(x=600,y=600)
    win.mainloop()

lilletool()