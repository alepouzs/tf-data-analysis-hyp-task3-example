import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu

chat_id = 487382438 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: 
    stat, p_value = mannwhitneyu(x, y, alternative = 'smaller')

    return p_value < 0.06
