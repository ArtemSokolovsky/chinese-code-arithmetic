import sys
import os
import time


sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from CRT import CRTInteger
from N.Natural import Natural
from Z.Integer import Integer



def create_big_natural(number_str):
    """Создает Natural из строки с числом"""
    digits = [int(d) for d in number_str]
    return Natural(len(digits) - 1, digits)


def str_to_integer(s):
    """Преобразует строку в Integer"""
    sign = 0
    if s[0] == '-':
        sign = 1
        s = s[1:]
    digits = [int(d) for d in s]
    return Integer(sign, len(digits) - 1, digits)


def find_coprime_moduli(count, digit_per_modulus):
    """
    Находит набор взаимно простых модулей заданного размера
    Для простоты используем последовательные простые числа
    """
    # Генерируем простые числа примерно заданного размера
    moduli = []

    # Базовые простые числа разной размерности
    small_primes_3digit = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149,
                           151, 157, 163, 167, 173, 179, 181, 191, 193, 197,
                           199,211,223,227,229,233]

    large_primes_20digit = [
        "10000000000000000061",
        "10000000000000000069",
        "10000000000000000079"
    ]

    if digit_per_modulus <= 3:
        # Берем первые count простых чисел из списка
        for i in range(min(count, len(small_primes_3digit))):
            moduli.append(create_big_natural(str(small_primes_3digit[i])))
    else:
        # Для больших модулей используем предопределенные
        for i in range(min(count, len(large_primes_20digit))):
            moduli.append(create_big_natural(large_primes_20digit[i]))

    return moduli


def calculate_M(moduli):
    """Вычисляет произведение модулей M"""
    M = 1
    for m in moduli:
        M *= int(m.show())
    return M


def test_performance_comparison():
    """Сравнение производительности 26 маленьких vs 3 больших модулей"""
    print("=" * 100)
    print("СРАВНЕНИЕ ЭФФЕКТИВНОСТИ: 26 МАЛЕНЬКИХ vs 3 БОЛЬШИХ МОДУЛЯ")
    print("=" * 100)

    # Вариант 1: 20 маленьких модулей (3-4 разряда)
    print("\n1. СИСТЕМА С 26 МАЛЕНЬКИМИ МОДУЛЯМИ (3 разряда):")
    moduli_26_small = find_coprime_moduli(26, 3)

    print(f"   Количество модулей: {len(moduli_26_small)}")
    print(f"   Пример модулей: {[int(m.show()) for m in moduli_26_small[:3]]}...")

    M_small = calculate_M(moduli_26_small)
    print(f"   M = ∏ m_i ≈ 10^{len(str(M_small))}")
    print(f"   Динамический диапазон: {M_small}")

    # Вариант 2: 3 больших модуля (20 разрядов)
    print("\n2. СИСТЕМА С 3 БОЛЬШИМИ МОДУЛЯМИ (~20 разрядов):")
    moduli_3_large = find_coprime_moduli(3, 26)

    print(f"   Количество модулей: {len(moduli_3_large)}")
    print(f"   Модули: {[int(m.show()) for m in moduli_3_large]}")

    M_large = calculate_M(moduli_3_large)
    print(f"   M = ∏ m_i ≈ 10^{len(str(M_large))}")
    print(f"   Динамический диапазон: {M_large}")

    print("\n" + "=" * 100)
    print("СРАВНЕНИЕ ПРОИЗВОДИТЕЛЬНОСТИ:")
    print("=" * 100)

    # Тестовое число (30 разрядов)
    test_num_str = "123456789012345678901234567890"
    test_num = str_to_integer(test_num_str)

    results = []

    for moduli, name in [(moduli_26_small, "26 маленьких модулей"),
                         (moduli_3_large, "3 больших модуля")]:
        print(f"\n{name}:")
        print("-" * 50)

        # Тест 1: Прямое преобразование
        start = time.time()
        crt = CRTInteger.from_integer(test_num, moduli)
        encode_time = time.time() - start

        print(f"  Прямое преобразование: {encode_time:.6f} сек")

        # Тест 2: Обратное преобразование
        start = time.time()
        restored = crt.to_integer()
        decode_time = time.time() - start

        print(f"  Обратное преобразование: {decode_time:.6f} сек")

        # Тест 3: Сложение
        crt2 = CRTInteger.from_integer(str_to_integer("987654321098765432109876543210"), moduli)

        start = time.time()
        crt_sum = crt + crt2
        add_time = time.time() - start

        print(f"  Сложение в СОК: {add_time:.6f} сек")

        # Тест 4: Умножение
        start = time.time()
        crt_mul = crt * crt2
        mul_time = time.time() - start

        print(f"  Умножение в СОК: {mul_time:.6f} сек")

        # Тест 5: Деление (если возможно)
        try:
            # Делитель 2 (обратим по всем модулям)
            divisor = str_to_integer("2")
            crt_divisor = CRTInteger.from_integer(divisor, moduli)

            start = time.time()
            crt_div = crt // crt_divisor
            div_time = time.time() - start

            print(f"  Деление в СОК: {div_time:.6f} сек")
        except Exception as e:
            print(f"  Деление в СОК: невозможно ({e})")
            div_time = None

        results.append({
            "name": name,
            "encode": encode_time,
            "decode": decode_time,
            "add": add_time,
            "mul": mul_time,
            "div": div_time
        })

    print("\n" + "=" * 100)
    print("РЕЗУЛЬТАТЫ СРАВНЕНИЯ:")
    print("=" * 100)

    # Сравнение производительности
    small = results[0]
    large = results[1]

    print(f"\nОтношение времени (26_малых / 3_больших):")

    comparisons = [
        ("Прямое преобразование", small["encode"], large["encode"]),
        ("Обратное преобразование", small["decode"], large["decode"]),
        ("Сложение", small["add"], large["add"]),
        ("Умножение", small["mul"], large["mul"])
    ]

    for name, t_small, t_large in comparisons:
        if t_large > 0:
            ratio = t_small / t_large
            faster = "26 малых быстрее" if ratio < 1 else "3 больших быстрее"
            print(f"  {name}: {ratio:.2f}x ({faster})")

    print("\n" + "=" * 100)
    print("ТЕОРЕТИЧЕСКИЙ АНАЛИЗ (по учебнику Omondi & Premkumar):")
    print("=" * 100)

    print("\nПРЕИМУЩЕСТВА 26 МАЛЕНЬКИХ МОДУЛЕЙ:")
    print("1. Максимальный параллелизм (26 независимых каналов) - Глава 4, стр. 45")
    print("2. Быстрые операции по модулю (маленькие числа) - Глава 4, стр. 47")
    print("3. Простота аппаратной реализации - Глава 7, стр. 101")
    print("4. Высокая отказоустойчивость - Глава 8, стр. 113")

    print("\nПРЕИМУЩЕСТВА 3 БОЛЬШИХ МОДУЛЕЙ:")
    print("1. Простое обратное преобразование (КТО) - Глава 6, стр. 89")
    print("2. Легче деление и сравнение - Глава 6, стр. 90-92")
    print("3. Меньше памяти (3 остатка vs 20) - Глава 2, стр. 18")
    print("4. Проще масштабирование - Глава 7, стр. 101-105")

    print("\n" + "=" * 100)
    print("РЕКОМЕНДАЦИИ:")
    print("=" * 100)

    print("\nВыбор зависит от приложения:")
    print()
    print("Для ВЫСОКОПАРАЛЛЕЛЬНОЙ ОБРАБОТКИ СИГНАЛОВ:")
    print("  ✅ 20+ маленьких модулей")
    print("  Применение: ЦОС, фильтры, конволюции")
    print("  Причина: максимальный параллелизм, простые операции по модулю")
    print()
    print("Для ОБЩЕЙ ВЫЧИСЛИТЕЛЬНОЙ АРИФМЕТИКИ:")
    print("  ✅ 3-5 больших модулей")
    print("  Применение: криптография, большие числа, общие вычисления")
    print("  Причина: простое обратное преобразование, легче деление/сравнение")
    print()
    print("Для ОТКАЗОУСТОЙЧИВЫХ СИСТЕМ:")
    print("  ✅ 10-20 модулей (с избыточностью)")
    print("  Применение: аэрокосмические системы, медицинское оборудование")
    print("  Причина: возможность коррекции ошибок (Глава 8)")
    print()
    print("Оптимальный компромисс (рекомендация учебника):")
    print("  ⚖️  4 модулей сбалансированной размерности")
    print("  Причина: баланс между параллелизмом и сложностью операций")


if __name__ == '__main__':
    test_performance_comparison()