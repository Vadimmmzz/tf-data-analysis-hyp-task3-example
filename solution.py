import pandas as pd
import numpy as np


chat_id = 230865321 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    a = 0.01
    p = stats.mannwhitneyu(x, y).pvalue
    return p<a # Ваш ответ, True или False
