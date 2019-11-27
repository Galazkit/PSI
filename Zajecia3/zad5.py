class Calculator:
    @staticmethod
    def add(liczba1, liczba2):
        return liczba1 + liczba2

    @staticmethod
    def difference(liczba1, liczba2):
        return liczba1 - liczba2

    @staticmethod
    def multiply(liczba1, liczba2):
        return liczba1 * liczba2

    @staticmethod
    def divide(liczba1, liczba2):
        if liczba2 != 0:
            return liczba1 / liczba2
        return "Dividing by zero is forbidden!"

print(Calculator.add(12, 4))
print(Calculator.difference(2, 6))
print(Calculator.multiply(7, -2))
print(Calculator.divide(12, 5))