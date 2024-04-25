import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image

class MainMenu(tk.Tk):

    def create_playlist(self):
        # Create a new frame in the main window
        self.create_frame = tk.Frame(self)

        # Create a label and a text box entry
        label = tk.Label(self.create_frame, text="Enter a playlist name:")
        label.pack()
        entry = tk.Entry(self.create_frame)
        entry.pack()

        # Create a confirmation button
        confirm_button = tk.Button(self.create_frame, text="Create Playlist", command=lambda: self.to_playlist(entry.get()))
        confirm_button.pack()

        # Create a cancel button
        cancel_button = tk.Button(self.create_frame, text="Cancel", command=self.to_main_menu)
        cancel_button.pack()

        # Remove the main menu functions and open the create_frame
        self.mm_frame.forget()
        self.create_frame.pack(fill="both", expand=True)

    # Return to main menu
    def to_main_menu(self):
        self.create_frame.forget()
        self.mm_frame.pack(fill='both', expand=True)

    # Go to Playlist
    def to_playlist(self, entry):
        self.new_playlist = YourPlaylist(self, entry)

    # Return to login
    def to_login(self):
        self.register_frame.forget()
        self.title("Login Screen")
        self.login_frame.pack()

    # Go to search
    def to_Search_Screen(self):
        self.mm_frame.forget()
        self.title("Search Screen")
        self.search_frame.pack()

    # Add friend
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

    # *************** Main Menu **************************
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Main Menu')
        self.geometry('1600x900')

        ######## Main Menu Frame ##########################################################################
        self.mm_frame = tk.Frame(self)
        
        #******** Left Side Functions *************************************
        left_frame = tk.Frame(self.mm_frame)
        # Pack the frame to the left side of the main frame
        left_frame.pack(side='left', fill='both')
        

        # "Your Playlists Title + List of your Playlists"
        self.playlistsLabel = tk.Label(left_frame, text='Your Playlists', font='Arial 14')
        self.playlistsLabel.pack(side='top', fill='x')

        self.playlist = tk.Listbox(left_frame, width = 50, height = 30)
        self.playlist.pack(side='top', fill='both')

        # Back button
        self.back_icon = ImageTk.PhotoImage(Image.open("back.png"))
        self.back_button = tk.Button(left_frame, image = self.back_icon, command = self.to_login)
        self.back_button.pack(side = 'bottom', pady=10)


        #******** Right Side Functions *************************************
        right_frame = tk.Frame(self.mm_frame)
        # Pack the frame to the right side of the main frame
        right_frame.pack(side='right', fill = 'both')

        # "Your Friend List Title + List of your Friends"
        self.friendslistLabel = tk.Label(right_frame, text='Friend List', font = 'Arial 14')
        self.friendslistLabel.pack(side='top', fill = 'x')

        self.friendslist = tk.Listbox(right_frame, width = 50, height = 30)
        self.friendslist.pack(side='top', fill = 'both')


        #******** Middle Functions *************************************
        middle_frame = tk.Frame(self.mm_frame)
        # Pack the frame to the middle of the main frame
        middle_frame.pack(side='top', fill='both')

        # Main Menu Title
        self.mainMenuLabel = tk.Label(middle_frame, text='Main Menu', font = 'Arial 18')
        self.mainMenuLabel.pack()


        # Create Playlist Button
        self.createPlaylist = tk.Button(middle_frame, text='Create Playlist', font = 'Arial 14', height=10, width=20, command = self.create_playlist) # command = create_playlist
        self.createPlaylist.pack(expand = True, padx=30)
        
        # Add Friend Button
        self.addFriend = tk.Button(middle_frame, text='Add Friend', font = 'Arial 14', height=10, width=20, command = self.add_friend) # command = add_friend
        self.addFriend.pack(expand = True, padx=30)

        # Go to Search Screen Button
        self.SearchButton = tk.Button(middle_frame, text='Search for Playlists', font = 'Arial 14', height=12, width=20, command=self.to_Search_Screen) # command = to_Search_Screen
        self.SearchButton.pack(expand = True, padx=30)

        self.mm_frame.pack(fill='both')
              

        # Iterate through users playlists and create buttons for each
        # Button leads to a new window for a playlist

        # Iterate through friendslist and create labels for each friend
        # Maybe buttons for friend profiles

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
    app = MainMenu()
    app.mainloop()