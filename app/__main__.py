import customtkinter as ctk
from windows.sidebar_frame import SideBar
from view import getAllData
from CTkTable import CTkTable

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
        self.value = getAllData()
        if not getAllData():
            self.table = ctk.CTkLabel(self, text="No data!", font=("Arial", 22, "bold"))
        else:
            self.table = CTkTable(
                self,
                values=self.value,
                padx=0,
                hover=True,
                header_color="#08162b",
                corner_radius=6,
            )
        self.table.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")


if __name__ == "__main__":
    app = App()
    app.mainloop()
