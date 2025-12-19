import re
from P.Polynomial import Polynomial
from Q.Rational import Rational
from TRANS.TRANS_INT_Q import TRANS_INT_Q
from TRANS.TRANS_STR_P import TRANS_STR_P
from TRANS.TRANS_Q_P import TRANS_Q_P
from TRANS.TRANS_INT_N import TRANS_INT_N
from TRANS.TRANS_INT_Z import TRANS_INT_Z
from CRT import CRTInteger
from N.Natural import Natural


def create_big_natural(number_str):
    """Создает Natural из строки с числом"""
    digits = [int(d) for d in number_str]
    return Natural(len(digits) - 1, digits)


def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def to_rpn(expression: str):
    expression = expression.replace(' ', '')

    # Обрабатываем специальные операторы
    expression = expression.replace('//', '§')  # временная замена для целочисленного деления

    # === ДОПОЛНИТЕЛЬНО: вставляем * между скобкой и x ===
    # Например: (...)x → (...)*x
    expression = re.sub(r'(?<=\))(?=x)', '*', expression)
    # Также: число сразу перед x (например 3x) → 3*x
    expression = re.sub(r'(?<=\d)(?=x)', '*', expression)

    # Разбиваем на токены (включая знаки)
    token_pattern = r'(x\^\d+|x|\d+\.\d+|\d+|[+\-*/§%^()])'  # добавлен § и %
    tokens = re.findall(token_pattern, expression)

    # === Обработка унарных минусов ===
    processed = []
    for i, tok in enumerate(tokens):
        if tok == '-':
            # Унарный минус — если стоит в начале или после оператора или открывающей скобки
            if i == 0 or tokens[i - 1] in {'+', '-', '*', '/', '§', '%', '^', '('}:
                if i + 1 < len(tokens):
                    nxt = tokens[i + 1]
                    combined = '-' + nxt
                    processed.append(combined)
                    tokens[i + 1] = ''  # помечаем, что этот токен уже использован
                continue
        if tok != '':
            processed.append(tok)

    # === Алгоритм сортировочной станции ===
    output = []
    stack = []

    precedence = {'^': 4, '*': 3, '/': 3, '§': 3, '%': 3, '+': 2, '-': 2}  # добавлены § и %
    right_assoc = {'^'}

    for token in processed:
        if re.fullmatch(r'-?\d+(\.\d+)?', token) or re.fullmatch(r'-?x(\^\d+)?', token):
            output.append(token)
        elif token in precedence:
            while stack and stack[-1] in precedence:
                top = stack[-1]
                if (token not in right_assoc and precedence[token] <= precedence[top]) or \
                        (token in right_assoc and precedence[token] < precedence[top]):
                    output.append(stack.pop())
                else:
                    break
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # убрать '('

    while stack:
        output.append(stack.pop())

    # Заменяем временный символ § обратно на //
    result = []
    for token in output:
        if token == '§':
            result.append('//')
        else:
            result.append(token)

    return result


def eval_rpn_p(tokens):
    stack = []

    for t in tokens:
        if t in ['+', '-', '*', '/', '%']:
            b = stack.pop()
            a = stack.pop()
            if t == '+':
                if type(a) == int:
                    a = TRANS_INT_Q(a)
                if type(b) == int:
                    b = TRANS_INT_Q(b)
                if type(a) == type(b) and type(a) != str:
                    stack.append(a + b)
                else:
                    if type(a) == Rational:
                        a = TRANS_Q_P(a)
                    if type(b) == Rational:
                        b = TRANS_Q_P(b)
                    stack.append(a + b)
            elif t == '%':
                if type(a) == int or type(b) == int:
                    raise TypeError
                if type(a) == Rational or type(b) == Rational:
                    raise TypeError
                stack.append(a % b)
            elif t == '-':
                if type(a) == int:
                    a = TRANS_INT_Q(a)
                if type(b) == int:
                    b = TRANS_INT_Q(b)
                if type(a) == type(b) and type(a) != str:
                    stack.append(a - b)
                else:
                    if type(a) == Rational:
                        a = TRANS_Q_P(a)
                    if type(b) == Rational:
                        b = TRANS_Q_P(b)
                    stack.append(a - b)
            elif t == '*':
                if type(a) == int:
                    a = TRANS_INT_Q(a)
                if type(b) == int:
                    b = TRANS_INT_Q(b)
                if type(a) == type(b) and type(a) != str:
                    stack.append(a * b)
                else:
                    if type(a) == Rational:
                        a = TRANS_Q_P(a)
                    if type(b) == Rational:
                        b = TRANS_Q_P(b)
                    stack.append(a * b)
            elif t == '/':
                if type(a) == int:
                    a = TRANS_INT_Q(a)
                if type(b) == int:
                    b = TRANS_INT_Q(b)
                if type(a) == type(b) and type(a) != str:
                    if type(a) == Polynomial:
                        stack.append(a // b)
                    else:
                        stack.append(a / b)

                else:
                    if type(a) == Rational:
                        a = TRANS_Q_P(a)
                    if type(b) == Rational:
                        b = TRANS_Q_P(b)
                    stack.append(a // b)
            elif t == '^':
                stack.append(a ** b)
        else:
            if is_number(t):
                stack.append(TRANS_INT_Q(int(t)))
            elif 'x' in t:
                stack.append(TRANS_STR_P(t))
            else:
                raise SyntaxError
    return stack[-1]


def eval_rpn_n(tokens):
    stack = []

    for t in tokens:
        if t in ['+', '-', '*', '/', '//', '%']:
            b = stack.pop()
            a = stack.pop()
            if t == '+':
                stack.append(a + b)
            elif t == '-':
                stack.append(a - b)
            elif t == '*':
                stack.append(a * b)
            elif t == '//':
                stack.append(a // b)
            elif t == '%':
                stack.append((a % b))
        else:
            stack.append(TRANS_INT_N(int(t)))

    return stack[-1]


def eval_rpn_z(tokens):
    stack = []

    for t in tokens:
        if t in ['+', '-', '*', '/', '//', '%']:
            b = stack.pop()
            a = stack.pop()
            if t == '+':
                stack.append(a + b)
            elif t == '-':
                stack.append(a - b)
            elif t == '*':
                stack.append(a * b)
            elif t == '//':
                stack.append(a // b)
            elif t == '%':
                stack.append((a % b))
        else:
            stack.append(TRANS_INT_Z(int(t)))

    return stack[-1]


def eval_rpn_q(tokens):
    stack = []

    for t in tokens:
        if t in ['+', '-', '*', '/', '//', '%']:
            b = stack.pop()
            a = stack.pop()
            if t == '+':
                stack.append(a + b)
            elif t == '-':
                stack.append(a - b)
            elif t == '*':
                stack.append(a * b)
            elif t == '/':
                stack.append(a / b)
        else:
            stack.append(TRANS_INT_Q(int(t)))

    return stack[-1]


def eval_rpn_rns(tokens):
    """Вычисление выражений в Системе Остаточных Классов (СОК)"""
    # Фиксированные модули (взаимно простые)
    moduli = [
        create_big_natural("5"),
        create_big_natural("7"),
        create_big_natural("11")
    ]

    details = []  # Для хранения деталей вычислений
    stack = []

    details.append("=" * 50)
    details.append("АРИФМЕТИКА НА КИТАЙСКОМ КОДЕ")
    details.append("=" * 50)
    details.append(f"Модули: {[int(m.show()) for m in moduli]}")
    details.append(f"M = 5 × 7 × 11 = 385")
    details.append(f"Диапазон: [-192, 192]")
    details.append("")

    for t in tokens:
        if t in ['+', '-', '*', '//']:
            if len(stack) < 2:
                raise ValueError(f"Недостаточно операндов для операции '{t}'")

            b_crt = stack.pop()
            a_crt = stack.pop()

            # Получаем значения в десятичной системе
            a_val = int(a_crt.to_integer().show())
            b_val = int(b_crt.to_integer().show())

            details.append(f"Операция: {a_val} {t} {b_val}")
            details.append("-" * 30)


            # Выполняем операцию в СОК
            if t == '+':
                result_crt = a_crt + b_crt
                op_name = "Сложение"
            elif t == '-':
                result_crt = a_crt - b_crt
                op_name = "Вычитание"
            elif t == '*':
                result_crt = a_crt * b_crt
                op_name = "Умножение"
            elif t == '//':
                result_crt = a_crt // b_crt
                op_name = "Деление"

            # Показываем остатки результата
            details.append(f"\n{op_name} в СОК (покоординатное):")
            for i, m in enumerate(moduli):
                a_res = int(a_crt.residues[i].show())
                b_res = int(b_crt.residues[i].show())
                res_res = int(result_crt.residues[i].show())
                m_val = int(m.show())

                if t == '//':
                    # Для деления показываем умножение на обратный
                    for inv in range(1, m_val):
                        if (b_res * inv) % m_val == 1:
                            details.append(f"  По модулю {m_val}: ({a_res} × {inv}) mod {m_val} = {res_res}")
                            break
                else:
                    details.append(f"  По модулю {m_val}: ({a_res} {t} {b_res}) mod {m_val} = {res_res}")

            stack.append(result_crt)
            details.append("")

        else:
            # Преобразуем число в СОК
            num = int(t)
            int_obj = TRANS_INT_Z(num)
            crt_obj = CRTInteger.from_integer(int_obj, moduli)
            stack.append(crt_obj)

            details.append(f"Число {num} преобразовано в СОК:")
            for i, m in enumerate(moduli):
                residue = int(crt_obj.residues[i].show())
                details.append(f"  {num} mod {int(m.show())} = {residue}")
            details.append("")

    if len(stack) != 1:
        raise ValueError("Некорректное выражение")

    result_crt = stack[0]
    result_int = result_crt.to_integer()
    result_val = int(result_int.show())

    # Показываем обратное преобразование
    details.append("=" * 50)
    details.append("ОБРАТНОЕ ПРЕОБРАЗОВАНИЕ ИЗ СОК")
    details.append("=" * 50)

    # Простое объяснение формулы КТО
    details.append("Формула Китайской теоремы об остатках:")
    details.append("X = (x₁·M₁·y₁ + x₂·M₂·y₂ + x₃·M₃·y₃) mod M")
    details.append("где:")
    details.append("  xᵢ - остатки по модулю mᵢ")
    details.append("  Mᵢ = M / mᵢ")
    details.append("  yᵢ - обратный к Mᵢ по модулю mᵢ")
    details.append("")

    # Показываем остатки результата
    details.append("Остатки результата:")
    for i, m in enumerate(moduli):
        residue = int(result_crt.residues[i].show())
        details.append(f"  x{i + 1} = {residue} (по модулю {int(m.show())})")

    details.append("")
    details.append(f"Результат преобразования: {result_val}")
    details.append("=" * 50)
    details.append("ВЫЧИСЛЕНИЕ ЗАВЕРШЕНО!")
    details.append("=" * 50)

    # Возвращаем результат и детали
    return result_int, "\n".join(details)