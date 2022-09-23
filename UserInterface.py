import tkinter as tk
from tkinter import ttk
from target_group_list import target_group_list

# Build a User Interface with Tkinter

# Create a Class for the User Interface
def calculate_average_cpp(self):
    # cpp = Cost per GRP
    # Strip input of any whitespace and into list
    cpp_list = self.cost_per_grp.get().split(" ")
    # check if List elements are all numbers and convert to float
    if all([x.isdigit() for x in cpp_list]):
        cpp_list = [float(x) for x in cpp_list]
        # calculate average CPP
        average_cpp = sum(cpp_list) / len(cpp_list)
        self.cost_per_grp = round(average_cpp, 2)

class UserInterface:
    def __init__(self, window):
        self.window = window
        self.window.title("Diminishing Reach Return Calculator")
        self.window.geometry('450x350')
        self.window.configure(background="black")
        self.window.grid_columnconfigure(0, weight=3)
        self.window.rowconfigure(1, weight=1)

        # Adding a headline
        headline = tk.Label(self.window, text="Diminishing Reach Return Calculator", font=("Helvetica", 20), bg="black",
                            fg="white")
        headline.grid(column=0, row=0, columnspan=2, sticky="nsew")

        # Add a multiple Choice Box that allows the user to select the Target Group
        self.target_group = tk.Label(self.window, text="Target Group:", font=("Helvetica", 12), bg="black", fg="white")
        self.target_group.grid(column=0, row=1, sticky="n", padx=5, pady=10)
        self.target_group = tk.ttk.Combobox(self.window)
        self.target_group['values'] = target_group_list
        self.target_group.current(0)  # set the selected item
        self.target_group.grid(column=1, row=1, sticky="n", padx=5, pady=10)

        # Add a multiple Choice Box that allows the user to select the Buying Target Group
        self.buying_target_group = tk.Label(self.window, text="Buying Target Group:", font=("Helvetica", 12), bg="black",
                                            fg="white")
        self.buying_target_group.grid(column=0, row=2, sticky="n", padx=5, pady=10)
        self.buying_target_group = tk.ttk.Combobox(self.window)
        self.buying_target_group['values'] = target_group_list
        self.buying_target_group.current(0)  # set the selected item
        self.buying_target_group.grid(column=1, row=2, sticky="n", padx=5, pady=10)

        # Add a Text Field Input for the CPP
        self.cost_per_grp = tk.Label(self.window, text="Cost per GRP:", font=("Helvetica", 12), bg="black", fg="white")
        self.cost_per_grp.grid(column=0, row=3, sticky="n", padx=5, pady=10)
        self.cost_per_grp = tk.Entry(self.window)
        self.cost_per_grp.grid(column=1, row=3, sticky="n", padx=5, pady=10)


        # Add a multiple Choice Box that allows the user to select the Country
        self.country = tk.Label(self.window, text="Country:", font=("Helvetica", 12), bg="black", fg="white")
        self.country.grid(column=0, row=4, sticky="n", padx=5, pady=10)
        self.country = tk.ttk.Combobox(self.window)
        self.country['values'] = ("Germany", "Austria", "Switzerland")
        self.country.grid(column=1, row=4, sticky="n", padx=5, pady=10)

        self.markets = ["G-CH", "F-CH"]

        # Build a dependent list of Markets based on the selected Country
        self.country.bind("<<ComboboxSelected>>", self.update_market_list)

        # Add a multiple Choice Box that allows the user to select the Market
        self.country_market = tk.Label(self.window, text="Market:", font=("Helvetica", 12), bg="black", fg="white")
        self.country_market.grid(column=0, row=5, sticky="n", padx=5, pady=10)
        self.country_market = tk.ttk.Combobox(self.window)
        self.country_market['values'] = self.markets
        self.country_market.grid(column=1, row=5, sticky="n", padx=5, pady=10)

        # Add a Button that allows the user to start the calculation
        self.button = tk.Button
        self.button = tk.Button(self.window, text="Calculate", command=self.get_user_input)
        self.button.grid(column=0, row=6, columnspan=2, sticky="ns", padx=5, pady=10)

    def update_market_list(self, e):
        if self.country.get() == "Germany":
            self.markets = ["Germany"]
        elif self.country.get() == "Austria":
            self.markets = ["Austria"]
        elif self.country.get() == "Switzerland":
            self.markets = ["G-CH", "F-CH"]
        self.country_market['values'] = self.markets


    def get_user_input(self):
        # Create User_Input Dictionary
        calculate_average_cpp(self)
        user_input = {
            "target_group": self.target_group.get(),
            "buying_target_group": self.buying_target_group.get(),
            "country": self.country.get(),
            "market": self.country_market.get(),
            "cpp": self.cost_per_grp
        }
        # Check whether User_Input Fields are filled
        if user_input["target_group"] == "" or user_input["buying_target_group"] == "" \
                or user_input["country"] == "" or user_input["market"] == "":
            print("Please fill out all fields")
            # TODO: Add a text that informs the user to fill out all fields
        else:
            # add user_input as a class attribute
            self.user_input = user_input
            print(user_input)
            self.window.destroy()
