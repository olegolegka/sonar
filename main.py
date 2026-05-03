import time

food = 10
mood = 100
energy = 100
leaved = True
print("Добро пожаловать в Тамагочи")
print("Это твой питомец")
name = input("Введите имя для питомца: ")
last_time = time.time()

while leaved == True:
    current_time = time.time()
    if current_time - last_time >= 60:
        minutes = (current_time - last_time) // 60
        print("Прошло",minutes,"минут, питомец проголодался и устал")
        food += 10*minutes
        mood -= 10*minutes
        energy -= 15*minutes
        last_time = current_time
    print("Состояние питомца:")
    print("Голод:",food)
    print("Настроение:",mood)
    print("Энергия:",energy)
    print("\\n--- Меню ---")
    print("1. Покормить (+30 сытости, +10 настроения)")
    print("2. Поиграть (+20 настроения, -20 энергии)")
    print("3. Уложить спать (Энергия +100, Голод +10)")
    print("4. Проверить состояние")
    choice = input("Выбери действие (1-4): ")
    if choice == "1":
        print("Ты покормил питомца")
        food = max(0,food - 30)
        mood = min(100,mood + 10)
    elif choice == "2":
        if energy > 0:
            print("Вы поиграли с питомцем")
            mood = min(100,mood+20)
            energy = max(0,energy - 20)
        else:
            print("Питомец слишком устал для игр")
    elif choice == "3":
        print("Питомец поспал")
        energy  = 100
        food = max(0,food + 10)
    elif choice == "4":
        print("Состояние питомца:")
        print("Голод:",food)
        print("Настроение:",mood)
        print("Энергия:",energy)
    else:
        print("Такого действия нет")
    if mood <= 0 or food >= 100:
        print("Питомец сбежал")
        leaved = False
        time.sleep(2)
print("Спасибо за игру")
