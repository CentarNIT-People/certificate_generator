import tkinter
import customtkinter
from main import excecute

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("1000x600")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="NIT Certficate Generator", text_font=("Roboto", 24))
label.pack(pady=12, padx=10)

entry = customtkinter.CTkTextbox(master=frame,  text_font=("Roboto", 14), width=300, height=200)
entry.pack(pady=12, padx=100)

entry_1 = customtkinter.CTkEntry(master=frame, placeholder_text="Course Name: ", width=300, height=50)
entry_1.pack(pady=10, padx=10)

entry_2 = customtkinter.CTkEntry(master=frame, placeholder_text="Group Name: ", width=300, height=50)
entry_2.pack(pady=10, padx=10)

entry_3 = customtkinter.CTkEntry(master=frame, placeholder_text="Group ID: ", width=300, height=50)
entry_3.pack(pady=10, padx=10)

def login():
    data = entry.textbox.get("1.0", "end-1c")
    firstnames = [data.split()[x] for x in range(len(data.split())) if x % 2 == 0]
    lastnames = [data.split()[x] for x in range(len(data.split())) if x % 2 != 0]
    full_names = [firstnames[x] + " " + lastnames[x] for x in range(len(firstnames))]
    print(excecute(full_names, entry_1.entry.get(), entry_2.entry.get(), entry_3.entry.get()))
    quit()

button = customtkinter.CTkButton(master=root, text="Generate Certificates", command=login)
button.place(relx=0.5, rely=0.92, anchor=tkinter.CENTER)

root.mainloop()
