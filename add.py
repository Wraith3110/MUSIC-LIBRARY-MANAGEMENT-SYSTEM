from tkinter import*
import tkinter.messagebox as msg
import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="145632sk",
    database="mldb"
)

def add_music():
    music=Toplevel()
    music.title("add music")
    def add():
        mtt=ttv.get()
        mat=atv.get()
        mal=alv.get()
        mg=gv.get()
        my=yv.get()

        cursor = db_connection.cursor()
        sql = "INSERT INTO music_library (title, artist, album, genre, release_year) VALUES (%s, %s, %s, %s, %s)"
        values = (mtt, mat, mal, mg, my)
        try:
            cursor.execute(sql, values)
            db_connection.commit()
            msg.showinfo("Success", "Playlist added successfully!")
        except mysql.connector.Error as err:
            msg.showerror("Error", f"Error while adding the playlist: {err}")

    #opening labels
    Label(music,text="WELCOME TO MUSIC LIBRARY SYSTEM MANAGER").grid(row=0,column=1,columnspan=10)

    #adding labels ,entry points and variables to the screen(tt=title,at=artist,al=album,y=year,in the last l: label,e:entry point,v:variable)
    ttl=Label(music,text="TITLE:")
    atl=Label(music,text="ARTIST:")
    all=Label(music,text="ALBUM:")
    gl=Label(music,text="GENRE:")
    yl=Label(music,text="YEAR:")

    ttv=StringVar()
    atv=StringVar()
    alv=StringVar()
    gv=StringVar()
    yv=IntVar()

    tte=Entry(music,textvariable=ttv)
    ate=Entry(music,textvariable=atv)
    ale=Entry(music,textvariable=alv)
    ge=Entry(music,textvariable=gv)
    ye=Entry(music,textvariable=yv)

    ttl.grid(row=1,column=1)
    atl.grid(row=2,column=1)
    all.grid(row=3,column=1)
    gl.grid(row=4,column=1)
    yl.grid(row=5,column=1)

    tte.grid(row=1,column=2)
    ate.grid(row=2,column=2)
    ale.grid(row=3,column=2)
    ge.grid(row=4,column=2)
    ye.grid(row=5,column=2)

    Button(music,text="add ",command=add).grid(row=6,column=1,columnspan=2)

def add_artist():
    artist=Toplevel()
    artist.title("add artist")
    def add():
        matn=atnv.get()
        mn=nv.get()
        mdob=dobv.get()
        

        cursor = db_connection.cursor()
        sql = "INSERT INTO artists(artist_name,nationality,date_of_birth) VALUES (%s, %s, %s)"
        values = (matn, mn, mdob)
        try:
            cursor.execute(sql, values)
            db_connection.commit()
            msg.showinfo("Success", "Playlist added successfully!")
        except mysql.connector.Error as err:
            msg.showerror("Error", f"Error while adding the playlist: {err}")

    #opening labels
    Label(artist,text="WELCOME TO MUSIC LIBRARY SYSTEM MANAGER").grid(row=0,column=1,columnspan=10)

    #adding labels ,entry points and variables to the screen(tt=title,at=artist,al=album,y=year,in the last l: label,e:entry point,v:variable)
    
    atnl=Label(artist,text="ARTIST NAME:")
    nl=Label(artist,text="NATIONALITY:")
    dobl=Label(artist,text="DOB:")
    

    atnv=StringVar()
    nv=StringVar()
    dobv=StringVar()
    
    atne=Entry(artist,textvariable=atnv)
    ne=Entry(artist,textvariable=nv)
    dobe=Entry(artist,textvariable=dobv)
    
    atnl.grid(row=1,column=1)
    nl.grid(row=2,column=1)
    dobl.grid(row=3,column=1)
    
    atne.grid(row=1,column=2)
    ne.grid(row=2,column=2)
    dobe.grid(row=3,column=2)

    Button(artist,text="add ",command=add).grid(row=6,column=1,columnspan=2)

def add_genre():
    genre=Toplevel()
    genre.title("add genre")
    def add():
        mgn=gnv.get()
        cursor = db_connection.cursor()
        sql = "INSERT INTO genres(genre_name) VALUES (%s)"
        values = (mgn,)
        try:
            cursor.execute(sql, values)
            db_connection.commit()
            msg.showinfo("Success", "Playlist added successfully!")
        except mysql.connector.Error as err:
            msg.showerror("Error", f"Error while adding the playlist: {err}")

    #opening labels
    Label(genre,text="WELCOME TO MUSIC LIBRARY SYSTEM MANAGER").grid(row=0,column=1,columnspan=10)
    Label(genre,text="ADD GENRE").grid(row=1,column=1)
    #adding labels ,entry points and variables to the screen(tt=title,at=artist,al=album,y=year,in the last l: label,e:entry point,v:variable)
    
    gnl=Label(genre,text="GENRE NAME:")
    gnv=StringVar()
    gne=Entry(genre,textvariable=gnv)
    gnl.grid(row=3,column=1)
    gne.grid(row=3,column=2)
   

    Button(genre,text="add ",command=add).grid(row=6,column=1,columnspan=2)

def add_playlist():
    playlist=Toplevel()
    playlist.title("add playlist")
    def add():
        mpn=pnv.get()
        md=de.get("1.0", END)
        cursor = db_connection.cursor()
        sql = "INSERT INTO playlists(playlist_name,description) VALUES (%s, %s)"
        values = (mpn,md)
        try:
            cursor.execute(sql, values)
            db_connection.commit()
            msg.showinfo("Success", "Playlist added successfully!")
        except mysql.connector.Error as err:
            msg.showerror("Error", f"Error while adding the playlist: {err}")

    #opening labels
    Label(playlist,text="WELCOME TO MUSIC LIBRARY SYSTEM MANAGER").grid(row=0,column=1,columnspan=10)

    #adding labels ,entry points and variables to the screen(tt=title,at=artist,al=album,y=year,in the last l: label,e:entry point,v:variable)
    
    pnl=Label(playlist,text="PLAYLIST NAME:")
    dl=Label(playlist,text="DISCRIPTION:")
    

    pnv=StringVar()
    # dv=StringVar()
    
    pne=Entry(playlist,textvariable=pnv)
    de=Text(playlist,height=3,width=20)
    
    pnl.grid(row=1,column=1)
    dl.grid(row=2,column=1)

    pne.grid(row=1,column=2)    
    de.grid(row=5,column=2)

    Button(playlist,text="add ",command=add).grid(row=10,column=1,columnspan=2)

def add_album():
    album=Toplevel()
    album.title("add album")
    def add():
        mat=atv.get()
        mrd=rdv.get()
        mrl=rlv.get()
        mac=acv.get()

        cursor = db_connection.cursor()
        sql = "INSERT INTO albums(album_title,release_date,record_label,album_cover) VALUES (%s, %s, %s, %s)"
        values = (mat, mrd, mrl, mac)
        try:
            cursor.execute(sql, values)
            db_connection.commit()
            msg.showinfo("Success", "Playlist added successfully!")
        except mysql.connector.Error as err:
            msg.showerror("Error", f"Error while adding the playlist: {err}")

    #opening labels
    Label(album,text="WELCOME TO MUSIC LIBRARY SYSTEM MANAGER").grid(row=0,column=1,columnspan=10)

    #adding labels ,entry points and variables to the screen(tt=title,at=artist,al=album,y=year,in the last l: label,e:entry point,v:variable)
   
    atl=Label(album,text="ALBUM TITLE:")
    rdl=Label(album,text="RELEASE DATE:")
    rll=Label(album,text="RELEASE LABEL:")
    acl=Label(album,text="ALBUM COVER:")

    
    atv=StringVar()
    rdv=StringVar()
    rlv=StringVar()
    acv=StringVar()

    
    ate=Entry(album,textvariable=atv)
    rde=Entry(album,textvariable=rdv)
    rle=Entry(album,textvariable=rlv)
    ace=Entry(album,textvariable=acv)

   
    atl.grid(row=2,column=1)
    rdl.grid(row=3,column=1)
    rll.grid(row=4,column=1)
    acl.grid(row=5,column=1)

    
    ate.grid(row=2,column=2)
    rde.grid(row=3,column=2)
    rle.grid(row=4,column=2)
    ace.grid(row=5,column=2)

    Button(album,text="add ",command=add).grid(row=6,column=1,columnspan=2)