import customtkinter as ctk
from .view import signin

class SignIn(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        cred_frame = ctk.CTkFrame(master, width=350, height=350)
        cred_frame.place(relx=.7, rely=0.5, anchor="center")

        label = ctk.CTkLabel(cred_frame, text="SIGN-IN", font=("Arial", 15, "bold"))
        label.place(relx=0.5, rely=0.1, anchor="center")

        username = ctk.CTkEntry(
            cred_frame, placeholder_text="Username/email", width=250
        )
        username.place(relx=0.5, rely=0.3, anchor="center")

        password = ctk.CTkEntry(cred_frame, placeholder_text="Password", width=250)
        password.place(relx=0.5, rely=0.4, anchor="center")

        button = ctk.CTkButton(cred_frame, text="Signin", width=250, command=lambda: signin(username.get(), password.get()))
        button.place(relx=0.5, rely=0.6, anchor="center")
