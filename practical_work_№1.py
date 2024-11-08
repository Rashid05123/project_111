# Текстовая игра: Побег из замка
# Цель игры: Пройти три уровня, взаимодействуя с различными предметами и решая головоломки

# Словарь с описаниями предметов, доступных в игре
items = {
    "ключ": "старый ржавый ключ, который может открыть дверь",
    "меч": "острый меч, способный поразить монстра",
    "шкатулка": "загадочная шкатулка с секретным кодом"
}

# Инвентарь игрока, где хранятся собранные предметы
inventory = []

# Множество для уникальных объектов (например, открытые двери)
opened_doors = set()

# Словарь с заданиями на каждом уровне
levels = {
    1: {"цель": "Найти ключ и открыть дверь", "предметы": ["ключ"], "дверь": "закрытая"},
    2: {"цель": "Победить монстра с помощью меча", "монстр": True, "предметы": ["меч"]},
    3: {"цель": "Разгадать код шкатулки", "загадка": "Какой предмет нужен для открытия?", "ответ": "ключ"}
}

# Функция для показа инвентаря игрока
def show_inventory():
    if inventory:
        print("Ваш инвентарь содержит:", ", ".join(inventory))
    else:
        print("Ваш инвентарь пуст.")

# Функция для обработки ввода игрока и выполнения действий
def process_input(command):
    match command.lower():
        case "инвентарь":
            show_inventory()
        case "осмотреть":
            print(f"Вы видите рядом {items.get('ключ')} и {items.get('меч')}.")
        case "взять ключ":
            if "ключ" not in inventory:
                inventory.append("ключ")
                print("Вы взяли ключ.")
            else:
                print("У вас уже есть ключ.")
        case "взять меч":
            if "меч" not in inventory:
                inventory.append("меч")
                print("Вы взяли меч.")
            else:
                print("У вас уже есть меч.")
        case "открыть дверь":
            if "ключ" in inventory and levels[1]["дверь"] == "закрытая":
                levels[1]["дверь"] = "открытая"
                opened_doors.add("первая дверь")
                print("Вы открыли первую дверь и прошли дальше.")
            else:
                print("Дверь закрыта. Нужен ключ.")
        case "атаковать монстра":
            if "меч" in inventory and levels[2]["монстр"]:
                levels[2]["монстр"] = False
                print("Вы победили монстра и прошли дальше!")
            else:
                print("У вас нет подходящего оружия для атаки.")
        case "открыть шкатулку":
            if "ключ" in inventory:
                print("Вы использовали ключ и открыли шкатулку! Победа!")
                exit()
            else:
                print("Нужен ключ для открытия шкатулки.")
        case _:
            print("Неизвестная команда. Попробуйте ещё раз.")

# Функция для первого уровня
def level_one():
    print("\n=== Уровень 1 ===")
    print("Описание:", levels[1]["цель"])
    while levels[1]["дверь"] == "закрытая":
        command = input("Ваше действие: ")
        process_input(command)
    print("Вы успешно прошли первый уровень!\n")

# Функция для второго уровня
def level_two():
    print("\n=== Уровень 2 ===")
    print("Описание:", levels[2]["цель"])
    while levels[2]["монстр"]:
        command = input("Ваше действие: ")
        process_input(command)
    print("Вы успешно прошли второй уровень!\n")

# Функция для третьего уровня
def level_three():
    print("\n=== Уровень 3 ===")
    print("Описание:", levels[3]["цель"])
    while True:
        command = input("Ваше действие: ")
        if command.lower() == "открыть шкатулку":
            answer = input(levels[3]["загадка"] + " ")
            if answer.lower() == levels[3]["ответ"]:
                process_input(command)
                break
            else:
                print("Неверный ответ. Попробуйте ещё раз.")
        else:
            process_input(command)

# Вспомогательная функция для проверки уровня
def check_level(level):
    print(f"Проверка уровня {level}. Цель: {levels[level]['цель']}")
    # Основная функция игры
def play_game():
    print("Добро пожаловать в игру! Ваша задача — выбраться из замка, пройдя три уровня.")
    print("Советы по командам: введите 'инвентарь' для проверки инвентаря, 'осмотреть' для осмотра окружающей среды.")
    
    check_level(1)
    level_one()
    
    check_level(2)
    level_two()
    
    check_level(3)
    level_three()
    
    print("Поздравляем! Вы выбрались из замка и победили в игре.")

# Запуск игры
play_game()
#Заключение