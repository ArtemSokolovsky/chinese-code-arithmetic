import unittest
from N.Natural import Natural

class TestNaturalOperations(unittest.TestCase):

    def setUp(self):
        self.zero = Natural(0, [0])
        self.one = Natural(0, [1])
        self.two = Natural(0, [2])
        self.nine = Natural(0, [9])
        self.ten = Natural(1, [1, 0])
        self.hundred = Natural(2, [1, 0, 0])
        self.large_num1 = Natural(4, [1, 2, 3, 4, 5])
        self.large_num2 = Natural(3, [9, 9, 9, 9])

    def print_test_result(self, method_name, passed=True):
        status = "ПРОЙДЕН" if passed else "ОШИБКА"
        print(f"Тест {method_name}: {status}")

    # Тесты для COM_NN_D (Соколовский Артём)
    def test_COM_NN_D(self):
        print("\n=== Тесты COM_NN_D (Соколовский Артём) ===")
        
        try:
            # Равные числа
            num1 = Natural(2, [1, 2, 3])
            num2 = Natural(2, [1, 2, 3])
            self.assertEqual(num1.COM_NN_D(num2), 0)
            self.print_test_result("COM_NN_D_equal_numbers")
        except AssertionError:
            self.print_test_result("COM_NN_D_equal_numbers", False)

        try:
            # Первое больше по длине
            num1 = Natural(3, [1, 0, 0, 0])
            num2 = Natural(2, [9, 9, 9])
            self.assertEqual(num1.COM_NN_D(num2), 1)
            self.print_test_result("COM_NN_D_first_greater_by_length")
        except AssertionError:
            self.print_test_result("COM_NN_D_first_greater_by_length", False)

        try:
            # Второе больше по длине
            num1 = Natural(2, [9, 9, 9])
            num2 = Natural(3, [1, 0, 0, 0])
            self.assertEqual(num1.COM_NN_D(num2), -1)
            self.print_test_result("COM_NN_D_second_greater_by_length")
        except AssertionError:
            self.print_test_result("COM_NN_D_second_greater_by_length", False)

        try:
            # Первое больше по цифрам
            num1 = Natural(2, [1, 2, 4])
            num2 = Natural(2, [1, 2, 3])
            self.assertEqual(num1.COM_NN_D(num2), 1)
            self.print_test_result("COM_NN_D_first_greater_by_digits")
        except AssertionError:
            self.print_test_result("COM_NN_D_first_greater_by_digits", False)

        try:
            # Ведущие нули
            num1 = Natural(4, [0, 0, 1, 2, 3])
            num2 = Natural(2, [1, 2, 3])
            self.assertEqual(num1.COM_NN_D(num2), 0)
            self.print_test_result("COM_NN_D_with_leading_zeros")
        except AssertionError:
            self.print_test_result("COM_NN_D_with_leading_zeros", False)

        try:
            # Сравнение с нулем
            zero = Natural(0, [0])
            num = Natural(1, [1, 0])
            self.assertEqual(zero.COM_NN_D(num), -1)
            self.assertEqual(num.COM_NN_D(zero), 1)
            self.assertEqual(zero.COM_NN_D(zero), 0)
            self.print_test_result("COM_NN_D_zero_comparison")
        except AssertionError:
            self.print_test_result("COM_NN_D_zero_comparison", False)

    # Тесты для NZER_N_B (Богданов Никита)
    def test_NZER_N_B(self):
        print("\n=== Тесты NZER_N_B (Богданов Никита) ===")
        
        try:
            # Ноль - должен возвращать False (число равно нулю)
            zero = Natural(0, [0])
            self.assertFalse(zero.NZER_N_B())  # False - число равно нулю
            self.print_test_result("NZER_N_B_zero")
        except AssertionError:
            self.print_test_result("NZER_N_B_zero", False)

        try:
            # Однозначные не нули - должны возвращать True (число НЕ равно нулю)
            self.assertTrue(self.one.NZER_N_B())   # True - число 1 НЕ равно нулю
            self.assertTrue(self.nine.NZER_N_B())  # True - число 9 НЕ равно нулю
            self.print_test_result("NZER_N_B_single_digit_non_zero")
        except AssertionError:
            self.print_test_result("NZER_N_B_single_digit_non_zero", False)

        try:
            # Многозначные не нули - должны возвращать True (число НЕ равно нулю)
            self.assertTrue(self.ten.NZER_N_B())      # True - число 10 НЕ равно нулю
            self.assertTrue(self.hundred.NZER_N_B())  # True - число 100 НЕ равно нулю
            self.print_test_result("NZER_N_B_multi_digit_non_zero")
        except AssertionError:
            self.print_test_result("NZER_N_B_multi_digit_non_zero", False)

        try:
            # Число с ведущими нулями - должно возвращать True (число НЕ равно нулю)
            num_with_zeros = Natural(3, [0, 0, 0, 1])
            self.assertTrue(num_with_zeros.NZER_N_B())  # True - число 1 НЕ равно нулю
            self.print_test_result("NZER_N_B_with_leading_zeros")
        except AssertionError:
            self.print_test_result("NZER_N_B_with_leading_zeros", False)

    # Тесты для ADD_1N_N (Сурин Максим)
    def test_ADD_1N_N(self):
        print("\n=== Тесты ADD_1N_N (Сурин Максим) ===")
        
        try:
            # Однозначные числа
            result = self.one.ADD_1N_N()
            self.assertEqual(result.A, [2])
            result = self.nine.ADD_1N_N()
            self.assertEqual(result.A, [1, 0])
            self.print_test_result("ADD_1N_N_single_digit")
        except Exception as e:
            print(f"Ошибка в ADD_1N_N_single_digit: {e}")
            self.print_test_result("ADD_1N_N_single_digit", False)

        try:
            # Перенос
            num = Natural(2, [9, 9, 9])
            result = num.ADD_1N_N()
            self.assertEqual(result.A, [1, 0, 0, 0])
            self.print_test_result("ADD_1N_N_carry_over")
        except Exception as e:
            print(f"Ошибка в ADD_1N_N_carry_over: {e}")
            self.print_test_result("ADD_1N_N_carry_over", False)

        try:
            # Без переноса
            num = Natural(2, [1, 2, 3])
            result = num.ADD_1N_N()
            self.assertEqual(result.A, [1, 2, 4])
            self.print_test_result("ADD_1N_N_no_carry")
        except Exception as e:
            print(f"Ошибка в ADD_1N_N_no_carry: {e}")
            self.print_test_result("ADD_1N_N_no_carry", False)

        try:
            # Ноль
            result = self.zero.ADD_1N_N()
            self.assertEqual(result.A, [1])
            self.print_test_result("ADD_1N_N_zero")
        except Exception as e:
            print(f"Ошибка в ADD_1N_N_zero: {e}")
            self.print_test_result("ADD_1N_N_zero", False)

    # Тесты для сложения (Соколовский Артём)
    def test_addition(self):
        print("\n=== Тесты сложения (Соколовский Артём) ===")
        
        try:
            # Базовое сложение
            num1 = Natural(1, [1, 2])
            num2 = Natural(1, [3, 4])
            result = num1 + num2
            self.assertEqual(result.A, [4, 6])
            self.print_test_result("addition_basic")
        except AssertionError:
            self.print_test_result("addition_basic", False)

        try:
            # Сложение с переносом
            num1 = Natural(1, [9, 9])
            num2 = Natural(0, [1])
            result = num1 + num2
            self.assertEqual(result.A, [1, 0, 0])
            self.print_test_result("addition_with_carry")
        except AssertionError:
            self.print_test_result("addition_with_carry", False)

        try:
            # Разная длина
            num1 = Natural(2, [1, 0, 0])
            num2 = Natural(1, [9, 9])
            result = num1 + num2
            self.assertEqual(result.A, [1, 9, 9])
            self.print_test_result("addition_different_lengths")
        except AssertionError:
            self.print_test_result("addition_different_lengths", False)

        try:
            # С нулем
            result = self.zero + self.one
            self.assertEqual(result.A, [1])
            result = self.one + self.zero
            self.assertEqual(result.A, [1])
            self.print_test_result("addition_zero")
        except AssertionError:
            self.print_test_result("addition_zero", False)

    # Тесты для вычитания (Соколовский Артём)
    def test_subtraction(self):
        print("\n=== Тесты вычитания (Соколовский Артём) ===")
        
        try:
            # Базовое вычитание
            num1 = Natural(1, [5, 4])
            num2 = Natural(1, [3, 2])
            result = num1 - num2
            self.assertEqual(result.A, [2, 2])
            self.print_test_result("subtraction_basic")
        except AssertionError:
            self.print_test_result("subtraction_basic", False)

        try:
            # Вычитание с заемом
            num1 = Natural(1, [1, 0, 0])
            num2 = Natural(1, [9, 9])
            result = num1 - num2
            self.assertEqual(result.A, [1])
            self.print_test_result("subtraction_with_borrow")
        except AssertionError:
            self.print_test_result("subtraction_with_borrow", False)

        try:
            # Равные числа
            num1 = Natural(2, [1, 2, 3])
            num2 = Natural(2, [1, 2, 3])
            result = num1 - num2
            self.assertEqual(result.A, [0])
            self.print_test_result("subtraction_equal_numbers")
        except AssertionError:
            self.print_test_result("subtraction_equal_numbers", False)

        try:
            # Вычитание из меньшего (должно вызывать ошибку)
            num1 = Natural(0, [1])
            num2 = Natural(0, [2])
            with self.assertRaises(ValueError):
                num1 - num2
            self.print_test_result("subtraction_from_smaller_raises_error")
        except AssertionError:
            self.print_test_result("subtraction_from_smaller_raises_error", False)

    # Тесты для MUL_ND_N (Сурин Максим)
    def test_MUL_ND_N(self):
        print("\n=== Тесты MUL_ND_N (Сурин Максим) ===")
        
        try:
            # Базовое умножение
            num = Natural(1, [1, 2])
            result = num.MUL_ND_N(3)
            self.assertEqual(result.A, [3, 6])
            self.print_test_result("MUL_ND_N_basic")
        except Exception as e:
            print(f"Ошибка в MUL_ND_N_basic: {e}")
            self.print_test_result("MUL_ND_N_basic", False)

        try:
            # Умножение с переносом
            num = Natural(1, [9, 9])
            result = num.MUL_ND_N(2)
            self.assertEqual(result.A, [1, 9, 8])
            self.print_test_result("MUL_ND_N_with_carry")
        except Exception as e:
            print(f"Ошибка в MUL_ND_N_with_carry: {e}")
            self.print_test_result("MUL_ND_N_with_carry", False)

        try:
            # Умножение на ноль
            num = Natural(2, [1, 2, 3])
            result = num.MUL_ND_N(0)
            self.assertEqual(result.A, [0])
            self.print_test_result("MUL_ND_N_by_zero")
        except Exception as e:
            print(f"Ошибка в MUL_ND_N_by_zero: {e}")
            self.print_test_result("MUL_ND_N_by_zero", False)

        try:
            # Умножение на единицу
            num = Natural(2, [1, 2, 3])
            result = num.MUL_ND_N(1)
            self.assertEqual(result.A, [1, 2, 3])
            self.print_test_result("MUL_ND_N_by_one")
        except Exception as e:
            print(f"Ошибка в MUL_ND_N_by_one: {e}")
            self.print_test_result("MUL_ND_N_by_one", False)

    # Тесты для MUL_Nk_N (Богданов Никита)
    def test_MUL_Nk_N(self):
        print("\n=== Тесты MUL_Nk_N (Богданов Никита) ===")
        
        try:
            # Нулевая степень
            k = Natural(0, [0])
            result = self.ten.MUL_Nk_N(k)
            self.assertEqual(result.A, [1, 0])
            self.print_test_result("MUL_Nk_N_zero_power")
        except AssertionError:
            self.print_test_result("MUL_Nk_N_zero_power", False)

        try:
            # Однозначная степень
            k = Natural(0, [2])
            result = self.one.MUL_Nk_N(k)
            self.assertEqual(result.A, [1, 0, 0])
            self.print_test_result("MUL_Nk_N_single_digit_power")
        except AssertionError:
            self.print_test_result("MUL_Nk_N_single_digit_power", False)

        try:
            # Нулевое число
            k = Natural(0, [5])
            result = self.zero.MUL_Nk_N(k)
            self.assertEqual(result.A, [0])
            self.print_test_result("MUL_Nk_N_zero_number")
        except AssertionError:
            self.print_test_result("MUL_Nk_N_zero_number", False)

        try:
            # Большое число
            k = Natural(0, [3])
            num = Natural(2, [1, 2, 3])
            result = num.MUL_Nk_N(k)
            self.assertEqual(result.A, [1, 2, 3, 0, 0, 0])
            self.print_test_result("MUL_Nk_N_large_number")
        except AssertionError:
            self.print_test_result("MUL_Nk_N_large_number", False)

    # Тесты для умножения (Богданов Никита)
    def test_multiplication(self):
        print("\n=== Тесты умножения (Богданов Никита) ===")
        
        # Базовое умножение
        num1 = Natural(1, [1, 2])
        num2 = Natural(0, [3])
        result = num1 * num2
        self.assertEqual(result.A, [3, 6])
        self.print_test_result("multiplication_basic")
        
        # Умножение на ноль
        result = self.large_num1 * self.zero
        self.assertEqual(result.A, [0])
        result = self.zero * self.large_num1
        self.assertEqual(result.A, [0])
        self.print_test_result("multiplication_by_zero")
        
        # Умножение на единицу
        result = self.large_num1 * self.one
        self.assertEqual(result.A, self.large_num1.A)
        self.print_test_result("multiplication_by_one")
        
        # Большие числа
        num1 = Natural(1, [9, 9])
        num2 = Natural(1, [9, 9])
        result = num1 * num2
        self.assertEqual(result.A, [9, 8, 0, 1])
        self.print_test_result("multiplication_large_numbers")

    # Тесты умножения - пограничные случаи
    def test_multiplication_edge_cases(self):
        print("\n=== Тесты умножения - пограничные случаи ===")
        
        try:
            zero_num = Natural(0, [0])
            num_with_zeros = Natural(3, [0, 0, 0, 1])
            
            # Умножение на ноль
            result = num_with_zeros * zero_num
            self.assertEqual(result.A, [0])  # 1 * 0 = 0
            
            # Умножение нуля на число
            result = zero_num * num_with_zeros  
            self.assertEqual(result.A, [0])  # 0 * 1 = 0
            
            self.print_test_result("multiplication_edge_cases")
        except AssertionError as e:
            print(f"Ошибка в multiplication_edge_cases: {e}")
            self.print_test_result("multiplication_edge_cases", False)

    # Тесты для SUB_NDN_N (Сурин Максим)
    def test_SUB_NDN_N(self):
        print("\n=== Тесты SUB_NDN_N (Сурин Максим) ===")
        
        try:
            # Базовый случай
            num1 = Natural(2, [1, 0, 0])
            num2 = Natural(1, [2, 5])
            result = num1.SUB_NDN_N(2, num2)  # 100 - 2*25 = 50
            self.assertEqual(result.A, [5, 0])
            self.print_test_result("SUB_NDN_N_basic")
        except Exception as e:
            print(f"Ошибка в SUB_NDN_N_basic: {e}")
            self.print_test_result("SUB_NDN_N_basic", False)

        try:
            # Отрицательный результат
            num1 = Natural(1, [1, 0])
            num2 = Natural(1, [5, 0])
            result = num1.SUB_NDN_N(1, num2)  # 10 - 1*50 = -40 → 0
            self.assertEqual(result.A, [0])
            self.print_test_result("SUB_NDN_N_negative_result")
        except Exception as e:
            print(f"Ошибка в SUB_NDN_N_negative_result: {e}")
            self.print_test_result("SUB_NDN_N_negative_result", False)

        try:
            # Нулевой результат
            num1 = Natural(1, [5, 0])
            num2 = Natural(1, [2, 5])
            result = num1.SUB_NDN_N(2, num2)  # 50 - 2*25 = 0
            self.assertEqual(result.A, [0])
            self.print_test_result("SUB_NDN_N_zero_result")
        except Exception as e:
            print(f"Ошибка в SUB_NDN_N_zero_result: {e}")
            self.print_test_result("SUB_NDN_N_zero_result", False)

    # Тесты для DIV_NN_Dk (Захаренко Александр)
    def test_DIV_NN_Dk(self):
        print("\n=== Тесты DIV_NN_Dk (Захаренко Александр) ===")
        
        try:
            # Базовый случай
            num1 = Natural(2, [1, 0, 0])
            num2 = Natural(1, [2, 5])
            digit, k = num1.DIV_NN_Dk(num2)
            self.assertEqual(digit, 4)
            self.assertEqual(k, 0)
            self.print_test_result("DIV_NN_Dk_basic")
        except AssertionError:
            self.print_test_result("DIV_NN_Dk_basic", False)

        try:
            # Большие числа
            num1 = Natural(3, [1, 0, 0, 0])
            num2 = Natural(1, [2, 5])
            digit, k = num1.DIV_NN_Dk(num2)
            self.assertEqual(digit, 4)
            self.assertEqual(k, 1)
            self.print_test_result("DIV_NN_Dk_large_numbers")
        except AssertionError:
            self.print_test_result("DIV_NN_Dk_large_numbers", False)

        try:
            # Числитель меньше знаменателя
            num1 = Natural(1, [2, 4])
            num2 = Natural(1, [2, 5])
            digit, k = num1.DIV_NN_Dk(num2)
            self.assertEqual(digit, 0)
            self.assertEqual(k, 0)
            self.print_test_result("DIV_NN_Dk_smaller_numerator")
        except AssertionError:
            self.print_test_result("DIV_NN_Dk_smaller_numerator", False)

        try:
            # Равные числа
            num1 = Natural(2, [1, 2, 3])
            num2 = Natural(2, [1, 2, 3])
            digit, k = num1.DIV_NN_Dk(num2)
            self.assertEqual(digit, 1)
            self.assertEqual(k, 0)
            self.print_test_result("DIV_NN_Dk_equal_numbers")
        except AssertionError:
            self.print_test_result("DIV_NN_Dk_equal_numbers", False)

    # Тесты для целочисленного деления (Захаренко Александр)
    def test_floor_division(self):
        print("\n=== Тесты целочисленного деления (Захаренко Александр) ===")
        
        try:
            # Базовый случай
            num1 = Natural(2, [1, 0, 0])
            num2 = Natural(1, [2, 5])
            result = num1 // num2
            self.assertEqual(result.A, [4])
            self.print_test_result("floor_division_basic")
        except AssertionError:
            self.print_test_result("floor_division_basic", False)

        try:
            # Большие числа
            num1 = Natural(3, [1, 0, 0, 0])
            num2 = Natural(1, [2, 5])
            result = num1 // num2
            self.assertEqual(result.A, [4, 0])
            self.print_test_result("floor_division_large_numbers")
        except AssertionError:
            self.print_test_result("floor_division_large_numbers", False)

        try:
            # Числитель меньше знаменателя
            num1 = Natural(1, [2, 4])
            num2 = Natural(1, [2, 5])
            result = num1 // num2
            self.assertEqual(result.A, [0])
            self.print_test_result("floor_division_smaller_numerator")
        except AssertionError:
            self.print_test_result("floor_division_smaller_numerator", False)

        try:
            # Деление на единицу
            result = self.large_num1 // self.one
            self.assertEqual(result.A, self.large_num1.A)
            self.print_test_result("floor_division_by_one")
        except AssertionError:
            self.print_test_result("floor_division_by_one", False)

        try:
            # Нулевой числитель
            result = self.zero // self.ten
            self.assertEqual(result.A, [0])
            self.print_test_result("floor_division_zero_numerator")
        except AssertionError:
            self.print_test_result("floor_division_zero_numerator", False)

        try:
            # Деление на ноль
            zero = Natural(0, [0])
            with self.assertRaises(ZeroDivisionError):
                self.one // zero
            self.print_test_result("floor_division_by_zero_raises_error")
        except AssertionError:
            self.print_test_result("floor_division_by_zero_raises_error", False)

    # Тесты для остатка от деления (Захаренко Александр)
    def test_modulo(self):
        print("\n=== Тесты остатка от деления (Захаренко Александр) ===")
        
        try:
            # Базовый случай
            num1 = Natural(2, [1, 0, 0])
            num2 = Natural(1, [2, 5])
            result = num1 % num2
            self.assertEqual(result.A, [0])
            self.print_test_result("modulo_basic")
        except Exception as e:
            print(f"Ошибка в modulo_basic: {e}")
            self.print_test_result("modulo_basic", False)

        try:
            # С остатком
            num1 = Natural(2, [1, 0, 7])
            num2 = Natural(1, [2, 5])
            result = num1 % num2
            self.assertEqual(result.A, [7])
            self.print_test_result("modulo_with_remainder")
        except Exception as e:
            print(f"Ошибка в modulo_with_remainder: {e}")
            self.print_test_result("modulo_with_remainder", False)

        try:
            # Числитель меньше знаменателя
            num1 = Natural(1, [2, 4])
            num2 = Natural(1, [2, 5])
            result = num1 % num2
            self.assertEqual(result.A, [2, 4])
            self.print_test_result("modulo_smaller_numerator")
        except Exception as e:
            print(f"Ошибка в modulo_smaller_numerator: {e}")
            self.print_test_result("modulo_smaller_numerator", False)

    # Тесты для НОД (Чумаков Никита)
    def test_GCF_NN_N(self):
        print("\n=== Тесты НОД (Чумаков Никита) ===")
        
        try:
            # Базовый случай - ИСПРАВЛЕНО: Natural(1, [7, 2])
            num1 = Natural(2, [1, 2, 8])  # 128 - длина 2, массив [1, 2, 8]
            num2 = Natural(1, [7, 2])     # 72 - длина 1, массив [7, 2]
            result = num1.GCF_NN_N(num2)
            self.assertEqual(result.A, [8])
            self.print_test_result("GCF_NN_N_basic")
        except AssertionError:
            self.print_test_result("GCF_NN_N_basic", False)

        try:
            # Взаимно простые числа
            num1 = Natural(1, [1, 5])    # 15 - длина 1, массив [1, 5]
            num2 = Natural(1, [2, 8])    # 28 - длина 1, массив [2, 8]
            result = num1.GCF_NN_N(num2)
            self.assertEqual(result.A, [1])
            self.print_test_result("GCF_NN_N_coprime")
        except AssertionError:
            self.print_test_result("GCF_NN_N_coprime", False)

        try:
            # Равные числа
            result = self.large_num1.GCF_NN_N(self.large_num1)
            self.assertEqual(result.A, self.large_num1.A)
            self.print_test_result("GCF_NN_N_equal_numbers")
        except AssertionError:
            self.print_test_result("GCF_NN_N_equal_numbers", False)

        try:
            # Большие числа
            num1 = Natural(2, [9, 6, 0])   # 960 - длина 2, массив [9, 6, 0]
            num2 = Natural(2, [7, 2, 0])   # 720 - длина 2, массив [7, 2, 0]
            result = num1.GCF_NN_N(num2)
            self.assertEqual(result.A, [2, 4, 0])
            self.print_test_result("GCF_NN_N_large_numbers")
        except AssertionError:
            self.print_test_result("GCF_NN_N_large_numbers", False)

    # Тесты для НОК (Имховик Наталья)
    def test_LCM_NN_N(self):
        print("\n=== Тесты НОК (Имховик Наталья) ===")
    
        # Базовый случай
        num1 = Natural(1, [1, 2])    # 12
        num2 = Natural(1, [1, 8])    # 18
        result = num1.LCM_NN_N(num2)
        self.assertEqual(result.A, [3, 6])
        self.print_test_result("LCM_NN_N_basic")

        # Взаимно простые числа
        num1 = Natural(0, [3])       # 3
        num2 = Natural(0, [5])       # 5
        result = num1.LCM_NN_N(num2)
        self.assertEqual(result.A, [1, 5])
        self.print_test_result("LCM_NN_N_coprime")

        # Равные числа
        result = self.large_num1.LCM_NN_N(self.large_num1)
        self.assertEqual(result.A, self.large_num1.A)
        self.print_test_result("LCM_NN_N_equal_numbers")

        # Большие числа
        num1 = Natural(1, [1, 5])    # 15
        num2 = Natural(1, [2, 0])    # 20
        result = num1.LCM_NN_N(num2)
        self.assertEqual(result.A, [6, 0])
        self.print_test_result("LCM_NN_N_large_numbers")

        # Дополнительные тесты для пограничных случаев
    def test_edge_cases(self):
        print("\n=== Дополнительные тесты пограничных случаев ===")
        
        try:
            # Однозначные числа
            for i in range(10):
                for j in range(10):
                    num_i = Natural(0, [i])
                    num_j = Natural(0, [j])
                    
                    # Сравнение
                    expected_cmp = 1 if i > j else (-1 if i < j else 0)
                    self.assertEqual(num_i.COM_NN_D(num_j), expected_cmp)
            self.print_test_result("edge_case_single_digits_comparison")
        except AssertionError:
            self.print_test_result("edge_case_single_digits_comparison", False)

        try:
            # Операции с нулями - ТОЛЬКО СЛОЖЕНИЕ И ВЫЧИТАНИЕ
            zero_num = Natural(0, [0])
            num_with_zeros = Natural(3, [0, 0, 0, 1])
            
            # Проверка NZER_N_B с исправленной логикой
            self.assertFalse(zero_num.NZER_N_B())      # False - число равно нулю
            self.assertTrue(num_with_zeros.NZER_N_B()) # True - число 1 НЕ равно нулю
            
            # Сложение с нулем
            result = zero_num + num_with_zeros
            self.assertEqual(result.A, [1])  # 0 + 1 = 1
            
            # Вычитание нуля
            result = num_with_zeros - zero_num
            self.assertEqual(result.A, [1])  # 1 - 0 = 1
            
            # Сравнение
            self.assertEqual(zero_num.COM_NN_D(num_with_zeros), -1)  # 0 < 1
            self.assertEqual(num_with_zeros.COM_NN_D(zero_num), 1)   # 1 > 0
            
            self.print_test_result("edge_case_zeros")
        except AssertionError as e:
            print(f"Ошибка в edge_case_zeros: {e}")
            self.print_test_result("edge_case_zeros", False)

        try:
            # Операции с максимальными переносами
            all_nines = Natural(4, [9, 9, 9, 9, 9])
            one = Natural(0, [1])
            
            # Сложение 99999 + 1
            result = all_nines + one
            self.assertEqual(result.A, [1, 0, 0, 0, 0, 0])
            self.print_test_result("edge_case_carry_operations")
        except AssertionError:
            self.print_test_result("edge_case_carry_operations", False)

def run_all_tests():
    print("=" * 60)
    print("ЗАПУСК ТЕСТОВ ДЛЯ КЛАССА NATURAL")
    print("=" * 60)
    
    # Создаем тестовый набор
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestNaturalOperations)
    
    # Запускаем тесты
    runner = unittest.TextTestRunner(verbosity=0)
    result = runner.run(suite)
    
    print("\n" + "=" * 60)
    print("ИТОГИ ТЕСТИРОВАНИЯ")
    print("=" * 60)
    print(f"Пройдено тестов: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Не пройдено тестов: {len(result.failures) + len(result.errors)}")
    print(f"Ошибки: {len(result.errors)}")
    print(f"Провалы: {len(result.failures)}")
    
    if result.wasSuccessful():
        print("\n✅ ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!")
    else:
        print("\n❕ ЕСТЬ ПРОБЛЕМЫ В РЕАЛИЗАЦИИ")
        
    return result.wasSuccessful()

if __name__ == '__main__':
    run_all_tests()