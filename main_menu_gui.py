import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image


class MainMenu(tk.Tk):
    def create_playlist(self):
    # Create a new window
        window = tk.Toplevel()
        window.geometry('500x300')

        # Create a label and a text box entry
        label = tk.Label(window, text="Enter a playlist name:")
        label.pack()
        entry = tk.Entry(window)
        entry.pack()

        # Create a frame at the bottom of the window
        button_frame = Frame(window)
        button_frame.pack(side=BOTTOM)

        # Create a confirmation button
        confirm_button = tk.Button(button_frame, text="Create Playlist", command=lambda: YourPlaylist(self, entry.get()))
        confirm_button.pack()

        # Create a cancel button
        cancel_button = Button(button_frame, text="Cancel", command=window.destroy)
        cancel_button.pack(side=RIGHT, padx=5, pady=5, fill=X)

    def add_friend(self):
    # Create a new window
        window = tk.Toplevel()
        window.geometry('500x300')
        # Create a label and an entry widget
        label = tk.Label(window, text="Enter username:")
        label.pack()
        entry = tk.Entry(window)
        entry.pack()

        # Create a confirmation button
        confirm_button = tk.Button(window, text="Add Friend", command=lambda: self.add_friend(entry.get()))
        confirm_button.pack()


    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Main Menu')
        self.geometry('1600x900')

        self.new_frame = tk.Frame(self)

        self.mainMenuLabel = tk.Label(self, text='Main Menu', font = 'Arial 18')
        self.mainMenuLabel.place(x=700, y = 10)

        self.playlistsLabel = tk.Label(self, text='Your Playlists', font = 'Arial 14', height=10, width=10)
        self.playlistsLabel.place(x=100, y = 5)

        self.friendslistLabel = tk.Label(self, text='FriendList', font = 'Arial 14', height=10, width=10)
        self.friendslistLabel.place(x=1250, y = 5)

        self.createPlaylist = tk.Button(self, text='Create Playlist', font = 'Arial 14', height=10, width=20, command = self.create_playlist) # command = create_playlist
        self.createPlaylist.place(x=670, y = 80)

        self.addFriend = tk.Button(self, text='Add Friend', font = 'Arial 14', height=10, width=20, command = self.add_friend) # command = add_friend
        self.addFriend.place(x=670, y = 330)

       # confirm_button = tk.Button(button_frame, text="Create Playlist", command=lambda: YourPlaylist(self, entry.get()))

        self.SearchButton = tk.Button(self, text='Search for Playlists', font = 'Arial 14', height=12, width=20, command=lambda: SearchScreen(self)) # command = open_playlist
        self.SearchButton.place(x=670, y = 580)

        # Iterate through users playlists and create buttons for each
        # Button leads to a new window for a playlist

        # Iterate through friendslist and create labels for each friend
        # Maybe buttons for friend profiles



if __name__ == '__main__':
    app = MainMenu()
    app.mainloop()