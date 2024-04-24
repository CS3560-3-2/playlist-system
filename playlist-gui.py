import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

def test():
  print('insert songs here')

window = tk.Tk()
window.title('Your Playlist')
window.geometry('1600x900')


table = ttk.Treeview(window, columns = ('title', 'artist', 'duration'), show = 'headings')
table.heading('title', text = 'Song Title')
table.heading('artist', text = 'Artist')
table.heading('duration', text = 'Duration')
table.pack(fill = 'both', expand = True)

title_label = ttk.Label(master = window, font = 'Arial 18')
title_label.pack()

# Insert songs here
for i in range(100):
  # table.insert(song requested, index = i, values = data)
  i += 1

def item_select(_):
  print(table.selection())
  for i in table.selection():
    print(table.item(i)['values'])

def delete_song(_):
  print('Song has been removed')
  for i in table.selection():
    table.delete(i)

play_icon = ImageTk.PhotoImage(Image.open("play.png"))
button = tk.Button(window, image = play_icon, command = test)
button.pack()

window.mainloop()