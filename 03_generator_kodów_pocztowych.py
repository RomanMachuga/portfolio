"""
Generator kodów pocztowych.
Program przyjmuje 2 stringi, na przykład '79-900' i '80-155'. Dalej zwraca listę kodów pomiędzy nimi
"""

import os
from typing import List


def code_verification(code_str: str) -> str:
    """Weryfikacja wprowadzonych przez użytkownika kodów pocztowych"""

    len_code_str = len(code_str)

    while len_code_str != 6 or code_str[2] != '-':
        code_str = input('\nKod musi zawierać 6 znaków, w tym znak "-" na pozycji trzeciej. Jeszcze raz wpisz poprawny kod pocztowy: >')
        len_code_str = len(code_str)
    return code_str


def convert(code_str: str) -> int:
    """Konwertowanie tekstowych kodów pocztowych na liczby całkowite"""

    return int(code_str.replace('-', ''))


def code_manipulation(code_str: str) -> int:
    """Ogólne manipulacje na kodach pocztowych (weryfikacja i konwertowanie)"""

    code_str = code_verification(code_str)
    code = convert(code_str)
    return code


def get_codes_list(code1: int, code2: int) -> List[str]:
    """Tworzenie listy kodów między podanymi przez użytkownika"""

    new_codes_str = [str(code)[:2] + '-' + str(code)[2:] for code in range(code1, code2 + 1)]
    return new_codes_str


def codes_print(new_codes_str: List[str]) -> None:
    """Drukowanie kodów"""

    for code in new_codes_str:
        if code != new_codes_str[len(new_codes_str) - 1]:
            print(code, end=', ')
        else:
            print(f'{code}.')


def main():
    os.system('cls')
    print('Wpisz dwa kody pocztowe (w formacie 00-000):')
    code1_str = input('Kod 1: >')
    code1 = code_manipulation(code1_str)
    code2_str = input('Kod 2: >')
    code2 = code_manipulation(code2_str)
    
    while code2 <= code1:
        code2_str = input('Kod 2 musi być większy od kodu 1. Wpisz jeszcze raz Kod 2: >')
        code2 = code_manipulation(code2_str)

    new_codes_str = get_codes_list(code1, code2)
    print('\nOto są kody z podanego zakresu:')
    codes_print(new_codes_str)


if __name__ == '__main__':
    main()
    