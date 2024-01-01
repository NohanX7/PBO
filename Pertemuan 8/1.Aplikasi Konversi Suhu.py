import tkinter as tk
from tkinter import ttk

def convert_temperature():
    try:
        input_temperature = float(entry_temperature.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()

        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                result = (input_temperature * 9/5) + 32
            elif to_unit == "Reamur":
                result = input_temperature * 4/5
            elif to_unit == "Kelvin":
                result = input_temperature + 273.15
            else:
                result = input_temperature

        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                result = (input_temperature - 32) * 5/9
            elif to_unit == "Reamur":
                result = (input_temperature - 32) * 4/9
            elif to_unit == "Kelvin":
                result = (input_temperature - 32) * 5/9 + 273.15
            else:
                result = input_temperature

        elif from_unit == "Reamur":
            if to_unit == "Celsius":
                result = input_temperature * 5/4
            elif to_unit == "Fahrenheit":
                result = input_temperature * 9/4 + 32
            elif to_unit == "Kelvin":
                result = input_temperature * 5/4 + 273.15
            else:
                result = input_temperature

        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                result = input_temperature - 273.15
            elif to_unit == "Fahrenheit":
                result = (input_temperature - 273.15) * 9/5 + 32
            elif to_unit == "Reamur":
                result = (input_temperature - 273.15) * 4/5
            else:
                result = input_temperature

        else:
            result = input_temperature

        label_result.config(text=f"Result: {result:.2f} {to_unit}")

    except ValueError:
        label_result.config(text="Invalid input. Please enter a valid number.")

# Membuat GUI
app = tk.Tk()
app.title("Temperature Converter TIF22D/Nova Subhan/220511170")

# Label dan Entry untuk input suhu
label_temperature = ttk.Label(app, text="Masukkan Temperature :")
label_temperature.grid(row=0, column=0, padx=10, pady=10)

entry_temperature = ttk.Entry(app)
entry_temperature.grid(row=0, column=1, padx=10, pady=10)

# Combo box untuk unit suhu dari dan ke
label_from = ttk.Label(app, text="Dari :")
label_from.grid(row=1, column=0, padx=10, pady=10)

combo_from = ttk.Combobox(app, values=["Celsius", "Fahrenheit", "Reamur", "Kelvin"])
combo_from.grid(row=1, column=1, padx=10, pady=10)
combo_from.set("Celsius")

label_to = ttk.Label(app, text="Ke :")
label_to.grid(row=2, column=0, padx=10, pady=10)

combo_to = ttk.Combobox(app, values=["Celsius", "Fahrenheit", "Reamur", "Kelvin"])
combo_to.grid(row=2, column=1, padx=10, pady=10)
combo_to.set("Celsius")

# Tombol konversi
btn_convert = ttk.Button(app, text="Konversi", command=convert_temperature)
btn_convert.grid(row=3, column=0, columnspan=2, pady=10)

# Label untuk menampilkan hasil konversi
label_result = ttk.Label(app, text="Hasil :")
label_result.grid(row=4, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi
app.mainloop()
