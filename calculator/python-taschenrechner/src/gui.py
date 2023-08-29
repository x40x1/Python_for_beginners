import tkinter as tk
from calculator import Calculator

class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Taschenrechner")

        self.calculator = Calculator()

        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.result_label = tk.Label(self.master, textvariable=self.result_var, font=("Arial", 20))
        self.result_label.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        self.create_button("1", 1, 0)
        self.create_button("2", 1, 1)
        self.create_button("3", 1, 2)
        self.create_button("+", 1, 3)

        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("-", 2, 3)

        self.create_button("7", 3, 0)
        self.create_button("8", 3, 1)
        self.create_button("9", 3, 2)
        self.create_button("*", 3, 3)

        self.create_button("C", 4, 0)
        self.create_button("0", 4, 1)
        self.create_button("=", 4, 2)
        self.create_button("/", 4, 3)

    def create_button(self, text, row, column):
        button = tk.Button(self.master, text=text, font=("Arial", 20), width=5, height=2, command=lambda: self.button_click(text))
        button.grid(row=row, column=column, padx=5, pady=5)

    def button_click(self, text):
        if text == "C":
            self.calculator.clear()
            self.result_var.set("0")
        elif text == "=":
            result = self.calculator.calculate()
            self.result_var.set(result)
        else:
            self.calculator.add_input(text)
            self.result_var.set(self.calculator.get_input())

if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()