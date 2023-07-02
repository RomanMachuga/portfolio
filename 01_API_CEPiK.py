"""
Program pobiera dane z API CEPiK (Centralna Ewidencja Pojazdów i Kierowców) - http://www.cepik.gov.pl/interfejs-dla-cepik
Program pobiera dane dla wszystkich województw dla podanego roku (każdy miesiąc jako osobny plik). Wynik jest zapisywany w plikach CSV w katalogu z kodem województwa, na przykład "w14".
Przykładowy adres URL: https://api.cepik.gov.pl/pojazdy?wojewodztwo=14&data-od=20100101&data-do=20101231&typ-daty=2&tylko-zarejestrowane=true&pokaz-wszystkie-pola=true&limit=500
"""

import csv
import os
import time
from datetime import datetime
from typing import Dict, Tuple

import requests

URL1 = 'https://api.cepik.gov.pl/pojazdy?wojewodztwo='
URL2 = '&data-od='
URL3 = '&data-do='
URL4 = '&typ-daty=2&tylko-zarejestrowane=true&pokaz-wszystkie-pola=true&limit=500'
KODY_WOJEWODZTW = {'02': 'Dolnośląskie',
                   '04': 'Kujawsko-Pomorskie',
                   '06': 'Lubelskie',
                   '08': 'Lubuskie',
                   '10': 'Łódzkie',
                   '12': 'Małopolskie',
                   '14': 'Mazowieckie',
                   '16': 'Opolskie',
                   '18': 'Podkarpackie',
                   '20': 'Podlaskie',
                   '22': 'Pomorskie',
                   '24': 'Śląskie',
                   '26': 'Świętokrzyskie',
                   '28': 'Warmińsko-Mazurskie',
                   '30': 'Wielkopolskie',
                   '32': 'Zachodniopomorskie'}
MIESIACE = list(range(1, 13))
SLEEP = 30


def get_url(rok: int, miesiac: int, kod: str, page=1) -> str:
    """Tworzenie adresu URL dla podanego roku i kodu województwa"""
    
    if miesiac == 12:
        url = f'{URL1}{kod}{URL2}{str(rok)}{str(miesiac)}01{URL3}{str(rok + 1)}0101{URL4}&page={page}'
    else:
        url = f'{URL1}{kod}{URL2}{str(rok)}{miesiac:02}01{URL3}{str(rok)}{(miesiac + 1):02}01{URL4}&page={page}'

    return url


def get_response(url: str, rok: int, dir_name: str) -> Dict:
    """Pobieranie z API CEPiK do JSON. Jeśli pobiertanie jest niemożliwe, to program czeka 20 s i wykonuję ponowną próbę"""

    while True:
        try:
            requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += '@SECLEVEL=1'  # ignorowanie (pominięcie) błędów SSL
            response = requests.get(url)
            data = response.json()
            break
        except:
            report_row = f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - Błąd pobierania danych. Ponowna próba za {SLEEP} s'
            print(report_row)
            create_file_txt_report(report_row)
            time.sleep(SLEEP)
    
    return data
    

def get_count_pages(data: Dict) -> int:
    """Wyznaczenie ilości stron wyników dla konkretnego roku i województwa (stronicowanie)"""

    pages = data['links']['last']
    pages = int(pages[pages.index('=', 88) + 1:pages.index('&', 92)])
    return pages


def get_file_name_and_dir_name(rok: int, miesiac: int, kod: str) -> Tuple[str, str]:
    """Generowanie nazw katalogu i pliku względem podanego roku i kodu województwa, a także z uwzględnieniem misiąca"""

    file_name = f'w{kod}_r{str(rok)}_m{miesiac:02}.csv'
    dir_name = f'w{kod}'
    return file_name, dir_name


def create_file_csv(rok: int, data: Dict, file_name: str, dir_name: str, page: int) -> None:
    """Tworzenie pliku CSV zawierającego wszystkie rekordy dt. wybraneo roku i województwa"""

    if not os.path.exists(str(rok)):
        os.mkdir(str(rok))
    
    if not os.path.exists(f'{str(rok)}\{dir_name}'):
        os.mkdir(f'{str(rok)}\{dir_name}')

    with open(f'{str(rok)}\{dir_name}\{file_name}', 'a', encoding='utf-8', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        
        if page == 1:
            naglowki = ['id'] + list(data['data'][0]['attributes'].keys())
            csvwriter.writerow(naglowki)

        for i in range(len(data['data'])):
            wiersz = [data['data'][i]['id']] + list(data['data'][i]['attributes'].values())
            csvwriter.writerow(wiersz)


def create_file_txt_report(report_row: str) -> None:
    """Tworzenie pliku TXT zawierajacego listę pobranych stron z CEPiK"""

    with open(f'download_report.txt', 'a', encoding='utf-8') as txtfile:
        txtfile.writelines(f'{report_row}\n')


def main() -> None:
    os.system('cls')
    rok = int(input('Podaj rok : > '))
    report_row = f'\nPoczątek pobierania: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n'
    create_file_txt_report(report_row)
    
    for kod in list(KODY_WOJEWODZTW.keys())[11:]:
        for miesiac in MIESIACE:
            file_name, dir_name = get_file_name_and_dir_name(rok, miesiac, kod)
            url = get_url(rok, miesiac, kod)
            data = get_response(url, rok, dir_name)
            pages = get_count_pages(data)

            # Przy pobieraniu ilości stron czasami pojawia się błąd pokazujący dostępność tylko 2 stron. Dlatego podejmuje się cztery dodatkowe próby sprawdzenia/pobrania tej ilości
            if pages <= 2:
                cycle = 2  # liczba cyklów pobierania ilości stron.

                while pages <= 2 and cycle <= 8:
                    report_row = f'Ilość stron = {pages}. Próba pobierania nr {cycle} za {SLEEP} s.'
                    print(report_row)
                    create_file_txt_report(report_row)
                    time.sleep(SLEEP)
                    cycle += 1
                    data = get_response(url, rok, dir_name)
                    pages = get_count_pages(data)

            for page in range(1, pages + 1):
                url = get_url(rok, miesiac, kod, page)
                data = get_response(url, rok, dir_name)
                create_file_csv(rok, data, file_name, dir_name, page)
                report_row = f'w{kod}, {rok}-{miesiac:02}, str_{page:02}/{pages:02}'
                print(report_row)
                create_file_txt_report(report_row)


if __name__ == '__main__':
    main()
    