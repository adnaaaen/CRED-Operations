import customtkinter as ctk
from .view import signin
from screen.main_window import Library

class SignIn(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        cred_frame = ctk.CTkFrame(master, width=350, height=350)
        cred_frame.place(relx=.7, rely=0.5, anchor="center")
        self.master.title("Auth")
        self.label = ctk.CTkLabel(cred_frame, text="SIGN-IN", font=("Arial", 15, "bold"))
        self.label.place(relx=0.5, rely=0.1, anchor="center")

        self.username = ctk.CTkEntry(
            cred_frame, placeholder_text="Username/email", width=250
        )
        self.username.place(relx=0.5, rely=0.3, anchor="center")

        self.password = ctk.CTkEntry(cred_frame, placeholder_text="Password", width=250)
        self.password.place(relx=0.5, rely=0.4, anchor="center")

        self.button = ctk.CTkButton(cred_frame, text="Signin", width=250, command=self.isSignIn)
        self.button.place(relx=0.5, rely=0.6, anchor="center")
        
    def isSignIn(self) -> None:
        print("its working")
        if signin(username=self.username.get(), password=self.password.get()):
            self.master.destroy()
            lib = Library()
            lib.mainloop()
