import Operation


class Client:

    def __init__(self, name: str):
        self.name = name
        self.balance = 0
        self.operations = []

    def get_name(self):
        return self.name

    def get_balance(self):
        return self.balance

    def set_balance(self, new_balance):
        self.balance = new_balance

    def add_operation(self, operation: Operation):
        self.operations.append(operation)

    def count_operations(self):
        return len(self.operations)

    def print_history(self):
        print(f"Операции клиента {self.name}:")
        if self.count_operations() == 0:
            print("Операций пока не проводилось")
        for operation in self.operations:
            print(operation)
