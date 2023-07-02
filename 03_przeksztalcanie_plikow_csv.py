"""
Skrypt opracowany dla przekształcania bazy pacjetów przychodni przez wyrównanie ilości kolumn po nazwie każdego leku
Program po kolei pobiera pliki CSV z folderu, przekształca je, zmieniając nazwy kolumn i dodając brakujące. Zmodyfikowany dataset z powrotem zapisywany do pliku CSV
"""

import glob
import os

import pandas as pd


INSERT_COLUMNS = 6  # ilość kolumn do wstawiania po nazwie każdego leku
PATH_OLD = r'06_data\csv_old\*.*'
PATH_NEW = r'06_data\csv_new'

os.system('cls')
filename_list = glob.glob(PATH_OLD)
count_of_df_columns = 9 + 19 * (INSERT_COLUMNS + 1)  # wzór na wyliczenie ogólnej ilości kolumn w każdym pliku CSV

for file in filename_list:
    df = pd.read_csv(file, delimiter='\t', encoding='1250')
    unnamed_count = 0

    for i in range(count_of_df_columns - 1):
        if df.columns[i].find('Unnamed:') == 0:
            unnamed_count += 1
            df = df.rename(columns={df.columns[i]: df.columns[i - unnamed_count] + ' ' + str(unnamed_count)})
            count_of_insert = INSERT_COLUMNS - unnamed_count
            
            if i == len(df.columns) - 1:  # czynności z dodawania brakujących kolumn w przypadku znalezienia się na końcu datasetu
                for j in range(1, count_of_insert + 1):
                    df.insert(i + j, df.columns[i - unnamed_count] + ' ' + str(unnamed_count + j), None)
                
            else:  # dodawanie brakujących kolumn w przypadku kolumny ze środku datasetu
                if df.columns[i + 1].find('Unnamed:') != 0:
                    for j in range(1, count_of_insert + 1):
                        df.insert(i + j, df.columns[i - unnamed_count] + ' ' + str(unnamed_count + j), None)

        else:
            unnamed_count = 0
    
    new_csv_name = file.split('\\')[2]  # nazwa przekształcenego pliku
    df.to_csv(f'{PATH_NEW}\{new_csv_name}', index=False, sep=';', encoding='utf-8')
    print(f'\nPlik {new_csv_name} zapisano!\n')

print('Edycja plików zakończona.')
