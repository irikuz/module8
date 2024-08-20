def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for num in numbers:
        try:
            result += num
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {num}')

    return result, incorrect_data
def calculate_average(numbers):
    try:
        sum_, incorrect_data = personal_sum(numbers)
        if sum_:
            return sum_ / len(numbers) - incorrect_data # Вычисляем среднее арифметическое
        else:
            return 0  # Если numbers пуста, возвращаем 0
    except ZeroDivisionError:
        return 0  # Обрабатываем исключение при делении на 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None  # Возвращаем None, если в numbers не коллекция или другой некорректный тип данных




print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
