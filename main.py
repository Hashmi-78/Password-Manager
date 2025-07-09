from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import json

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    char_list= [choice(letters) for char in range(randint(8, 10))]
    numbers_list = [choice(numbers) for char in range(randint(2, 4))]
    symbols_list = [choice(symbols) for char in range(randint(2, 4))]

    password_list = char_list + numbers_list + symbols_list
    shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0,END)
    password_input.insert(0,password)
    pyperclip.copy(password)

def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website : {
            "email":email,
            "password":password,
        }
    }
    
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Invalid Input", message="Please fill out the required Fields!")
    else:
        try:
            with open("data.json", "r") as data_file:
                #reading data
                data = json.load(data_file)
                #saving data
                data.update(new_data)
        except FileNotFoundError:        
            with open("data.json","w") as data_file:
                #writing data
                json.dump(new_data,data_file, indent=4)
                website_input.delete(0,END)
                password_input.delete(0,END)
        else:
            with open("data.json","w") as data_file:
                json.dump(data,data_file, indent=4)
        finally:   
                messagebox.showinfo(title="Success", message=f"Details for {website} saved successfully!\n Email: {email}\n Password : {password}")
                website_input.delete(0,END)
                password_input.delete(0,END)
                
def search_password():
    website = website_input.get()

    if len(website) == 0:
        messagebox.showerror(title="Erorr",message="Please fill out the requied field!")
    
    try:
        with open("data.json","r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="No Data is found!")
    
    if website in data:
        email = data[website]["email"]
        password = data[website]["password"]
        messagebox.showinfo(title=website, message = f"Email : {email}\n Password : {password}")
        pyperclip.copy(password)
    else:
        messagebox.showerror(title="Error", message="No file Found")  

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200,width=200)
logo = PhotoImage(file="D:/python/turtle/Password Manager/logo.png")

canvas.create_image(100,100,image=logo)
canvas.grid(column=1,row=1,columnspan=3)

website_label = Label(text="Website", font=("Arial",10,"normal"))
website_label.grid(column=0,row=2, sticky="w")
email_label = Label(text="Email/Username", font=("Arial",10,"normal"))
email_label.grid(column=0,row=3)
password_label = Label(text="Password", font=("Arial",10,"normal"))
password_label.grid(column=0,row=4,sticky="w")

website_input = Entry(width=36)
website_input.grid(column=1,row=2, columnspan=2,sticky="w",pady=3)
website_input.focus()
email_input = Entry(width=50)
email_input.grid(column=1,row=3, columnspan=2,sticky="w",pady=3)
email_input.insert(0,"umerhashmi898@gmail.com")
password_input = Entry(width=27)
password_input.grid(column=1,row=4,sticky="w",pady=3)

search_button = Button(text="Search",font=("Arial",10,"normal"),width=10,pady=3,command=search_password)
search_button.grid(column=2,row=2)

generate_button = Button(text="Generate Password",font=("Arial",10,"normal"),command=generate_password)
generate_button.grid(column=2,row=4)

add_button = Button(text="Add",font=("Arial",10,"normal"),width=36,pady=3,command=save_password)
add_button.grid(column=1,row=6,columnspan=2)



window.mainloop()