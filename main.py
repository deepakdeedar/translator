from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_input.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)


# ---------------------------- SEARCH PASSWORD ----------------------------- #
def find_password():
    web = website_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data file found.")
    else:
        if web in data:
            email = data[web]["email"]
            password = data[web]["password"]
            messagebox.showinfo(title=web, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {web} exists.")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    print("yes")
    web = website_input.get()
    user = username_input.get()
    pswd = password_input.get()
    new_data = {
        web: {
            "email": user,
            "password": pswd
        }
    }

    if len(web) == 0 or len(pswd) == 0:
        messagebox.showerror(title="Oops" , message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=web,
                                       message=f"These are the details entered: \nEmail: {user}\n Password: {pswd}\nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(height=200, width=200)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(row=0, column=1)

website = Label(text="Website: ")
website.grid(row=1, column=0)

website_input = Entry(width=35)
website_input.grid(row=1, column=1)

search_btn = Button(text="Search", width=15, command=find_password)
search_btn.grid(row=1, column=2)

username = Label(text="Email/Username: ")
username.grid(row=2, column=0)

username_input = Entry(width=35)
username_input.insert(0, "deepakdeedarsingla111@gmail.com")
username_input.grid(row=2, column=1, columnspan=2)

password = Label(text="Password: ")
password.grid(row=3, column=0)

password_input = Entry(width=35)
password_input.grid(row=3, column=1)

gen_pass = Button(text="Generate Password", command=generate_password)
gen_pass.grid(row=3, column=2)

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()