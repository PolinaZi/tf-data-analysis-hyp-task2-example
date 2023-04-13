import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp

chat_id = 1117973953 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.02
    p_value = anderson_ksamp([x, y]).pvalue 
    return p_value < alpha
