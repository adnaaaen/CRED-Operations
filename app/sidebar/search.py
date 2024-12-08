import customtkinter as ctk
from service import book_service


class SearchBook(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.minsize(400, 300)
        self.title("SEARCH")

        self.book_id = ctk.CTkEntry(self, placeholder_text="Book Name", width=250)
        # self.radio_var = ctk.IntVar(value=2)
        # self.radio_one = ctk.CTkRadioButton(
        #     self, value=1, text="Search by Name", variable=self.radio_var
        # )
        # self.radio_two = ctk.CTkRadioButton(
        #     self, value=2, text="Search by Book", variable=self.radio_var
        # )
        # self.label = ctk.CTkLabel(
        #     self,
        #     text=f"Search a {'Name' if self.radio_var.get() == 1 else 'Department'}!",
        #     font=("Arial", 19, "bold"),
        # )
        # self.label.pack(padx=20, pady=20)

        # self.radio_one.place(relx=0.6, rely=0.5, anchor="center")
        # self.radio_two.place(relx=0.8, rely=0.7, anchor="center")
        # self.book_id.place(relx=0.5, rely=0.3, anchor="center")

        # TODO: fix the search window with radio buttons

        self.button = ctk.CTkButton(
            self,
            text="search",
            width=250,
            fg_color="green",
            font=("Arial", 15, "bold"),
            hover_color="#094d14",
            # command=book_service.search_with_key,
        )
        self.button.place(relx=0.5, rely=0.8, anchor="center")
