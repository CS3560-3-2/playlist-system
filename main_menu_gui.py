import tkinter as tk
from tkinter import *

mainMenu = tk.Tk()
mainMenu.title('Main Menu')
#Geometry to be determined

emptySpace = tk.Label(mainMenu, text = "     ")

mainMenuLabel = tk.Label(mainMenu, text  = 'Main Menu')
mainMenuLabel.grid(row = 0, column = 0, columnspan = 2)

playlistsLabel = tk.Label(mainMenu, text  = 'Playlists')
playlistsLabel.grid(row = 1, column = 0)

friendslistLabel = tk.Label(mainMenu, text  = 'Friends')
friendslistLabel.grid(row = 1, column = 1)

createPlaylist = tk.Button(mainMenu, text = 'Create Playlist') #command = create playlist
createPlaylist.grid(row = 2, column = 0)

addFriend = tk.Button(mainMenu, text = 'Add Friend') #command = addfriend
addFriend.grid(row = 2, column = 1)

#Iterate through users playlists and create buttons for each
#Button leads to new window for a playlist
testButton1 = tk.Button(mainMenu, text = 'sample playlist') #command = openplaylist
testButton1.grid(row = 3, column = 0)

#Iterate through friendslist and create labels for each friend, maybe buttons for friend profiles
testLabel1 = tk.Label(mainMenu, text = 'sample friend')
testLabel1.grid(row = 3, column = 1)

mainMenu.mainloop()

