from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Lists of characters for password generation
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Generate random letters, symbols, and numbers for the password
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    # Combine all characters and shuffle for randomness
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    # Create password string from list and insert into entry field
    password = "".join(password_list)
    password_entry.insert(0,password)

    # Copy password to clipboard
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # Gather data from entries
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password
        }
    }

    # Check for empty fields
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo("Oops", "Please don't leave any fields empty!")
    else:
        # Try to open existing data file to read data
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            # If file not found, create a new one with the new data
            with open("data.json", "w") as data_file:
                json.dump(new_data,data_file, indent=4)
        else:
            # Update existing data with new entry and save
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            # Clear entries after saving
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    # Get the website entered by the user
    website = website_entry.get()

    try:
        # Try to open the data file to search for the website
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        # Show error if data file doesn't exist
        messagebox.showinfo("Error","No Data File Found.")
    else:
        # Show email and password if website is found, otherwise show an error
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(website,f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo("Error", "No Data File Found.")

# ---------------------------- UI SETUP ------------------------------- #
# Creating main window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50,bg='white')

# Attach the image to the main window
canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)  # Add image to canvas
canvas.grid(column= 1, row=0)

# Add labels
website_label = Label(text="Website:", bg="white")
website_label.grid(column= 0, row=1)

email_username_label = Label(text="Email/Username:", bg="white")
email_username_label.grid(column= 0, row=2)

password_label = Label(text="Password:", bg="white")
password_label.grid(column= 0, row=3)

# Add entries
website_entry = Entry(width=21)
website_entry.grid(column= 1, row=1)
website_entry.focus()

email_username_entry = Entry(width=39)
email_username_entry.grid(column= 1, row=2,columnspan=2)
email_username_entry.insert(0, "priel@email.com")

password_entry = Entry(width=21)
password_entry.grid(column= 1, row=3)

# Add buttons
add_button = Button(text="Add",width=36,command=save)
add_button.grid(column= 1, row=4,columnspan=2)

generate_button = Button(text="Generate Password",command=generate_password)
generate_button.grid(column= 2, row=3)

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column= 2, row=1)

window.mainloop()