import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp
from hyppo.ksample import MMD

chat_id = 1117973953 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.02
    p_value = MMD(compute_kernel="laplacian", gamma=1).test(x, y)[1]
    return p_value < alpha
