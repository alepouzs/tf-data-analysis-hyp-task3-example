import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest

chat_id = 487382438 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool: 
    stat, p_value = ztest(x, value = 300, alternative = 's')

    return p_value < 0.06
