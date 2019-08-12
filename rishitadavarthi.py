from tkinter import *
from random import *
import tkinter.messagebox

tiles=[]
correct=[]
size=3
percentage=10
total=0
score=0
remainingTiles=[]

def instructions():
    global window,main,tiles,correct,size,percentage,total,score,remainingTiles

    tiles=[]
    remainingTiles=[]
    correct=[]
    size=3
    percentage=10
    total=0
    score=0

    window=Tk()
    window.title("New game")
    tekst=Label(window,text="The goal is to click all the green tiles")
    tekst.pack()
    playB=Button(window,text="Play",command=lambda:loadLevel())
    playB.pack()
    mainloop()
    return

def reveal():
    global tiles,main
    
    for i in range(size):
        for j in range(size):
            if(correct[i][j]):
                tiles[i][j].config(bg="green")
    main.after(1000*size,lambda:hide())
    return

def hide():
    for i in range(size):
        for j in range(size):
            tiles[i][j].config(bg="black",state="normal")
    return

def clickTile(r,s):
    global total,tiles,main,percentage,size,score,remainingTiles

    if(not correct[r][s]):
        tiles[r][s].config(bg="red")
        for i in remainingTiles:
            tiles[i[0]][i[1]].config(bg="purple")
        tkinter.messagebox.showinfo('You lost','Total score: '+str(score))
        
        main.destroy()
        instructions()
    else:
        del(remainingTiles[remainingTiles.index([r,s])])
        tiles[r][s].config(bg="green",state="disabled")
        total-=1
        if(total==0):
            score+=1
            tkinter.messagebox.showinfo('Well done','Get ready for the next level')
            if(percentage==50):
                percentage=10
                size+=1
            else:
                percentage+=10
            main.destroy()
            loadLevel()
    return

def loadLevel():
    global tiles,window,total,correct,main,remainingTiles

    if(size==3 and percentage==10):
        window.destroy()

    correct=[]
    total=0

    main=Tk()
    main.title("Level "+str(size-2)+"."+str(percentage))
    main.config(bg="white",width=10+size*52,height=16+size*55)
    
    tiles=[]
    for i in range(size):
        tiles.append([])
        correct.append([])
        for j in range(size):
            tiles[i].append([])
            correct[i].append([])
    
    for i in range(size):
        for j in range(size):
            tiles[i][j]=Button(main,bg="black",state="disabled",width=6,height=3,command=lambda i=i,j=j:clickTile(i,j))
            tiles[i][j].place(x=5+j*52,y=5+i*55)
            if(randint(0,100)<percentage):
                correct[i][j]=True
                remainingTiles.append([i,j])
                total+=1
            else:
                correct[i][j]=False
    if(not correct[0][0]):
        correct[0][0]=True
        total+=1
        remainingTiles.append([0,0])
        
    reveal()
    mainloop()
    return

instructions()
