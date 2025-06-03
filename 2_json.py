import csv
import json
from typing import List, Dict, Any
import sys 

def save_data_to_csv(data: List[Dict[str, Any]], filename: str):
    if not data:
        print(f"входные данные для сохранения в '{filename}' пусты")
        return

    fieldnames = data[0].keys()

    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader() 
            for row in data:
                processed_row = {k: (", ".join(map(str, v)) if isinstance(v, list) else v) for k, v in row.items()}
                writer.writerow(processed_row) 

        print(f"данные успешно сохранены в файл '{filename}'")

    except IOError as e:
        print(f"ошибка ввода/вывода при работе с файлом {filename}: {e}")
    except Exception as e:
        print(f"произошла непредвиденная ошибка при сохранении в {filename}: {e}")

def load_data_from_json(filename: str) -> List[Dict[str, Any]]:
    try:
        with open(filename, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            print(f"данные успешно загружены из файла '{filename}'")
            return data
    except FileNotFoundError:
        print(f"ошибка: Файл '{filename}' не найден.")
        return []
    except json.JSONDecodeError:
        print(f"не удалось декодировать JSON из файла '{filename}'")
        return []
    except Exception as e:
        print(f"произошла ошибка при чтении JSON файла '{filename}': {e}")
        return []

def display_menu():
    print("\n--- меню ---")
    print("1. сохранить данные сотрудников из employees.json в CSV")
    print("0. выход из программы")
    print("------------")

def main():
    employees_data = [] 

    while True:
        display_menu()
        choice = input("выберите действие: ")

        if choice == '1':
            print("выбрано: сохранить данные в CSV")
            json_file_path = "employees.json"
            csv_file_path = "employees.csv"
            
            employees_data = load_data_from_json(json_file_path) 
            
            if employees_data: 
                 save_data_to_csv(employees_data, csv_file_path)
            else:
                 print("нет данных для сохранения")

        elif choice == '0':
            print("выход из программы")
            sys.exit() 

        else:
            print("неверный ввод. выберите действие из меню")

if __name__ == "__main__":
    main()

    print("\nпробуем сохранить пустые данные:")
    empty_data = []
    save_data_to_csv(empty_data, "empty_file.csv")

    print("\nпробуем сохранить некорректные данные:")
    incorrect_data = ["строка1", "строка2"]