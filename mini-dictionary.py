from tkinter import *
root= Tk()
root2= Tk()

f= Frame(root, width=500, height= 500, bg="green")
f.pack()

f2=Frame(root2, width=1000, height=1000, bg="red")
f2.pack()

l= Label(f, text= 'Welcome to the dictionary!')

l.grid(padx=150, pady=135)

def mylab(event):
    ml= Label(f, text="Let's Start!!")
    ml.pack()


bu=Button(f, text="Start")
bu.bind("<Button-1>", mylab )
bu.grid()


def globall():
    i = 0
    res=[]
    with open("glossary.txt", "rt")as mf:
        for i, line in enumerate(mf):
            if i <= 30 and line!='\n':
                res.append(line.split()[0])
    return "\t".join(res)


def globalinfo(event):
    a=globall()
    l1= Label(f2, text=a)
    l1.grid()


b1= Button(f2, text='Global')
b1.bind("<Button-1>", globalinfo )
b1.grid()



def auto():
    j= 30
    res=[]
    with open("glossary.txt", "rt")as mf:
        for j, line in enumerate(mf):
            if j <= 60 and line!='\n':
                res.append(line.split()[0])
    return "\t".join(res)


def autoinfo(event):
    a=auto()
    l1= Label(f2, text=a)
    l1.grid()


b2= Button(f2, text='Automobiles')
b2.bind("<Button-1>", autoinfo )
b2.grid()



root3= Tk()

def retrieve_input():
    inputValue=textBox.get("1.0","end-1c")
    print(inputValue)
    with open("glossary.txt", "rt") as sf:
        for line in sf:
            for k in line.split():
                if k == inputValue:
                    print(line)


textBox=Text(root3, height=2, width=10)
textBox.pack()
buttonCommit=Button(root3, height=1, width=10, text="Commit", command=lambda: retrieve_input())

buttonCommit.pack()


f.pack_propagate(False)
root.mainloop()
root2.mainloop()
root3.mainloop()


