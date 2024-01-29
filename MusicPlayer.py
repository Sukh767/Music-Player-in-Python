from tkinter import *
from PIL import ImageTk, Image   #VS code Terminal "pip install Pillow"
import os
from pygame import mixer   #VS code Terminal "pip install pygame"
#colors
col1 = "#ffffff"  #white
col2 = "#3C1DC6" #purple
col3 = "#333333" #black
col4 = "#CFC7F8" #light purple

#events
def play_music():
    running = listbox.get(ACTIVE)
    running_song['text'] = running
    mixer.music.load(running)
    mixer.music.play()

def pause_music():
    mixer.music.pause()
    
def continue_music():
    mixer.music.unpause()
    
def stop_music():
    mixer.music.stop()
    
def next_music():
    playing = running_song['text']
    index = songs.index(playing)
    new_index = index + 1
    playing = songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()
    
    listbox.delete(0,END)
    
    show()
    
    listbox.select_set(new_index)
    running_song['text'] = playing


def previous_music():
    playing = running_song['text']
    index = songs.index(playing)
    new_index = index - 1
    playing = songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()
    
    listbox.delete(0,END)
    
    show()
    
    listbox.select_set(new_index)
    running_song['text'] = playing


window =Tk()
window.title ("")
window.geometry('352x255')
window.configure(background = col1)
window.resizable(width = FALSE, height = FALSE)


#Frames
left_frame = Frame(window, width = 150,height = 150, bg = col1)
left_frame.grid(row=0,column=0,padx=1,pady=1)

right_frame = Frame(window, width = 250,height = 150, bg = col3)
right_frame.grid(row=0,column=1,padx=0)

down_frame = Frame(window, width = 400,height = 100, bg = col4)
down_frame.grid(row=1,column=0,columnspan=3,padx=0,pady=1)

#right frame
listbox = Listbox(right_frame, selectmode=SINGLE,font=("Arial 9 bold"),width =22,bg = col3,fg=col1 )
listbox.grid(row=0,column=0)


w = Scrollbar(right_frame)
w.grid(row=0,column=1)

listbox.config(yscrollcommand=w.set)
w.config(command= listbox.yview)



#images
img_1 = Image.open("C:\\Users\\priti\\OneDrive\\Desktop\\CODE\\CODE FOR LIFE\\PYTHON\\URL\\Icons\\icon.png")  #Paste the file(icon) path here
img_1 = img_1.resize((130,130))
img_1 = ImageTk.PhotoImage(img_1)
app_image = Label(left_frame, height=120, image = img_1, padx=10,bg = col1)
app_image.place(x=10,y=15)

img_2 = Image.open("C:\\Users\\priti\\OneDrive\\Desktop\\CODE\\CODE FOR LIFE\\PYTHON\\URL\\Icons\\play.png")
img_2 = img_2.resize((30,30))
img_2 = ImageTk.PhotoImage(img_2)
play_button = Button(down_frame, height=40, width = 40, image = img_2, padx=10,bg = col1, font=("Ivy 10"),command=play_music)
play_button.place(x=28+56,y=35)

img_3 = Image.open("C:\\Users\\priti\\OneDrive\\Desktop\\CODE\\CODE FOR LIFE\\PYTHON\\URL\\Icons\\prev.png")
img_3 = img_3.resize((30,30))
img_3 = ImageTk.PhotoImage(img_3)
prev_button = Button(down_frame, height=40,width=40, image = img_3, padx=10,bg = col1, font=("Ivy 10"),command=previous_music)
prev_button.place(x=38,y=35)

img_4 = Image.open("C:\\Users\\priti\\OneDrive\\Desktop\\CODE\\CODE FOR LIFE\\PYTHON\\URL\\Icons\\fast.png")
img_4 = img_4.resize((30,30))
img_4 = ImageTk.PhotoImage(img_4)
next_button = Button(down_frame, height=40,width=40, image = img_4, padx=10,bg = col1, font=("Ivy 10"),command=next_music)
next_button.place(x=28+102,y=35)

img_5 = Image.open("C:\\Users\\priti\\OneDrive\\Desktop\\CODE\\CODE FOR LIFE\\PYTHON\\URL\\Icons\\pauseS.png")
img_5 = img_5.resize((30,30))
img_5 = ImageTk.PhotoImage(img_5)
pause_button = Button(down_frame, height=40,width=40, image = img_5, padx=10,bg = col1, font=("Ivy 10"),command=pause_music)
pause_button.place(x=28+148,y=35)

img_6 = Image.open("C:\\Users\\priti\\OneDrive\\Desktop\\CODE\\CODE FOR LIFE\\PYTHON\\URL\\Icons\\nextS.png")
img_6 = img_6.resize((30,30))
img_6 = ImageTk.PhotoImage(img_6)
continue_button = Button(down_frame, height=40,width=40, image = img_6, padx=10,bg = col1, font=("Ivy 10"),command= continue_music)
continue_button.place(x=28+194,y=35)

img_7 = Image.open("C:\\Users\\priti\\OneDrive\\Desktop\\CODE\\CODE FOR LIFE\\PYTHON\\URL\\Icons\\pause-button.png")
img_7 = img_7.resize((30,30))
img_7 = ImageTk.PhotoImage(img_7)
stop_button = Button(down_frame, height=40,width=40, image = img_7, padx=10,bg = col1, font=("Ivy 10"),command=stop_music)
stop_button.place(x=28+240,y=35)

line = Label(left_frame, width = 200,height=1, padx=10,bg = col3)
line.place(x=0,y=1)

line = Label(left_frame, width = 200,height=1, padx=10,bg = col1)
line.place(x=0,y=3)

running_song = Label(down_frame,text = "choose a Song", font=("Ivy 10"), width =44, height =1, padx=10, bg=col1,fg =col3, anchor=NW)
running_song.place(x=0,y=1)



os.chdir(r"C:\\Users\\priti\\OneDrive\\Desktop\\CODE\\CODE FOR LIFE\\PYTHON\\URL\\MUSIC ENG") #Music directory path
songs = os.listdir()

def show():
    for i in songs:
        listbox.insert(END, i)
show()       


mixer.init()
music_state = StringVar()
music_state.set("Choose one!")
        
window.mainloop()