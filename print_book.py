"""Печать книги"""
import math


name_book = input("Введите название книги: ").replace(" ", "_").lower()
# создание и открытие файла
file = open(f"./result/{name_book}.txt", "w", encoding="utf-8")


def computation(amount_notebook: int, notebook_sheets: int, number_notebook=1, last_page_notebook=None):
    # проверка передачи номера последней страницы
    check = 0
    if last_page_notebook is None:
        check = 1

    while number_notebook <= amount_notebook:
        if check:
            # последняя страница тетрадки
            last_page_notebook = (notebook_sheets * 4) * number_notebook

        # первая страница тетрадки
        first_page_notebook = last_page_notebook - (notebook_sheets * 4) + 1

        # список номеров строниц для первой стороны печати
        first_print = []
        # список номеров строниц для второй стороны печати
        second_print = []

        # номер листа тетради
        number_list_notebook = 1
        while number_list_notebook <= notebook_sheets:
            first_print.append (last_page_notebook)
            second_print.append (first_page_notebook + 1)
            first_print.append (first_page_notebook)
            second_print.append (last_page_notebook - 1)
            last_page_notebook -= 2
            first_page_notebook += 2
            number_list_notebook += 1

        file.write(f"\nДля печати тетрадки номер {number_notebook} необходимо так печатать страницы:\n")
        file.write(f"Первая сторона печати:\n{first_print}\n")
        file.write(f"Вторая сторона печати:\n{second_print}\n")
        number_notebook += 1


def data_input():
    # количество страниц книги
    pages = int(input("Введите количество страниц книги: "))
    amount_lists = math.ceil(pages / 4)
    file.write(f"В книге {pages} страниц\n")

    if pages != amount_lists * 4:
        file.write(f"Для коректной печати - добавте в конец книги {amount_lists*4 - pages} пустых стр.\n")

    file.write(f"{'-'*70}\n")

    # количество листов тетради
    notebook_sheets = int(input("Введите желаемое количество листов одной тетради: "))

    # количество тетрадей в книге
    amount_notebook = amount_lists // notebook_sheets
    computation(amount_notebook, notebook_sheets)

    if amount_notebook != amount_lists / notebook_sheets:
        temp_notebook_sheets = amount_lists - notebook_sheets * amount_notebook
        computation(amount_notebook+1, temp_notebook_sheets, amount_notebook+1, amount_lists*4)


data_input()
file.close()
print("Готово")
