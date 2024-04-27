import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from api import getSong, playSong
from dotenv import load_dotenv
import os
import spotipy
from spotipy.client import Spotify
from spotipy.oauth2 import SpotifyOAuth
from cs_3560_project import Song, MusicPlaylist

# *************** Login Screen **************************
class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login Screen")
        self.geometry("1600x900")

        #create each frame within the app class
        #pack() function used to display elements on screen

        ##
        #LOGIN FRAME
        ##
        self.login_frame = tk.Frame(self)
        username_label = tk.Label(self.login_frame, text = "Username:")
        username_label.pack()

        username_entry = tk.Entry(self.login_frame)
        username_entry.pack()

        password_label = tk.Label(self.login_frame, text = "Password:")
        password_label.pack()

        password_entry = tk.Entry(self.login_frame, show ="*")
        password_entry.pack()

        #command used to call functions within the program
        login_button = tk.Button(self.login_frame, text = "Login", command = self.to_mainMenu)
        login_button.pack()

        register_label = tk.Label(self.login_frame, text = "Don't have an account?")
        register_label.pack()

        register_button = tk.Button(self.login_frame, text = "Register", command = self.to_register)
        register_button.pack()



        ##
        #REGISTER FRAME
        ##
        self.register_frame = tk.Frame(self)
        username_label = tk.Label(self.register_frame, text = "Username:")
        username_label.pack()

        username_entry = tk.Entry(self.register_frame)
        username_entry.pack()

        password_label = tk.Label(self.register_frame, text = "Password:")
        password_label.pack()

        password_entry = tk.Entry(self.register_frame, show ="*")
        password_entry.pack()

        password_label2 = tk.Label(self.register_frame, text = "Confirm Password:")
        password_label2.pack()

        password_entry2 = tk.Entry(self.register_frame, show ="*")
        password_entry2.pack()

        register_button = tk.Button(self.register_frame, text = "Register", command = self.to_login)
        register_button.pack()

        self.login_frame.pack()

# --------------------------------Login Screen Functions ---------------------------------------------------
    def to_mainMenu(self):
        self.withdraw()
        self.main_menu = MainMenu()

    def to_register(self):
        #forget the current frame/screen
        self.login_frame.forget()
        #show the register frame/screen
        self.title("Register Screen")
        self.register_frame.pack()

    def to_login(self):
        self.register_frame.forget()
        self.title("Login Screen")
        self.login_frame.pack()








class MainMenu(tk.Tk):
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
        self.back_button = tk.Button(left_frame, text = 'Return to Login', command = self.to_login)
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


# --------------------------------Main Menu Functions ---------------------------------------------------
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
        if (entry == ""): # Error message when playlist name is empty
            error = tk.Toplevel(self)
            error.title("Error")
            error.geometry("200x100")
            label = tk.Label(error, text="Please give your playlist a name")
            label.pack()
        else:
            my_playlist = MusicPlaylist(entry)
            self.new_playlist = YourPlaylist(self, entry, my_playlist)
            self.playlist.insert(tk.END, entry)

    # Return to login
    def to_login(self):
        self.withdraw()
        self.login = Login()

    # Go to search
    def to_Search_Screen(self):
        self.search = Search()


############################################################################
# Test for friend request function
    user_data = {}

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
        confirm_button = tk.Button(window, text="Add Friend", command=lambda: self.send_fr(entry.get()))
        confirm_button.pack()

        # Create a cancel button
        cancel_button = tk.Button(window, text="Cancel", command=window.destroy)
        cancel_button.pack()

    # Check for user
    def check_user(username, requester):
        if username in user_data:
            # Send a friend request to the user
            user_data[username]['friend_requests'].append(requester)
        else:
            # Print an error message
            print(f"User not found: {username}")

    # Send Friend Request        
    def send_fr(username):
        if username in user_data:
        # Send a friend request to the user
            check_user(username, self.username)
            print(f"Friend request sent to {username}")
        else:
            print(f"User not found: {username}")

    # Accept Friend Request
    def accept_friend_request(self, requester):
        # Condition: username exists and requester inputs their name 
        if self.username in user_data and requester in user_data[self.username]['friend_requests']:
        # 1) Remove the friend request from the user's list of friend requests
            user_data[self.username]['friend_requests'].remove(requester)

        # 2) Add the requester as a friend of the user
            if 'friends' not in user_data[self.username]:
                user_data[self.username]['friends'] = []
            user_data[self.username]['friends'].append(requester)

        # 3) Add the user as a friend of the requester
            if 'friends' not in user_data[requester]:
                user_data[requester]['friends'] = []
            user_data[requester]['friends'].append(self.username)
            # Accept Message
            print(f"Friend request accepted from {requester}")

    # Decline Friend Request
    def reject_friend_request(self, requester):
        if self.username in user_data and requester in user_data[self.username]['friend_requests']:
        # Remove the friend request from the user's list of friend requests
            user_data[self.username]['friend_requests'].remove(requester)
            # Decline Message
            print(f"Friend request rejected from {requester}")
            


              
# *************** Playlist Class **************************
class YourPlaylist(tk.Toplevel):
    def __init__(self, master, playlist, name = None):
        tk.Toplevel.__init__(self, master)
        self.name = name
        self.title(name)
        self.geometry('1600x900')
        label = tk.Label(self, text=f"{self.name}")
        label.pack()
        ######## Playlist Frame ##########################################################################
        self.playlist_frame = tk.Frame(self)
        self._playlist = playlist

        # Display Headings (Title/Artist/Duration Headings)
        self.table = ttk.Treeview(self.playlist_frame, columns=('title', 'artist', 'duration'), show='headings')
        self.table.heading('title', text='Song Title')
        self.table.heading('artist', text='Artist')
        self.table.heading('duration', text='Duration')
        self.table.pack(fill='both', expand = True)

        self.title_label = ttk.Label(master=self.playlist_frame, font='Arial 18')
        self.title_label.pack()

        # Display Buttons at bottom

        button_frame = tk.Frame(self.playlist_frame)
        self.play_button = tk.Button(button_frame, text = 'Play', command=self.play)
        self.search_button = tk.Button(button_frame, text = 'Search', command=self.to_search)

        # Pack the buttons into the frame and center them
        self.play_button.pack()
        self.search_button.pack()
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
        MusicPlaylist(self._playlist).play(0)

    def update(self):
        for song in MusicPlaylist(self._playlist).songs:
            self.table.insert(Song(song))

    def to_search(self):
        self.search = Search(self._playlist)



class Search(Tk):
    # *************** Search Screen **************************
    def __init__(self, playlist):
        tk.Tk.__init__(self)
        self.title('Search Screen')
        self.geometry("1600x900")
        self._playlist = MusicPlaylist(playlist)
        search_label = Label(self, text="Search for music.")
        search_label.pack()

        search_bar = Entry(self)
        search_bar.pack()

        result_list = Listbox(self)
        result_list.pack()

        # --------------------------------Main Menu Functions ---------------------------------------------------
        def update(data):
            result_list.delete(0, END)

            for item in data:
                result_list.insert(END, (item[2] + " - " + item[1]))

        def check(e):
            typed = search_bar.get()
            update(getSong(typed))

        def add_selected(e):
            typed = search_bar.get()
            #returns list of songs
            songs = getSong(typed)
            selected = result_list.curselection()
            new_song = (songs[selected[0]][0], songs[selected[0]][1], songs[selected[0]][2], songs[selected[0]][3])
            print(new_song)
            self._playlist.add_song(new_song)
            self._playlist.display_songs()
            print(self._playlist.songs)
            #playSong() takes the id of the selected song
            #playSong(songs[selected[0]][0])
        
        #on event, run the specified function
        search_bar.bind("<Return>", check)
        result_list.bind("<<ListboxSelect>>", add_selected)


if __name__ == '__main__':
    app = Login()
    app.mainloop()