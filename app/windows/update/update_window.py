import customtkinter as ctk
# from .view import updateBook``

class UpdateBook(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("600x500")
        self.minsize(600, 500)
        self.title("UPDATE")
        self.label = ctk.CTkLabel(
            self, text="Update a Book!", font=("Arial", 19, "bold")
        )
        self.label.pack(padx=20, pady=20)
        self.book_id = ctk.CTkEntry(self, placeholder_text="Book id...", width=250)
        self.book_id.place(relx=0.5, rely=0.2, anchor="center")
        
        self.book_name = ctk.CTkEntry(
            self, placeholder_text="New book name...", width=250
        )
        self.book_name.place(relx=0.5, rely=0.32, anchor="center")

        self.author_name = ctk.CTkEntry(self, placeholder_text="New author name...", width=250)
        self.author_name.place(relx=0.5, rely=0.42, anchor="center")

        self.department = ctk.CTkEntry(self, placeholder_text="New department...", width=250)
        self.department.place(relx=0.5, rely=0.52, anchor="center")

        self.book_price = ctk.CTkEntry(self, placeholder_text="New price...", width=250)
        self.book_price.place(relx=0.5, rely=0.62, anchor="center")

        self.button = ctk.CTkButton(
            self,
            text="Update book",
            width=250,
            fg_color="green",
            font=("Arial", 15, "bold"),
            hover_color="#094d14",
        )
        self.button.place(relx=0.5, rely=0.8, anchor="center")
