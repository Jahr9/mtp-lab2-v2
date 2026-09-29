"""Чистые функции для трёх средних и двух повышенных заданий."""

VOWELS = frozenset("аеёиоуыэюяaeiou")


def _require_integer(value: int, name: str) -> None:
    """Отклонить нецелый аргумент, включая логические значения."""
    if type(value) is not int:
        raise TypeError(f"{name} must be an integer")


def sum_odd_numbers(n: int) -> int:
    """Вернуть сумму положительных нечётных чисел от 1 до n включительно."""
    _require_integer(n, "n")
    if n < 0:
        raise ValueError("n must be non-negative")
    total = 0
    for number in range(1, n + 1, 2):
        total += number
    return total


def gcd_basic(a: int, b: int) -> int:
    """Найти неотрицательный НОД перебором делителей; НОД(0, 0) = 0."""
    _require_integer(a, "a")
    _require_integer(b, "b")
    a, b = abs(a), abs(b)
    if a == 0:
        return b
    if b == 0:
        return a
    divisor = min(a, b)
    while divisor > 0:
        if a % divisor == 0 and b % divisor == 0:
            return divisor
        divisor -= 1
    return 1


def gcd_euclid(a: int, b: int) -> int:
    """Найти НОД алгоритмом Евклида через остатки; НОД(0, 0) = 0."""
    _require_integer(a, "a")
    _require_integer(b, "b")
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def count_vowels(text: str) -> int:
    """Подсчитать русские и английские гласные без учёта регистра."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    count = 0
    for character in text.lower():
        if character in VOWELS:
            count += 1
    return count
