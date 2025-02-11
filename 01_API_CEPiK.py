"""
Program pobiera dane z API CEPiK (Centralna Ewidencja Pojazdów i Kierowców) - http://www.cepik.gov.pl/interfejs-dla-cepik
Program pobiera dane dla wszystkich województw dla podanego roku (każdy miesiąc jako osobny plik). Wynik jest zapisywany w plikach CSV w katalogu z kodem województwa, na przykład "w14".
Przykładowy adres URL: https://api.cepik.gov.pl/pojazdy?wojewodztwo=14&data-od=20100101&data-do=20101231&typ-daty=2&tylko-zarejestrowane=true&pokaz-wszystkie-pola=true&limit=500
"""

import csv
import os
import ssl
import time
from datetime import datetime
from typing import Dict, Tuple
from urllib.parse import parse_qs, urlparse

import requests
import urllib3
from urllib3.poolmanager import PoolManager

# Wyłączenie ostrzeżeń związanych z weryfikacją certyfikatu SSL (verify=False)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Niestandardowy adapter SSL, który ustawia niższy poziom zabezpieczeń
class SSLAdapter(requests.adapters.HTTPAdapter):
    
    def init_poolmanager(self, connections, maxsize, block=False, **kwargs):
        context = ssl.create_default_context()
        # Wyłączenie weryfikacji nazwy hosta oraz ustawienie trybu weryfikacji na CERT_NONE, aby uniknąć błędu "Cannot set verify_mode to CERT_NONE when check_hostname is enabled"
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        context.set_ciphers("DEFAULT:@SECLEVEL=1")
        self.poolmanager = PoolManager(
            num_pools=connections,
            maxsize=maxsize,
            block=block,
            ssl_context=context
        )

# Utworzenie globalnej sesji z zamontowanym niestandardowym adapterem
session = requests.Session()
session.mount("https://", SSLAdapter())

URL1 = "https://api.cepik.gov.pl/pojazdy?wojewodztwo="
URL2 = "&data-od="
URL3 = "&data-do="
URL4 = "&typ-daty=2&tylko-zarejestrowane=true&pokaz-wszystkie-pola=true&limit=500"
KODY_WOJEWODZTW = {
    "02": "Dolnośląskie",
    "04": "Kujawsko-Pomorskie",
    "06": "Lubelskie",
    "08": "Lubuskie",
    "10": "Łódzkie",
    "12": "Małopolskie",
    "14": "Mazowieckie",
    "16": "Opolskie",
    "18": "Podkarpackie",
    "20": "Podlaskie",
    "22": "Pomorskie",
    "24": "Śląskie",
    "26": "Świętokrzyskie",
    "28": "Warmińsko-Mazurskie",
    "30": "Wielkopolskie",
    "32": "Zachodniopomorskie"
}
MIESIACE = list(range(1, 13))
SLEEP = 30


def get_url(rok: int, miesiac: int, kod: str, page: int = 1) -> str:
    if miesiac == 12:
        url = f"{URL1}{kod}{URL2}{rok}{miesiac:02}01{URL3}{rok+1}0101{URL4}&page={page}"
    else:
        url = f"{URL1}{kod}{URL2}{rok}{miesiac:02}01{URL3}{rok}{(miesiac+1):02}01{URL4}&page={page}"
    return url


def get_response(url: str, rok: int, dir_name: str) -> Dict:
    while True:
        try:
            # Używamy globalnej sesji z niestandardowym adapterem
            response = session.get(url, verify=False)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            report_row = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Błąd pobierania danych: {e}. Ponowna próba za {SLEEP} s"
            print(report_row)
            create_file_txt_report(report_row)
            time.sleep(SLEEP)


def get_count_pages(data: Dict) -> int:
    last_link = data.get("links", {}).get("last")

    if last_link:
        parsed = urlparse(last_link)
        qs = parse_qs(parsed.query)
        page_numbers = qs.get("page", ["1"])

        try:
            pages = int(page_numbers[0])
        except ValueError:
            pages = 1
    else:
        pages = 1
    return pages


def get_file_name_and_dir_name(rok: int, miesiac: int, kod: str) -> Tuple[str, str]:
    file_name = f"w{kod}_r{rok}_m{miesiac:02}.csv"
    dir_name = f"w{kod}"
    return file_name, dir_name


def create_file_csv(rok: int, data: Dict, file_name: str, dir_name: str, page: int) -> None:
    year_dir = str(rok)
    province_dir = os.path.join(year_dir, dir_name)

    if not os.path.exists(year_dir):
        os.mkdir(year_dir)
    
    if not os.path.exists(province_dir):
        os.mkdir(province_dir)
    
    file_path = os.path.join(province_dir, file_name)

    if not data.get("data"):
        return
    
    with open(file_path, "a", encoding="utf-8", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)

        if page == 1:
            headers = ["id"] + list(data["data"][0]["attributes"].keys())
            csvwriter.writerow(headers)
        
        for item in data["data"]:
            row = [item.get("id")] + list(item.get("attributes", {}).values())
            csvwriter.writerow(row)


def create_file_txt_report(report_row: str) -> None:
    with open("download_report.txt", "a", encoding="utf-8") as txtfile:
        txtfile.write(f"{report_row}\n")


def main() -> None:
    os.system("cls" if os.name == "nt" else "clear")

    try:
        rok = int(input("Podaj rok: "))
    except ValueError:
        print("Niepoprawny rok. Program kończy działanie.")
        return
    
    report_row = f"\nPoczątek pobierania: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    create_file_txt_report(report_row)

    for kod in KODY_WOJEWODZTW.keys():
        for miesiac in MIESIACE:
            file_name, dir_name = get_file_name_and_dir_name(rok, miesiac, kod)
            url = get_url(rok, miesiac, kod)
            data = get_response(url, rok, dir_name)
            pages = get_count_pages(data)

            if pages <= 2:
                cycle = 2

                while pages <= 2 and cycle <= 8:
                    report_row = f"Ilość stron = {pages}. Próba pobierania nr {cycle} za {SLEEP} s."
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
                report_row = f"w{kod}, {rok}-{miesiac:02}, strona {page:02}/{pages:02}"
                print(report_row)
                create_file_txt_report(report_row)


if __name__ == "__main__":
    main()
