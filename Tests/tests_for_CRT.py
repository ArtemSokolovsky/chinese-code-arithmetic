import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from CRT import CRTInteger
from N.Natural import Natural
from TRANS.TRANS_INT_Z import TRANS_INT_Z


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


# Импортируем Integer из нашего модуля
from Z.Integer import Integer


def test_division_in_soc():
    """Тест деления в СОК"""
    print("=" * 80)
    print("ТЕСТ ДЕЛЕНИЯ В СОК")
    print("=" * 80)

    # Используем корректные модули (взаимно простые)
    moduli = [
        create_big_natural("5"),
        create_big_natural("7"),
        create_big_natural("11")
    ]

    print("Модули системы:", [m.show() for m in moduli])
    print("M (произведение модулей) = 5 * 7 * 11 = 385")
    print("Диапазон представления: [-192, 192]")
    print()

    # Тест 1: Простое деление (15 / 3 = 5)
    print("1. ПРОСТОЕ ДЕЛЕНИЕ (15 / 3 = 5):")

    A = TRANS_INT_Z(15)
    B = TRANS_INT_Z(3)

    print(f"  A = 15, остатки по модулям:")
    for i, m in enumerate(moduli):
        a_mod = 15 % int(m.show())
        print(f"    15 mod {m.show()} = {a_mod}")

    print(f"  B = 3, остатки по модулям:")
    for i, m in enumerate(moduli):
        b_mod = 3 % int(m.show())
        print(f"    3 mod {m.show()} = {b_mod}")

    print("  Обратные элементы к 3 по модулям:")
    print("    3⁻¹ mod 5 = 2 (3*2=6≡1 mod 5)")
    print("    3⁻¹ mod 7 = 5 (3*5=15≡1 mod 7)")
    print("    3⁻¹ mod 11 = 4 (3*4=12≡1 mod 11)")

    crt_A = CRTInteger.from_integer(A, moduli)
    crt_B = CRTInteger.from_integer(B, moduli)

    try:
        crt_div = crt_A // crt_B
        div_int = crt_div.to_integer()

        print(f"  Результат деления в СОК: {div_int.show()}")

        # Проверим покоординатные вычисления
        print("  Покоординатные вычисления:")
        for i, m in enumerate(moduli):
            a_residue = int(crt_A.residues[i].show())
            b_residue = int(crt_B.residues[i].show())
            m_int = int(m.show())

            # Найдем обратный вручную для проверки
            for x in range(1, m_int):
                if (b_residue * x) % m_int == 1:
                    inv = x
                    break

            result = (a_residue * inv) % m_int
            print(f"    ({a_residue} * {inv}) mod {m_int} = {result}")

        if div_int.show() == "5":
            print("  ✅ Деление выполнено корректно!")
        else:
            print(f"  ❌ Ошибка: ожидалось 5, получено {div_int.show()}")

    except Exception as e:
        print(f"  ❌ Ошибка: {e}")

    # Тест 2: Деление с отрицательными числами
    print("\n2. ДЕЛЕНИЕ С ОТРИЦАТЕЛЬНЫМИ ЧИСЛАМИ (-15 / 3 = -5):")

    A_neg = TRANS_INT_Z(-15)
    crt_A_neg = CRTInteger.from_integer(A_neg, moduli)

    try:
        crt_div_neg = crt_A_neg // crt_B
        div_neg_int = crt_div_neg.to_integer()

        print(f"  Результат: {div_neg_int.show()}")

        if div_neg_int.show() == "-5":
            print("  ✅ Деление отрицательных чисел выполнено корректно!")
        else:
            print(f"  ❌ Ошибка: ожидалось -5, получено {div_neg_int.show()}")

    except Exception as e:
        print(f"  ❌ Ошибка: {e}")

    # Тест 3: Деление на необратимый элемент (15 / 5)
    print("\n3. ДЕЛЕНИЕ НА НЕОБРАТИМЫЙ ЭЛЕМЕНТ (15 / 5):")

    B_bad = TRANS_INT_Z(5)
    crt_B_bad = CRTInteger.from_integer(B_bad, moduli)

    try:
        crt_bad_div = crt_A // crt_B_bad
        print(f"  ❌ Деление не должно было сработать, но сработало!")
    except (ValueError, ZeroDivisionError) as e:
        print(f"  ✅ Деление правильно отказало (как и должно быть): {e}")

    # Тест 4: Деление больших чисел
    print("\n4. ДЕЛЕНИЕ БОЛЬШИХ ЧИСЕЛ (42 / 6 = 7):")

    A_big = str_to_integer("42")
    B_big = str_to_integer("6")

    crt_A_big = CRTInteger.from_integer(A_big, moduli)
    crt_B_big = CRTInteger.from_integer(B_big, moduli)

    try:
        crt_big_div = crt_A_big // crt_B_big
        big_div_int = crt_big_div.to_integer()

        print(f"  Результат: {big_div_int.show()}")

        if big_div_int.show() == "7":
            print("  ✅ Деление больших чисел выполнено корректно!")
        else:
            print(f"  ❌ Ошибка: ожидалось 7, получено {big_div_int.show()}")

    except Exception as e:
        print(f"  ❌ Ошибка: {e}")

    # Тест 5: Проверка всех арифметических операций в одном примере
    print("\n5. КОМБИНИРОВАННЫЕ ОПЕРАЦИИ В СОК:")
    print("   Выражение: (10 + 5) * 2 / 3 = 10")

    num1 = TRANS_INT_Z(10)
    num2 = TRANS_INT_Z(5)
    num3 = TRANS_INT_Z(2)
    num4 = TRANS_INT_Z(3)

    crt1 = CRTInteger.from_integer(num1, moduli)
    crt2 = CRTInteger.from_integer(num2, moduli)
    crt3 = CRTInteger.from_integer(num3, moduli)
    crt4 = CRTInteger.from_integer(num4, moduli)

    try:
        # (10 + 5) = 15
        sum_crt = crt1 + crt2
        # 15 * 2 = 30
        mul_crt = sum_crt * crt3
        # 30 / 3 = 10
        div_crt = mul_crt // crt4

        result_int = div_crt.to_integer()
        print(f"  Результат вычислений в СОК: {result_int.show()}")

        if result_int.show() == "10":
            print("  ✅ Все операции в СОК выполнены корректно!")
        else:
            print(f"  ❌ Ошибка: ожидалось 10, получено {result_int.show()}")

    except Exception as e:
        print(f"  ❌ Ошибка при выполнении операций: {e}")

    print("\n" + "=" * 80)
    print("ВЫВОД:")
    print("=" * 80)
    print("Деление в СОК реализовано как покоординатное умножение на обратный элемент.")
    print("Деление возможно только если делитель обратим по всем модулям.")
    print("Для нахождения обратного элемента используется расширенный алгоритм Евклида.")
    print("Все операции (+, -, *, /) выполняются строго покоординатно в СОК.")
    print("=" * 80)


if __name__ == '__main__':
    test_division_in_soc()