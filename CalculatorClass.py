import tkinter as tk

# Create the root window
root = tk.Tk()
root.title("Calculator")

# Create an Entry widget to display the input and output
display = tk.Entry(root, font=("Arial", 18), borderwidth=2, relief="ridge", justify='right')
display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Create a list to hold the expression (used to evaluate operations)
expression = []


# Define a function to handle button clicks
def on_button_click(value):
    if value == "=":
        try:
            result = eval("".join(expression))
            display.delete(0, tk.END)
            display.insert(0, str(result))
            expression.clear()
            expression.append(str(result))
        except Exception:
            display.delete(0, tk.END)
            display.insert(0, "Error")
            expression.clear()
    elif value == "C":
        display.delete(0, tk.END)
        expression.clear()
    else:
        expression.append(value)
        display.insert(tk.END, value)


# Create the calculator buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "C", "+",
]


# Add buttons to the GUI grid
row = 1
col = 0
for button in buttons:
    action = lambda x=button: on_button_click(x)
    b = tk.Button(root, text=button, font=("Arial", 18), width=5, height=2)
    b.grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Add the equals button
equals_button = tk.Button(root, text="=", command=lambda: on_button_click("="), font=("Arial", 18), width=5, height=2)
equals_button.grid(row=5, column=3, padx=5, pady=5)

# Run the Tkinter main event loop
root.mainloop()