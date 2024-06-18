import customtkinter as ctk
from .view import signup

class SignUp(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        cred_frame1 = ctk.CTkFrame(master, width=350, height=350)
        cred_frame1.place(relx=0.3, rely=0.5, anchor="center")

        label = ctk.CTkLabel(cred_frame1, text="SIGN-UP", font=("Arial", 15, "bold"))
        label.place(relx=0.5, rely=0.1, anchor="center")

        username = ctk.CTkEntry(
            cred_frame1, placeholder_text="choose an username", width=250
        )
        username.place(relx=0.5, rely=0.3, anchor="center")

        password = ctk.CTkEntry(cred_frame1, placeholder_text="Password", width=250)
        password.place(relx=0.5, rely=0.4, anchor="center")

        email = ctk.CTkEntry(
            cred_frame1, placeholder_text="Email", width=250
        )
        email.place(relx=0.5, rely=0.5, anchor="center")

        phone_no = ctk.CTkEntry(cred_frame1, placeholder_text="Phone Number", width=250)
        phone_no.place(relx=0.5, rely=0.6, anchor="center")

        button = ctk.CTkButton(
            cred_frame1,
            text="Signup",
            width=250,
            fg_color="green",
            hover_color="#094d14",
            command= lambda: signup(username.get(), password.get(), email.get(), phone_no.get())
        )
        button.place(relx=0.5, rely=0.8, anchor="center")
