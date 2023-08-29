import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # create display
        self.display = tk.Entry(master, width=30, justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # create buttons
        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("/", 1, 3)

        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("*", 2, 3)

        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("-", 3, 3)

        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)
        self.create_button("C", 4, 2)
        self.create_button("+", 4, 3)

        self.create_button("=", 5, 0, columnspan=4)

        # initialize variables
        self.num1 = None
        self.num2 = None
        self.operator = None
        self.result = None

    def create_button(self, text, row, column, columnspan=1):
        button = tk.Button(self.master, text=text, width=5, height=2, command=lambda: self.button_click(text))
        button.grid(row=row, column=column, columnspan=columnspan, padx=5, pady=5)

    def button_click(self, text):
        if text.isdigit() or text == ".":
            if self.operator is None:
                if self.num1 is None:
                    self.num1 = text
                else:
                    self.num1 += text
                self.display.delete(0, tk.END)
                self.display.insert(0, self.num1)
            else:
                if self.num2 is None:
                    self.num2 = text
                else:
                    self.num2 += text
                self.display.delete(0, tk.END)
                self.display.insert(0, self.num2)
        elif text == "C":
            self.num1 = None
            self.num2 = None
            self.operator = None
            self.result = None
            self.display.delete(0, tk.END)
        elif text in ["+", "-", "*", "/"]:
            self.operator = text
        elif text == "=":
            if self.num1 is not None and self.num2 is not None and self.operator is not None:
                num1 = float(self.num1)
                num2 = float(self.num2)
                if self.operator == "+":
                    self.result = num1 + num2
                elif self.operator == "-":
                    self.result = num1 - num2
                elif self.operator == "*":
                    self.result = num1 * num2
                elif self.operator == "/":
                    self.result = num1 / num2
                self.display.delete(0, tk.END)
                self.display.insert(0, self.result)
                self.num1 = str(self.result)
                self.num2 = None
                self.operator = None

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
