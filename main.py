"""Консольный запуск заданий лабораторной работы № 2."""

import argparse

from lab2.algorithms import (
    count_vowels,
    gcd_basic,
    gcd_euclid,
    sum_odd_numbers,
)


def show_demo() -> None:
    """Вывести воспроизводимые примеры всех вычислительных заданий."""
    print(f"Sum of odd numbers through 10: {sum_odd_numbers(10)}")
    print(f"GCD by divisors (48, 18): {gcd_basic(48, 18)}")
    print(f"GCD by Euclid (48, 18): {gcd_euclid(48, 18)}")
    print(f"Vowels in 'Hello, Python!': {count_vowels('Hello, Python!')}")
    print(f"Vowels in 'Привет, мир!': {count_vowels('Привет, мир!')}")


def main() -> None:
    """Прочитать аргументы и вызвать функции импортированного модуля."""
    parser = argparse.ArgumentParser(description="Lab 2, variant 2")
    commands = parser.add_subparsers(dest="command")
    odd = commands.add_parser("sum", help="Sum odd numbers through N")
    odd.add_argument("n", type=int)
    for name in ("gcd", "euclid"):
        gcd = commands.add_parser(name, help="Greatest common divisor")
        gcd.add_argument("a", type=int)
        gcd.add_argument("b", type=int)
    vowels = commands.add_parser("vowels", help="Count Russian/English vowels")
    vowels.add_argument("text")
    args = parser.parse_args()
    try:
        if args.command == "sum":
            print(sum_odd_numbers(args.n))
        elif args.command == "gcd":
            print(gcd_basic(args.a, args.b))
        elif args.command == "euclid":
            print(gcd_euclid(args.a, args.b))
        elif args.command == "vowels":
            print(count_vowels(args.text))
        else:
            show_demo()
    except (TypeError, ValueError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
