#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def geometric_mean(*args):
    """
    Вычисляет среднее геометрическое своих аргументов.

    Args:
    - *args (float): Аргументы для вычисления среднего геометрического.

    Returns:
    - float: Среднее геометрическое аргументов.
    """
    if not args:
        return None

    product = 1
    count = 0

    # Умножаем все аргументы между собой
    for num in args:
        product *= num
        count += 1

    # Возводим произведение в степень, обратную количеству аргументов
    mean = product ** (1 / count)
    return mean


if __name__ == '__main__':
    print(geometric_mean(12, 12, 12, 32, 10, 123))
