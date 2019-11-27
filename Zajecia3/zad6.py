import zad5
class ScienceCalculator(zad5.Calculator):
    @staticmethod
    def power(liczba1, liczba2):
        return liczba1 ** liczba2

    @staticmethod
    def modulo(liczba1, liczba2):
        return liczba1 % liczba2

print("\nPo dziedziczeniu ")
print(ScienceCalculator.multiply(2, -6))
print(ScienceCalculator.power(6, 2))
print(ScienceCalculator.modulo(16, 7))