from tkinter import *
from api import getSong, playSong

root = Tk()
root.geometry("1600x900")

def update(data):
    result_list.delete(0, END)

    for item in data:
        result_list.insert(END, (item[2] + " - " + item[1]))

def check(e):
    typed = search_bar.get()
    update(getSong(typed))

def play_selected(e):
    typed = search_bar.get()
    songs = getSong(typed)
    selected = result_list.curselection()
    playSong(songs, selected[0])

search_label = Label(root, text="Search for music.")
search_label.pack()

search_bar = Entry(root)
search_bar.pack()

result_list = Listbox(root)
result_list.pack()

#on event, run the specified function
search_bar.bind("<Return>", check)
result_list.bind("<<ListboxSelect>>", play_selected)

root.mainloop()
