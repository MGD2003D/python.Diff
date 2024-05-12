"""
калькулятор
"""

def add(x_val, y_val):
    """
    Возвращает сумму x_val и y_val
    """
    return x_val + y_val


def subtract(x_val, y_val):
    """
    Возвращает разность
    """
    return x_val - y_val


def multiply(x_val, y_val):
    """
    Возвращает результат произведения
    """
    return x_val * y_val


def divide(x_val, y_val):
    """
    Возваращет результат деления или ошибку при делении на ноль
    """
    if y_val == 0:
        raise ValueError("ERROR")
    return x_val / y_val
