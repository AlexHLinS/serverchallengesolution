from math import exp
import numpy as np
import pandas as pd

# Функции вычисления нормированного скора в зависимости от параметров компании, результат от 0 до 1
def calc_lifetime_coef(years):
    return 1/(1+3*exp(3-years))    
def calc_staff_coef(staff):
    return 1/(1+20*exp(-staff/20))
def calc_capital_score(capital):
    return 1/(1+1000*exp(-4-capital/500000))

# Результаирующий скор с вкладом каждой из функций
def calc_rule_based_score_df(df):
    """
    Input pandas table should contain columns 'lifetime', 'staff', 'capital'
    """
    res = df.copy()
    res['rb_score'] = res['lifetime'].apply(lambda x: calc_lifetime_coef(x) * 0.2) + \
        res['staff'].apply(lambda x : calc_staff_coef(x) * 0.4) + \
        res['capital'].apply(lambda x : calc_capital_score(x) * 0.4)
    return res
