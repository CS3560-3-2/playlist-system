import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image


#implement these at later date
def validate_login():
    userid  = username_entry.get()
    password = password_entry.get()

    #check the db to see if the user exists and if so, does the password match?
    #use methods from 'cs_3560_project.py' to perform these checks from the db
    if userid == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def validate_register():
    password = password_entry.get()
    password2 = password_entry2.get()

    if password == password2:
        messagebox.showinfo("Registration Successful!")
    else:
        messagebox.showerror("Registration Failed", "Invalid username or password.")
    #create an Account object. Make sure we have code within the Account class that updates the db with credentials

class App(tk.Tk):
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
        login_button = tk.Button(self.login_frame, text = "Login", command = validate_login)
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


        #MAIN MENU
    
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

        confirm_button = tk.Button(button_frame, text="Create Playlist", command=lambda: YourPlaylist(self, entry.get()))

        self.SearchButton = tk.Button(self, text='Search for Playlists', font = 'Arial 14', height=12, width=20, command=lambda: SearchScreen(self)) # command = open_playlist
        self.SearchButton.place(x=670, y = 580)


        #PLAYLIST
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

        #SEARCH SCREEN
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
            playSong(songs[selected[0]][0])

        search_label = Label(root, text="Search for music.")
        search_label.pack()

        search_bar = Entry(root)
        search_bar.pack()

        result_list = Listbox(root)
        result_list.pack()

            #on event, run the specified function
        search_bar.bind("<Return>", check)
        result_list.bind("<<ListboxSelect>>", play_selected)

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

if __name__ == '__main__':
    # instantiate App and run it
    app = App()
    app.mainloop()




