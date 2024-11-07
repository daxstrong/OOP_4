import math


class Number:
    """Класс-оболочка для числового типа float."""

    def __init__(self, value):
        """Инициализация с приведением к типу float."""
        self.value = float(value)

    def __add__(self, other):
        """Метод сложения. Принимает другой объект Number или число."""
        if isinstance(other, Number):
            return Number(self.value + other.value)
        else:
            return Number(self.value + float(other))

    def __truediv__(self, other):
        """Метод деления. Принимает другой объект Number или число."""
        if isinstance(other, Number):
            if other.value == 0:
                raise ZeroDivisionError("Деление на ноль.")
            return Number(self.value / other.value)
        else:
            if float(other) == 0:
                raise ZeroDivisionError("Деление на ноль.")
            return Number(self.value / float(other))

    def __repr__(self):
        """Представление объекта для вывода."""
        return f"Number({self.value})"


class Real(Number):
    """Производный класс от Number с дополнительными методами."""

    def power(self, exponent):
        """Метод возведения числа в произвольную степень."""
        return Real(self.value ** exponent)

    def logarithm(self, base=math.e):
        """Метод вычисления логарифма числа по заданному основанию."""
        if self.value <= 0:
            raise ValueError("Логарифм не определен для неположительных чисел.")
        return Real(math.log(self.value, base))

    def __repr__(self):
        """Представление объекта для вывода."""
        return f"Real({self.value})"


if __name__ == '__main__':
    # Создание объектов класса Number
    num1 = Number(10.5)
    num2 = Number(2.5)

    # Демонстрация сложения
    sum_result = num1 + num2
    print(f"{num1} + {num2} = {sum_result}")

    # Демонстрация деления
    div_result = num1 / num2
    print(f"{num1} / {num2} = {div_result}")

    # Создание объекта класса Real
    real_num = Real(16.0)

    # Демонстрация возведения в степень
    power_result = real_num.power(0.5)
    print(f"{real_num} в степени 0.5 = {power_result}")

    # Демонстрация вычисления логарифма
    log_result = real_num.logarithm(math.sqrt(16))  # Логарифм по основанию 4
    print(f"Логарифм {real_num} по основанию 4 = {log_result}")