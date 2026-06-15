# Домашнее задание
# Необходимо разработать программу на Python с использованием tkinter, которая позволяет пользователю генерировать безопасные пароли с учетом заданных параметров. В качестве параметров пользователь может выбрать, 
# из каких символов должен состоять пароль: цифры, строчные/заглавные буквы, спецсимволы.
# Входные данные:
# - параметры генерации, выбранные пользователем
# Вычислить и вывести:
# - пароль, соответствующий выбранным параметрам
# - если параметры не выбраны, то вывести сообщение об ошибке
# Доп.задача:
# - вывести список всех ранее сгенерированных паролей

from tkinter import *
from tkinter import messagebox
from random import *

root = Tk()
root.geometry("800x600")
root.title("Генератор паролей")

res = Label(root, text=f"Сгенерированый пароль: ")
res.place(x = 280, y = 450)

def password_copy():
    password = res["text"]
    root.clipboard_clear()
    root.clipboard_append(password)

def generate_password():
    print(var_long.get())
    if var_long.get() == 0:
        messagebox.showinfo("Ошибка","Выбери длину проля!")
        return
    
    if var_choice_alpha.get() == 0 and var_digit.get() == 0 and var_symbol.get() == 0:
          messagebox.showerror("Ошибка", "Выбери хотя бы один параметр!")
          return


    if var_long.get() == 1:
        length = 6
    elif var_long.get() == 2:
        length = 8
    else:
        length = 12


    symbol = ""
    if var_choice_alpha.get() == 1:
        symbol += "qwertyuiopasdfghjklzxcvbnm".upper()
    if var_choice_alpha.get() == 2:
        symbol += "abcdefghijklmnopqrstuvwxyz"
    if var_symbol.get() == 1:
        symbol += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if var_digit.get() == 1:
        symbol += "0123456789" 

    print(symbol)

    password = ""

    for i in range(length):
        password += choice(symbol) 

    res.config(text= f"Сгенерированый пароль: {password}")
       
    earlier_res.insert(0, password)


earlier_res = Listbox(root,width=35, height=17)
earlier_res.place(x = 550 , y = 300)


Label(root, text="Выбери из чего должен состоять пароль", font="bold").place(x = 243 , y = 75)

Label(root, text="Длина пароля", font="bold").place(x = 100 , y = 140)

Label(root, text="Строчные / Заглавные буквы", font = "bold").place(x = 550,  y = 140)


Label(root, text = "Спецсимволы должны быть?", font = "bold").place(x  = 280 , y = 140)




Label(root, text="Должны ли быть цифры?", font="bold").place(x = 280 , y = 300)


Button(root,text="Сгенерировать пароль", fg = "white", bg = "green", command=generate_password).place(x = 280, y = 420)


#Длинра пароля

var_long = IntVar()


Radiobutton(root, text= "6", font="bold", variable = var_long, value= 1).place(x = 100 , y = 180)

Radiobutton(root, text="8", font="bold", variable=var_long, value= 2).place(x = 100 , y = 220)

Radiobutton(root, text="12", font = "bold" , variable= var_long, value= 3).place(x = 100 , y = 260)


#стр\загл букв


var_symbol = IntVar()

Radiobutton(root, text= "Да", font = "roman",variable=var_symbol, value= 1).place(x = 280 , y = 180)
Radiobutton(root, text= "Нет", font = "roman",variable=var_symbol, value= 2).place(x = 280 , y = 220)



#Спецсимв


var_choice_alpha = IntVar()

Radiobutton(root, text= "Заглавные", font = "bold",variable=var_choice_alpha,value= 1).place(x = 550 , y = 180)
Radiobutton(root, text= "Строчные", font = "bold",variable=var_choice_alpha,value= 2).place(x = 550 , y = 220)

#цифры

var_digit = IntVar()

Radiobutton(root, text= "Да", font = "roman",variable=var_digit,value= 1).place(x = 280 , y = 340)
Radiobutton(root, text= "Нет", font = "roman",variable=var_digit,value= 2).place(x = 280 , y = 380)


btn_copy = Button(root, text="Копировать пароль",command=password_copy, bg = "red", fg= "white")
btn_copy.place(x = 160, y = 420)



root.mainloop()