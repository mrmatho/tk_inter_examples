import customtkinter as ctk


def c_to_f(celsius_value: float) -> float:
    return (celsius_value * 9 / 5) + 32


def f_to_c(fahrenheit_value: float) -> float:
    return (fahrenheit_value - 32) * 5 / 9


def main():
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("Temperature Converter (CustomTkinter)")
    root.geometry("420x250")

    c_var = ctk.StringVar()
    f_var = ctk.StringVar()
    result_var = ctk.StringVar(value="Enter a value and choose conversion.")

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

    container = ctk.CTkFrame(root)
    container.pack(fill="both", expand=True, padx=16, pady=16)

    ctk.CTkLabel(container, text="Celsius").grid(row=0, column=0, padx=10, pady=(12, 8), sticky="w")
    ctk.CTkEntry(container, textvariable=c_var, width=180).grid(row=0, column=1, padx=10, pady=(12, 8), sticky="ew")

    ctk.CTkLabel(container, text="Fahrenheit").grid(row=1, column=0, padx=10, pady=8, sticky="w")
    ctk.CTkEntry(container, textvariable=f_var, width=180).grid(row=1, column=1, padx=10, pady=8, sticky="ew")

    ctk.CTkButton(container, text="C -> F", command=convert_c_to_f).grid(row=2, column=0, padx=10, pady=8, sticky="ew")
    ctk.CTkButton(container, text="F -> C", command=convert_f_to_c).grid(row=2, column=1, padx=10, pady=8, sticky="ew")
    ctk.CTkButton(container, text="Clear", command=clear_fields).grid(row=3, column=0, columnspan=2, padx=10, pady=4, sticky="ew")

    ctk.CTkLabel(container, textvariable=result_var).grid(row=4, column=0, columnspan=2, padx=10, pady=(10, 12), sticky="w")

    container.grid_columnconfigure(1, weight=1)
    root.mainloop()


if __name__ == "__main__":
    main()
