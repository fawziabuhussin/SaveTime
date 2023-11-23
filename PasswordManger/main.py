from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '!@#$%^&*()_-+=<>?/{}[]|'
numbers = '0123456789'

def generate_pass():

    letter_chars = [random.choice(letters) for _ in range(random.randint(8, 10))]
    symbol_chars = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    number_chars = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_chars = letter_chars + symbol_chars + number_chars
    random.shuffle(password_chars)
    password = "".join(password_chars)

    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = pass_entry.get()
    new_data = { website:
                     {
                        "username" : username,
                         "password" : password
                     }
    }

    if len(website) == 0 or len(password) == 0:
            messagebox.showinfo(title="Oops", message=f"Please, fill the blank")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the data you entered: \nUsername: "
                                                           f"{username}\nPassword: {password}\n Is it ok to save?")

        if is_ok :
            # with open("password.txt", "a") as passwords_file: *** IF I WANT TO USE AS TXT ***
            # passwords_file.write(f"{website} :- {username} | {password}\n") *** THIS IS HOW TO SAVE IN TXT ***
            try :
                with open("password.json", "r") as data_file:
                    #Read the data:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("password.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                #Update the data.
                data.update(new_data)
                #Save the data.
                with open("password.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

            #Remove the password after entering.
            website_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- SEARCH ENGINE ------------------------------- #


def search_user():
    try:
        with open("password.json", "r") as data_file:
            # Read the data:
            data = json.load(data_file)
            website = website_entry.get()
            if len(website) == 0:
                messagebox.showinfo(title="Oops", message=f"Please, fill the blank")
            else :
                if website in data:
                    username = data[website]['username']
                    password = data[website]['password']
                    messagebox.showinfo(title=website, message=f"Username: {username}\nPassword: {password}")
                else:
                    messagebox.showinfo(title="Oops", message=f"Info about {website} not found, please add it!")

    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message=f"No data file found")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100,100, image=img)
canvas.grid(row=0, column=1)


# LABELS.
website_label = Label(text="website:", fg="black")
username_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

website_label.grid(row=1, column=0)
username_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)


# ENTRIES.
website_entry = Entry(width=31)
username_entry = Entry(width=49)
pass_entry = Entry(width=31)

website_entry.grid(row=1, column=1)
username_entry.grid(row=2, column=1, columnspan=2)
pass_entry.grid(row=3, column=1)

website_entry.focus()
username_entry.insert(END, "foze820@gmail.com")


# BUTTONS.

search_button = Button(text="Search", relief="ridge" , width=15, bg="white", fg="red", command=search_user)
generate_password_button = Button(text="Generate Password", relief="ridge", command= generate_pass, bg="white", fg="red")
add_button = Button(text="Add", width=42, relief="ridge", command=save_password, bg="black", fg="white")

search_button.grid(row=1, column= 2)
generate_password_button.grid(row=3, column= 2)
add_button.grid(row=4, column=1, columnspan=2)




window.mainloop()


