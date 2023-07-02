"""
Program pobiera dane historyczne kursów walut (tabela A) z API NBP (Narodowy Bank Poski) - http://api.nbp.pl/
W jednym pobraniu można sciągnąć dane z okresu, który nie przekracza 93 dni (ograniczenie NBP)
Program pyta o datę początkową oraz końcową. Wynik jest zapisywany w pliku CSV
Przykładowy adres URL: https://api.nbp.pl/api/exchangerates/tables/a/2012-01-01/2012-01-31/?format=json
"""

import csv
import os
import sys
from datetime import datetime
from typing import Dict

import requests
from dateutil import parser


URL_LEFT = 'https://api.nbp.pl/api/exchangerates/tables/a/'
URL_RIGHT = '?format=json'


def input_date() -> datetime:
    """Pobieranie od użytkownika daty"""

    while True:
        date_ = input('> ')

        try:
            date_ = parser.parse(date_, dayfirst=True)
            date_ = date_.date()
            break
        except ValueError:
            print('Nieprawidłowy format daty. Spróbuj jeszcze raz ', end='')

    return date_


def get_url(start_day: datetime, end_day: datetime) -> str:
    """Tworzenie adresu URL dla podanych dat początkowej i końcowej"""
    
    return URL_LEFT + start_day.strftime('%Y-%m-%d') + '/' + end_day.strftime('%Y-%m-%d') + '/' + URL_RIGHT


def get_response(url: str) -> Dict:
    """Pobieranie z API NBP do JSON"""
    
    try:
        response = requests.get(url)
        data_json = response.json()
    except:
        print('Błąd pobierania danych')
        sys.exit(1)

    return data_json
    

def get_file_name(start_date: datetime, end_date: datetime) -> str:
    """Generowanie nazwy pliku względem podanych dat"""

    return 'exchange_' + start_date.strftime('%Y-%m-%d') + '_' + end_date.strftime('%Y-%m-%d') + '.csv'


def create_file_csv(data_json: Dict, file_name: str) -> None:
    """Tworzenie pliku CSV zawierającego wszystkie rekordy dt. wybranego okresu"""

    if not os.path.exists('exchange'):
        os.mkdir('exchange')
    
    headline = ['date'] + list(data_json[0]['rates'][0].keys())  # nagłówek

    with open(f'exchange/{file_name}', 'a', encoding='utf-8', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(headline)

        for i in range(len(data_json)):
            # tworzenie nowej listy z datą i danymi dt. kursów walut dla tej daty
            date_str = data_json[i]['effectiveDate']
            currency_list = data_json[i]['rates']

            for j in range(len(currency_list)):
                line = [date_str] + list(currency_list[j].values()) 
                csvwriter.writerow(line)


def main() -> None:
    os.system('cls')
    print('Podaj datę początkową: ', end='')
    start_date = input_date()
    print('Podaj datę końcową: ', end='')
    
    while True:
        end_date = input_date()

        if (end_date - start_date).days <= 93:
            break
        else:
            print('Wprowadzony okres jest dłuższy niż 93 dni. Wpisz inną datę końcową ', end='')

    url = get_url(start_date, end_date)
    data_json = get_response(url)
    file_name = get_file_name(start_date, end_date)
    create_file_csv(data_json, file_name)
    print(f'\nPlik {file_name} został utworzony.')


if __name__ == '__main__':
    main()
    