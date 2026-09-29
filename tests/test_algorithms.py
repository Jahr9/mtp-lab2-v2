"""Контрольные, граничные и сравнительные проверки алгоритмов."""

import math
import unittest

from lab2.algorithms import (
    count_vowels,
    gcd_basic,
    gcd_euclid,
    sum_odd_numbers,
)


class OddSumTests(unittest.TestCase):
    def test_even_boundary(self):
        self.assertEqual(sum_odd_numbers(10), 25)

    def test_odd_boundary_is_included(self):
        self.assertEqual(sum_odd_numbers(9), 25)

    def test_zero_and_one(self):
        self.assertEqual(sum_odd_numbers(0), 0)
        self.assertEqual(sum_odd_numbers(1), 1)

    def test_negative_rejected(self):
        with self.assertRaises(ValueError):
            sum_odd_numbers(-1)

    def test_non_integer_rejected(self):
        for value in (1.5, "10", True, None):
            with self.subTest(value=value), self.assertRaises(TypeError):
                sum_odd_numbers(value)

    def test_against_closed_form(self):
        for n in range(101):
            with self.subTest(n=n):
                self.assertEqual(sum_odd_numbers(n), ((n + 1) // 2) ** 2)


class GcdTests(unittest.TestCase):
    def test_regular_inputs(self):
        for function in (gcd_basic, gcd_euclid):
            self.assertEqual(function(48, 18), 6)
            self.assertEqual(function(17, 13), 1)
            self.assertEqual(function(12, 12), 12)

    def test_signs_and_zeros(self):
        cases = [(-48, 18, 6), (-48, -18, 6), (0, 7, 7),
                 (7, 0, 7), (0, 0, 0)]
        for function in (gcd_basic, gcd_euclid):
            for a, b, result in cases:
                with self.subTest(function=function.__name__, a=a, b=b):
                    self.assertEqual(function(a, b), result)

    def test_non_integers_rejected(self):
        for function in (gcd_basic, gcd_euclid):
            for value in (1.5, "2", True, None):
                with self.subTest(function=function.__name__, value=value):
                    with self.assertRaises(TypeError):
                        function(value, 6)
                    with self.assertRaises(TypeError):
                        function(6, value)

    def test_both_algorithms_against_standard_library(self):
        for a in range(-30, 31):
            for b in range(-30, 31):
                with self.subTest(a=a, b=b):
                    expected = math.gcd(a, b)
                    self.assertEqual(gcd_basic(a, b), expected)
                    self.assertEqual(gcd_euclid(a, b), expected)

    def test_euclid_large_consecutive_fibonacci(self):
        self.assertEqual(gcd_euclid(832040, 514229), 1)


class VowelTests(unittest.TestCase):
    def test_russian(self):
        self.assertEqual(count_vowels("Привет, мир!"), 3)

    def test_english(self):
        self.assertEqual(count_vowels("Hello, Python!"), 3)

    def test_uppercase_and_yo(self):
        self.assertEqual(count_vowels("АЕЁИОУЫЭЮЯ AEIOU"), 15)

    def test_empty_and_non_vowels(self):
        self.assertEqual(count_vowels(""), 0)
        self.assertEqual(count_vowels("123! бвг yY"), 0)

    def test_repeated_vowels(self):
        self.assertEqual(count_vowels("аааЕЕ"), 5)

    def test_non_string_rejected(self):
        with self.assertRaises(TypeError):
            count_vowels(123)


if __name__ == "__main__":
    unittest.main()
