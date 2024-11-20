'''
Создать объект Series, содержащий список группы. 
В качестве индексов использовать номер в журнале старосты.
Индекс старосты задать 'Starosta'.
Вывести:
1) Список всех элементов
2) Каждый второй элемент списка
3) Набор индексов

Создать DataFrame со столбацами Name, IsStarosta,
Phone, Gender, YearBirth, внести 10 записей.
Столбец Age должен рассчитываться как разница текущего года и даты рождения.
Индексы должны содержать первые символы фамилии, имени и отчества в латинице
Вывести:
1) Первые 3 записи DataFrame
2) Столбец с именами
3) Столбцы имени, пола и возраста
4) Данные о старосте
5) Минимальный и максимальный возраст
6) Сводная таблица из количества девушек и юношей и их среднего возраста
7) Распределение студентов по возрасту
Добавить функцию Сохранения DataFrame в формате csv-файла.
Добавить функцию создания нового DataFrame на основе данных из csv-файла.
'''
import pandas as pd
from datetime import datetime

def seriesMenu(series):
    while True:
        print("1. Вывести всех студентов")
        print("2. Вывести каждого второго студента")
        print("3. Вывести индексы списка")
        print("4. Перейти на следующую страницу")
        print("5. Выйти из программы")
        choice = input()
        match choice:
            case "1":
                print(series)
            case "2":
                print(series.iloc[1::2])
            case "3":
                print(series.index)
            case "4":
                dataframe_menu(createDataFrame())
                break
            case "5":
                break
            case _:
                print("Input error. Please, try again.")

def dataframe_menu(df):
    while True:
        print("1. Вывести первые 3 записи")
        print("2. Вывести столбец с именами")
        print("3. Вывести столбцы: имя, пол, возраст")
        print("4. Вывести данные о старосте")
        print("5. Вывести минимальный и максимальный возраст")
        print("6. Вывести сводную таблицу (по полу и среднему возрасту)")
        print("7. Вывести распределение студентов по годам рождения")
        print("8. Сохранить таблицу в CSV файл")
        print("9. Загрузить таблицу из CSV файла")
        print("10. Предыдущая страница")
        print("11. Выйти из программы")
        choice = input()
        match choice:
            case "1":
                print(df.head(3))
            case "2":
                print(df["Name"])
            case "3":
                print(df[["Name", "Gender", "Age"]])
            case "4":
                print(df[df["IsStarosta"]])
            case "5":
                print("Минимальный возраст:", df["Age"].min())
                print("Максимальный возраст:", df["Age"].max())
            case "6":
                print("Количество студентов по полу:")
                print(df["Gender"].value_counts())
                print("\nСредний возраст по полу:")
                print(df.groupby("Gender")["Age"].mean())
            case "7":
                print(df["YearBirth"].value_counts())
            case "8":
                df.to_csv("studentsData.csv")
                print("Таблица сохранена в файл studentsData.csv")
            case "9":
                df = pd.read_csv("studentsData.csv", index_col=0)
                print("Таблица загружена из файла studentsData.csv")
            case "10":
                seriesMenu(createSeries())
                break
            case "11":
                break
            case _:
                print("Input error. Please, try again.")

def createSeries():
    namesList = [
        "Иванов", "Петров", "Сидоров", "Смирнов", "Кузнецов", "Попов", "Васильев", 
        "Фёдоров", "Михайлов", "Александров", "Соколов", "Лебедев", "Козлов", 
        "Новиков", "Морозов", "Захаров", "Зайцев", "Борисов", "Кириллов", 
        "Орлов", "Макаров", "Андреев", "Волков", "Коновалов", "Егоров"
    ]
    seriesData = {i+1: namesList[i] for i in range(25)}
    seriesData["starosta"] = seriesData.pop(13)
    return pd.Series(seriesData)

def createDataFrame():
    data = {
        "Name": ["Иванов И.И.", "Петров П.П.", "Сидоров С.С.", "Козлов К.К.", "Смирнова С.С.",
                "Михайлова М.М.", "Фёдорова Ф.Ф.", "Алексеева А.А.", "Воробьёв В.В.", "Григорьев Г.Г."],
        "IsStarosta": [False, False, False, True, False, False, False, False, False, False],
        "Phone": ["+79160000001", "+79160000002", "+79160000003", "+79160000004", "+79160000005",
                "+79160000006", "+79160000007", "+79160000008", "+79160000009", "+79160000010"],
        "Gender": ["M", "M", "M", "M", "F", "F", "F", "F", "M", "M"],
        "YearBirth": [2000, 2001, 1999, 2000, 2001, 2000, 1999, 2001, 2002, 2000]
    }
    df = pd.DataFrame(data)
    currentYear = datetime.now().year
    df["Age"] = currentYear - df["YearBirth"]
    df.index = [name.split()[0][0] + name.split()[1][0] + name.split()[1][1] for name in df["Name"]]
    return df

seriesMenu(createSeries())
