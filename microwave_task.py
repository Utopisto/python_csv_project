import time

class Microwave:
    def __init__(self, power: int, initial_time: int):
        self.power = power
        self.time_set = initial_time
        self.time_remaining = initial_time
        self.is_running = False
        self.door_open = False

    def set_time(self, seconds: int):
        self.time_set = seconds
        self.time_remaining = seconds
        print(f"время установлено: {self.time_set} сек.")

    def set_power(self, watts: int):
        self.power = watts
        print(f"мощность установлена: {self.power} Вт.")

    def start(self):
        if not self.door_open and not self.is_running and self.time_remaining > 0:
            self.is_running = True
            print("запущено")
        else:
            print("нельзя запустить")

    def stop(self):
        self.is_running = False
        print("остановлено")

    def open_door(self):
        self.door_open = True
        self.stop()
        print("дверь открыта")

    def close_door(self):
        self.door_open = False
        print("дверь закрыта")

    def status(self):
        status_str = "работает" if self.is_running else "остановлена"
        door_str = "открыта" if self.door_open else "закрыта"
        print("\n--- статус ---")
        print(f"мощность: {self.power} Вт")
        print(f"время: {self.time_set} сек.")
        print(f"состояние: {status_str}")
        print(f"дверь: {door_str}")
        print("--------------")

def get_integer_input(prompt: str):
    return int(input(prompt))

def task_microwave():
    print("--- настройка ---")
    initial_power = get_integer_input("мощность (Вт): ")
    initial_time = get_integer_input("время (сек): ")

    my_microwave = Microwave(initial_power, initial_time)
    print("\nнастроено!")

    while True:
        my_microwave.status()
        print("\n--- действия ---")
        print("1. время")
        print("2. мощность")
        print("3. старт")
        print("4. стоп")
        print("5. открыть")
        print("6. закрыть")
        print("7. назад")

        choice = input("выбери: ")

        if choice == '1':
            new_time = get_integer_input("новое время (сек): ")
            my_microwave.set_time(new_time)
        elif choice == '2':
            new_power = get_integer_input("новая мощность (Вт): ")
            my_microwave.set_power(new_power)
        elif choice == '3':
            my_microwave.start()
        elif choice == '4':
            my_microwave.stop()
        elif choice == '5':
            my_microwave.open_door()
        elif choice == '6':
            my_microwave.close_door()
        elif choice == '7':
            break
        else:
            print("неверно.")

if __name__ == "__main__":
    task_microwave() 