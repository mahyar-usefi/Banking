import customtkinter as ctk
import tkinter.messagebox as tkmb
from tkinter import font


OPTIONS = [
    "None",
    "اقتصاد نوین", "پارسیان", "پاسارگاد", "پست بانک ایران", "تجارت",
    "موسسه اعتباری توسعه", "توسعه صادرات", "رفاه", "سامان", "سپه",
    "سرمایه", "صادرات ایران", "صنعت و معدن", "کار آفرین", "کشاورزی",
    "مرکزی جمهوری اسلامی ایران", "مسکن", "ملت", "ملی ایران", "شهر"
]


def on_select_bank(choice):
    code = ""
    match choice:
        case "اقتصاد نوین":
            code = "055"
        case "پارسیان":
            code = "054"
        case "پاسارگاد":
            code = "057"
        case "پست بانک ایران":
            code = "021"
        case "تجارت":
            code = "018"
        case "موسسه اعتباری توسعه":
            code = "051"
        case "توسعه صادرات":
            code = "019"
        case "رفاه":
            code = "013"
        case "سامان":
            code = "056"
        case "سپه":
            code = "015"
        case "سرمایه":
            code = "058"
        case "صادرات ایران":
            code = "019"
        case "صنعت و معدن":
            code = "011"
        case "کار آفرین":
            code = "053"
        case "کشاورزی":
            code = "016"
        case "مرکزی جمهوری اسلامی ایران":
            code = "010"
        case "مسکن":
            code = "014"
        case "ملت":
            code = "012"
        case "ملی ایران":
            code = "017"
        case "شهر":
            code = "061"
    bank_code_label.configure(text=code)


def calc_sheba_number():
    bank_code = bank_code_label.cget("text")
    if not bank_code:
        tkmb.showerror(
            title="Invalid bank",
            message="لطفا نام بانک را انتخاب نمایید"
        )
    else:
        acc_number = acc_number_entry.get()
        bban = bank_code + acc_number.zfill(19)
        control_number = str(98 - (int(bban + "182700") % 97))
        if len(control_number) == 1:
            control_number = "0" + control_number
        sheba_number = "IR" + control_number + bban
        sheba_number_label.grid()
        sheba_number_label.configure(text=sheba_number)


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.resizable(False, False)
root.geometry("400x400")
root.eval("tk::PlaceWindow . center")
root.title("Convert Acc number to IBAN")

custom_font = ctk.CTkFont(family="Times New Roman Baltic", size=18)
persian_font = ctk.CTkFont(family="B Nazanin", size=18)

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=30, fill='both', expand=True)


option_menu_label = ctk.CTkLabel(master=frame, text="Bank: ", font=custom_font)
option_menu_label.grid(row=0, column=0, padx=50, pady=20)

option_menu_bank = ctk.CTkOptionMenu(master=frame, values=OPTIONS, command=on_select_bank, font=custom_font)
option_menu_bank.grid(row=0, column=1, padx=5, pady=20)


acc_number_label = ctk.CTkLabel(master=frame, text="Account Number: ", font=custom_font)
acc_number_label.grid(row=1, column=0, padx=10, pady=12)

acc_number_entry = ctk.CTkEntry(master=frame)
acc_number_entry.grid(row=1, column=1, padx=30, pady=12)

bank_code_label = ctk.CTkLabel(master=frame, text="")
bank_code_label.grid(row=2, column=0, columnspan=2, pady=10)


calculate_sheba_number = ctk.CTkButton(master=frame, text="محاسبه شماره شبا", command=calc_sheba_number, font=persian_font)
calculate_sheba_number.grid(row=2, column=0, columnspan=2, pady=50)


sheba_number_label = ctk.CTkLabel(master=frame, text="", font=custom_font)
sheba_number_label.grid(row=3, column=0, columnspan=2, pady=5)
sheba_number_label.grid_remove()

print(font.families())
root.mainloop()
