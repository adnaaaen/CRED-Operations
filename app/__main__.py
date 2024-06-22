import customtkinter as ctk
from auth.SIGNIN.signin import SignIn
from auth.SIGNUP.signup import SignUp
class Auth(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("900x400")
        self.title("Auth")
        self.signup_frame = SignUp(master=self)
        self.signin_frame = SignIn(master=self)

if __name__ == "__main__":
    auth = Auth()
    auth.mainloop()
