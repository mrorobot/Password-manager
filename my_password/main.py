from tkinter import *
import json
from tkinter import messagebox
import random
windows=Tk()

def gen_pass():
    alpha= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
      'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
      'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    num=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols=["!","@", "#", "$", "%", "&", "*"]
    rand_alpha=random.choices(alpha,k=4)
    rand_num=random.choices(num,k=2)
    rand_sym = random.choices(symbols, k=2)
    pass_item=rand_alpha + rand_num+ rand_sym
    print(pass_item)
    random.shuffle(pass_item)
    password="".join(pass_item)
    pass_entry.insert(0, password)
# def save():
#
#
#     web=web_entry.get()
#     email=email_entry.get()
#     password=pass_entry.get()
#     data_dict={web:{"email":email, "password":password}}
#     if len(web)==0 or len(email)==0:
#         messagebox.showinfo(title="Password generator", message="please dont leave any field impty")
#     else:
#         is_ok = messagebox.askokcancel(title="Password genrator",
#                                        message=f"Do you wanna save this/n Website:{web}\n email:{email}\n password:{password}")
#         if is_ok:
#             try:
#                 with open("data.json", "r")as new_file:
#                     data = json.load(new_file)
#
#             except:
#                 with open("data.json", "w") as file:
#                     json.dump(data_dict, file, indent=4)
#             else:
#                 data.update(data_dict)
#             web_entry.delete(0, END)
#             pass_entry.delete(0, END)
#
data_dict={}
def save():
    web = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    data_dict = {web: {"email": email, "password": password}}

    if len(web) == 0 or len(email) == 0:
        messagebox.showinfo(title="Password generator", message="Please don't leave any field empty.")
    else:
        is_ok = messagebox.askokcancel(title="Password generator",
                                       message=f"Do you want to save this?\nWebsite: {web}\nEmail: {email}\nPassword: {password}")
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                data = {}

            # Update the data dictionary with the new entry
            data.update(data_dict)

            # Write the updated data back to the file
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)

            web_entry.delete(0, END)
            pass_entry.delete(0, END)

def search():
    website=web_entry.get()
    try:
        with open("data.json") as file:
            data=json.load(file)

    except (FileNotFoundError, json.decoder.JSONDecodeError):
        print("not found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"email={email} \n password= {password}")
        else:
            messagebox.showinfo(title=website, message="data not found")





windows.config(padx=20,pady=20)
canvas= Canvas(height=300, width=300)
image=PhotoImage(file="a4dzg1n9.png")
canvas.create_image(150,150,image=image)
canvas.grid(row=0, column=1)
web_label=Label(text="Website")
web_label.grid(row=1, column=0)
email_label=Label(text="Email/Username")
email_label.grid(row=2, column=0)
pass_label=Label(text="Password")
pass_label.grid(row=3, column=0)

email_entry=Entry(width=35)
email_entry.insert(0,"sidshahvez430@gmail.com")
email_entry.grid(row=2,column=1,columnspan=2)
web_entry=Entry(width=35)
web_entry.grid(row=1,column=1,columnspan=2)
web_entry.focus()
pass_entry=Entry(width=21)
pass_entry.grid(row=3,column=1)

search_b=Button(text="search", command=search)
search_b.grid(row=1,column=2)
pass_gen=Button(text="generate", command=gen_pass)
pass_gen.grid(column=2,row=3)
add=Button(text="Add", width=35, command=save)
add.grid(column=1,row=4,columnspan=2)
i=0


windows.mainloop()