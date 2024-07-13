while True:
    num1 = input("Введіть перше число: ")
    operator = input("Введіть оператор (+, -, *, /): ")
    num2 = input("Введіть друге число: ")

    if not num1.replace('.', '', 1).isdigit() or not num2.replace('.', '', 1).isdigit():
        print("Помилка: Введіть коректне число!")
        continue

    num1 = float(num1)
    num2 = float(num2)

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Помилка: Ділення на нуль!")
            continue
        result = num1 / num2
    else:
        print("Невідомий оператор!")
        continue

    print(f"Результат: {result}")

    choice = input("Бажаєте продовжити? (y/n): ").lower()
    if choice != 'y':
        break

print("Дякуємо за використання калькулятора!")