import customtkinter as ctk


def main():
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("green")

    # Create the main window
    root = ctk.CTk()
    root.title("Score Tracker (CustomTkinter)")
    root.geometry("460x320")

    # Dictionary to hold the current score for each category
    scores = {
        "Focus": 0,
        "Collaboration": 0,
        "Creativity": 0,
    }

    # IntVars to link score values to the displayed labels
    score_vars = {name: ctk.IntVar(value=0) for name in scores}
    total_var = ctk.IntVar(value=0)

    # Sync the score variables and total with the current scores dict
    def update_view():
        for name, value in scores.items():
            score_vars[name].set(value)
        total_var.set(sum(scores.values()))

    # Increment the score for a category
    def add_point(category: str):
        scores[category] += 1
        update_view()

    # Decrement the score for a category, minimum 0
    def subtract_point(category: str):
        if scores[category] > 0:
            scores[category] -= 1
            update_view()

    # Reset all scores to zero
    def reset_all():
        for key in scores:
            scores[key] = 0
        update_view()

    frame = ctk.CTkFrame(root)
    frame.pack(fill="both", expand=True, padx=16, pady=16)

    # Add the title label
    ctk.CTkLabel(frame, text="Class Score Tracker", font=("Arial", 20, "bold")).grid(
        row=0, column=0, columnspan=4, pady=(12, 10)
    )

    # Add a row of controls for each score category
    row = 1
    for category in scores:
        ctk.CTkLabel(frame, text=category, anchor="w", width=130).grid(row=row, column=0, padx=10, pady=8, sticky="w")
        ctk.CTkLabel(frame, textvariable=score_vars[category], width=55).grid(row=row, column=1, padx=4, pady=8)
        ctk.CTkButton(frame, text="+", width=44, command=lambda c=category: add_point(c)).grid(row=row, column=2, padx=4, pady=8)
        ctk.CTkButton(frame, text="-", width=44, command=lambda c=category: subtract_point(c)).grid(row=row, column=3, padx=4, pady=8)
        row += 1

    # Add the total score display
    ctk.CTkLabel(frame, text="Total", font=("Arial", 14, "bold"), anchor="w", width=130).grid(
        row=row, column=0, padx=10, pady=(14, 8), sticky="w"
    )
    ctk.CTkLabel(frame, textvariable=total_var, font=("Arial", 14, "bold"), width=55).grid(
        row=row, column=1, padx=4, pady=(14, 8)
    )

    # Add the reset button
    ctk.CTkButton(frame, text="Reset", command=reset_all).grid(
        row=row + 1, column=0, columnspan=4, padx=10, pady=(8, 14), sticky="ew"
    )

    frame.grid_columnconfigure(0, weight=1)
    update_view()
    # Start the event loop
    root.mainloop()


if __name__ == "__main__":
    main()
