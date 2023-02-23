import customtkinter

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("1920x1080")
root.title("Shopping list")

main_frame = customtkinter.CTkFrame(master=root)
main_frame.pack(pady=20, padx=60, fill="both", expand=True)


def save_data_from_top_level_window_to_list(name_entry, approximate_cost_entry, amount_entry):
    shopping_list.append(itemToBuy(name_entry.get(), float(approximate_cost_entry.get()), amount_entry.get()))


def close_add_new_item_top_level_window(window, name_entry, approximate_cost_entry, amount_entry):
    save_data_from_top_level_window_to_list(name_entry, approximate_cost_entry, amount_entry)
    window.destroy()


def open_add_new_item_top_level_window():
    window = customtkinter.CTkToplevel()
    window.geometry("400x600")
    window.title("Add a new item")
    window.resizable(False, False)

    # Adding all the necessary interface:
    name_entry = customtkinter.CTkEntry(master=window, placeholder_text="Product name", fg_color="#3E065F",
                                        font=("GajrajOne", 20), height=50)
    name_entry.pack(pady=12, padx=20, fill="both")

    approximate_cost_entry = customtkinter.CTkEntry(master=window, placeholder_text="Product approximate cost",
                                                    fg_color="#3E065F",
                                                    font=("GajrajOne", 20), height=50)
    approximate_cost_entry.pack(pady=12, padx=20, fill="both")

    amount_entry = customtkinter.CTkEntry(master=window, placeholder_text="Product amount", fg_color="#3E065F",
                                          font=("GajrajOne", 20), height=50)
    amount_entry.pack(pady=12, padx=20, fill="both")

    save_new_item_button = customtkinter.CTkButton(master=window, fg_color="#700B97", text="Add new item",
                                                   font=("GajrajOne", 30),
                                                   command=lambda: close_add_new_item_top_level_window(window, name_entry,
                                                                                                       approximate_cost_entry, amount_entry))
    save_new_item_button.pack(pady=12, padx=20, fill="both")


add_new_item_button = customtkinter.CTkButton(master=main_frame, fg_color="#700B97", text="Add new item",
                                              font=("GajrajOne", 50), command=open_add_new_item_top_level_window)
add_new_item_button.pack(pady=12, padx=20, fill="both")


class itemToBuy:
    def __init__(self, name_of_item: str, approximate_cost: float, amount: str):
        self.__name_of_item = name_of_item
        self.__approximate_cost = approximate_cost
        self.__amount = amount
        self.already_bought = False

        self.product_frame = customtkinter.CTkFrame(master=main_frame, fg_color="#3E065F")
        self.product_frame.pack(pady=12, padx=20, fill="both")

        # Adding all the necessary interface:
        self.already_bought_check_box = customtkinter.CTkCheckBox(master=self.product_frame, text="", hover=True,
                                                                  command=self.buy)
        self.already_bought_check_box.grid(row=0, column=0, padx=(30, 0), pady=12)

        self.name_of_item_label = customtkinter.CTkLabel(master=self.product_frame,
                                                         text=self.__name_of_item + " — " + str(
                                                             self.__approximate_cost) + " $ — " + str(
                                                             self.__amount), font=("GajrajOne", 50))

        self.name_of_item_label.grid(row=0, column=1, pady=12)

    def buy(self):
        if not self.already_bought:
            self.already_bought_check_box.select()
            self.already_bought = True
            self.product_frame.configure(fg_color="green")
        else:
            self.already_bought_check_box.deselect()
            self.already_bought = False
            self.product_frame.configure(fg_color="#3E065F")


shopping_list = [itemToBuy("Milk", 4.43, "1 bottle"), itemToBuy('Bread', 2.5, '1 loaf'), itemToBuy('Cheese', 4.0, '8 oz')]


root.mainloop()
