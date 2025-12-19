import tkinter as tk
from tkinter import messagebox
from parser import *
from P.Polynomial import Polynomial
from TRANS.TRANS_Q_P import TRANS_Q_P


class CalculatorSelector:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Выбор калькулятора")

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        window_width = int(screen_width * 0.3)
        window_height = int(screen_height * 0.5)

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.window.minsize(int(screen_width * 0.25), int(screen_height * 0.4))
        self.window.resizable(True, True)

        self.create_widgets()

    def run(self):
        """Запускает приложение"""
        self.window.mainloop()

    def create_widgets(self):
        title_label = tk.Label(self.window, text="Выберите тип калькулятора",
                               font=('Arial', 16, 'bold'))
        title_label.pack(pady=20)

        # Кнопки для выбора типа калькулятора
        button_style = {'font': ('Arial', 14), 'height': 2, 'width': 20}

        natural_btn = tk.Button(self.window, text="Натуральные числа",
                                command=self.open_natural_calculator, **button_style)
        natural_btn.pack(pady=5)

        integer_btn = tk.Button(self.window, text="Целые числа",
                                command=self.open_integer_calculator, **button_style)
        integer_btn.pack(pady=5)

        rational_btn = tk.Button(self.window, text="Рациональные числа",
                                 command=self.open_rational_calculator, **button_style)
        rational_btn.pack(pady=5)

        polynomial_btn = tk.Button(self.window, text="Полиномы",
                                   command=self.open_polynomial_calculator, **button_style)
        polynomial_btn.pack(pady=5)

        # НОВАЯ КНОПКА ДЛЯ СОК
        rns_btn = tk.Button(self.window, text="Система СОК",
                            command=self.open_rns_calculator, **button_style)
        rns_btn.pack(pady=5)

    def open_natural_calculator(self):
        geometry = self.window.geometry()
        self.window.destroy()
        calculator = Calculator("natural")
        calculator.window.geometry(geometry)
        calculator.run()

    def open_integer_calculator(self):
        geometry = self.window.geometry()
        self.window.destroy()
        calculator = Calculator("integer")
        calculator.window.geometry(geometry)
        calculator.run()

    def open_rational_calculator(self):
        geometry = self.window.geometry()
        self.window.destroy()
        calculator = Calculator("rational")
        calculator.window.geometry(geometry)
        calculator.run()

    def open_polynomial_calculator(self):
        geometry = self.window.geometry()
        self.window.destroy()
        calculator = Calculator("polynomial")
        calculator.window.geometry(geometry)
        calculator.run()

    def open_rns_calculator(self):
        """Открывает калькулятор СОК"""
        geometry = self.window.geometry()
        self.window.destroy()
        calculator = Calculator("rns")
        calculator.window.geometry(geometry)
        calculator.run()


class Calculator:
    def __init__(self, calc_type):
        self.calc_type = calc_type
        self.window = tk.Tk()

        # Для СОК делаем окно больше
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        if calc_type == "rns":
            window_width = int(screen_width * 0.35)
            window_height = int(screen_height * 0.5)
        else:
            window_width = int(screen_width * 0.22)
            window_height = int(screen_height * 0.51)

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        if calc_type == "rns":
            self.window.minsize(500, 400)
        else:
            self.window.minsize(window_width, window_height)

        self.window.resizable(True, True)

        titles = {
            "natural": "Калькулятор натуральных чисел",
            "integer": "Калькулятор целых чисел",
            "rational": "Калькулятор рациональных чисел",
            "polynomial": "Калькулятор полиномов",
            "rns": "Калькулятор СОК (20-разрядные модули)"
        }
        self.window.title(titles.get(calc_type, "Калькулятор"))

        self.expression = ""

        # Для СОК дополнительная информация о вычислениях
        self.rns_details = ""

        self.create_widgets()

    def create_widgets(self):
        # Для СОК создаем другой интерфейс
        if self.calc_type == "rns":
            self.create_rns_widgets()
        else:
            self.create_standard_widgets()

    def create_standard_widgets(self):
        """Создание стандартного интерфейса (для натуральных, целых, рациональных, полиномов)"""
        main_frame = tk.Frame(self.window)
        main_frame.pack(expand=True, fill='both', padx=10, pady=10)

        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.columnconfigure(2, weight=1)
        main_frame.columnconfigure(3, weight=1)
        main_frame.columnconfigure(4, weight=1)

        type_label = tk.Label(main_frame,
                              text=f"Тип: {self.get_calc_type_name()}",
                              font=('Arial', 10, 'bold'),
                              fg='blue')
        type_label.grid(row=0, column=0, columnspan=5, pady=(10, 5), sticky='ew')

        self.display = tk.Entry(main_frame, font=('Arial', 16), justify='right')
        self.display.grid(row=1, column=0, columnspan=5, padx=5, pady=5, sticky='ew')

        info_label = tk.Label(main_frame, text="Введите выражение", font=('Arial', 10))
        info_label.grid(row=2, column=0, columnspan=5, pady=(0, 10))

        button_frame = tk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=5, sticky='nsew', pady=10)

        main_frame.rowconfigure(3, weight=1)

        for i in range(5):
            button_frame.columnconfigure(i, weight=1)
        for i in range(5):
            button_frame.rowconfigure(i, weight=1)

        buttons = [
            '7', '8', '9', '/', 'x²',
            '4', '5', '6', '*', 'x³',
            '1', '2', '3', '-', 'xⁿ',
            '0', 'x', '=', '+', 'C',
            '(', ')', '%', '//', '<—'
        ]

        row = 0
        col = 0

        for button in buttons:
            if button == '=':
                cmd = self.show_result
            elif button == 'C':
                cmd = self.clear
            elif button == '<—':
                cmd = self.backspace
            elif button in ['x²', 'x³', 'xⁿ']:
                cmd = lambda x=button: self.add_power(x)
            else:
                cmd = lambda x=button: self.add_to_expression(x)

            btn = tk.Button(
                button_frame,
                text=button,
                font=('Arial', 12),
                command=cmd
            )

            btn.grid(row=row, column=col, padx=2, pady=2, sticky='nsew')

            col += 1
            if col > 4:
                col = 0
                row += 1

        bottom_frame = tk.Frame(main_frame)
        bottom_frame.grid(row=4, column=0, columnspan=5, sticky='ew', pady=10)

        bottom_frame.columnconfigure(0, weight=1)
        bottom_frame.columnconfigure(1, weight=1)

        back_btn = tk.Button(
            bottom_frame,
            text="Назад к выбору",
            font=('Arial', 12),
            command=self.back_to_selector,
            height=2,
            bg='lightgreen'
        )
        back_btn.grid(row=0, column=0, sticky='ew', padx=(0, 5))

        calc_btn = tk.Button(
            bottom_frame,
            text="Вычислить",
            font=('Arial', 12),
            command=self.show_result,
            height=2,
            bg='lightblue'
        )
        calc_btn.grid(row=0, column=1, sticky='ew', padx=(5, 0))

        self.update_display()

    def create_rns_widgets(self):
        """Создание интерфейса для калькулятора СОК (20-разрядные модули)"""
        main_frame = tk.Frame(self.window)
        main_frame.pack(expand=True, fill='both', padx=10, pady=10)

        # Информация о системе СОК
        info_frame = tk.LabelFrame(main_frame, text="СОК с 4 модулями (20 разрядов)",
                                   font=('Arial', 10, 'bold'))
        info_frame.pack(fill='x', pady=(0, 10))

        info_text = """Используется 4 взаимно простых 20-разрядных модуля:
• m1 = 10000000000000000001
• m2 = 10000000000000000003
• m3 = 10000000000000000007
• m4 = 10000000000000000009

Диапазон: примерно ±10^80
Операции: +, -, *, // (целочисленное деление)"""

        info_label = tk.Label(info_frame, text=info_text, font=('Courier', 8),
                              justify='left', anchor='w')
        info_label.pack(padx=10, pady=5, fill='x')

        # Поле ввода выражения
        input_frame = tk.LabelFrame(main_frame, text="Ввод выражения",
                                    font=('Arial', 10, 'bold'))
        input_frame.pack(fill='x', pady=(0, 10))

        self.display = tk.Entry(input_frame, font=('Arial', 14), justify='right')
        self.display.pack(fill='x', padx=10, pady=5)

        # Кнопки для СОК
        buttons_frame = tk.Frame(input_frame)
        buttons_frame.pack(padx=10, pady=10)

        buttons = [
            '7', '8', '9', '//', 'C',
            '4', '5', '6', '*', '⌫',
            '1', '2', '3', '-', '(',
            '0', '=', '+', ')', ''
        ]

        row = 0
        col = 0

        for button in buttons:
            if button == '=':
                cmd = self.show_result
            elif button == 'C':
                cmd = self.clear
            elif button == '⌫':
                cmd = self.backspace
            elif button == '':
                continue  # Пропускаем пустую кнопку
            else:
                cmd = lambda x=button: self.add_to_expression(x)

            btn = tk.Button(
                buttons_frame,
                text=button,
                font=('Arial', 12),
                width=6,
                height=2,
                command=cmd
            )

            btn.grid(row=row, column=col, padx=2, pady=2)

            col += 1
            if col > 4:
                col = 0
                row += 1

        # Кнопки управления
        bottom_frame = tk.Frame(main_frame)
        bottom_frame.pack(fill='x', pady=(0, 10))

        bottom_frame.columnconfigure(0, weight=1)
        bottom_frame.columnconfigure(1, weight=1)

        back_btn = tk.Button(
            bottom_frame,
            text="Назад к выбору",
            font=('Arial', 12),
            command=self.back_to_selector,
            height=2,
            bg='lightgreen'
        )
        back_btn.grid(row=0, column=0, sticky='ew', padx=(0, 5))

        calc_btn = tk.Button(
            bottom_frame,
            text="Вычислить в СОК",
            font=('Arial', 12, 'bold'),
            command=self.show_result,
            height=2,
            bg='lightblue'
        )
        calc_btn.grid(row=0, column=1, sticky='ew', padx=(5, 0))

        self.update_display()

    def get_calc_type_name(self):
        """Возвращает читаемое название типа калькулятора"""
        names = {
            "natural": "Натуральные числа",
            "integer": "Целые числа",
            "rational": "Рациональные числа",
            "polynomial": "Полиномы",
            "rns": "Система Остаточных Классов (20-разрядные модули)"
        }
        return names.get(self.calc_type, "Неизвестный тип")

    def add_to_expression(self, value):
        """Добавляет символ к выражению"""
        if self.calc_type in ["natural", "integer"] and len(value) == 1 and value[0] == '/':
            messagebox.showwarning("Ошибка", "В данном калькуляторе нельзя использовать операцию деления")
            return
        elif self.calc_type in ["rational", "polynomial"] and value[:2] == '//':
            messagebox.showwarning("Ошибка",
                                   "В данном калькуляторе нельзя использовать операцию целочисленного деления")
            return
        elif self.calc_type in ["rational"] and value[0] == '%':
            messagebox.showwarning("Ошибка", "В данном калькуляторе нельзя использовать операцию остатка от деления")
            return
        elif self.calc_type == "rns" and value == '/':
            messagebox.showwarning("Ошибка", "В СОК используется только целочисленное деление (//)")
            return

        self.expression += str(value)
        self.update_display()

    def add_power(self, power_type):
        """Добавляет степень переменной"""
        if self.calc_type in ["natural", "integer", "rational"]:
            messagebox.showwarning("Ошибка", "В данном калькуляторе нельзя использовать переменную 'x'")
            return
        if self.calc_type == "rns":
            messagebox.showwarning("Ошибка", "В калькуляторе СОК нельзя использовать переменную 'x'")
            return
        if power_type == 'x²':
            self.expression += 'x^2'
        elif power_type == 'x³':
            self.expression += 'x^3'
        elif power_type == 'xⁿ':
            self.expression += 'x^'
        self.update_display()

    def clear(self):
        """Очищает выражение"""
        self.expression = ""
        self.update_display()

    def backspace(self):
        """Очищает последний символ выражения"""
        self.expression = self.expression[:-1]
        self.update_display()

    def show_result(self):
        """Получаем результат"""
        if self.expression:
            try:
                # Вычисляем результат в зависимости от типа калькулятора
                result = self.process_expression(self.expression)

                # Выводим результат
                self.clear()
                self.expression = str(result)
                self.update_display()

            except Exception as e:
                messagebox.showerror("Ошибка", f"Ошибка вычисления: {e}")
        else:
            messagebox.showwarning("Предупреждение", "Введите выражение")

    def update_display(self):
        """Обновляет отображение выражения"""
        if self.calc_type != "rns":
            self.display.config(state='normal')
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)
            self.display.config(state='readonly')
        else:
            self.display.config(state='normal')
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)
            self.display.config(state='normal')

    def process_expression(self, expr):
        """Обрабатывает выражение в зависимости от типа калькулятора"""
        if self.calc_type == "natural":
            ans = eval_rpn_n(to_rpn(expr))
            return f"{ans.show()}"
        elif self.calc_type == "integer":
            ans = eval_rpn_z(to_rpn(expr))
            return f"{ans.show()}"
        elif self.calc_type == "rational":
            ans = eval_rpn_q(to_rpn(expr))
            return f"{ans.show()}"
        elif self.calc_type == "polynomial":
            ans = eval_rpn_p(to_rpn(expr))
            if type(ans) != Polynomial:
                ans = TRANS_Q_P(ans)
            return f"{ans.show()}"
        elif self.calc_type == "rns":
            # Для СОК получаем результат и детали
            ans_int, details = eval_rpn_rns(to_rpn(expr))
            return f"{ans_int.show()}"

        return 'answer'

    def back_to_selector(self):
        """Возврат к окну выбора калькулятора"""
        geometry = self.window.geometry()
        self.window.destroy()
        selector = CalculatorSelector()
        selector.window.geometry(geometry)
        selector.run()

    def run(self):
        """Запускает приложение"""
        self.window.mainloop()


# Запуск приложения начинается с выбора калькулятора
if __name__ == "__main__":
    selector = CalculatorSelector().run()