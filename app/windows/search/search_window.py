import customtkinter as ctk

class SearchBook(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.minsize(400, 300)
        self.title("SEARCH")
        self.label = ctk.CTkLabel(
            self, text="Search a book!", font=("Arial", 19, "bold")
        )
        self.label.pack(padx=20, pady=20)

        self.book_id = ctk.CTkEntry(self, placeholder_text="Book id...(integer)", width=250)
        self.book_id.place(relx=0.5, rely=0.3, anchor="center")

        self.button = ctk.CTkButton(
            self,
            text="search",
            width=250,
            fg_color="green",
            font=("Arial", 15, "bold"),
            hover_color="#094d14",
        )
        self.button.place(relx=0.5, rely=0.8, anchor="center")

