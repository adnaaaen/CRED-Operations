import customtkinter as ctk
from SIGNIN.signin import SignIn
from SIGNUP.signup import SignUp

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("900x400")
        self.title("Auth")
        self.signin_frame = SignIn(master=self)
        self.signup_frame = SignUp(master=self)


if __name__ == "__main__":
    app = App()
    app.mainloop()
