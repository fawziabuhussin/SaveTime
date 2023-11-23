from tkinter import *
from tkinter import messagebox
import random
import pyperclip

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

    if len(website) == 0 or len(username) or len(password) :
            messagebox.showinfo(title="Oops", message=f"Please, fill the blank")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the data you entered: \nUsername: "
                                                           f"{username}\nPassword: {password}\n Is it ok to save?")

        if is_ok :
            with open("password.txt", "a") as passwords_file:
                passwords_file.write(f"{website} :- {username} | {password}\n")
                website_entry.delete(0, END)
                pass_entry.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100,100, image=img)
canvas.grid(row=0, column=1)


# LABELS.
website_label = Label(text="website:")
username_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

website_label.grid(row=1, column=0)
username_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)


# ENTRIES.
website_entry = Entry(width=49)
website_entry.focus()

username_entry = Entry(width=49)
username_entry.insert(END, "foze820@gmail.com")
pass_entry = Entry(width=31)

website_entry.grid(row=1, column=1, columnspan=2)
username_entry.grid(row=2, column=1, columnspan=2)
pass_entry.grid(row=3, column=1)


# BUTTONS.
generate_password_button = Button(text="Generate Password", relief="ridge", command= generate_pass)
add_button = Button(text="Add", width=42, relief="ridge", command=save_password)

generate_password_button.grid(row=3, column= 2)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()


