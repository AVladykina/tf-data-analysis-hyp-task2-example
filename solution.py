import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

chat_id = 433242632 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    ks_stat, p_value = ks_2samp(x, y)
    alpha = 0.04
    n = len(x)
    crit_value = 1.36 / np.sqrt(n)

    return ks_stat > crit_value
    
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    # Ваш ответ, True или False
