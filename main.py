import customtkinter
import pickle
from PIL import Image

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("1920x1080")
root.title("Shopping list")

main_frame = customtkinter.CTkScrollableFrame(master=root)
main_frame.pack(pady=20, padx=60, fill="both", expand=True)

shopping_list = []
delete_item_image = customtkinter.CTkImage(light_image=Image.open("trash.png"),
                                           dark_image=Image.open("trash.png"),
                                           size=(70, 70))


def save_data_from_top_level_window_to_list(name_entry, approximate_cost_entry, amount_entry):
    shopping_list.append(
        item_to_buy(name_entry.get(), float(approximate_cost_entry.get()), amount_entry.get(), False))


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
                                                   command=lambda: close_add_new_item_top_level_window(window,
                                                                                                       name_entry,
                                                                                                       approximate_cost_entry,
                                                                                                       amount_entry))
    save_new_item_button.pack(pady=12, padx=20, fill="both")


add_new_item_button = customtkinter.CTkButton(master=main_frame, fg_color="#700B97", text="Add new item",
                                              font=("GajrajOne", 50), command=open_add_new_item_top_level_window)
add_new_item_button.pack(pady=12, padx=20, fill="both")


def delete_item(item_to_delete, item_to_delete_frame):
    item_to_delete_frame.destroy()
    shopping_list.remove(item_to_delete)


class item_to_buy:
    def __init__(self, name_of_item: str, approximate_cost: float, amount: str, already_bought: bool):
        self.name_of_item = name_of_item
        self.approximate_cost = approximate_cost
        self.amount = amount
        self.already_bought = already_bought

        self.product_frame = customtkinter.CTkFrame(master=main_frame, fg_color="#3E065F")
        self.product_frame.pack(pady=12, padx=20, fill="both")

        # Adding all the necessary interface:
        self.already_bought_check_box = customtkinter.CTkCheckBox(master=self.product_frame, text="", hover=True,
                                                                  command=self.buy_item)
        self.already_bought_check_box.grid(row=0, column=0, padx=(30, 0), pady=12)

        self.name_of_item_label = customtkinter.CTkLabel(master=self.product_frame,
                                                         text=self.name_of_item + " — " + str(
                                                             self.approximate_cost) + " $ — " + str(
                                                             self.amount), font=("GajrajOne", 50))

        self.name_of_item_label.grid(row=0, column=1, pady=12)

        self.delete_item_button = customtkinter.CTkButton(master=self.product_frame, image=delete_item_image, text="", fg_color="transparent", hover_color="#8E05C2",
                                                          command=lambda: delete_item(self, self.product_frame))
        self.delete_item_button.grid(row=0, column=5, pady=12, padx=15, sticky="e", columnspan=1)

        # checking if this item has already been bought
        if self.already_bought:
            self.product_frame.configure(fg_color="green")
            self.already_bought_check_box.select()

    def buy_item(self):
        if not self.already_bought:
            self.already_bought_check_box.select()
            self.already_bought = True
            self.product_frame.configure(fg_color="green")
        else:
            self.already_bought_check_box.deselect()
            self.already_bought = False
            self.product_frame.configure(fg_color="#3E065F")


class item_to_buy_to_store:
    def __init__(self, name_of_item: str, approximate_cost: float, amount: str, already_bought: bool):
        self.name_of_item = name_of_item
        self.approximate_cost = approximate_cost
        self.amount = amount
        self.already_bought = already_bought


def get_data_from_file():
    try:
        data_file_read = open("data.txt", 'rb')
    except FileNotFoundError:
        print('Problems opening the file')
        return

    temporary_receiving_data_list = pickle.load(data_file_read)
    data_file_read.close()
    for j in temporary_receiving_data_list:
        shopping_list.append(item_to_buy(j.name_of_item, j.approximate_cost, j.amount, j.already_bought))


get_data_from_file()

root.mainloop()

temporary_sending_data_list = []
for i in shopping_list:
    temporary_sending_data_list.append(
        item_to_buy_to_store(i.name_of_item, i.approximate_cost, i.amount, i.already_bought))
try:
    data_file_write = open("data.txt", 'wb')
    pickle.dump(temporary_sending_data_list, data_file_write)
    data_file_write.close()
except FileNotFoundError:
    print('Problems opening the file')
