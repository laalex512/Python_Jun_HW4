from datetime import datetime

import keys


class Operation:
    date_time: datetime
    balance: float
    message = ""

    def __init__(self, balance: float, type: str, value: float, count_operations: int):
        self.balance = balance
        self.date_time = datetime.now()
        """Проверка на богатство:"""
        self.minus_luxurie()
        """Проверка на кратность:"""
        if not value % keys.MULTIPLE == 0:
            self.message += f"Ошибка, не кратно {keys.MULTIPLE} ye."
        else:
            """Проверка на кешбэк"""
            self.is_cashback(count_operations)
            """Проверка типа операции и вызов соответствующего метода"""
            match type:
                case "in":
                    self.cash_in(value)
                case "out":
                    self.cash_out(value)

    """Проверка на богатство:"""

    def minus_luxurie(self):
        if self.balance > keys.MAX_LUXURIES:
            tax_luxurie = self.balance * keys.TAX_LUXURIES
            self.balance -= tax_luxurie
            self.message += f"Снят налог на богатство {tax_luxurie} ye. "

    """Проверка на кешбэк"""

    def is_cashback(self, count_operations):
        if count_operations > 0 and count_operations % keys.OPERATIONS_FOR_CASHBACK == 0:
            cash_back = self.balance * keys.CASHBACK
            self.balance += cash_back
            self.message += f"Кешбэк + {cash_back}. "

    def cash_in(self, value):
        self.message += f"Пополнение на {value} ye. "
        self.balance += value

    def cash_out(self, value):
        """Проверка на наличие снимаемых средств:"""
        if value > self.balance:
            self.message += f"Ошибка, недостаточно средств. "
        else:
            tax = value * keys.COMMISSION
            if tax < keys.COMMISSION_MIN:
                tax = keys.COMMISSION_MIN
            elif tax > keys.COMMISSION_MAX:
                tax = keys.COMMISSION_MAX
            self.message += f"Снятие {value} ye. Коммиссия за снятие: {tax}. "
            self.balance -= (value + tax)

    def __str__(self):
        return f"{self.date_time}: {self.message}Остаток: {self.balance}"
