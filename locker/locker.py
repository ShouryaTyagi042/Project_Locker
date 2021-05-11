import tkinter as tk
from tkinter import messagebox
import base64
import os
import time
import sys
root = tk.Tk()
root.title("Credentials")
# setting the windows size
root.geometry("800x250")
root.configure(bg="#c1f1dc")
# declaring string variable
# for storing name and password
name_var = tk.StringVar()
passw_var = tk.StringVar()


# defining a function that will
# get the name and password and
# print them on the screen
def submit():

    name = name_var.get()
    password = passw_var.get()

    # print("The name is : " + name)
    # print("The password is : " + password)

    message = "SAMSUNGgalaxym20"
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    encode = base64_bytes.decode('ascii')

    message1 = "GintokiSakata8864"
    message_bytes1 = message1.encode('ascii')
    base64_bytes1 = base64.b64encode(message_bytes1)
    encode1 = base64_bytes1.decode('ascii')

    def goto(linenum):
        global line
        line = linenum

    line = 1
    while True:
        # pw = str(input("Enter your password for Lock or Unlock your folder: "))

        base64_bytes = encode.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode('ascii')

        base64_bytes = encode1.encode('ascii')
        message_bytes1 = base64.b64decode(base64_bytes)
        message1 = message_bytes1.decode('ascii')

        if password == message and name == message1:
            # Change Dir Path where you have Locker Folder
            os.chdir("F:\\Android\\media\\com.nomedia")
        # If Locker folder or Recycle bin does not exist then we will be create Locker Folder
            if not os.path.exists("Locker"):
                if not os.path.exists("Locker.{645ff040-5081-101b-9f08-00aa002f954e}"):
                    os.mkdir("Locker")
                    messagebox.showinfo("Info", "Locker folder is created .")
                else:
                    os.popen(
                        'attrib -h Locker.{645ff040-5081-101b-9f08-00aa002f954e}')
                    os.rename(
                        "Locker.{645ff040-5081-101b-9f08-00aa002f954e}", "Locker")
                    messagebox.showinfo("Info", "Folder is unlocked")
                    sys.exit()
            else:
                os.rename(
                    "Locker", "Locker.{645ff040-5081-101b-9f08-00aa002f954e}")
                os.popen(
                    'attrib +h Locker.{645ff040-5081-101b-9f08-00aa002f954e}')
                messagebox.showinfo("Info", "Folder is locked")
                sys.exit()

        else:
            print("Wrong password!, Please Enter right password")
            time.sleep(5)
            goto(1)

    name_var.set("")
    passw_var.set("")


# creating a label for
# name using widget Label
name_label = tk.Label(root, text='Username', font=(
    'Baskerville Old Face', 40, 'bold'), fg="#496076", bg="#c1f1dc")

# creating a entry for input
# name using widget Entry
name_entry = tk.Entry(root, textvariable=name_var,
                      font=('Baskerville Old Face', 20, 'normal'), bg="#496076", fg="#c1f1dc", width=40)

# creating a label for password
passw_label = tk.Label(root, text='Password', font=(
    'Baskerville Old Face', 40, 'bold'), fg="#496076", bg="#c1f1dc")

# creating a entry for password
passw_entry = tk.Entry(root, textvariable=passw_var,
                       font=('Baskerville Old Face', 20, 'normal'), show='*', bg="#496076", fg="#c1f1dc", width=40)

# creating a button using the widget
# Button that will call the submit function
sub_btn = tk.Button(root, text='Submit', command=submit, font=('Baskerville Old Face', 20, 'normal'),
                    bg="#496076", fg="#c1f1dc",  width=20)

# placing the label and entry in
# the required position using grid
# method
name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
passw_label.grid(row=1, column=0)
passw_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)

# performing an infinite loop
# for the window to display
root.mainloop()
