import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

class YourPlaylist(tk.Toplevel):
    def __init__(self, master, name = None):
        tk.Toplevel.__init__(self, master)
        self.name = name
        self.title(name)
        self.geometry('1600x900')
        label = tk.Label(self, text=f"{self.name}")
        label.pack()
        ######## Playlist Frame ##########################################################################
        self.playlist_frame = tk.Frame(self)

        # Display Headings (Title/Artist/Duration Headings)
        self.table = ttk.Treeview(self.playlist_frame, columns=('title', 'artist', 'duration'), show='headings')
        self.table.heading('title', text='Song Title')
        self.table.heading('artist', text='Artist')
        self.table.heading('duration', text='Duration')
        self.table.pack(fill='both', expand = True)

        self.title_label = ttk.Label(master=self.playlist_frame, font='Arial 18')
        self.title_label.pack()

        # Insert songs here
        for i in range(100):
            # table.insert(song requested, index = i, values = data)
            i += 1

        #self.table.bind('<Double-Button-1>', self.item_select)

        # Display Icons at bottom
        self.play_icon = ImageTk.PhotoImage(Image.open("play.png"))
        self.pause_icon = ImageTk.PhotoImage(Image.open("pause.png"))
        self.skip_icon = ImageTk.PhotoImage(Image.open("skip.png"))
        self.shuffle_icon = ImageTk.PhotoImage(Image.open("shuffle.png"))

        button_frame = tk.Frame(self.playlist_frame)
        self.play_button = tk.Button(button_frame, image=self.play_icon, command=self.play)
        self.skip_button = tk.Button(button_frame, image=self.skip_icon, command=self.skip)
        self.shuffle_button = tk.Button(button_frame, image=self.shuffle_icon, command=self.shuffle)

        # Pack the buttons into the frame and center them
        self.shuffle_button.pack(side='left', fill='both', expand=True, padx=1)
        self.play_button.pack(side='left', fill='both', expand=True, padx=1)
        self.skip_button.pack(side='left', fill='both', expand=True, padx=1)
        button_frame.pack(fill='both', expand=False)

        self.playlist_frame.pack(fill='both', expand = True)

    def item_select(self, _):
        print(self.table.selection())
        for i in self.table.selection():
            print(self.table.item(i)['values'])

    def delete_song(self):
        print('Song has been removed')
        for i in self.table.selection():
            self.table.delete(i)

    def play(self):
        self.play_button.config(image=self.pause_icon, command=self.pause)
        # Insert song

    def pause(self):
        self.play_button.config(image=self.play_icon, command=self.play)
        print('Paused the current song.')

    def skip(self):
        print('Song has been skipped.')

    def shuffle(self):
        print('Playlist has been shuffled.')  

if __name__ == '__main__':
    app = YourPlaylist()
    app.mainloop()