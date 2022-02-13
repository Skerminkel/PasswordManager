from tkinter import *
from tkinter import messagebox
from random import choice, randint
from chars import char_list
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def spinbox_used():
    return spinbox.get()


def generate():
    length = int(spinbox_used())
    password_list = [choice(char_list) for _ in range(length)]
    password = "".join(password_list)
    password_entry.insert(0, password)

    pyperclip.copy(password)


def search():
    try:
        with open("NoneOfYourBusiness.json", "r") as f:
            data_dict = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(
                title="No entry", message=f"You don't have anything saved for {website_entry.get()}"
            )
    else:
        try:
            result = data_dict[website_entry.get()]
        except KeyError:
            messagebox.showinfo(
                title="No entry", message=f"You don't have anything saved for {website_entry.get()}"
            )
        else:
            username_entry.delete(0, END)
            username_entry.insert(0, result["username"])
            password_entry.insert(0, result["password"])

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {"username": username,
                  "password": password}
    }
    if len(website_entry.get()) == 0 or len(username_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showwarning(title="Can't save.", message="You have one or more empty fields.")

    else:
        confirm = messagebox.askokcancel(title="These are the details:", message=f"{website}\n{username}\n{password}")
        if confirm:
            try:
                with open("NoneOfYourBusiness.json", "r") as f:
                    data = json.load(f)  # Read from .json
            except FileNotFoundError:
                with open("NoneOfYourBusiness.json", "w") as f2:
                    json.dump(new_data, f2, indent=4)
            else:
                data.update(new_data)  # Update with new data
                with open("NoneOfYourBusiness.json", "w") as f3:
                    json.dump(data, f3, indent=4)  # Write to .json

            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()

        else:
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
win = Tk()
win.title("Password Manager")
win.minsize(width=100, height=100)
win.config(padx=50, pady=30)
LOGO = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=LOGO)
canvas.grid(column=1, row=0, columnspan=2)

website_lab = Label(text="Website:")
website_lab.grid(column=0, row=1)
username_lab = Label(text="Email/Username:")
username_lab.grid(column=0, row=2)
password_lab = Label(text="Password:")
password_lab.grid(column=0, row=3)

gen_pass = Button(text="Generate Password", command=generate)
gen_pass.grid(column=3, row=3, sticky="ew", columnspan=2)
add = Button(text="Add", command=save)
add.grid(column=1, row=4, columnspan=4, sticky="ew")
search_button = Button(text="Search", command=search)
search_button.grid(column=3, row=1, columnspan=2, sticky="ew")

website_entry = Entry()
website_entry.grid(column=1, row=1, columnspan=2, sticky="ew")
website_entry.focus()
username_entry = Entry()
username_entry.grid(column=1, row=2, columnspan=2, sticky="ew")
username_entry.insert(0, "waynedas1@gmail.com")
password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="ew", columnspan=2)

spinbox = Spinbox(from_=8, to=20, width=4, command=spinbox_used)
spinbox.grid(column=2, row=3, sticky="e")

win.mainloop()
