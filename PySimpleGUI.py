import tkinter as tk
from tkinter import ttk

#fungsi convert yang menerima convert dari widget
def convert():
    value = input_value.get()
    input_base = input_base_value.get()
    output_base = output_base_value.get()

# fungsi convert yang melakukan konversi bilangan berdasarkan basis input
    if not input_base or not output_base:
        return
    if input_base == 'Desimal':
        decimal_value = int(value)
    elif input_base == 'Biner':
        decimal_value = int(value, 2)
    elif input_base == 'Oktal':
        decimal_value = int(value, 8)
    elif input_base == 'Hexadesimal':
        decimal_value = int(value, 16)

# fungsi convert yang berfungsi untuk menghasilkan nilai konversi yang diinginkan, berdasarkan basis output
    if output_base == 'Desimal':
        output_value = str(decimal_value)
    elif output_base == 'Biner':
        output_value = bin(decimal_value)[2:]
    elif output_base == 'Oktal':
        output_value = oct(decimal_value)[2:]
    elif output_base == 'Hexadesimal':
        output_value = hex(decimal_value)[2:]

    output_label.config(text=output_value)

#fungsi convert_ascii yang berfungsi untuk mengkonversi string yang dimasukkan oleh pengguna melalui widget input_ascii
def convert_ascii():
    value = input_ascii.get()
    output_value = ''
    for char in value:
        output_value += str(ord(char)) + ' '
#for yang digunakan untuk mengiterasi setiap karakter (char) dalam variabel value. Setiap karakter tersebut diubah 
# menjadi kode Unicode-nya menggunakan fungsi ord() yang mengembalikan nilai bilangan bulat yang mewakili kode Unicode dari karakter tersebut
    output_ascii_label.config(text=output_value)

#Styling Frame
window = tk.Tk()
window.title("Konversi Bilangan dan ASCII")
window.geometry("320x270")
window.configure(bg="#90e0ef")

# Konversi bilangan
input_value_label = tk.Label(text="Masukkan Nilai:", bg="#90e0ef")
input_value_label.pack()

input_value = ttk.Entry(width=40)
input_value.pack()

input_base_label = tk.Label(text="Dari:", bg="#90e0ef")
input_base_label.pack()

input_base_value = tk.StringVar(window)
input_base_value.set("-")
input_base = ttk.Combobox(window, textvariable=input_base_value, values=["Desimal", "Biner", "Oktal", "Hexadesimal"])
input_base.pack()

output_base_label = tk.Label(text="Ke:", bg="#90e0ef")
output_base_label.pack()

output_base_value = tk.StringVar(window)
output_base_value.set("-")
output_base = ttk.Combobox(window, textvariable=output_base_value, values=["Desimal", "Biner", "Oktal", "Hexadesimal"])
output_base.pack()

convert_button = tk.Button(text="Convert", command=convert, bg="#00b4d8")
convert_button.pack()

output_label = ttk.Label(text="", background="#90e0ef")
output_label.pack()

# Konversi ASCII
input_ascii_label = tk.Label(text="Masukkan String:", bg="#90e0ef")
input_ascii_label.pack()

input_ascii = ttk.Entry(width=40)
input_ascii.pack()

convert_ascii_button = tk.Button(text="Convert", command=convert_ascii, bg="#00b4d8")
convert_ascii_button.pack()

output_ascii_label = ttk.Label(text="", background="#90e0ef")
output_ascii_label.pack()

window.mainloop()
