'''
Импортировать файл polit.csv и описать на его основе DataFrame
ctry - страна
fh09 - индекс Freedom House за 2009 год
polity09 - индекс polity2 за 2009 год
gini - индекс Джини за 2000-2010 года
fparl08 - доля женщин в парламенте в 2008 году
mena - регион Middle East and North Africa
lati - регион Latin America
cari - регион Caribbean, former British, French, Dutch colony
east - регион East Asia
sovi - регион Former Soviet Bloc
afri - регион Africa
corr0509 - индекс Control Corruption за 2005-2009 годы
Загрузить таблицу и создать датафрейм,
удалить строки с пропущенными значениями.
Сохранить изменения в файле polit.csv
Сохранить в NotFree страны с hf09 > 5.
Сохранить в afW страны afri с fparl08 > 30.
Сохранить в laDem страны afri и lati с Polity09 >= 8.
Добавить столбец CorrRound в котором значения corr0509 будут округлены до 2 знаков.
Добавить столбец statusFH в котором будут храниться типы стран в зависимости от значений fh09
Сгруппировать страны по столбах statusFH и вывести минимальное и максимальное
значение gini по каждой группе.
Записать разные группы statusFH в разные csv-файлы
'''

import pandas as pd
polit = pd.read_csv('polit.csv', delimiter=';', decimal=',', on_bad_lines='skip', encoding='utf-8')
polit.dropna(inplace=True)
notFree = polit[polit['fh09'] > 5]
afW = polit[(polit['afri'] == 1) & (polit['fparl08'] > 30)]
laDem = polit[((polit['afri'] == 1) | (polit['lati'] == 1)) & (polit['polity09'] >= 8)]
polit['corrRound'] = polit['corr0509'].round(2)
def determineStatusFH(fh09):
    if 7.0 >= fh09 >= 5.5:
        return "NotFree"
    elif 5.5 > fh09 > 2.5:
        return "PartlyFree"
    elif 2.5 >= fh09 >= 1.0:
        return "Free"
    return "Unknown"
def determineMin(series):
    min = series.iloc[0]
    for item in series:
        if item < min:
            min = item
    return min
polit['statusFH'] = polit['fh09'].apply(determineStatusFH)
giniStats = polit.groupby('statusFH')['gini'].agg([determineMin, 'max'])
print(notFree, "\n")
print(afW, "\n")
print(laDem, "\n")
print(giniStats)
for status, groupDF in polit.groupby('statusFH'):
    filename = f"{status.replace(' ', '_').lower()}Data.csv"
    groupDF.to_csv(filename, index=False)
    print(f"Сохранено в файл {filename}")
input()
