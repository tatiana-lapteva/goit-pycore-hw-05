
from typing import Callable
import re



def generator_numbers(text: str):
    """ extracts any . separated digits """
    pattern = r"\d+\.\d+"
    result = re.findall(pattern, text)
    for item in result:
        yield float(item)

   
def sum_profit(text: str, func: Callable):
    """ extract floats and count sum of them """
    sum_profit = 0
    for item in generator_numbers(text):
        sum_profit += item
    return sum_profit




text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

