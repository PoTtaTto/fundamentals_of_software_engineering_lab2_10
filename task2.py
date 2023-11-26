# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def harmonic_mean(*args):
    """
    Вычисляет среднее гармоническое своих аргументов.

    Args:
    - *args (float): Аргументы для вычисления среднего гармонического.

    Returns:
    - float or None: Среднее гармоническое аргументов или None, если список аргументов пуст.
    """
    if not args:  # Проверка на пустой список аргументов
        return None

    reciprocal_sum = sum(1 / num for num in args)
    mean = len(args) / reciprocal_sum
    return mean


if __name__ == '__main__':
    print(harmonic_mean(1, 2, 3, 4, 5))
