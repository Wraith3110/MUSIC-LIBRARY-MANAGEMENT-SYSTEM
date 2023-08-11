import add as a
import dele as d
import show as st
import addtoplay as atp
from tkinter import*
import tkinter.messagebox as msg
import displ as dis


root=Tk()
root.geometry("1000x1000")
root.title("MUSIC LIBRARY SYSTEM")
root.configure(bg="#f3dfc1")
Label(root,text="Welcome to Music Library").grid(row=0,column=1,columnspan=2)
Label(root,text="CLICK HERE TO ADD SONG").grid(row=3,column=2)
Label(root,text="CLICK HERE TO ADD ARTIST").grid(row=4,column=2)
Label(root,text="CLICK HERE TO ADD GENRE").grid(row=5,column=2)
Label(root,text="CLICK HERE TO ADD PLAYLIST").grid(row=6,column=2)
Label(root,text="CLICK HERE TO ADD ALBUM").grid(row=7,column=2)
Label(root,text="CLICK HERE TO ADD YOUR OWN QUERY TO DELETE").grid(row=8,column=2)
Label(root,text="CLICK HERE TO DISPLAY THE DATA OF TABLE").grid(row=9,column=2)
Label(root,text="CLICK HERE TO DISPLAY ALL THE ATBLES").grid(row=10,column=2)

Button(root,text="add song",command=a.add_music).grid(row=3,column=3,columnspan=2)
Button(root,text="add artist",command=a.add_artist).grid(row=4,column=3,columnspan=2)
Button(root,text="add genre",command=a.add_genre).grid(row=5,column=3,columnspan=2)
Button(root,text="add PLAYLIST",command=atp.ex).grid(row=6,column=3,columnspan=2)
Button(root,text="add album",command=a.add_album).grid(row=7,column=3,columnspan=2)
Button(root,text="add deletion query",command=d.ex).grid(row=8,column=3,columnspan=2)
Button(root,text="display data",command=dis.dip).grid(row=9,column=3,columnspan=2)
Button(root,text="show Tables",command=st.table).grid(row=10,column=3,columnspan=2)

root.mainloop()