import customtkinter as ctk
from .view import addNewBook

class AddNewBook(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("600x500")
        self.minsize(600, 500)
        self.title("CREATE")
        self.label = ctk.CTkLabel(
            self, text="Add a new Book!", font=("Arial", 19, "bold")
        )
        self.label.pack(padx=20, pady=20)

        self.book_name = ctk.CTkEntry(
            self, placeholder_text="Book name...", width=250
        )
        self.book_name.place(relx=0.5, rely=0.3, anchor="center")

        self.author_name = ctk.CTkEntry(self, placeholder_text="Author name...", width=250)
        self.author_name.place(relx=0.5, rely=0.4, anchor="center")

        self.department = ctk.CTkEntry(self, placeholder_text="Department...", width=250)
        self.department.place(relx=0.5, rely=0.5, anchor="center")

        self.book_price = ctk.CTkEntry(self, placeholder_text="Price...", width=250)
        self.book_price.place(relx=0.5, rely=0.6, anchor="center")

        self.button = ctk.CTkButton(
            self,
            text="Add Book",
            width=250,
            fg_color="green",
            font=("Arial", 15, "bold"),
            hover_color="#094d14",
            command=lambda: addNewBook(
                self.book_name.get(), self.author_name.get(), self.department.get(), self.book_price.get()
            ),
        )
        self.button.place(relx=0.5, rely=0.8, anchor="center")
