import customtkinter as ctk


def main():
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    # Create the main window
    root = ctk.CTk()
    root.title("Hello CustomTkinter")
    root.geometry("300x200")

    # Add a label
    label = ctk.CTkLabel(root, text="Hello, World!", font=("Arial", 24))
    label.pack(expand=True)

    # Add a button that updates the label text
    button = ctk.CTkButton(
        root,
        text="Click Me!",
        command=lambda: label.configure(text="You clicked the button!"),
    )
    button.pack(pady=10)

    # Start the event loop
    root.mainloop()


if __name__ == "__main__":
    main()
