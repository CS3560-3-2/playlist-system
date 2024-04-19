import tkinter as tk
from tkinter import *
from tkinter import messagebox

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




