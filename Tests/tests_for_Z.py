import unittest
from Z.Integer import Integer
from N.Natural import Natural
from TRANS.TRANS_N_Z import TRANS_N_Z
from TRANS.TRANS_Z_N import TRANS_Z_N

class TestIntegerOperations(unittest.TestCase):

    def setUp(self):
        # Создаем тестовые данные
        self.zero_natural = Natural(0, [0])
        self.one_natural = Natural(0, [1])
        self.five_natural = Natural(0, [5])
        self.ten_natural = Natural(1, [1, 0])
        self.hundred_natural = Natural(2, [1, 0, 0])
        
        # Целые числа
        self.zero_int = Integer(0, 0, [0])
        self.one_pos = Integer(0, 0, [1])
        self.one_neg = Integer(1, 0, [1])
        self.five_pos = Integer(0, 0, [5])
        self.five_neg = Integer(1, 0, [5])
        self.ten_pos = Integer(0, 1, [1, 0])
        self.ten_neg = Integer(1, 1, [1, 0])
        self.hundred_pos = Integer(0, 2, [1, 0, 0])
        self.hundred_neg = Integer(1, 2, [1, 0, 0])
        self.large_pos = Integer(0, 4, [1, 2, 3, 4, 5])
        self.large_neg = Integer(1, 4, [1, 2, 3, 4, 5])

    def print_test_result(self, method_name, passed=True):
        status = "ПРОЙДЕН" if passed else "ОШИБКА"
        print(f"Тест {method_name}: {status}")

    # Тесты для сложения целых (Сурин Максим)
    def test_addition(self):
        print("\n=== Тесты сложения целых (Сурин Максим) ===")
        
        try:
            # Положительное + положительное
            result = self.five_pos + self.ten_pos
            self.assertEqual(result.s, 0)
            self.assertEqual(result.A, [1, 5])
            self.print_test_result("addition_positive_plus_positive")
        except Exception as e:
            print(f"Ошибка в addition_positive_plus_positive: {e}")
            self.print_test_result("addition_positive_plus_positive", False)

        try:
            # Отрицательное + отрицательное
            result = self.five_neg + self.ten_neg
            self.assertEqual(result.s, 1)
            self.assertEqual(result.A, [1, 5])
            self.print_test_result("addition_negative_plus_negative")
        except Exception as e:
            print(f"Ошибка в addition_negative_plus_negative: {e}")
            self.print_test_result("addition_negative_plus_negative", False)

        try:
            # Положительное + отрицательное (результат положительный)
            result = self.ten_pos + self.five_neg  # 10 + (-5) = 5
            self.assertEqual(result.s, 0)
            self.assertEqual(result.A, [5])
            self.print_test_result("addition_positive_plus_negative_positive_result")
        except Exception as e:
            print(f"Ошибка в addition_positive_plus_negative_positive_result: {e}")
            self.print_test_result("addition_positive_plus_negative_positive_result", False)

        try:
            # Положительное + отрицательное (результат отрицательный)
            result = self.five_pos + self.ten_neg  # 5 + (-10) = -5
            self.assertEqual(result.s, 1)
            self.assertEqual(result.A, [5])
            self.print_test_result("addition_positive_plus_negative_negative_result")
        except Exception as e:
            print(f"Ошибка в addition_positive_plus_negative_negative_result: {e}")
            self.print_test_result("addition_positive_plus_negative_negative_result", False)

        try:
            # Отрицательное + положительное (результат положительный)
            result = self.ten_neg + self.five_pos  # -10 + 5 = -5
            self.assertEqual(result.s, 1)
            self.assertEqual(result.A, [5])
            self.print_test_result("addition_negative_plus_positive_negative_result")
        except Exception as e:
            print(f"Ошибка в addition_negative_plus_positive_negative_result: {e}")
            self.print_test_result("addition_negative_plus_positive_negative_result", False)

        try:
            # Отрицательное + положительное (результат отрицательный)
            result = self.five_neg + self.ten_pos  # -5 + 10 = 5
            self.assertEqual(result.s, 0)
            self.assertEqual(result.A, [5])
            self.print_test_result("addition_negative_plus_positive_positive_result")
        except Exception as e:
            print(f"Ошибка в addition_negative_plus_positive_positive_result: {e}")
            self.print_test_result("addition_negative_plus_positive_positive_result", False)

        try:
            # Сложение с нулем
            result = self.zero_int + self.five_pos
            self.assertEqual(result.s, 0)
            self.assertEqual(result.A, [5])
            result = self.five_pos + self.zero_int
            self.assertEqual(result.s, 0)
            self.assertEqual(result.A, [5])
            self.print_test_result("addition_with_zero")
        except Exception as e:
            print(f"Ошибка в addition_with_zero: {e}")
            self.print_test_result("addition_with_zero", False)

        try:
            # Большие числа
            result = self.hundred_pos + self.ten_neg  # 100 + (-10) = 90
            self.assertEqual(result.s, 0)
            self.assertEqual(result.A, [9, 0])
            self.print_test_result("addition_large_numbers")
        except Exception as e:
            print(f"Ошибка в addition_large_numbers: {e}")
            self.print_test_result("addition_large_numbers", False)

    # Тесты для ABS_Z_Z (Имховик Наталья)
    def test_ABS_Z_Z(self):
        print("\n=== Тесты ABS_Z_Z (Имховик Наталья) ===")
        
        try:
            # Абсолютное значение положительного
            result = self.ten_pos.ABS_Z_Z()
            self.assertEqual(result.s, 0)
            self.assertEqual(result.A, [1, 0])
            self.print_test_result("ABS_Z_Z_positive")
        except Exception as e:
            print(f"Ошибка в ABS_Z_Z_positive: {e}")
            self.print_test_result("ABS_Z_Z_positive", False)

        try:
            # Абсолютное значение отрицательного
            result = self.ten_neg.ABS_Z_Z()
            self.assertEqual(result.s, 0)
            self.assertEqual(result.A, [1, 0])
            self.print_test_result("ABS_Z_Z_negative")
        except Exception as e:
            print(f"Ошибка в ABS_Z_Z_negative: {e}")
            self.print_test_result("ABS_Z_Z_negative", False)

        try:
            # Абсолютное значение нуля
            result = self.zero_int.ABS_Z_Z()
            self.assertEqual(result.s, 0)
            self.assertEqual(result.A, [0])
            self.print_test_result("ABS_Z_Z_zero")
        except Exception as e:
            print(f"Ошибка в ABS_Z_Z_zero: {e}")
            self.print_test_result("ABS_Z_Z_zero", False)

    # Тесты для SGN_Z_D (Чумаков Никита)
    def test_SGN_Z_D(self):
        print("\n=== Тесты SGN_Z_D (Чумаков Никита) ===")
        
        try:
            # Знак положительного числа
            self.assertEqual(self.ten_pos.SGN_Z_D(), -1)
            self.print_test_result("SGN_Z_D_positive")
        except Exception as e:
            print(f"Ошибка в SGN_Z_D_positive: {e}")
            self.print_test_result("SGN_Z_D_positive", False)

        try:
            # Знак отрицательного числа
            self.assertEqual(self.ten_neg.SGN_Z_D(), 1)
            self.print_test_result("SGN_Z_D_negative")
        except Exception as e:
            print(f"Ошибка в SGN_Z_D_negative: {e}")
            self.print_test_result("SGN_Z_D_negative", False)

        try:
            # Знак нуля
            self.assertEqual(self.zero_int.SGN_Z_D(), 0)
            self.print_test_result("SGN_Z_D_zero")
        except Exception as e:
            print(f"Ошибка в SGN_Z_D_zero: {e}")
            self.print_test_result("SGN_Z_D_zero", False)

        try:
            # Знак числа с ведущими нулями
            num_with_zeros = Integer(1, 3, [0, 0, 0, 1])  # -1
            self.assertEqual(num_with_zeros.SGN_Z_D(), 1)
            self.print_test_result("SGN_Z_D_with_zeros")
        except Exception as e:
            print(f"Ошибка в SGN_Z_D_with_zeros: {e}")
            self.print_test_result("SGN_Z_D_with_zeros", False)

    # Тесты для MUL_ZM_Z (Захаренко Александр)
    def test_MUL_ZM_Z(self):
        print("\n=== Тесты MUL_ZM_Z (Захаренко Александр) ===")
        
        try:
            # Умножение положительного на -1
            result = self.ten_pos.MUL_ZM_Z()
            self.assertEqual(result.s, 1)
            self.assertEqual(result.A, [1, 0])
            self.print_test_result("MUL_ZM_Z_positive")
        except Exception as e:
            print(f"Ошибка в MUL_ZM_Z_positive: {e}")
            self.print_test_result("MUL_ZM_Z_positive", False)

        try:
            # Умножение отрицательного на -1
            result = self.ten_neg.MUL_ZM_Z()
            self.assertEqual(result.s, 0)
            self.assertEqual(result.A, [1, 0])
            self.print_test_result("MUL_ZM_Z_negative")
        except Exception as e:
            print(f"Ошибка в MUL_ZM_Z_negative: {e}")
            self.print_test_result("MUL_ZM_Z_negative", False)

        try:
            # Умножение нуля на -1
            result = self.zero_int.MUL_ZM_Z()
            self.assertEqual(result.s, 0)
            self.assertEqual(result.A, [0])
            self.print_test_result("MUL_ZM_Z_zero")
        except Exception as e:
            print(f"Ошибка в MUL_ZM_Z_zero: {e}")
            self.print_test_result("MUL_ZM_Z_zero", False)

    # Тесты для TRANS_N_Z (Имховик Наталья)
    def test_TRANS_N_Z(self):
        print("\n=== Тесты TRANS_N_Z (Имховик Наталья) ===")
        
        try:
            # Преобразование нуля
            result = TRANS_N_Z(self.zero_natural)
            self.assertEqual(result.s, 0)
            self.assertEqual(result.A, [0])
            self.print_test_result("TRANS_N_Z_zero")
        except Exception as e:
            print(f"Ошибка в TRANS_N_Z_zero: {e}")
            self.print_test_result("TRANS_N_Z_zero", False)

        try:
            # Преобразование положительного числа
            result = TRANS_N_Z(self.ten_natural)
            self.assertEqual(result.s, 0)
            self.assertEqual(result.A, [1, 0])
            self.print_test_result("TRANS_N_Z_positive")
        except Exception as e:
            print(f"Ошибка в TRANS_N_Z_positive: {e}")
            self.print_test_result("TRANS_N_Z_positive", False)

        try:
            # Преобразование большого числа
            large_natural = Natural(3, [9, 9, 9, 9])
            result = TRANS_N_Z(large_natural)
            self.assertEqual(result.s, 0)
            self.assertEqual(result.A, [9, 9, 9, 9])
            self.print_test_result("TRANS_N_Z_large_number")
        except Exception as e:
            print(f"Ошибка в TRANS_N_Z_large_number: {e}")
            self.print_test_result("TRANS_N_Z_large_number", False)

    # Тесты для TRANS_Z_N (Чумаков Никита)
    def test_TRANS_Z_N(self):
        print("\n=== Тесты TRANS_Z_N (Чумаков Никита) ===")
        
        try:
            # Преобразование положительного целого
            result = TRANS_Z_N(self.ten_pos)
            self.assertEqual(result.A, [1, 0])
            self.print_test_result("TRANS_Z_N_positive")
        except Exception as e:
            print(f"Ошибка в TRANS_Z_N_positive: {e}")
            self.print_test_result("TRANS_Z_N_positive", False)

        try:
            # Преобразование нуля
            result = TRANS_Z_N(self.zero_int)
            self.assertEqual(result.A, [0])
            self.print_test_result("TRANS_Z_N_zero")
        except Exception as e:
            print(f"Ошибка в TRANS_Z_N_zero: {e}")
            self.print_test_result("TRANS_Z_N_zero", False)

        try:
            # Ошибка при преобразовании отрицательного
            with self.assertRaises(ValueError):
                TRANS_Z_N(self.ten_neg)
            self.print_test_result("TRANS_Z_N_negative_error")
        except Exception as e:
            print(f"Ошибка в TRANS_Z_N_negative_error: {e}")
            self.print_test_result("TRANS_Z_N_negative_error", False)

    # Тесты для вычитания целых (Сурин Максим)
    def test_subtraction(self):
        print("\n=== Тесты вычитания целых (Сурин Максим) ===")
        
        try:
            # Положительное - положительное (результат положительный)
            result = self.ten_pos - self.five_pos
            self.assertEqual(result.s, 0)
            self.assertEqual(result.A, [5])
            self.print_test_result("subtraction_positive_minus_positive_positive_result")
        except Exception as e:
            print(f"Ошибка в subtraction_positive_minus_positive_positive_result: {e}")
            self.print_test_result("subtraction_positive_minus_positive_positive_result", False)

        try:
            # Положительное - положительное (результат отрицательный)
            result = self.five_pos - self.ten_pos
            self.assertEqual(result.s, 1)
            self.assertEqual(result.A, [5])
            self.print_test_result("subtraction_positive_minus_positive_negative_result")
        except Exception as e:
            print(f"Ошибка в subtraction_positive_minus_positive_negative_result: {e}")
            self.print_test_result("subtraction_positive_minus_positive_negative_result", False)

        try:
            # Отрицательное - отрицательное
            result = self.five_neg - self.ten_neg
            self.assertEqual(result.s, 0)
            self.assertEqual(result.A, [5])
            self.print_test_result("subtraction_negative_minus_negative")
        except Exception as e:
            print(f"Ошибка в subtraction_negative_minus_negative: {e}")
            self.print_test_result("subtraction_negative_minus_negative", False)

        try:
            # Положительное - отрицательное
            result = self.five_pos - self.ten_neg
            self.assertEqual(result.s, 0)
            self.assertEqual(result.A, [1, 5])
            self.print_test_result("subtraction_positive_minus_negative")
        except Exception as e:
            print(f"Ошибка в subtraction_positive_minus_negative: {e}")
            self.print_test_result("subtraction_positive_minus_negative", False)

        try:
            # Отрицательное - положительное
            result = self.five_neg - self.ten_pos
            self.assertEqual(result.s, 1)
            self.assertEqual(result.A, [1, 5])
            self.print_test_result("subtraction_negative_minus_positive")
        except Exception as e:
            print(f"Ошибка в subtraction_negative_minus_positive: {e}")
            self.print_test_result("subtraction_negative_minus_positive", False)

        try:
            # Вычитание нуля
            result = self.ten_pos - self.zero_int
            self.assertEqual(result.s, 0)
            self.assertEqual(result.A, [1, 0])
            self.print_test_result("subtraction_minus_zero")
        except Exception as e:
            print(f"Ошибка в subtraction_minus_zero: {e}")
            self.print_test_result("subtraction_minus_zero", False)

        try:
            # Ноль минус число
            result = self.zero_int - self.ten_pos
            self.assertEqual(result.s, 1)
            self.assertEqual(result.A, [1, 0])
            self.print_test_result("subtraction_zero_minus_number")
        except Exception as e:
            print(f"Ошибка в subtraction_zero_minus_number: {e}")
            self.print_test_result("subtraction_zero_minus_number", False)

    # Тесты для умножения целых (Соколовский Артём)
    def test_multiplication(self):
        print("\n=== Тесты умножения целых (Соколовский Артём) ===")
        
        try:
            # Положительное × положительное
            result = self.five_pos * self.ten_pos
            self.assertEqual(result.s, 0)
            self.assertEqual(result.A, [5, 0])
            self.print_test_result("multiplication_positive_times_positive")
        except Exception as e:
            print(f"Ошибка в multiplication_positive_times_positive: {e}")
            self.print_test_result("multiplication_positive_times_positive", False)

        try:
            # Положительное × отрицательное
            result = self.five_pos * self.ten_neg
            self.assertEqual(result.s, 1)
            self.assertEqual(result.A, [5, 0])
            self.print_test_result("multiplication_positive_times_negative")
        except Exception as e:
            print(f"Ошибка в multiplication_positive_times_negative: {e}")
            self.print_test_result("multiplication_positive_times_negative", False)

        try:
            # Отрицательное × положительное
            result = self.five_neg * self.ten_pos
            self.assertEqual(result.s, 1)
            self.assertEqual(result.A, [5, 0])
            self.print_test_result("multiplication_negative_times_positive")
        except Exception as e:
            print(f"Ошибка в multiplication_negative_times_positive: {e}")
            self.print_test_result("multiplication_negative_times_positive", False)

        try:
            # Отрицательное × отрицательное
            result = self.five_neg * self.ten_neg
            self.assertEqual(result.s, 0)
            self.assertEqual(result.A, [5, 0])
            self.print_test_result("multiplication_negative_times_negative")
        except Exception as e:
            print(f"Ошибка в multiplication_negative_times_negative: {e}")
            self.print_test_result("multiplication_negative_times_negative", False)

        try:
            # Умножение на ноль
            result = self.ten_pos * self.zero_int
            self.assertEqual(result.s, 0)
            self.assertEqual(result.A, [0])
            self.print_test_result("multiplication_by_zero")
        except Exception as e:
            print(f"Ошибка в multiplication_by_zero: {e}")
            self.print_test_result("multiplication_by_zero", False)

        try:
            # Ноль на число
            result = self.zero_int * self.ten_pos
            self.assertEqual(result.s, 0)
            self.assertEqual(result.A, [0])
            self.print_test_result("multiplication_zero_times_number")
        except Exception as e:
            print(f"Ошибка в multiplication_zero_times_number: {e}")
            self.print_test_result("multiplication_zero_times_number", False)

        try:
            # Большие числа
            result = self.large_pos * self.ten_pos
            self.assertEqual(result.s, 0)
            # 12345 × 10 = 123450
            self.assertEqual(result.A, [1, 2, 3, 4, 5, 0])
            self.print_test_result("multiplication_large_numbers")
        except Exception as e:
            print(f"Ошибка в multiplication_large_numbers: {e}")
            self.print_test_result("multiplication_large_numbers", False)

    # Тесты для деления (Соколовский Артём)
    def test_division(self):
        print("\n=== Тесты деления целых (Соколовский Артём) ===")
        
        try:
            # Положительное ÷ положительное
            result = self.ten_pos // self.five_pos
            self.assertEqual(result.s, 0)
            self.assertEqual(result.A, [2])
            self.print_test_result("division_positive_by_positive")
        except Exception as e:
            print(f"Ошибка в division_positive_by_positive: {e}")
            self.print_test_result("division_positive_by_positive", False)

        try:
            # Положительное ÷ отрицательное
            result = self.ten_pos // self.five_neg
            self.assertEqual(result.s, 1)
            self.assertEqual(result.A, [2])
            self.print_test_result("division_positive_by_negative")
        except Exception as e:
            print(f"Ошибка в division_positive_by_negative: {e}")
            self.print_test_result("division_positive_by_negative", False)

        try:
            # Отрицательное ÷ положительное
            result = self.ten_neg // self.five_pos
            self.assertEqual(result.s, 1)
            self.assertEqual(result.A, [2])
            self.print_test_result("division_negative_by_positive")
        except Exception as e:
            print(f"Ошибка в division_negative_by_positive: {e}")
            self.print_test_result("division_negative_by_positive", False)

        try:
            # Отрицательное ÷ отрицательное
            result = self.ten_neg // self.five_neg
            self.assertEqual(result.s, 0)
            self.assertEqual(result.A, [2])
            self.print_test_result("division_negative_by_negative")
        except Exception as e:
            print(f"Ошибка в division_negative_by_negative: {e}")
            self.print_test_result("division_negative_by_negative", False)

        try:
            # Деление на единицу
            result = self.ten_pos // self.one_pos
            self.assertEqual(result.s, 0)
            self.assertEqual(result.A, [1, 0])
            self.print_test_result("division_by_one")
        except Exception as e:
            print(f"Ошибка в division_by_one: {e}")
            self.print_test_result("division_by_one", False)

        try:
            # Деление меньшего на большее
            result = self.five_pos // self.ten_pos
            self.assertEqual(result.s, 0)
            self.assertEqual(result.A, [0])
            self.print_test_result("division_smaller_by_larger")
        except Exception as e:
            print(f"Ошибка в division_smaller_by_larger: {e}")
            self.print_test_result("division_smaller_by_larger", False)

        try:
            # Деление на ноль
            with self.assertRaises(ZeroDivisionError):
                self.ten_pos // self.zero_int
            self.print_test_result("division_by_zero_error")
        except Exception as e:
            print(f"Ошибка в division_by_zero_error: {e}")
            self.print_test_result("division_by_zero_error", False)

    # Тесты для остатка от деления (Богданов Никита)
    def test_modulo(self):
        print("\n=== Тесты остатка от деления целых (Богданов Никита) ===")
        
        try:
            # Положительное % положительное
            result = self.ten_pos % self.five_pos
            self.assertEqual(result.s, 0)
            self.assertEqual(result.A, [0])
            self.print_test_result("modulo_positive_by_positive")
        except Exception as e:
            print(f"Ошибка в modulo_positive_by_positive: {e}")
            self.print_test_result("modulo_positive_by_positive", False)

        try:
            # Положительное % положительное с остатком
            seven_pos = Integer(0, 0, [7])
            three_pos = Integer(0, 0, [3])
            result = seven_pos % three_pos
            self.assertEqual(result.s, 0)
            self.assertEqual(result.A, [1])
            self.print_test_result("modulo_positive_with_remainder")
        except Exception as e:
            print(f"Ошибка в modulo_positive_with_remainder: {e}")
            self.print_test_result("modulo_positive_with_remainder", False)

        try:
            # Отрицательное % положительное
            result = self.ten_neg % self.five_pos
            # -10 % 5 = 0
            self.assertEqual(result.s, 0)
            self.assertEqual(result.A, [0])
            self.print_test_result("modulo_negative_by_positive")
        except Exception as e:
            print(f"Ошибка в modulo_negative_by_positive: {e}")
            self.print_test_result("modulo_negative_by_positive", False)

        try:
            # Положительное % отрицательное
            result = self.ten_pos % self.five_neg
            # 10 % -5 = 0
            self.assertEqual(result.s, 0)
            self.assertEqual(result.A, [0])
            self.print_test_result("modulo_positive_by_negative")
        except Exception as e:
            print(f"Ошибка в modulo_positive_by_negative: {e}")
            self.print_test_result("modulo_positive_by_negative", False)

        try:
            # Остаток от деления на ноль
            with self.assertRaises(ValueError):
                self.ten_pos % self.zero_int
            self.print_test_result("modulo_by_zero_error")
        except Exception as e:
            print(f"Ошибка в modulo_by_zero_error: {e}")
            self.print_test_result("modulo_by_zero_error", False)

    # Комплексные тесты
    def test_complex_operations(self):
        print("\n=== Комплексные тесты операций с целыми числами ===")
        
        try:
            # (a + b) × c
            a = Integer(0, 0, [3])
            b = Integer(1, 0, [2])  # -2
            c = Integer(0, 0, [4])
            
            sum_ab = a + b  # 3 + (-2) = 1
            result = sum_ab * c  # 1 × 4 = 4
            
            self.assertEqual(result.s, 0)
            self.assertEqual(result.A, [4])
            self.print_test_result("complex_operation_1")
        except Exception as e:
            print(f"Ошибка в complex_operation_1: {e}")
            self.print_test_result("complex_operation_1", False)

        try:
            # a × b - c
            a = Integer(1, 0, [5])  # -5
            b = Integer(0, 0, [3])
            c = Integer(0, 0, [2])
            
            mul_ab = a * b  # -5 × 3 = -15
            result = mul_ab - c  # -15 - 2 = -17
            
            self.assertEqual(result.s, 1)
            self.assertEqual(result.A, [1, 7])
            self.print_test_result("complex_operation_2")
        except Exception as e:
            print(f"Ошибка в complex_operation_2: {e}")
            self.print_test_result("complex_operation_2", False)

    # Тесты пограничных случаев
    def test_edge_cases(self):
        print("\n=== Тесты пограничных случаев для целых чисел ===")
        
        try:
            # Числа с ведущими нулями
            num_with_zeros = Integer(1, 3, [0, 0, 0, 1])  # -1
            self.assertEqual(num_with_zeros.SGN_Z_D(), 1)
            self.assertEqual(num_with_zeros.ABS_Z_Z().A, [0, 0, 0, 1])
            self.print_test_result("edge_case_leading_zeros")
        except Exception as e:
            print(f"Ошибка в edge_case_leading_zeros: {e}")
            self.print_test_result("edge_case_leading_zeros", False)

        try:
            # Большие отрицательные числа
            large_neg = Integer(1, 4, [9, 9, 9, 9, 9])  # -99999
            result = large_neg.MUL_ZM_Z()  # должен стать 99999
            self.assertEqual(result.s, 0)
            self.assertEqual(result.A, [9, 9, 9, 9, 9])
            self.print_test_result("edge_case_large_negative")
        except Exception as e:
            print(f"Ошибка в edge_case_large_negative: {e}")
            self.print_test_result("edge_case_large_negative", False)

        try:
            # Операции с максимальными значениями
            max_digit = Integer(0, 0, [9])
            one = Integer(0, 0, [1])
            
            result = max_digit * one
            self.assertEqual(result.s, 0)
            self.assertEqual(result.A, [9])
            self.print_test_result("edge_case_max_values")
        except Exception as e:
            print(f"Ошибка в edge_case_max_values: {e}")
            self.print_test_result("edge_case_max_values", False)

def run_all_integer_tests():
    print("=" * 60)
    print("ЗАПУСК ТЕСТОВ ДЛЯ КЛАССА INTEGER И ПРЕОБРАЗОВАНИЙ")
    print("=" * 60)
    
    # Создаем тестовый набор
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestIntegerOperations)
    
    # Запускаем тесты
    runner = unittest.TextTestRunner(verbosity=0)
    result = runner.run(suite)
    
    print("\n" + "=" * 60)
    print("ИТОГИ ТЕСТИРОВАНИЯ INTEGER")
    print("=" * 60)
    print(f"Пройдено тестов: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Не пройдено тестов: {len(result.failures) + len(result.errors)}")
    print(f"Ошибки: {len(result.errors)}")
    print(f"Провалы: {len(result.failures)}")
    
    if result.wasSuccessful():
        print("\n✅ ВСЕ ТЕСТЫ INTEGER ПРОЙДЕНЫ УСПЕШНО!")
    else:
        print("\n❕ ЕСТЬ ПРОБЛЕМЫ В РЕАЛИЗАЦИИ INTEGER")
        
    return result.wasSuccessful()

if __name__ == '__main__':
    run_all_integer_tests()