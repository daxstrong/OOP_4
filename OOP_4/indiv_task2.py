from abc import ABC, abstractmethod

class Integer(ABC):
    def __init__(self, digits):
        """Initialize with a list of digits."""
        self.digits = digits

    @abstractmethod
    def add(self, other):
        """Add another Integer and return a new Integer."""
        pass

    @abstractmethod
    def subtract(self, other):
        """Subtract another Integer and return a new Integer."""
        pass

    @abstractmethod
    def display(self):
        """Display the number."""
        pass

class Decimal(Integer):
    def __init__(self, digits):
        super().__init__(digits)

    def to_int(self):
        """Convert digit list to integer."""
        return int(''.join(map(str, self.digits)))

    @classmethod
    def from_int(cls, number):
        """Create Decimal from integer."""
        return cls([int(d) for d in str(number)])

    def add(self, other):
        if not isinstance(other, Decimal):
            raise TypeError("Can only add Decimal with Decimal")
        result = self.to_int() + other.to_int()
        return Decimal.from_int(result)

    def subtract(self, other):
        if not isinstance(other, Decimal):
            raise TypeError("Can only subtract Decimal with Decimal")
        result = self.to_int() - other.to_int()
        if result < 0:
            raise ValueError("Result cannot be negative in Decimal")
        return Decimal.from_int(result)

    def display(self):
        """Display the decimal number."""
        print(''.join(map(str, self.digits)))

class Binary(Integer):
    def __init__(self, digits):
        super().__init__(digits)

    def to_int(self):
        """Convert binary digit list to integer."""
        return int(''.join(map(str, self.digits)), 2)

    @classmethod
    def from_int(cls, number):
        """Create Binary from integer."""
        binary_str = bin(number)[2:]  # Remove '0b' prefix
        return cls([int(d) for d in binary_str])

    def add(self, other):
        if not isinstance(other, Binary):
            raise TypeError("Can only add Binary with Binary")
        result = self.to_int() + other.to_int()
        return Binary.from_int(result)

    def subtract(self, other):
        if not isinstance(other, Binary):
            raise TypeError("Can only subtract Binary with Binary")
        result = self.to_int() - other.to_int()
        if result < 0:
            raise ValueError("Result cannot be negative in Binary")
        return Binary.from_int(result)

    def display(self):
        """Display the binary number."""
        print(''.join(map(str, self.digits)))

if __name__ == "__main__":
    # Создаем два десятичных числа
    dec1 = Decimal([1, 2, 3])  # 123
    dec2 = Decimal([4, 5, 6])  # 456

    # Добавляем десятичные числа
    dec_sum = dec1.add(dec2)
    print("Decimal Sum:")
    dec_sum.display()  # Ожидается 579

    # Вычитаем десятичные числа
    dec_diff = dec2.subtract(dec1)
    print("Decimal Difference:")
    dec_diff.display()  # Ожидается 333

    # Создаем два двоичных числа
    bin1 = Binary([1, 0, 1, 1])  # 11 в десятичной
    bin2 = Binary([1, 1, 0, 1])  # 13 в десятичной

    # Добавляем двоичные числа
    bin_sum = bin1.add(bin2)
    print("Binary Sum:")
    bin_sum.display()  # Ожидается 11000 (24 в десятичной)

    # Вычитаем двоичные числа
    bin_diff = bin2.subtract(bin1)
    print("Binary Difference:")
    bin_diff.display()  # Ожидается 10 (2 в десятичной)