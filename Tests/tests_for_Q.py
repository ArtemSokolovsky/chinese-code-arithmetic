import unittest
from Q.Rational import Rational
from N.Natural import Natural
from Z.Integer import Integer
from TRANS.TRANS_N_Z import TRANS_N_Z

class TestRationalOperations(unittest.TestCase):

    def setUp(self):
        # Создаем тестовые данные
        # Натуральные числа
        self.zero_natural = Natural(0, [0])
        self.one_natural = Natural(0, [1])
        self.two_natural = Natural(0, [2])
        self.three_natural = Natural(0, [3])
        self.five_natural = Natural(0, [5])
        self.ten_natural = Natural(1, [1, 0])
        
        # Целые числа
        self.zero_int = Integer(0, 0, [0])
        self.one_pos = Integer(0, 0, [1])
        self.one_neg = Integer(1, 0, [1])
        self.two_pos = Integer(0, 0, [2])
        self.three_pos = Integer(0, 0, [3])
        self.five_pos = Integer(0, 0, [5])
        self.five_neg = Integer(1, 0, [5])
        self.ten_pos = Integer(0, 1, [1, 0])
        self.ten_neg = Integer(1, 1, [1, 0])
        
        # Рациональные числа
        self.zero_rational = Rational(self.zero_int, self.one_natural)
        self.half = Rational(self.one_pos, self.two_natural)
        self.third = Rational(self.one_pos, self.three_natural)
        self.two_thirds = Rational(self.two_pos, self.three_natural)
        self.three_halves = Rational(self.three_pos, self.two_natural)
        self.negative_half = Rational(self.one_neg, self.two_natural)
        self.five_tenths = Rational(self.five_pos, self.ten_natural)
        self.ten_fifths = Rational(self.ten_pos, self.five_natural)

    def print_test_result(self, method_name, passed=True):
        status = "ПРОЙДЕН" if passed else "ОШИБКА"
        print(f"Тест {method_name}: {status}")

    # Тесты для RED_Q_Q (Сурин Максим)
    def test_RED_Q_Q(self):
        print("\n=== Тесты RED_Q_Q (Сурин Максим) ===")
        
        try:
            # Сокращение дроби 5/10 -> 1/2
            result = self.five_tenths.RED_Q_Q()
            self.assertEqual(result.numerator.A, [1])
            self.assertEqual(result.numerator.s, 0)
            self.assertEqual(result.denominator.A, [2])
            self.print_test_result("RED_Q_Q_simple_reduction")
        except Exception as e:
            print(f"Ошибка в RED_Q_Q_simple_reduction: {e}")
            self.print_test_result("RED_Q_Q_simple_reduction", False)

        try:
            # Сокращение дроби 10/5 -> 2/1
            result = self.ten_fifths.RED_Q_Q()
            self.assertEqual(result.numerator.A, [2])
            self.assertEqual(result.numerator.s, 0)
            self.assertEqual(result.denominator.A, [1])
            self.print_test_result("RED_Q_Q_integer_result")
        except Exception as e:
            print(f"Ошибка в RED_Q_Q_integer_result: {e}")
            self.print_test_result("RED_Q_Q_integer_result", False)

        try:
            # Сокращение уже сокращенной дроби
            result = self.half.RED_Q_Q()
            self.assertEqual(result.numerator.A, [1])
            self.assertEqual(result.denominator.A, [2])
            self.print_test_result("RED_Q_Q_already_reduced")
        except Exception as e:
            print(f"Ошибка в RED_Q_Q_already_reduced: {e}")
            self.print_test_result("RED_Q_Q_already_reduced", False)

        try:
            # Сокращение отрицательной дроби
            negative_five_tenths = Rational(self.five_neg, self.ten_natural)
            result = negative_five_tenths.RED_Q_Q()
            self.assertEqual(result.numerator.A, [1])
            self.assertEqual(result.numerator.s, 1)
            self.assertEqual(result.denominator.A, [2])
            self.print_test_result("RED_Q_Q_negative")
        except Exception as e:
            print(f"Ошибка в RED_Q_Q_negative: {e}")
            self.print_test_result("RED_Q_Q_negative", False)

        try:
            # Сокращение нуля
            result = self.zero_rational.RED_Q_Q()
            self.assertEqual(result.numerator.A, [0])
            self.assertEqual(result.denominator.A, [1])
            self.print_test_result("RED_Q_Q_zero")
        except Exception as e:
            print(f"Ошибка в RED_Q_Q_zero: {e}")
            self.print_test_result("RED_Q_Q_zero", False)

    # Тесты для INT_Q_B (Захаренко Александр)
    def test_INT_Q_B(self):
        print("\n=== Тесты INT_Q_B (Захаренко Александр) ===")
        
        try:
            # Целое число (2/1)
            integer_rational = Rational(self.two_pos, self.one_natural)
            self.assertTrue(integer_rational.INT_Q_B())
            self.print_test_result("INT_Q_B_true_integer")
        except Exception as e:
            print(f"Ошибка в INT_Q_B_true_integer: {e}")
            self.print_test_result("INT_Q_B_true_integer", False)

        try:
            # Не целое число (1/2)
            self.assertFalse(self.half.INT_Q_B())
            self.print_test_result("INT_Q_B_false_fraction")
        except Exception as e:
            print(f"Ошибка в INT_Q_B_false_fraction: {e}")
            self.print_test_result("INT_Q_B_false_fraction", False)

        try:
            # Ноль (0/1)
            self.assertTrue(self.zero_rational.INT_Q_B())
            self.print_test_result("INT_Q_B_zero")
        except Exception as e:
            print(f"Ошибка в INT_Q_B_zero: {e}")
            self.print_test_result("INT_Q_B_zero", False)

        try:
            # Отрицательное целое (-5/1)
            negative_integer = Rational(self.five_neg, self.one_natural)
            self.assertTrue(negative_integer.INT_Q_B())
            self.print_test_result("INT_Q_B_negative_integer")
        except Exception as e:
            print(f"Ошибка в INT_Q_B_negative_integer: {e}")
            self.print_test_result("INT_Q_B_negative_integer", False)

    # Тесты для ADD_QQ_Q (Имховик Наталья)
    def test_ADD_QQ_Q(self):
        print("\n=== Тесты ADD_QQ_Q (Имховик Наталья) ===")
        
        try:
            # 1/2 + 1/3 = 5/6
            result = self.half + self.third
            self.assertEqual(result.numerator.A, [5])
            self.assertEqual(result.numerator.s, 0)
            self.assertEqual(result.denominator.A, [6])
            self.print_test_result("ADD_QQ_Q_basic")
        except Exception as e:
            print(f"Ошибка в ADD_QQ_Q_basic: {e}")
            self.print_test_result("ADD_QQ_Q_basic", False)

        try:
            # 1/2 + (-1/2) = 0/1
            result = self.half + self.negative_half
            self.assertEqual(result.numerator.A, [0])
            self.assertEqual(result.denominator.A, [1])
            self.print_test_result("ADD_QQ_Q_opposite_signs")
        except Exception as e:
            print(f"Ошибка в ADD_QQ_Q_opposite_signs: {e}")
            self.print_test_result("ADD_QQ_Q_opposite_signs", False)

        try:
            # 0 + 1/2 = 1/2
            result = self.zero_rational + self.half
            self.assertEqual(result.numerator.A, [1])
            self.assertEqual(result.denominator.A, [2])
            self.print_test_result("ADD_QQ_Q_with_zero")
        except Exception as e:
            print(f"Ошибка в ADD_QQ_Q_with_zero: {e}")
            self.print_test_result("ADD_QQ_Q_with_zero", False)

    # Тесты для SUB_QQ_Q (Имховик Наталья)
    def test_SUB_QQ_Q(self):
        print("\n=== Тесты SUB_QQ_Q (Имховик Наталья) ===")
        
        try:
            # 1/2 - 1/3 = 1/6
            result = self.half - self.third
            self.assertEqual(result.numerator.A, [1])
            self.assertEqual(result.numerator.s, 0)
            self.assertEqual(result.denominator.A, [6])
            self.print_test_result("SUB_QQ_Q_basic")
        except Exception as e:
            print(f"Ошибка в SUB_QQ_Q_basic: {e}")
            self.print_test_result("SUB_QQ_Q_basic", False)

        try:
            # 1/3 - 1/2 = -1/6
            result = self.third - self.half
            self.assertEqual(result.numerator.A, [1])
            self.assertEqual(result.numerator.s, 1)
            self.assertEqual(result.denominator.A, [6])
            self.print_test_result("SUB_QQ_Q_negative_result")
        except Exception as e:
            print(f"Ошибка в SUB_QQ_Q_negative_result: {e}")
            self.print_test_result("SUB_QQ_Q_negative_result", False)

        try:
            # 1/2 - 0 = 1/2
            result = self.half - self.zero_rational
            self.assertEqual(result.numerator.A, [1])
            self.assertEqual(result.denominator.A, [2])
            self.print_test_result("SUB_QQ_Q_subtract_zero")
        except Exception as e:
            print(f"Ошибка в SUB_QQ_Q_subtract_zero: {e}")
            self.print_test_result("SUB_QQ_Q_subtract_zero", False)

        try:
            # 0 - 1/2 = -1/2
            result = self.zero_rational - self.half
            self.assertEqual(result.numerator.A, [1])
            self.assertEqual(result.numerator.s, 1)
            self.assertEqual(result.denominator.A, [2])
            self.print_test_result("SUB_QQ_Q_zero_minus_fraction")
        except Exception as e:
            print(f"Ошибка в SUB_QQ_Q_zero_minus_fraction: {e}")
            self.print_test_result("SUB_QQ_Q_zero_minus_fraction", False)

    # Тесты для умножения (Чумаков Никита)
    def test_multiplication(self):
        print("\n=== Тесты умножения рациональных (Чумаков Никита) ===")
        
        try:
            # 1/2 × 2/3 = 2/6 = 1/3
            result = self.half * self.two_thirds
            self.assertEqual(result.numerator.A, [1])
            self.assertEqual(result.denominator.A, [3])
            self.print_test_result("multiplication_basic")
        except Exception as e:
            print(f"Ошибка в multiplication_basic: {e}")
            self.print_test_result("multiplication_basic", False)

        try:
            # 1/2 × (-1/2) = -1/4
            result = self.half * self.negative_half
            self.assertEqual(result.numerator.A, [1])
            self.assertEqual(result.numerator.s, 1)
            self.assertEqual(result.denominator.A, [4])
            self.print_test_result("multiplication_with_negative")
        except Exception as e:
            print(f"Ошибка в multiplication_with_negative: {e}")
            self.print_test_result("multiplication_with_negative", False)

        try:
            # (-1/3) × (-1/2) = 1/6
            negative_third = Rational(self.one_neg, self.three_natural)
            result = negative_third * self.negative_half
            self.assertEqual(result.numerator.A, [1])
            self.assertEqual(result.numerator.s, 0)
            self.assertEqual(result.denominator.A, [6])
            self.print_test_result("multiplication_both_negative")
        except Exception as e:
            print(f"Ошибка в multiplication_both_negative: {e}")
            self.print_test_result("multiplication_both_negative", False)

        try:
            # 0 × 1/2 = 0
            result = self.zero_rational * self.half
            self.assertEqual(result.numerator.A, [0])
            self.assertEqual(result.denominator.A, [1])
            self.print_test_result("multiplication_with_zero")
        except Exception as e:
            print(f"Ошибка в multiplication_with_zero: {e}")
            self.print_test_result("multiplication_with_zero", False)

    # Тесты для деления (Чумаков Никита)
    def test_division(self):
        print("\n=== Тесты деления рациональных (Чумаков Никита) ===")
        
        try:
            # (1/2) ÷ (2/3) = 3/4
            result = self.half / self.two_thirds
            self.assertEqual(result.numerator.A, [3])
            self.assertEqual(result.numerator.s, 0)
            self.assertEqual(result.denominator.A, [4])
            self.print_test_result("division_basic")
        except Exception as e:
            print(f"Ошибка в division_basic: {e}")
            self.print_test_result("division_basic", False)

        try:
            # (1/2) ÷ (-1/3) = -3/2
            negative_third = Rational(self.one_neg, self.three_natural)
            result = self.half / negative_third
            self.assertEqual(result.numerator.A, [3])
            self.assertEqual(result.numerator.s, 1)
            self.assertEqual(result.denominator.A, [2])
            self.print_test_result("division_by_negative")
        except Exception as e:
            print(f"Ошибка в division_by_negative: {e}")
            self.print_test_result("division_by_negative", False)

        try:
            # 0 ÷ 1/2 = 0
            result = self.zero_rational / self.half
            self.assertEqual(result.numerator.A, [0])
            self.assertEqual(result.denominator.A, [1])
            self.print_test_result("division_zero_by_fraction")
        except Exception as e:
            print(f"Ошибка в division_zero_by_fraction: {e}")
            self.print_test_result("division_zero_by_fraction", False)

        try:
            # Деление на ноль
            zero_fraction = Rational(self.zero_int, self.one_natural)
            with self.assertRaises(ZeroDivisionError):
                self.half / zero_fraction
            self.print_test_result("division_by_zero_error")
        except Exception as e:
            print(f"Ошибка в division_by_zero_error: {e}")
            self.print_test_result("division_by_zero_error", False)

    # Комплексные тесты
    def test_complex_operations(self):
        print("\n=== Комплексные тесты операций с рациональными числами ===")
        
        try:
            # (1/2 + 1/3) × (2/3 - 1/6) = (5/6) × (1/2) = 5/12
            sum_result = self.half + self.third  # 5/6
            one_sixth = Rational(self.one_pos, Natural(0, [6]))
            sub_result = self.two_thirds - one_sixth  # 1/2
            result = sum_result * sub_result  # 5/12
            
            self.assertEqual(result.numerator.A, [5])
            self.assertEqual(result.denominator.A, [1, 2])
            self.print_test_result("complex_operation_1")
        except Exception as e:
            print(f"Ошибка в complex_operation_1: {e}")
            self.print_test_result("complex_operation_1", False)

    # Тесты пограничных случаев
    def test_edge_cases(self):
        print("\n=== Тесты пограничных случаев для рациональных чисел ===")
        
        try:
            # Единичные дроби
            one_over_one = Rational(self.one_pos, self.one_natural)
            self.assertTrue(one_over_one.INT_Q_B())
            self.assertEqual(one_over_one.RED_Q_Q().numerator.A, [1])
            self.assertEqual(one_over_one.RED_Q_Q().denominator.A, [1])
            self.print_test_result("edge_case_unit_fractions")
        except Exception as e:
            print(f"Ошибка в edge_case_unit_fractions: {e}")
            self.print_test_result("edge_case_unit_fractions", False)

def run_all_rational_tests():
    print("=" * 60)
    print("ЗАПУСК ТЕСТОВ ДЛЯ КЛАССА RATIONAL")
    print("=" * 60)
    
    # Создаем тестовый набор
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestRationalOperations)
    
    # Запускаем тесты
    runner = unittest.TextTestRunner(verbosity=0)
    result = runner.run(suite)
    
    print("\n" + "=" * 60)
    print("ИТОГИ ТЕСТИРОВАНИЯ RATIONAL")
    print("=" * 60)
    print(f"Пройдено тестов: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Не пройдено тестов: {len(result.failures) + len(result.errors)}")
    print(f"Ошибки: {len(result.errors)}")
    print(f"Провалы: {len(result.failures)}")
    
    if result.wasSuccessful():
        print("\n✅ ВСЕ ТЕСТЫ RATIONAL ПРОЙДЕНЫ УСПЕШНО!")
    else:
        print("\n❕ ЕСТЬ ПРОБЛЕМЫ В РЕАЛИЗАЦИИ RATIONAL")
        
    return result.wasSuccessful()

if __name__ == '__main__':
    run_all_rational_tests()
