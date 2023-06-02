from Cash_machine import Cash_Machine
from Client import Client


def start():
    clients = [Client("Ivan Ivanov"), Client("Petr Petrov"), Client("Fedor Fedorov")]
    c_machine = Cash_Machine()
    while True:
        input_message = input("Введите команду(help - список команд):")
        match input_message:
            case "help":
                print(f"start - включение банкомата \n stop - выключение банкомата \n "
                      f"in - внести средства \n out - снять средства \n q - выход")
            case "start":
                print("Выберите клиента:")
                for i, client in enumerate(clients, start=1):
                    print(f"{i} - {client.get_name()}")
                id_client = int(input())
                c_machine.start_machine(clients[id_client - 1])
            case "stop":
                c_machine.stop()
            case "in":
                value = float(input("Введите сумму для пополнения:"))
                print(c_machine.cash_in(value))
            case "out":
                value = float(input("Введите сумму для снятия:"))
                print(c_machine.cash_out(value))
            case "q":
                break

    for client in clients:
        client.print_history()
