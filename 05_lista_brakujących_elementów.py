"""
Lista brakujących elementów.
Podana jest lista, zawierająca elementy o wartościach 1-n. Program sprawdza jakich elementów brakuje 1-n = [1,2,3,4,5,...,10], na przykład:
    - n=10
    - wejście: [2,3,7,4,9], 10
    - wyjście: [1,5,6,8,10]
"""

import os
import sys
from typing import List


def get_list_n(n: int) -> List[int]:
    """Generowanie listy z n elementów"""

    return [element for element in range(1, n + 1)]


def get_existing_list_of_number(input_existing_list: List[str], n: int, large_elements=False) -> List[int]:
    """Generowanie listy liczb całkowitych z wprowadzonych liczb"""

    existing_list = list(set(input_existing_list))
    existing_list_of_number = []

    for ex_l in existing_list:
        if int(ex_l) <= n:
            existing_list_of_number.append(int(ex_l))
        else:
            large_elements = True
    
    if large_elements:
        print(f'\nLista wprowadzona zawierała liczby, większe od n={n}. Te elementy zostały usunięte')

    existing_list_of_number.sort()
    return existing_list_of_number


def get_missing_list(existing_list: List[int], list_n: List[int]) -> List[int]:
    """Generowanie listy liczb brakujących"""

    return [l_n for l_n in list_n if l_n not in existing_list]


def main():
    os.system('cls')

    try:
        n = int(input('Wpisz wartość n: >'))
    except ValueError:
        print('Wpisano błędną wartość.')
        sys.exit(1)
    
    list_n = get_list_n(n)
    input_existing_list = input('Wpisz przez spację lub przecinek istniejące elementy listy: >').strip().replace(',', ' ').split(' ')
    existing_list_of_number = get_existing_list_of_number(input_existing_list, n)
    missing_list = get_missing_list(existing_list_of_number, list_n)
    print('\nLista wprowadzona:', existing_list_of_number)
    print('\nLista brakujących elementów:', missing_list)


if __name__ == '__main__':
    main()
    
