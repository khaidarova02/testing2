﻿"""
 Анализ данных

 (C) 2023 Alisa Haidarova, PetrGU, Petrozavodsk, Russia
 License: GNU General Public License (GPL)
 Email: i.nesy.chav@gmail.com
"""

import sympy as sp
import numpy as np


def calculate_statistics(arr: np.ndarray):
    """
    Возвращает статистические показатели для данных
    (размер, сумма, среднее, медиана, минимум, максимум,
    дисперсия, стандартное отклонение).

    Параметры
    ----------
    arr : np.ndarray
        одномерный массив элементов числового типа

    Возвращает
    ----------
    statistics_dict : dictinary
        словарь со статистическими показателями
    """
    statistics_dict = {
        "count": arr.size,
        "sum": arr.sum(),
        "mean": np.mean(arr),
        "median": np.median(arr),
        "min": arr.min(),
        "max": arr.max(),
        "variance": arr.var(),
        "standard_deviation": arr.std()
    }
    return statistics_dict


def get_partition(arr: np.ndarray, count_inter: int):
    """
    Разбивает выборку

    Параметры
    ----------
    arr : np.ndarray
        одномерный массив элементов числового типа
    count_inter : int
        количество интервалов для разбиения

    Возвращает
    ----------
     : list
        список со списками номеров интервала и значениями частот
    """
    hist, _ = np.histogram(arr, count_inter)
    frequency = [h / arr.size for h in hist]
    return [list(range(count_inter)), frequency]


def number_generation(average: float, var: float, size: int):
    """
    Генерирует числа для сравнения исходной выборки,
    подчиненные нормальному, экспоненциальному и
    гамма распределениям

    Параметры
    ----------
    average : float
        среднее выборочной исходной выборки
    var : float
        дисперсия исходной выборки
    size : int
        размер исходной выборки

    Возвращает
    ----------
    norm_numbers : np.array
        массив нормально распределенных значений
    exp_numbers : np.array
        массив экспоненциально распределенных значений
    gamma_numbers : np.array
        массив гамма распределенных значений
    """

    def decide_system():
        x, y = sp.symbols('x y')
        eq1 = x * y - average
        eq2 = x * y**2 - var
        sol = sp.solve([eq1, eq2], [x, y])[0]
        return sol[0], sol[1]

    np.random.seed(12)

    norm_numbers = np.random.normal(average, np.sqrt(var), size)
    exp_numbers = np.random.exponential(average, size)

    alpha, beta = decide_system()
    gamma_numbers = np.random.gamma(alpha, beta, size)

    return norm_numbers, exp_numbers, gamma_numbers