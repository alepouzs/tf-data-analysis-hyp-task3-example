import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 487382438 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: 
    stat, p_value = ttest_ind(x, y, alternative = 'less')

    return p_value < 0.06
