import tkinter as tk


def main():
    # Create the main window
    root = tk.Tk()
    root.title("Hello Tkinter")
    root.geometry("300x200")

    # Add a label
    label = tk.Label(root, text="Hello, World!", font=("Arial", 18))
    label.pack(expand=True)

    # Add a button that closes the window
    button = tk.Button(root, text="Click Me!", command=lambda: label.config(text="You clicked the button!"))
    button.pack(pady=10)

    # Start the event loop
    root.mainloop()


if __name__ == "__main__":
    main()
