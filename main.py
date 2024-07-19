import customtkinter as ctk
import tkinter.messagebox as tkmb

from PIL import Image


OPTIONS = [
    "None",
    "اقتصاد نوین", "پارسیان", "پاسارگاد", "پست بانک ایران", "تجارت",
    "موسسه اعتباری توسعه", "توسعه صادرات", "رفاه", "سامان", "سپه",
    "سرمایه", "صادرات ایران", "صنعت و معدن", "کار آفرین", "کشاورزی",
    "مرکزی جمهوری اسلامی ایران", "مسکن", "ملت", "ملی ایران", "شهر"
]

BANK_CODES = {
    "اقتصاد نوین": "055",
    "پارسیان": "054",
    "پاسارگاد": "057",
    "پست بانک ایران": "021",
    "تجارت": "018",
    "موسسه اعتباری توسعه": "051",
    "توسعه صادرات": "019",
    "رفاه": "013",
    "سامان": "056",
    "سپه": "015",
    "سرمایه": "058",
    "صادرات ایران": "019",
    "صنعت و معدن": "011",
    "کار آفرین": "053",
    "کشاورزی": "016",
    "مرکزی جمهوری اسلامی ایران": "010",
    "مسکن": "014",
    "ملت": "012",
    "ملی ایران": "017",
    "شهر": "061"
}


def on_select_bank(choice):
    code = BANK_CODES.get(choice, None)
    bank_code_label.configure(text=code)


def calc_sheba_number():
    bank_code = bank_code_label.cget("text")
    if not bank_code:
        tkmb.showerror(
            title="Invalid bank",
            message="لطفا نام بانک را انتخاب نمایید"
        )
    elif not acc_number_entry.get():
        acc_number_entry.focus_set()
    elif not acc_number_entry.get().isdigit():
        tkmb.showerror(
            title="Invalid Acc number",
            message="فیلد شماره حساب فقط شامل عدد می باشد"
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
        copy_to_clipboard_btn.grid()


def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(sheba_number_label.cget("text"))
    root.update()


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.resizable(False, False)
root.geometry("600x400+550+250")
root.title("Convert Acc number to IBAN")

eng_font = ctk.CTkFont(family="Times New Roman Baltic", size=18)
persian_font = ctk.CTkFont(family="B Nazanin", size=18)

frame = ctk.CTkFrame(master=root)
frame.pack(fill='both', expand=True)

option_menu_label = ctk.CTkLabel(master=frame, text="Bank: ", font=eng_font)
option_menu_label.grid(sticky="w", row=0, column=0, padx=15, pady=20)

option_menu_bank = ctk.CTkOptionMenu(
    master=frame, values=OPTIONS,
    command=on_select_bank, font=eng_font,
    dropdown_font=persian_font, anchor="c"
)
option_menu_bank.configure(width=200, height=30)
option_menu_bank.grid(sticky="w", row=0, column=1)

acc_number_label = ctk.CTkLabel(master=frame, text="Account Number: ", font=eng_font)
acc_number_label.grid(sticky="w", row=1, column=0, padx=15)

acc_number_entry = ctk.CTkEntry(master=frame)
acc_number_entry.configure(width=200)
acc_number_entry.grid(sticky="w", row=1, column=1)

bank_code_label = ctk.CTkLabel(master=frame, text="")
bank_code_label.grid_remove()

calculate_sheba_number_btn = ctk.CTkButton(master=frame, text="محاسبه شماره شبا", command=calc_sheba_number, font=persian_font)
calculate_sheba_number_btn.grid(sticky="e", row=1, column=2, padx=5)

icon_image = ctk.CTkImage(dark_image=Image.open("icons/copy.png"), size=(20, 20))

copy_to_clipboard_btn = ctk.CTkButton(
    master=frame, image=icon_image,
    text="", command=copy_to_clipboard,
    font=persian_font, width=10
)
copy_to_clipboard_btn.grid(row=5, column=2)
copy_to_clipboard_btn.grid_remove()

sheba_number_label = ctk.CTkLabel(master=frame, text="", font=eng_font)
sheba_number_label.configure(height=230)
sheba_number_label.grid(row=5, column=1)
sheba_number_label.grid_remove()

root.mainloop()
