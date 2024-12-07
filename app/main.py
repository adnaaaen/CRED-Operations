import customtkinter as ctk
from sidebar import SideBar
from CTkTable import CTkTable
from dependency import Base, engine
from utils import table_data

Base.metadata.create_all(bind=engine)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x600")
        self.title("App")
        self.minsize(1200, 600)
        self._set_appearance_mode("dark")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=8)

        self.sidebar = SideBar(master=self)
        self.sidebar.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.refresh_btn = ctk.CTkButton(
            self, text="Refresh", fg_color="Blue", command=self.update_table
        )

        self.refresh_btn.place(rely=0.2, relx=0.1, anchor="nw")

        self.value = table_data()
        if not self.value:
            self.table = ctk.CTkLabel(self, text="No data!", font=("Arial", 22, "bold"))
        else:
            self.table = CTkTable(
                self,
                values=self.value,
                padx=0,
                hover=True,
                header_color="#08162b",
                corner_radius=6,
                row=len(self.value) - 1,
            )
        self.table.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    def update_table(self) -> None:
        self.value = table_data()
        self.table = CTkTable(
            self,
            values=self.value,
            padx=0,
            hover=True,
            header_color="#08162b",
            corner_radius=6,
            row=len(self.value) - 1,
        )
        self.table.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")


if __name__ == "__main__":
    app = App()
    app.mainloop()
