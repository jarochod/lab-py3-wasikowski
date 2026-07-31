import tkinter as tk

window = tk.Tk()
window.title("Calculator")


class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        # Create a frame for the display
        self.display_frame = tk.Frame(self.master)
        self.display_frame.pack()

        # Create an entry widget for the display
        self.display_var = tk.StringVar()
        self.expression_str = ""

        # self.display_var.set(self.expression_str)
        self.display = tk.Entry(self.display_frame, textvariable=self.display_var, font=('Arial', 14), width=28, borderwidth=5)
        self.display.pack()

        # Create a frame for the buttons
        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack()


        # Create buttons dynamically
        self.buttons = [
            ["7", "8", "9", "+"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "*"],
            ["0", ",", "Clear", "/"],
            ["C", "(", ")", "="]
        ]

        self.create_buttons()

# Function to create buttons based on the defined layout
    def create_buttons(self):
        for row, row_items in enumerate(self.buttons):
            for col, char in enumerate(row_items):
                button = tk.Button(self.button_frame, text=char, width=10, height=2,
                                   command=lambda c=char: self.on_button_click(c))
                button.grid(row=row, column=col)

# Function to handle button clicks
    def on_button_click(self, char):
        if char == '=':
            try:
                result = str(eval(self.expression_str.replace(",", ".")))
                self.display_var.set(result)
                self.expression_str = result
            except Exception as e:
                self.display_var.set("Error")
                self.expression_str = ""
        elif char == "Clear":
            self.expression_str = ""
            self.display_var.set(self.expression_str)
        elif char == "C":
            self.expression_str = self.expression_str[:-1]
            self.display_var.set(self.expression_str)
        else:
            self.expression_str += str(char)
            self.display_var.set(self.expression_str)


# Create an instance of the Calculator class
calc = Calculator(window)

# Start the main loop
window.mainloop()