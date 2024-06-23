import customtkinter as ctk
from .operations.create.create_window import AddNewBookWindow
from .operations.delete.delete_window import DeleteBook

class SideBar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.add_button = ctk.CTkButton(
            self,
            text="Add book",
            font=("Arial", 15, "bold"),
            fg_color="green",
            hover_color="#094d14",
            command=self.create_window
        )
        self.add_button.place(rely=0.1, relx=0.2, anchor="nw")

        self.delete_button = ctk.CTkButton(
            self,
            text="Delete a book",
            font=("Arial", 15, "bold"),
            fg_color="red",
            hover_color="#400b08",
            command=self.delete_book
        )
        self.delete_button.place(rely=0.2, relx=0.2, anchor="nw")
        
        self.toplevel_window = None

    def create_window(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = AddNewBookWindow(self) 
        else:
            self.toplevel_window.focus() 
       
    def delete_book(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = DeleteBook(self) 
        else:
            self.toplevel_window.focus()  
