import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Score Tracker (Tkinter)")
    root.geometry("420x290")

    scores = {
        "Focus": 0,
        "Collaboration": 0,
        "Creativity": 0,
    }

    score_vars = {name: tk.IntVar(value=0) for name in scores}
    total_var = tk.IntVar(value=0)

    def update_view():
        for name, value in scores.items():
            score_vars[name].set(value)
        total_var.set(sum(scores.values()))

    def add_point(category: str):
        scores[category] += 1
        update_view()

    def subtract_point(category: str):
        if scores[category] > 0:
            scores[category] -= 1
            update_view()

    def reset_all():
        for key in scores:
            scores[key] = 0
        update_view()

    tk.Label(root, text="Class Score Tracker", font=("Arial", 16, "bold")).grid(
        row=0, column=0, columnspan=4, pady=(14, 10)
    )

    row = 1
    for category in scores:
        tk.Label(root, text=category, width=14, anchor="w").grid(row=row, column=0, padx=10, pady=8, sticky="w")
        tk.Label(root, textvariable=score_vars[category], width=6).grid(row=row, column=1, padx=4, pady=8)
        tk.Button(root, text="+", width=6, command=lambda c=category: add_point(c)).grid(row=row, column=2, padx=4, pady=8)
        tk.Button(root, text="-", width=6, command=lambda c=category: subtract_point(c)).grid(row=row, column=3, padx=4, pady=8)
        row += 1

    tk.Label(root, text="Total", font=("Arial", 12, "bold"), anchor="w").grid(row=row, column=0, padx=10, pady=(14, 8), sticky="w")
    tk.Label(root, textvariable=total_var, font=("Arial", 12, "bold"), width=6).grid(row=row, column=1, padx=4, pady=(14, 8))

    tk.Button(root, text="Reset", command=reset_all).grid(row=row + 1, column=0, columnspan=4, pady=(8, 14), ipadx=10)

    update_view()
    root.mainloop()


if __name__ == "__main__":
    main()
