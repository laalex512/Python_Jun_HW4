import Client
from Operation import Operation


class Cash_Machine:
    def __init__(self):
        self.client: Client
        self.power_on = False

    def start_machine(self, client):
        self.power_on = True
        self.client = client

    def cash_in(self, value) -> str:
        if self.power_on:
            operation = Operation(self.client.get_balance(), "in", value, self.client.count_operations())
            self.client.add_operation(operation)
            self.client.set_balance(operation.balance)
            return str(operation)
        else:
            return "Банкомат выключен. Введите 'start' "

    def cash_out(self, value):
        if self.power_on:
            operation = Operation(self.client.get_balance(), "out", value, self.client.count_operations())
            self.client.add_operation(operation)
            return str(operation)
        else:
            return "Банкомат выключен. Введите 'start' "

    def stop(self):
        self.power_on = False
        self.client = None
