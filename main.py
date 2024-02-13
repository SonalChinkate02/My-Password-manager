
from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pass():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters)for _ in range(randint(4, 8))]
    password_sym = [choice(symbols)for _ in range(randint(2, 4))]
    password_num = [choice(numbers)for _ in range(randint(2, 4))]

    password_list=[]
    password_list = password_letters + password_sym + password_num
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0,f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {website:{
        "email":email,
        "password":password
    }}


    if len(website)==0 or len(password)== 0:
        messagebox.showinfo(title="error",message="Please make sure don\'t leave any fields empty")
    else:
            try:
                with open("data.json","r") as data_file:
                    #Reading old data
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("data.json", 'w') as data_file:
                    json.dump(new_data,data_file, indent=4)
            else:
                #updating old data with new data
                data.update(new_data)
            
                with open("data.json", 'w') as data_file:
                    #Saving updated data
                    json.dump(data,data_file, indent=4)

            finally:
                website_input.delete(0,END)
                password_input.delete(0,END)

            messagebox.showinfo(title="Message",message="Saved Successfully")

#-----------------------------------FIND PASSWORD---------------------------------#
def find_password():
    website = website_input.get()
    try:
        with open("data.json","r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error",message="No Data File Found.")
    else:
        if website in data:
            entry = data[website]
            email = entry["email"]
            password = entry["password"]
            messagebox.showinfo(title=website, message=f"Email:{email}\nPassword:{password}")
        else:
            messagebox.showinfo(title=website, message=f"No details for  {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)


canvas = Canvas(width=200,height=200)
logo_image = PhotoImage(file="new_lock.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(column=1,row=0)

#Labels
website_label = Label(text="Website",font=("Bookman Old Style",11,'bold'))
website_label.grid(column=0,row=1)
email_label = Label(text="Email/Username",font=("Bookman Old Style",11,'bold'))
email_label.grid(column=0,row=2)
password_label = Label(text="Password",font=("Bookman Old Style",11,'bold'))
password_label.grid(column=0,row=3)

#Input entries
website_input = Entry(width=40)
website_input.grid(column=1,row=1,columnspan=2)
website_input.focus()
email_input = Entry(width=40)
email_input.grid(column=1,row=2,columnspan=2)
email_input.insert(0,"yourEmailAddress@gmail.com")
password_input = Entry(width=30, show="*")
password_input.grid(column=1,row=3)

search_button = Button(text="Search", command=find_password)
search_button.config(background="#7074c9",fg="#ffffff")
search_button.grid(column=3, row=1)

gen_pass_button = Button(text="Generate Password",command=generate_pass)
gen_pass_button.config(background="#7074c9",fg="#ffffff")
gen_pass_button.grid(column=2,row=3)

add_button = Button(text="Add",width=38, command=save)
add_button.config(background="#5049dd",fg="#ffffff")
add_button.grid(column=1,row=5,columnspan=2)

window.mainloop()