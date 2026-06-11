import tkinter as tk


def c_to_f(celsius_value: float) -> float:
    return (celsius_value * 9 / 5) + 32


def f_to_c(fahrenheit_value: float) -> float:
    return (fahrenheit_value - 32) * 5 / 9


def main():
    root = tk.Tk()
    root.title("Temperature Converter (Tkinter)")
    root.geometry("380x220")

    c_var = tk.StringVar()
    f_var = tk.StringVar()
    result_var = tk.StringVar(value="Enter a value and choose conversion.")

    def convert_c_to_f():
        try:
            celsius = float(c_var.get())
        except ValueError:
            result_var.set("Please enter a valid Celsius value.")
            return

        fahrenheit = c_to_f(celsius)
        f_var.set(f"{fahrenheit:.2f}")
        result_var.set(f"{celsius:.2f} C = {fahrenheit:.2f} F")

    def convert_f_to_c():
        try:
            fahrenheit = float(f_var.get())
        except ValueError:
            result_var.set("Please enter a valid Fahrenheit value.")
            return

        celsius = f_to_c(fahrenheit)
        c_var.set(f"{celsius:.2f}")
        result_var.set(f"{fahrenheit:.2f} F = {celsius:.2f} C")

    def clear_fields():
        c_var.set("")
        f_var.set("")
        result_var.set("Enter a value and choose conversion.")

    tk.Label(root, text="Celsius").grid(row=0, column=0, padx=10, pady=(16, 6), sticky="w")
    tk.Entry(root, textvariable=c_var, width=18).grid(row=0, column=1, padx=10, pady=(16, 6), sticky="ew")

    tk.Label(root, text="Fahrenheit").grid(row=1, column=0, padx=10, pady=6, sticky="w")
    tk.Entry(root, textvariable=f_var, width=18).grid(row=1, column=1, padx=10, pady=6, sticky="ew")

    tk.Button(root, text="C -> F", command=convert_c_to_f).grid(row=2, column=0, padx=10, pady=8, sticky="ew")
    tk.Button(root, text="F -> C", command=convert_f_to_c).grid(row=2, column=1, padx=10, pady=8, sticky="ew")
    tk.Button(root, text="Clear", command=clear_fields).grid(row=3, column=0, columnspan=2, padx=10, pady=4, sticky="ew")

    tk.Label(root, textvariable=result_var, fg="navy").grid(row=4, column=0, columnspan=2, padx=10, pady=(10, 12), sticky="w")

    root.grid_columnconfigure(1, weight=1)
    root.mainloop()


if __name__ == "__main__":
    main()
