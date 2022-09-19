from tkinter import *
from tkinter.ttk import Combobox
from target_group_list import target_group_list

window = Tk()

window.title("Point of Exponential Cost Increase Calculator")
window.geometry('600x300')
window.configure(background="black")
window.grid_columnconfigure(0, weight=1)
window.rowconfigure(1, weight=1)

# Adding a headline
headline = Label(window, text="Point of Exponential Cost Increase Calculator", font=("Helvetica", 20), bg="black",
                 fg="white")
headline.grid(column=0, row=0)

# Add a multiple Choice Box that allows the user to select the Target Group
target_group = Combobox(window)
target_group['values'] = target_group_list
target_group.current(0)  # set the selected item
target_group.grid(column=0, row=1, sticky="n", padx=5, pady=10)

# Add a multiple Choice Box that allows the user to select the Buying Target Group
buying_target_group = Combobox(window)
buying_target_group['values'] = target_group_list
buying_target_group.current(0)  # set the selected item
buying_target_group.grid(column=0, row=2, sticky="n", padx=5, pady=10)

# Add a multiple Choice Box that allows the user to select the Country
country = Combobox(window)
country['values'] = ("Germany", "Austria", "Switzerland")
country.grid(column=0, row=3, sticky="n", padx=5, pady=10)

markets = ["G-CH", "F-CH"]


# Build a dependent list of Markets based on the selected Country
def build_market_list():
    country.get()
    if country.get() == "Switzerland":
        country_market.config(values=markets)
    else:
        country_market.config(values=country.get())


country_market = Combobox(window)
country_market.grid(column=0, row=4, sticky="n", padx=5, pady=10)
country.bind("<<ComboboxSelected>>", build_market_list)

# Add a Button in the center of the window
btn = Button(window, text="Calculate", bg="black", fg="black")
btn.grid(column=0, row=5, sticky="ns", padx=5, pady=10)


# Save all User Input in a dictionary
def clicked():
    user_input = {
        "target_group": target_group.get(),
        "buying_target_group": buying_target_group.get(),
        "country": country.get(),
        "market": country_market.get()
    }
    print(user_input)


btn.configure(command=clicked)

window.mainloop()
