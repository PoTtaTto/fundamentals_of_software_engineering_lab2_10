# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def sum_between_negatives(*args):
    """
    Находит сумму аргументов, расположенных между первым и вторым отрицательными аргументами.

    Args:
    - *args: Произвольное количество аргументов.

    Returns:
    - int or float or None: Сумма аргументов между первым и вторым отрицательными аргументами,
                            либо None, если нет двух отрицательных аргументов подряд.
    """
    first_negative_found = False
    sum_between = 0

    for arg in args:
        if arg < 0:
            if not first_negative_found:
                first_negative_found = True
                continue
            else:
                return sum_between  # Нашли второе отрицательное число, возвращаем сумму

        if first_negative_found:
            sum_between += arg

    return None  # Если нет двух отрицательных аргументов подряд, возвращаем None


if __name__ == '__main__':
    print(sum_between_negatives())