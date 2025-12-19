import unittest
from P.Polynomial import Polynomial
from N.Natural import Natural
from Z.Integer import Integer
from Q.Rational import Rational

class TestPolynomialOperations(unittest.TestCase):

    def setUp(self):
        # Создаем тестовые данные
        # Натуральные числа
        self.zero_natural = Natural(0, [0])
        self.one_natural = Natural(0, [1])
        self.two_natural = Natural(0, [2])
        self.three_natural = Natural(0, [3])
        
        # Целые числа
        self.zero_int = Integer(0, 0, [0])
        self.one_pos = Integer(0, 0, [1])
        self.one_neg = Integer(1, 0, [1])
        self.two_pos = Integer(0, 0, [2])
        self.three_pos = Integer(0, 0, [3])
        self.four_pos = Integer(0, 0, [4])
        
        # Рациональные числа
        self.zero_rational = Rational(self.zero_int, self.one_natural)
        self.one_rational = Rational(self.one_pos, self.one_natural)
        self.two_rational = Rational(self.two_pos, self.one_natural)
        self.three_rational = Rational(self.three_pos, self.one_natural)
        self.four_rational = Rational(self.four_pos, self.one_natural)
        self.half = Rational(self.one_pos, self.two_natural)
        self.third = Rational(self.one_pos, self.three_natural)
        
        # Полиномы
        # P(x) = 0
        self.zero_poly = Polynomial(0, [self.zero_rational])
        
        # P(x) = 1
        self.one_poly = Polynomial(0, [self.one_rational])
        
        # P(x) = 2
        self.two_poly = Polynomial(0, [self.two_rational])
        
        # P(x) = x + 1
        self.linear_poly = Polynomial(1, [self.one_rational, self.one_rational])
        
        # P(x) = x^2 + 2x + 1
        self.quadratic_poly = Polynomial(2, [self.one_rational, self.two_rational, self.one_rational])
        
        # P(x) = 2x^2 + 3x + 1
        self.quadratic_poly2 = Polynomial(2, [self.two_rational, self.three_rational, self.one_rational])
        
        # P(x) = x^3 + x^2 + x + 1
        self.cubic_poly = Polynomial(3, [self.one_rational, self.one_rational, self.one_rational, self.one_rational])
        
        # P(x) = 3x^2 + 2x + 1
        self.quadratic_poly3 = Polynomial(2, [self.three_rational, self.two_rational, self.one_rational])

    def print_test_result(self, method_name, passed=True):
        status = "ПРОЙДЕН" if passed else "ОШИБКА"
        print(f"Тест {method_name}: {status}")

    # Тесты для сложения многочленов (Богданов Никита)
    def test_addition(self):
        print("\n=== Тесты сложения многочленов (Богданов Никита) ===")
        
        try:
            # Сложение одинаковых многочленов
            result = self.one_poly + self.one_poly
            self.assertEqual(result.m, 0)
            self.assertEqual(result.C[0].numerator.A, [2])
            self.print_test_result("addition_same_polynomials")
        except Exception as e:
            print(f"Ошибка в addition_same_polynomials: {e}")
            self.print_test_result("addition_same_polynomials", False)

        try:
            # Сложение с нулевым многочленом
            result = self.linear_poly + self.zero_poly
            self.assertEqual(result.m, 1)
            self.assertEqual(result.C[0].numerator.A, [1])
            self.assertEqual(result.C[1].numerator.A, [1])
            self.print_test_result("addition_with_zero")
        except Exception as e:
            print(f"Ошибка в addition_with_zero: {e}")
            self.print_test_result("addition_with_zero", False)

        try:
            # Сложение разных степеней
            # (x + 1) + (x^2 + 2x + 1) = x^2 + 3x + 2
            result = self.linear_poly + self.quadratic_poly
            self.assertEqual(result.m, 2)
            self.assertEqual(result.C[0].numerator.A, [1])  # x^2
            self.assertEqual(result.C[1].numerator.A, [3])  # 3x
            self.assertEqual(result.C[2].numerator.A, [2])  # 2
            self.print_test_result("addition_different_degrees")
        except Exception as e:
            print(f"Ошибка в addition_different_degrees: {e}")
            self.print_test_result("addition_different_degrees", False)

    # Тесты для вычитания многочленов (Богданов Никита)
    def test_subtraction(self):
        print("\n=== Тесты вычитания многочленов (Богданов Никита) ===")
        
        try:
            # Вычитание одинаковых многочленов
            result = self.one_poly - self.one_poly
            self.assertEqual(result.C[0].numerator.A, [0])
            self.print_test_result("subtraction_same_polynomials")
        except Exception as e:
            print(f"Ошибка в subtraction_same_polynomials: {e}")
            self.print_test_result("subtraction_same_polynomials", False)

        try:
            # Вычитание нулевого многочлена
            result = self.linear_poly - self.zero_poly
            self.assertEqual(result.m, 1)
            self.assertEqual(result.C[0].numerator.A, [1])
            self.assertEqual(result.C[1].numerator.A, [1])
            self.print_test_result("subtraction_zero")
        except Exception as e:
            print(f"Ошибка в subtraction_zero: {e}")
            self.print_test_result("subtraction_zero", False)

        try:
            # Вычитание разных степеней
            # (x^2 + 2x + 1) - (x + 1) = x^2 + x
            result = self.quadratic_poly - self.linear_poly
            self.assertEqual(result.m, 2)
            self.assertEqual(result.C[0].numerator.A, [1])  # x^2
            self.assertEqual(result.C[1].numerator.A, [1])  # x
            self.assertEqual(result.C[2].numerator.A, [0])  # 0
            self.print_test_result("subtraction_different_degrees")
        except Exception as e:
            print(f"Ошибка в subtraction_different_degrees: {e}")
            self.print_test_result("subtraction_different_degrees", False)

    # Тесты для MUL_PQ_P (Захаренко Александр)
    def test_MUL_PQ_P(self):
        print("\n=== Тесты MUL_PQ_P (Захаренко Александр) ===")
        
        try:
            # Умножение на 1
            result = self.linear_poly.MUL_PQ_P(self.one_rational)
            self.assertEqual(result.m, 1)
            self.assertEqual(result.C[0].numerator.A, [1])
            self.assertEqual(result.C[1].numerator.A, [1])
            self.print_test_result("MUL_PQ_P_by_one")
        except Exception as e:
            print(f"Ошибка в MUL_PQ_P_by_one: {e}")
            self.print_test_result("MUL_PQ_P_by_one", False)

        try:
            # Умножение на 2
            result = self.linear_poly.MUL_PQ_P(self.two_rational)
            self.assertEqual(result.m, 1)
            self.assertEqual(result.C[0].numerator.A, [2])
            self.assertEqual(result.C[1].numerator.A, [2])
            self.print_test_result("MUL_PQ_P_by_two")
        except Exception as e:
            print(f"Ошибка в MUL_PQ_P_by_two: {e}")
            self.print_test_result("MUL_PQ_P_by_two", False)

        try:
            # Умножение на дробь
            result = self.linear_poly.MUL_PQ_P(self.half)
            self.assertEqual(result.m, 1)
            self.assertEqual(result.C[0].numerator.A, [1])
            self.assertEqual(result.C[0].denominator.A, [2])
            self.assertEqual(result.C[1].numerator.A, [1])
            self.assertEqual(result.C[1].denominator.A, [2])
            self.print_test_result("MUL_PQ_P_by_fraction")
        except Exception as e:
            print(f"Ошибка в MUL_PQ_P_by_fraction: {e}")
            self.print_test_result("MUL_PQ_P_by_fraction", False)

        try:
            # Умножение на ноль
            result = self.linear_poly.MUL_PQ_P(self.zero_rational)
            self.assertEqual(result.C[0].numerator.A, [0])
            self.print_test_result("MUL_PQ_P_by_zero")
        except Exception as e:
            print(f"Ошибка в MUL_PQ_P_by_zero: {e}")
            self.print_test_result("MUL_PQ_P_by_zero", False)

    # Тесты для MUL_Pxk_P (Захаренко Александр)
    def test_MUL_Pxk_P(self):
        print("\n=== Тесты MUL_Pxk_P (Захаренко Александр) ===")
        
        try:
            # Умножение на x^0 (без изменений)
            result = self.linear_poly.MUL_Pxk_P(0)
            self.assertEqual(result.m, 1)
            self.assertEqual(result.C[0].numerator.A, [1])
            self.assertEqual(result.C[1].numerator.A, [1])
            self.print_test_result("MUL_Pxk_P_zero_power")
        except Exception as e:
            print(f"Ошибка в MUL_Pxk_P_zero_power: {e}")
            self.print_test_result("MUL_Pxk_P_zero_power", False)

        try:
            # Умножение на x^1
            # (x + 1) * x = x^2 + x
            result = self.linear_poly.MUL_Pxk_P(1)
            self.assertEqual(result.m, 2)
            self.assertEqual(len(result.C), 3)
            self.assertEqual(result.C[0].numerator.A, [1])  # x^2
            self.assertEqual(result.C[1].numerator.A, [1])  # x
            self.assertEqual(result.C[2].numerator.A, [0])  # 0
            self.print_test_result("MUL_Pxk_P_first_power")
        except Exception as e:
            print(f"Ошибка в MUL_Pxk_P_first_power: {e}")
            self.print_test_result("MUL_Pxk_P_first_power", False)

        try:
            # Умножение на x^2
            # (x + 1) * x^2 = x^3 + x^2
            result = self.linear_poly.MUL_Pxk_P(2)
            self.assertEqual(result.m, 3)
            self.assertEqual(len(result.C), 4)
            self.assertEqual(result.C[0].numerator.A, [1])  # x^3
            self.assertEqual(result.C[1].numerator.A, [1])  # x^2
            self.assertEqual(result.C[2].numerator.A, [0])  # 0
            self.assertEqual(result.C[3].numerator.A, [0])  # 0
            self.print_test_result("MUL_Pxk_P_second_power")
        except Exception as e:
            print(f"Ошибка в MUL_Pxk_P_second_power: {e}")
            self.print_test_result("MUL_Pxk_P_second_power", False)

    # Тесты для LED_P_Q (Сурин Максим)
    def test_LED_P_Q(self):
        print("\n=== Тесты LED_P_Q (Сурин Максим) ===")
        
        try:
            # Старший коэффициент линейного многочлена
            result = self.linear_poly.LED_P_Q()
            self.assertEqual(result.numerator.A, [1])
            self.assertEqual(result.denominator.A, [1])
            self.print_test_result("LED_P_Q_linear")
        except Exception as e:
            print(f"Ошибка в LED_P_Q_linear: {e}")
            self.print_test_result("LED_P_Q_linear", False)

        try:
            # Старший коэффициент квадратного многочлена
            result = self.quadratic_poly.LED_P_Q()
            self.assertEqual(result.numerator.A, [1])
            self.assertEqual(result.denominator.A, [1])
            self.print_test_result("LED_P_Q_quadratic")
        except Exception as e:
            print(f"Ошибка в LED_P_Q_quadratic: {e}")
            self.print_test_result("LED_P_Q_quadratic", False)

        try:
            # Старший коэффициент нулевого многочлена
            result = self.zero_poly.LED_P_Q()
            self.assertEqual(result.numerator.A, [0])
            self.print_test_result("LED_P_Q_zero")
        except Exception as e:
            print(f"Ошибка в LED_P_Q_zero: {e}")
            self.print_test_result("LED_P_Q_zero", False)

    # Тесты для DEG_P_N (Чумаков Никита)
    def test_DEG_P_N(self):
        print("\n=== Тесты DEG_P_N (Чумаков Никита) ===")
        
        try:
            # Степень нулевого многочлена
            result = self.zero_poly.DEG_P_N()
            self.assertEqual(result.A, [0])
            self.print_test_result("DEG_P_N_zero")
        except Exception as e:
            print(f"Ошибка в DEG_P_N_zero: {e}")
            self.print_test_result("DEG_P_N_zero", False)

        try:
            # Степень константного многочлена
            result = self.one_poly.DEG_P_N()
            self.assertEqual(result.A, [0])
            self.print_test_result("DEG_P_N_constant")
        except Exception as e:
            print(f"Ошибка в DEG_P_N_constant: {e}")
            self.print_test_result("DEG_P_N_constant", False)

        try:
            # Степень линейного многочлена
            result = self.linear_poly.DEG_P_N()
            self.assertEqual(result.A, [1])
            self.print_test_result("DEG_P_N_linear")
        except Exception as e:
            print(f"Ошибка в DEG_P_N_linear: {e}")
            self.print_test_result("DEG_P_N_linear", False)

        try:
            # Степень квадратного многочлена
            result = self.quadratic_poly.DEG_P_N()
            self.assertEqual(result.A, [2])
            self.print_test_result("DEG_P_N_quadratic")
        except Exception as e:
            print(f"Ошибка в DEG_P_N_quadratic: {e}")
            self.print_test_result("DEG_P_N_quadratic", False)

    # Тесты для умножения многочленов (Сурин Максим)
    def test_multiplication(self):
        print("\n=== Тесты умножения многочленов (Сурин Максим) ===")
        
        try:
            # Умножение на 1
            result = self.linear_poly * self.one_poly
            self.assertEqual(result.m, 1)
            self.assertEqual(result.C[0].numerator.A, [1])
            self.assertEqual(result.C[1].numerator.A, [1])
            self.print_test_result("multiplication_by_one")
        except Exception as e:
            print(f"Ошибка в multiplication_by_one: {e}")
            self.print_test_result("multiplication_by_one", False)

        try:
            # Умножение на ноль
            result = self.linear_poly * self.zero_poly
            self.assertEqual(result.C[0].numerator.A, [0])
            self.print_test_result("multiplication_by_zero")
        except Exception as e:
            print(f"Ошибка в multiplication_by_zero: {e}")
            self.print_test_result("multiplication_by_zero", False)

        try:
            # Умножение линейных многочленов
            # (x + 1) * (x + 1) = x^2 + 2x + 1
            result = self.linear_poly * self.linear_poly
            self.assertEqual(result.m, 2)
            self.assertEqual(result.C[0].numerator.A, [1])  # x^2
            self.assertEqual(result.C[1].numerator.A, [2])  # 2x
            self.assertEqual(result.C[2].numerator.A, [1])  # 1
            self.print_test_result("multiplication_linear_polynomials")
        except Exception as e:
            print(f"Ошибка в multiplication_linear_polynomials: {e}")
            self.print_test_result("multiplication_linear_polynomials", False)

    # Тесты для деления многочленов (Чумаков Никита)
    def test_division(self):
        print("\n=== Тесты деления многочленов (Чумаков Никита) ===")
        
        try:
            # Деление на 1
            result = self.linear_poly // self.one_poly
            self.assertEqual(result.m, 1)
            self.assertEqual(result.C[0].numerator.A, [1])
            self.assertEqual(result.C[1].numerator.A, [1])
            self.print_test_result("division_by_one")
        except Exception as e:
            print(f"Ошибка в division_by_one: {e}")
            self.print_test_result("division_by_one", False)

        try:
            # Деление одинаковых многочленов
            result = self.linear_poly // self.linear_poly
            self.assertEqual(result.m, 0)
            self.assertEqual(result.C[0].numerator.A, [1])
            self.print_test_result("division_same_polynomials")
        except Exception as e:
            print(f"Ошибка в division_same_polynomials: {e}")
            self.print_test_result("division_same_polynomials", False)

        try:
            # Деление на многочлен большей степени
            # (x + 1) // (x^2 + 2x + 1) = 0
            result = self.linear_poly // self.quadratic_poly
            self.assertEqual(result.C[0].numerator.A, [0])
            self.print_test_result("division_by_higher_degree")
        except Exception as e:
            print(f"Ошибка в division_by_higher_degree: {e}")
            self.print_test_result("division_by_higher_degree", False)

        try:
            # Деление на ноль
            with self.assertRaises(ZeroDivisionError):
                self.linear_poly // self.zero_poly
            self.print_test_result("division_by_zero_error")
        except Exception as e:
            print(f"Ошибка в division_by_zero_error: {e}")
            self.print_test_result("division_by_zero_error", False)

    # Тесты для MOD_PP_P (Имховик Наталья)
    def test_MOD_PP_P(self):
        print("\n=== Тесты MOD_PP_P (Имховик Наталья) ===")
        
        try:
            # Остаток от деления на 1
            result = self.linear_poly % self.one_poly
            self.assertEqual(result.C[0].numerator.A, [0])
            self.print_test_result("MOD_PP_P_by_one")
        except Exception as e:
            print(f"Ошибка в MOD_PP_P_by_one: {e}")
            self.print_test_result("MOD_PP_P_by_one", False)

        try:
            # Остаток от деления одинаковых многочленов
            result = self.linear_poly % self.linear_poly
            self.assertEqual(result.C[0].numerator.A, [0])
            self.print_test_result("MOD_PP_P_same_polynomials")
        except Exception as e:
            print(f"Ошибка в MOD_PP_P_same_polynomials: {e}")
            self.print_test_result("MOD_PP_P_same_polynomials", False)

    # Тесты для GCF_PP_P (Имховик Наталья)
    def test_GCF_PP_P(self):
        print("\n=== Тесты GCF_PP_P (Имховик Наталья) ===")
        
        try:
            # НОД одинаковых многочленов
            result = self.linear_poly.GCF_PP_P(self.linear_poly)
            self.assertEqual(result.m, 1)
            self.assertEqual(result.C[0].numerator.A, [1])
            self.assertEqual(result.C[1].numerator.A, [1])
            self.print_test_result("GCF_PP_P_same_polynomials")
        except Exception as e:
            print(f"Ошибка в GCF_PP_P_same_polynomials: {e}")
            self.print_test_result("GCF_PP_P_same_polynomials", False)

        try:
            # НОД многочлена с самим собой
            result = self.quadratic_poly.GCF_PP_P(self.quadratic_poly)
            self.assertEqual(result.m, 2)
            self.assertEqual(result.C[0].numerator.A, [1])
            self.assertEqual(result.C[1].numerator.A, [2])
            self.assertEqual(result.C[2].numerator.A, [1])
            self.print_test_result("GCF_PP_P_self")
        except Exception as e:
            print(f"Ошибка в GCF_PP_P_self: {e}")
            self.print_test_result("GCF_PP_P_self", False)

    # Тесты для DER_P_P (Соколовский Артём)
    def test_DER_P_P(self):
        print("\n=== Тесты DER_P_P (Соколовский Артём) ===")
        
        try:
            # Производная константы
            result = self.one_poly.DER_P_P()
            self.assertEqual(result.C[0].numerator.A, [0])
            self.print_test_result("DER_P_P_constant")
        except Exception as e:
            print(f"Ошибка в DER_P_P_constant: {e}")
            self.print_test_result("DER_P_P_constant", False)

        try:
            # Производная линейного многочлена
            # (x + 1)' = 1
            result = self.linear_poly.DER_P_P()
            self.assertEqual(result.m, 0)
            self.assertEqual(result.C[0].numerator.A, [1])
            self.print_test_result("DER_P_P_linear")
        except Exception as e:
            print(f"Ошибка в DER_P_P_linear: {e}")
            self.print_test_result("DER_P_P_linear", False)

        try:
            # Производная квадратного многочлена
            # (x^2 + 2x + 1)' = 2x + 2
            result = self.quadratic_poly.DER_P_P()
            self.assertEqual(result.m, 1)
            self.assertEqual(result.C[0].numerator.A, [2])  # 2x
            self.assertEqual(result.C[1].numerator.A, [2])  # 2
            self.print_test_result("DER_P_P_quadratic")
        except Exception as e:
            print(f"Ошибка в DER_P_P_quadratic: {e}")
            self.print_test_result("DER_P_P_quadratic", False)

        try:
            # Производная кубического многочлена
            # (x^3 + x^2 + x + 1)' = 3x^2 + 2x + 1
            result = self.cubic_poly.DER_P_P()
            self.assertEqual(result.m, 2)
            self.assertEqual(result.C[0].numerator.A, [3])  # 3x^2
            self.assertEqual(result.C[1].numerator.A, [2])  # 2x
            self.assertEqual(result.C[2].numerator.A, [1])  # 1
            self.print_test_result("DER_P_P_cubic")
        except Exception as e:
            print(f"Ошибка в DER_P_P_cubic: {e}")
            self.print_test_result("DER_P_P_cubic", False)

    # Тесты для NMR_P_P (Соколовский Артём)
    def test_NMR_P_P(self):
        print("\n=== Тесты NMR_P_P (Соколовский Артём) ===")
        
        try:
            # Неприводимый многочлен для константы
            result = self.one_poly.NMR_P_P()
            self.assertEqual(result.C[0].numerator.A, [1])
            self.print_test_result("NMR_P_P_constant")
        except Exception as e:
            print(f"Ошибка в NMR_P_P_constant: {e}")
            self.print_test_result("NMR_P_P_constant", False)

        try:
            # Неприводимый многочлен для линейного
            result = self.linear_poly.NMR_P_P()
            self.assertEqual(result.m, 1)
            self.assertEqual(result.C[0].numerator.A, [1])
            self.assertEqual(result.C[1].numerator.A, [1])
            self.print_test_result("NMR_P_P_linear")
        except Exception as e:
            print(f"Ошибка в NMR_P_P_linear: {e}")
            self.print_test_result("NMR_P_P_linear", False)

    # Тесты для FAC_P_Q (Соколовский Артём)
    def test_FAC_P_Q(self):
        print("\n=== Тесты FAC_P_Q (Соколовский Артём) ===")
        
        try:
            # Вынесение множителя для константного многочлена
            factor, new_poly = self.one_poly.FAC_P_Q()
            self.assertEqual(new_poly.C[0].numerator.A, [1])
            self.print_test_result("FAC_P_Q_constant")
        except Exception as e:
            print(f"Ошибка в FAC_P_Q_constant: {e}")
            self.print_test_result("FAC_P_Q_constant", False)

        try:
            # Вынесение множителя для линейного многочлена
            factor, new_poly = self.linear_poly.FAC_P_Q()
            self.assertEqual(new_poly.m, 1)
            self.print_test_result("FAC_P_Q_linear")
        except Exception as e:
            print(f"Ошибка в FAC_P_Q_linear: {e}")
            self.print_test_result("FAC_P_Q_linear", False)

    # Комплексные тесты
    def test_complex_operations(self):
        print("\n=== Комплексные тесты операций с многочленами ===")
        
        try:
            # (x + 1) + (x^2 + 2x + 1) - (x + 1) = x^2 + 2x + 1
            sum_result = self.linear_poly + self.quadratic_poly
            result = sum_result - self.linear_poly
            self.assertEqual(result.m, 2)
            self.assertEqual(result.C[0].numerator.A, [1])  # x^2
            self.assertEqual(result.C[1].numerator.A, [2])  # 2x
            self.assertEqual(result.C[2].numerator.A, [1])  # 1
            self.print_test_result("complex_operation_1")
        except Exception as e:
            print(f"Ошибка в complex_operation_1: {e}")
            self.print_test_result("complex_operation_1", False)

        try:
            # 2 * (x + 1) = 2x + 2
            result = self.linear_poly.MUL_PQ_P(self.two_rational)
            self.assertEqual(result.m, 1)
            self.assertEqual(result.C[0].numerator.A, [2])
            self.assertEqual(result.C[1].numerator.A, [2])
            self.print_test_result("complex_operation_2")
        except Exception as e:
            print(f"Ошибка в complex_operation_2: {e}")
            self.print_test_result("complex_operation_2", False)

    # Тесты пограничных случаев
    def test_edge_cases(self):
        print("\n=== Тесты пограничных случаев для многочленов ===")
        
        try:
            # Многочлен с ведущими нулями
            poly_with_zeros = Polynomial(3, [
                self.zero_rational,
                self.one_rational,
                self.two_rational,
                self.three_rational
            ])
            # После операций ведущие нули должны убираться
            result = poly_with_zeros + self.zero_poly
            self.assertEqual(result.m, 2)  # Степень должна уменьшиться
            self.print_test_result("edge_case_leading_zeros")
        except Exception as e:
            print(f"Ошибка в edge_case_leading_zeros: {e}")
            self.print_test_result("edge_case_leading_zeros", False)

        try:
            # Операции с максимальными значениями
            large_coeff = Rational(Integer(0, 2, [9, 9, 9]), Natural(0, [1]))
            large_poly = Polynomial(1, [large_coeff, large_coeff])
            result = large_poly + large_poly
            self.assertEqual(result.C[0].numerator.A, [1, 9, 9, 8])
            self.print_test_result("edge_case_large_numbers")
        except Exception as e:
            print(f"Ошибка в edge_case_large_numbers: {e}")
            self.print_test_result("edge_case_large_numbers", False)

def run_all_polynomial_tests():
    print("=" * 60)
    print("ЗАПУСК ТЕСТОВ ДЛЯ КЛАССА POLYNOMIAL")
    print("=" * 60)
    
    # Создаем тестовый набор
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestPolynomialOperations)
    
    # Запускаем тесты
    runner = unittest.TextTestRunner(verbosity=0)
    result = runner.run(suite)
    
    print("\n" + "=" * 60)
    print("ИТОГИ ТЕСТИРОВАНИЯ POLYNOMIAL")
    print("=" * 60)
    print(f"Пройдено тестов: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Не пройдено тестов: {len(result.failures) + len(result.errors)}")
    print(f"Ошибки: {len(result.errors)}")
    print(f"Провалы: {len(result.failures)}")
    
    if result.wasSuccessful():
        print("\n✅ ВСЕ ТЕСТЫ POLYNOMIAL ПРОЙДЕНЫ УСПЕШНО!")
    else:
        print("\n❕ ЕСТЬ ПРОБЛЕМЫ В РЕАЛИЗАЦИИ POLYNOMIAL")
        
    return result.wasSuccessful()

if __name__ == '__main__':
    run_all_polynomial_tests()
