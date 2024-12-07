import customtkinter as ctk
from .create import AddBook
from .delete import DeleteBook
from .update import UpdateBook
from .search import SearchBook


class SideBar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.add_button = ctk.CTkButton(
            self,
            text="Add book",
            font=("Arial", 15, "bold"),
            width=170,
            fg_color="green",
            hover_color="#094d14",
            command=self.create_window,
        )
        self.add_button.place(rely=0.04, relx=0.1, anchor="nw")

        self.update_button = ctk.CTkButton(
            self,
            text="Update book",
            width=170,
            font=("Arial", 15, "bold"),
            fg_color="green",
            hover_color="#094d14",
            command=self.update_book,
        )
        self.update_button.place(rely=0.12, relx=0.1, anchor="nw")

        self.search_button = ctk.CTkButton(
            self,
            text="Search book",
            font=("Arial", 15, "bold"),
            width=170,
            fg_color="green",
            hover_color="#094d14",
            command=self.search_book,
        )
        self.search_button.place(rely=0.2, relx=0.1, anchor="nw")

        self.delete_button = ctk.CTkButton(
            self,
            text="Delete book",
            font=("Arial", 15, "bold"),
            width=170,
            fg_color="red",
            hover_color="#400b08",
            command=self.delete_book,
        )
        self.delete_button.place(rely=0.28, relx=0.1, anchor="nw")

        self.toplevel_window = None

    def create_window(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = AddBook(self)
        else:
            self.toplevel_window.focus()

    def delete_book(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = DeleteBook(self)
        else:
            self.toplevel_window.focus()

    def update_book(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = UpdateBook(self)
        else:
            self.toplevel_window.focus()

    def search_book(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = SearchBook(self)
        else:
            self.toplevel_window.focus()
