# -*- coding: utf-8 -*-
"""CS 3560 Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XU82rU2cKDygnliFh_PdQhfFHIL63xVj
"""
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from dotenv import load_dotenv
import spotipy
from spotipy.client import Spotify
from spotipy.oauth2 import SpotifyOAuth
import mysql.connector 
import os
import hashlib
import random
from api import getSong, playSong, ms_to_mins_secs, pauseSong

from functools import partial
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

# Note: methods are not all compilable, *** is used to note the methods/use cases that need work


mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "OrangeNoodleBug2#",
  database = "playlist",
   
) 
cursor = mydb.cursor()

class Song:
  def __init__(self, name, artist, duration, song_id): #genre used for recommendations
    self._song_id = song_id
    self._song_name = name
    self._song_artist = artist
    self._song_duration = duration
  
  @property
  def song_id(self):
    return self._song_id
  
  @property
  def song_name(self):
    return self._song_name
  
  @property
  def song_artist(self):
    return self._song_artist
  
  @property
  def song_duration(self):
    return ms_to_mins_secs(int(self._song_duration))
  
  def __str__(self):
    return self._song_name
  
class FriendRequest:
  def __init__(self, sender, recipient):
      self.sender = sender
      self.recipient = recipient
      DataBase.sendFriendRequestFromDB(sender, recipient)


class Account:
  # Method to create an account ***
  def __init__(self, username, password):

    #setting up salt and hash object
    salt = os.urandom(32)
    hash_object = hashlib.sha256()
    pw = password
    hash_object.update(salt + pw.encode())

    #Account properties
    self._username = username
    self._password = hash_object.hexdigest()
    self._friend_list = []
    self._playlists = []
    self._account_ID = 0

  # Sending a friend request ***
  def send_fr(username):
    if username: # If username exists in system
      # -> Send accept_fr to other 
      return None

  # Responding to a friend request ***
  def accept_fr():
    response = input("X has sent you a friend request: Would you like to accept or decline?")
    if (response == "Accept"):
      friendlist.append(username)
      return "You and user are now friends"
    else:
      return "You have declined the request"

  def getUsername(self):
    return self._username
  
  def getPassword(self):
    return self._password
  
  def getAccountID(self):
    print (self._account_ID)
    return self._account_ID[0]
  
  def playlists(self):
    val = self._account_ID
    command = ("SELECT playlist_ID FROM Playlist WHERE user_ID = %s;")
    command.execute(command, val)
    playlists = cursor.fetchall()
    return playlists 
  # Sends account data to the table in database
  def addAccount(username, passwordOne, passwordTwo):
    #fetchone creates an error if multiple accounts with the same username exists
    #this conditions prevents duplicate accounts
    command = "SELECT COUNT(*) FROM User WHERE Username = %s"
    cursor.execute(command, (username,))
    result = cursor.fetchone()[0]  # Fetch the count result
    if result > 0:  # True if username exists, False otherwise
       print('Username has already been taken')
       return False

    if passwordOne != passwordTwo:
      print('Try again passwords don\'t match')
      return False
      
    if(passwordOne == passwordTwo):
        DataBase.addAccountsToDB(username, passwordOne)
        #print("U: " + username + " P:" + passwordOne)
        #cursor.execute("SELECT * FROM User")
        #for x in cursor:
        #   print (x)
  
  
  def checkLogin(window, username, password):
      if ((username, password) == DataBase.checkLoginInDB(username, password)):
        print ('success')
        Account._account_ID = (DataBase.getAccountIDFromDB(username))
        window.to_mainMenu(Account._account_ID)
      else:
        print('try again')
        

  
# Create subclass of music playlist for an account
class MusicPlaylist:
  # Method to create a playlist ***
  def __init__(self, playlist_name):
    self._songs = []
    self._playlist_name = playlist_name
    self._length = 0
    self._duration = 0
    self._current_song = None
    self._playing = False
    self._playlist_ID = 0
    self._user_ID = 0

  @property
  def songs(self):
    return self._songs

  @property
  def playlist_name(self):
    return self._playlist_name
    
  @playlist_name.setter
  def playlist_name(self, value):
    self._playlist_name = value

  @property
  def length(self):
    return self._length
    
  @length.setter
  def length(self, value):
    self._length = value

  @property
  def duration(self):
    return ms_to_mins_secs(self._duration)
  
  @property
  def current_song(self):
    return self._current_song
    
  @current_song.setter
  def current_song(self, value):
    self._current_song = value

  @property
  def playing(self):
    return self._playing
  
  @playing.setter
  def playing(self, value):
    self._playing = value

  #takes a tuple containing song name, artist, duration, and id as input
  #Sends song data to song table in database
  def add_song(self, song):
    new_song = Song(song[1], song[2], song[3], song[0])
    self._songs.append(new_song)
    self._length = self._length + 1
    self._duration = int(self._duration) + int(song[3])
    DataBase.addSongsToDB(song[1], song[2], song[3], song[0], id)

  #calls spotify api to search by name
  def search_song(self, name):
    search = getSong(name)
    return search

  #print elements in song list
  def display_songs(self):
    for song in self.songs:
      print(song)

  #returns a song object
  def get_song(self, index):
    return self.songs[int(index)]
  
  # Play a song based off it's index in the playlist***
  def play(self, playlist_index):
    #now_playing equals the Song object at the provided index
    now_playing = self.get_song(playlist_index)

    #current_song is set equal to the playlist of the currently playing song
    self.current_song = playlist_index
    self.playing = True
    playSong(now_playing.song_id)
    return None

  # Pause a song ***
  def pause(self):
    # Insert media player to pause a song
    pauseSong()
    return None

  # Skip a song ***
  def skip(self):
    #if on the last song of the playlist, loop back to the first
    if(int(self.current_song) == int(self.length - 1)):
      self.current_song = 0
    else:
      #set current song to next song and play it
      self.current_song = int(self.current_song) + 1
    self.play(self.current_song)
    return None

  # Shuffle playlist ***
  def shuffle(self):
    random.shuffle(self.songs)

  # Automatically play the next song (temporal event) ***
  def play_next(pl):
    # When song finishes, play next song in queue

    #have function sleep for amount of time corresponding to current song duration?
    #take into account song pauses
    return None

  # Share a playlist via link ***
  def share_pl(pl):
  # Update playlist record
    return None
  
  # Sends playlist data to playlist table in Database 

  def getFromDB(self,name, user_id):
    self._playlist_name = DataBase.getPlaylistNameFromDB(user_id)
    self._length = DataBase.getPlaylistLengthFromDB(DataBase.getPlaylistIDFromDB(name, user_id))
    self._duration = DataBase.getPlaylistDurationFromDB(DataBase.getPlaylistIDFromDB(name, user_id))
    self._playlist_ID = DataBase.getPlaylistIDFromDB(name, user_id)




#Methods that send songs to the database 
class DataBase:
  # Method that sends songs to song table in database
  def addSongsToDB( song_id, name, artist, duration,):
    addSong = "INSERT INTO Song (Name, Artist, Duration, song_ID) VALUES (%s, %s, %s, %s)"
    song = (name, artist, duration, song_id)
    cursor.execute(addSong,song)
    mydb.commit()
    cursor.reset()

  # Store list of all avalible accounts ***
  def addAccountsToDB(username, password):
    account = (username, password)
    addAccount = "INSERT INTO User (Username, Password) VALUES (%s, %s)"
    cursor.execute(addAccount, account)
    mydb.commit()
    cursor.reset()

  # Store list of all public playlists ***
  def addPlaylistsToDB(name, user_ID):
    addPlaylist = "INSERT INTO playlist (Name, user_ID) VALUES (%s, %s)"
    playlist = (name, user_ID)
    cursor.execute(addPlaylist, playlist)
    mydb.commit()
    cursor.reset()

  def sendFollowFromDB(user_id, follow_id):
    val = (user_id, follow_id)
    command = "INSERT INTO Friends (user_ID, friend_ID) VALUES (%s, %s)"
    cursor.execute(command, val)
    mydb.commit()
    cursor.reset()

  # Store list of friend requests in Freind request Table
  def sendFriendRequestFromDB(id, usernameTwo):
    val = (id, DataBase.getAccountIDFromDB(usernameTwo))
    command = "INSERT INTO FriendRequest (user_ID, friend_ID) VALUES (%s, %s)"
    cursor.execute(command, val)
    mydb.commit()
    cursor.reset()

  # Adds freinds from friend Request Table to Friends
  def addFriendFromDB(usernameOne, usernameTwo, acceptance):
    val = (usernameOne.getAccountIDFromDB, usernameTwo.getAccountIDFromDB)
    if acceptance == True :
      command = "UPDATE FriendRequest SET Added = 1; INSERT INTO Friends (user_ID, friend_ID) VALUES (%s, %s);"
      cursor.execute(command,val)
      mydb.commit()
      cursor.reset()
    else :
      command = "DELETE FROM FreindRequest WHERE user_ID = %s AND friend_ID = %s;"
      cursor.execute(command,val)
      mydb.commit()
      cursor.reset()

  # Stores all Songs from a Playlist
  def addToPlaylist(playlistID, songID):
    val = (playlistID, songID)
    command = "INSERT INTO Playlist_Songs (playlist_ID, song_ID) VALUES (%s, %s)"
    cursor.execute (command, val)
    mydb.commit()
    cursor.reset()

  #All getters and setters for the DataBase
  def getSongNameFromDB(id):
    val = (id,)
    command = "SELECT Name FROM Song WHERE song_ID = %s;"
    cursor.execute(command, val)
    songName = cursor.fetchone()
    cursor.reset()
    return songName
  
  def getSongArtistFromDB(id):
    val = (id,)
    command = "SELECT Artist FROM Song WHERE song_ID = %s;"
    cursor.execute(command, val)
    songArtist = cursor.fetchone()
    cursor.reset()
    return songArtist
  
  def getSongDurationFromDB(id):
    val = (id,)
    command = "SELECT Duration FROM Song WHERE song_ID = %s;"
    cursor.execute(command, val)
    songDuration = cursor.fetchone()
    cursor.reset()
    return songDuration
  
  def getSongID(name):
    val = (name, )
    command = "SELECT song_ID FROM Song WHERE Name = %s;"
    cursor.execute(command, val)
    song_ID = cursor.fetchone()
    cursor.reset()
    return song_ID
  
  def getPlaylistNameFromDB(name, id):
    val = (name, id)
    command = "SELECT Name FROM Playlist WHERE Name = %s AND user_ID = %s;"
    playlistName = cursor.execute(command, val)
    cursor.reset()
    return playlistName
  
  def getPlaylistLengthFromDB(id):
    val = (id)
    command = "SELECT Length FROM Playlist WHERE playlist_ID = %s;"
    cursor.execute(command, val)
    playlistLength = cursor.fetchone()
    cursor.reset()
    return playlistLength
  
  def getPlaylistDurationFromDB(id):
    val = (id)
    command = "SELECT Duration FROM Playlist WHERE playlist_ID = %s;"
    playlistLength = cursor.execute(command, val)
    cursor.reset()
    return playlistLength
  
  def getPlaylistIDFromDB(name,):
    val = (name,)
    command = "SELECT Name FROM Playlist WHERE Name = %s;"
    cursor.execute(command,val)
    playlist_ID = cursor.fetchone()
    cursor.reset()
    return playlist_ID
  
  def newPlaylistLength(length,id):
    val = (length, id)
    command = "UPDATE Playlist SET Length = %s WHERE playlist_ID = %s;"
    cursor.execute(command,val)
    mydb.commit()
    cursor.reset()
  
  def getAccountNameFromDB(name):
    val = (name, )
    command = "SELECT Username FROM User WHERE Username = %s;"
    accountName = cursor.execute(command, val)
    accountName = cursor.fetchone()
    cursor.reset()
    return accountName

  def getAccountIDFromDB(name):
    val = (name, )
    command = "SELECT user_ID FROM User WHERE Username = %s;"
    cursor.execute(command, val)
    accountID = cursor.fetchone()[0]
    cursor.reset()
    return accountID
  
  def checkLoginInDB(username, password):
    val = (username, password)
    command = "SELECT Username, Password FROM User WHERE Username = %s AND Password = %s;"
    cursor.execute(command, val)
    result = cursor.fetchone()  
    return result
    

  def getFriendRequestFromDB(username):
    command = "SELECT friend_ID FROM FriendRequest WHERE user_ID = %s;"
    cursor.execute(command, username.getAccountIDFromDB)
    requestList = cursor.fetchone()
    cursor.reset()
    return requestList

  def getFriendsFromDB(self):
    command = "SELECT friend_ID FROM Friends WHERE user_ID = %s;"
    cursor.execute(command , self.getAccountIDFromDB)
    friendList = cursor.fetchone()
    cursor.reset()
    return friendList
  
  def getSongsFromPlaylist(self, playlist_id):
    val = (playlist_id, )
    command = "SELECT song_ID FROM Playlist_songs WHERE playlist_ID = %s;"
    cursor.execute(command, val)
    songIDs = cursor.fetchall()
    cursor.reset()
    #returns tuple with all song IDS in a playlist
    return songIDs
  
  def getAllPlaylistsFromDB(id):
    val = (id, )
    command = "SELECT Name, playlist_ID FROM playlist WHERE user_ID = %s;"
    cursor.execute(command, val)
    allPlaylists = cursor.fetchall()
    cursor.reset()
    return allPlaylists
  
 

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

        login_username_entry = tk.Entry(self.login_frame)
        login_username_entry.pack()

        password_label = tk.Label(self.login_frame, text = "Password:")
        password_label.pack()

        login_password_entry = tk.Entry(self.login_frame, show ="*")
        login_password_entry.pack()

        #command used to call functions within the program
        login_button = tk.Button(self.login_frame, text = "Login", command = lambda: Account.checkLogin(self, login_username_entry.get(), login_password_entry.get()))
        

        
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

        register_button = tk.Button(
           self.register_frame, text = "Register", 
           command = lambda:(Account.addAccount(username_entry.get(), password_entry.get(), password_entry2.get()), self.to_login())
        )
        register_button.pack()

        self.login_frame.pack()

# --------------------------------Login Screen Functions ---------------------------------------------------
    def to_mainMenu(self, user_ID):
        self.withdraw()
        self._user_ID = user_ID
        self.main_menu = MainMenu(user_ID)

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
    def __init__(self, user_ID):
        super().__init__()
        self.title('Main Menu')
        self.geometry('1600x900')
        self._user_ID = user_ID

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

         #on login, iterate through database for a user's playlists, then create buttons for them
        # Create a cursor object to execute SQL queries

        #needs to return an array of all a user's playlists
        usersPlaylists = DataBase.getAllPlaylistsFromDB(user_ID)
        
        #buttons need to be in left frame
       # for playlist_tuple in usersPlaylists:
        #  playlistName = playlist_tuple[0]  # Access the first element (Name)
         # playlist_ID = playlist_tuple[1]  # Access the second element (playlist_ID)
          #self.playlist.insert(tk.END, playlistName)
          #self.playlist.bind("<Button-1>", lambda event, name = playlistName, pid = playlist_ID: (self.open_playlist(name, pid)))
          #print(playlistName, playlist_ID, ' 4')
          #self.playlist.pack(side='top', fill='both')

         #Create buttons for each playlist
        for playlist_name, playlist_id in usersPlaylists:
            #Insert playlist name into the listbox
          self.playlist.insert(tk.END, playlist_name)
             #Create a button for the playlist
          button = tk.Button(left_frame, text=playlist_name,
                               command=lambda name = playlist_name, pid=playlist_id: self.open_playlist(name, pid))
          button.pack(side='top', fill='both')

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
        self.createPlaylist = tk.Button(middle_frame, text='Create Playlist', font = 'Arial 14', height=10, width=20, command = lambda: self.create_playlist(self._user_ID)) # command = create_playlist
        self.createPlaylist.pack(expand = True, padx=30)
        
        # Follow Account Button
        self.addFriend = tk.Button(middle_frame, text='Follow an Account', font = 'Arial 14', height=10, width=20, command = self.add_follow) # command = add_friend
        self.addFriend.pack(expand = True, padx=30)


        self.mm_frame.pack(fill='both')

# --------------------------------Main Menu Functions ---------------------------------------------------
    def create_playlist(self, user_ID):
        # Create a new frame in the main window
        self.create_frame = tk.Frame(self)

        # Create a label and a text box entry
        label = tk.Label(self.create_frame, text="Enter a playlist name:")
        label.pack()
        entry = tk.Entry(self.create_frame)
        entry.pack()
        # Create a confirmation button
        confirm_button = tk.Button(self.create_frame, text="Create Playlist", command=lambda: [self.to_playlist(entry.get()), DataBase.addPlaylistsToDB(entry.get(), user_ID)])
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

    # Go to Playlist/create playlist
    def to_playlist(self, entry):
        if (entry == ""): # Error message when playlist name is empty
            error = tk.Toplevel(self)
            error.title("Error")
            error.geometry("200x100")
            label = tk.Label(error, text="Please give your playlist a name")
            label.pack()
        else:
            self.new_playlist = YourPlaylist(self, entry)
            self.playlist.insert(tk.END, entry)

    def open_playlist(self, playlistName, playlist_ID):
       self.new_playlist = YourPlaylist(self, playlistName, playlist_ID)

    # Return to login
    def to_login(self):
        self.withdraw()
        self.login = Login()


#Follow an account
    def add_follow(self):
     # Create a new window
        window = tk.Toplevel()
        window.geometry('500x300')
        # Create a label and an entry widget
        label = tk.Label(window, text="Enter username:")
        label.pack()
        entry = tk.Entry(window)
        entry.pack()

        # Create a confirmation button
        confirm_button = tk.Button(window, text="Follow Account", command=lambda: self.send_follow(entry.get(), self._user_ID))
        confirm_button.pack()

        # Create a cancel button
        cancel_button = tk.Button(window, text="Cancel", command=window.destroy)
        cancel_button.pack()

        # Check for user
    def check_user(username, user_ID):
        if username == DataBase.getAccountNameFromDB(username):
            # Send a friend request to the user
            user_ID
        else:
            # Print an error message
            print(f"User not found: {username}")

    # Send Friend Request        
    def send_follow(self, username, user_id):
        print(username)
        if DataBase.getAccountNameFromDB(username) is not None :
        # Send a friend request to the user
          followID = DataBase.getAccountIDFromDB(username)
          DataBase.sendFollowFromDB(user_id, followID)
          print(f"Now following {username}")
        else:
            print(f"User not found: {username}")



############################################################################
# Test for friend request function

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
        confirm_button = tk.Button(window, text="Add ", command=lambda: self.send_fr(entry.get(), self._user_ID))
        confirm_button.pack()

        # Create a cancel button
        cancel_button = tk.Button(window, text="Cancel", command=window.destroy)
        cancel_button.pack()

    # Check for user
    def check_user(username, user_ID):
        if username == DataBase.getAccountNameFromDB(username):
            # Send a friend request to the user
            user_ID
        else:
            # Print an error message
            print(f"User not found: {username}")

    # Send Friend Request        
    def send_fr(username, user_ID):
        if DataBase.getAccountNameFromDB(username) != None :
        # Send a friend request to the user
            DataBase.sendFriendRequestFromDB(user_ID, username)
            print(f"Friend request sent to {username}")
        else:
            print(f"User not found: {username}")

    # Accept Friend Request
    def accept_friend_request(self, requester):
        # Condition: username exists and requester inputs their name 
        if self.username in DataBase and requester in DataBase[self.username]['friend_requests']:
        # 1) Remove the friend request from the user's list of friend requests
            DataBase[self.username]['friend_requests'].remove(requester)

        # 2) Add the requester as a friend of the user
            if 'friends' not in DataBase[self.username]:
                DataBase[self.username]['friends'] = []
            DataBase[self.username]['friends'].append(requester)

        # 3) Add the user as a friend of the requester
            if 'friends' not in DataBase[requester]:
                DataBase[requester]['friends'] = []
            DataBase[requester]['friends'].append(self.username)
            # Accept Message
            print(f"Friend request accepted from {requester}")

    # Decline Friend Request
    def reject_friend_request(self, requester):
        if self.username in DataBase and requester in DataBase[self.username]['friend_requests']:
        # Remove the friend request from the user's list of friend requests
            DataBase[self.username]['friend_requests'].remove(requester)
            # Decline Message
            print(f"Friend request rejected from {requester}")
            


              
# *************** Playlist Class **************************
class YourPlaylist(tk.Toplevel):
    def __init__(self, master, name, playlistID=None):
        tk.Toplevel.__init__(self, master)
        self.name = name
        self.title(name)
        self.geometry('1600x900')
        self.songs = []
        label = tk.Label(self, text=f"{self.name}")
        label.pack()
        self.playlistID = playlistID
        ######## Playlist Frame ##########################################################################
        self.playlist_frame = tk.Frame(self)

        # Display Headings (Title/Artist/Duration Headings)
        self.table = ttk.Treeview(self.playlist_frame, columns=('title', 'artist', 'duration'), show='headings')
        self.table.heading('title', text='Song Title')
        self.table.heading('artist', text='Artist')
        self.table.heading('duration', text='Duration')
        self.table.pack(fill='both', expand = True)

        userSongs = DataBase.getSongsFromPlaylist(self, playlistID)


        for num in userSongs:
          songName = DataBase.getSongNameFromDB(num[0])
          songArtist = DataBase.getSongArtistFromDB(num[0])
          songDuration = DataBase.getSongDurationFromDB(num[0])
          time = ms_to_mins_secs(songDuration[0])
          self.table.insert('', 'end', values = (songName, songArtist, time))

        self.title_label = ttk.Label(master=self.playlist_frame, font='Arial 18')
        self.title_label.pack()

        # Display Buttons at bottom

        button_frame = tk.Frame(self.playlist_frame)
        self.play_button = tk.Button(button_frame, text = 'Play', command=self.play)
        self.search_button = tk.Button(button_frame, text = 'Search', command = self.to_search)

        # Pack the buttons into the frame and center them
        self.play_button.pack()
        self.search_button.pack()
        button_frame.pack(fill='both', expand=False)

        self.playlist_frame.pack(fill='both', expand = True)

        if playlistID is not None:
          songList = DataBase.getSongsFromPlaylist(self, playlistID)

# --------------------------------Playlist Functions ---------------------------------------------------
        def play_selected(e):
            selected = self.table.focus()
            self.contents = self.table.item(selected)

            name = self.contents['values'][0]
            name_without_brackets = name[1:-1]

           # name_without_brackets = name[1:-1]
            print(name)
           # print(name_without_brackets)
            
            try:
              id = DataBase.getSongID(name)
              print(id)
              playSong(id[0])
             
            except:
              id = DataBase.getSongID(name_without_brackets)
              print(id)
              playSong(id[0])

        self.table.bind("<<TreeviewSelect>>", play_selected)

    def item_select(self, _):
        print(self.table.selection())
        for i in self.table.selection():
            print(self.table.item(i)['values'])
    
    # Add Song
    def add_songs(self, song):
       self.table.insert('', 'end', values=song)

    # Delete Song
    def delete_song(self):
        print('Song has been removed')
        for i in self.table.selection():
            self.table.delete(i)

    # Play First Song
    def play(self):
        MusicPlaylist(self.name).play(0)

    def update(self):
        for song in MusicPlaylist(self._playlist).songs:
            self.table.insert(Song(song))
    
    # Go to Search Screen
    def to_search(self):
        #if self.playlistID is not None:
        self.withdraw()
        self.search = Search(self, self.name, self.playlistID)


class Search(tk.Tk):
    def __init__(self, master, name, playlistID):
        super().__init__()
        self.master = master  # Keep a reference to the parent window
        self.title('Search Screen')
        self.geometry("1600x900")
        self.name = name
        self._playlist = playlistID

        self.search_frame = tk.Frame(self)
        self.search_frame.pack()

        search_label = Label(self.search_frame, text="Search for music.")
        search_label.pack()

        search_bar = Entry(self.search_frame)
        search_bar.pack()

        result_list = Listbox(self.search_frame)
        result_list.pack()

        playlist_button = tk.Button(self.search_frame, text='Return to Playlist', command=lambda: self.to_playlist()) # command = to_playlist
        playlist_button.pack(side='bottom')

        # --------------------------------Search Screen Functions ---------------------------------------------------
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
            if selected:
                new_song = (songs[selected[0]][0], songs[selected[0]][1], songs[selected[0]][2], songs[selected[0]][3])
                print(new_song)
                #self._playlist.add_song(new_song)
                #self._playlist.display_songs()
                if (DataBase.getSongID(new_song[1]) != new_song[0]):
                  try:
                    DataBase.addSongsToDB(new_song[0], new_song[1], new_song[2], new_song[3]) 
                  except:
                     print()
                  DataBase.addToPlaylist(playlistID, new_song[0])

                else:
                   DataBase.addToPlaylist(playlistID, new_song[1])
                
            
            #playSong() takes the id of the selected song
            #playSong(songs[selected[0]][0])

        #on event, run the specified function
        search_bar.bind("<Return>", check)
        result_list.bind("<<ListboxSelect>>", add_selected)

    def to_playlist(self):
        self.withdraw()
        self.playlist = YourPlaylist(self, self.name, self._playlist)
        #MusicPlaylist.add_song(selected)


if __name__ == '__main__':
    print("Hello")
    app = Login()
    app.mainloop()