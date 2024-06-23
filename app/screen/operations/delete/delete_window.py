import customtkinter as ctk
from .view import deleteBook

class DeleteBook(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.minsize(400, 300)
        self.title("DELETE")
        self.label = ctk.CTkLabel(
            self, text="Delete a book!", font=("Arial", 19, "bold")
        )
        self.label.pack(padx=20, pady=20)

        self.book_id = ctk.CTkEntry(self, placeholder_text="Book id...(integer)", width=250)
        self.book_id.place(relx=0.5, rely=0.3, anchor="center")

        self.button = ctk.CTkButton(
            self,
            text="Delete Book",
            width=250,
            fg_color="red",
            hover_color="#400b08",
            command=lambda: deleteBook(self.book_id.get()),
        )
        self.button.place(relx=0.5, rely=0.8, anchor="center")
