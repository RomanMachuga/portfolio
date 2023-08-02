# Portfolio
<i><b>Moje portfolio zawierające kilka prywatnych projektów, zrealizowanych w Python</b></i>

Poniższe projekty zostały zrealizowane jako: 
* rozwiązanie zadań praktycznych, z którymi miałem do czynienie;
* próba napisania programów wymaganych do aplikowania na stanowisko juniora;
* projekt zaliczeniowy z przedmiotu na studiach podyplomowych "Data Science w praktyce".

### 1) API CEPiK
<b>Program do pobierania danych dla wybranego roku z API CEPiK i zapisywania do plików CSV (dla wszystkich województw)</b><br>
plik – <i>01_API_CEPiK.py</i>

Program pobiera dane z API CEPiK (Centralna Ewidencja Pojazdów i Kierowców - http://www.cepik.gov.pl/interfejs-dla-cepik) dla wszystkich województw dla podanego roku (każdy miesiąc jako osobny plik). Wynik jest zapisywany w plikach CSV w katalogu z kodem województwa, na przykład "w14".<br>
Przykładowy adres URL: https://api.cepik.gov.pl/pojazdy?wojewodztwo=14&data-od=20100101&data-do=20101231&typ-daty=2&tylko-zarejestrowane=true&pokaz-wszystkie-pola=true&limit=500<br>
*	Wejście – rok;
*	Wyjście – dwanaście plików CSV.

### 2) API NBP
<b>Program do pobierania historycznych kursów walut z API NBP</b><br>
plik – <i>02_pobieranie_z_API_NBP.py</i>

Program pobiera dane historyczne kursów walut (tabela A) z API NBP (Narodowy Bank Polski) - http://api.nbp.pl/. W jednym pobraniu można ściągnąć dane z okresu, który nie przekracza 93 dni (ograniczenie NBP)
Skrypt pyta o datę początkową oraz końcową. Wynik jest zapisywany w pliku CSV.<br>
Przykładowy adres URL: https://api.nbp.pl/api/exchangerates/tables/a/2012-01-01/2012-01-31/?format=json
*	Wejście – data początkowa, data końcowa;
*	Wyjście – jeden plik CSV.

### 3) Dostosowanie CSV
<b>Skrypt do przekształcania bazy pacjentów przychodni przez wyrównanie ilości kolumn po nazwie każdego leku (przy zastosowaniu Pandas)</b><br>
plik – <i>03_przeksztalcanie_plikow_csv.py</i>

Baza pacjentów to 65 plików CSV, zawierających średnio 13 tys. rekordów. Program po kolei pobiera pliki CSV z folderu, przekształca je, zmieniając nazwy kolumn i dodając brakujące. Zmodyfikowany dataset z powrotem zapisywany jest do pliku CSV.
* Wejście – wymagana ilość kolumn po nazwie leku, ścieżka do folderu z plikami do modyfikacji, folder końcowy do zapisywania plików przekształconych;
* Wyjście – pliki CSV po przekształceniu.

### 4) Generator kodów pocztowych
<b>Program do generowania kodów pocztowych pomiędzy dwoma podanymi</b><br>
plik – <i>04_generator_kodów_pocztowych.py</i>

Generator kodów pocztowych został napisany jako próba wykonania zadania testowego w celu aplikowania na stanowisko Juniora. Skrypt przyjmuje dwa stringi, na przykład '79-900' i '80-155'. Dalej zwraca listę kodów pomiędzy nimi.
*	Wejście – 2 stringi (kody pocztowe);
*	Wyjście – lista kodów pomiędzy dwoma podanymi.

### 5) Lista brakujących elementów
<b>Skrypt otrzymuje elementy z listy 1-n, szuka brakujących i je wypisuje</b><br>
plik – <i>05_lista_brakujących_elementów.py</i>

Program Lista brakujących elementów został napisany jako próba wykonania zadania testowego w celu aplikowania na stanowisko Juniora. Podana jest lista, zawierająca elementy o wartościach 1-n. Program sprawdza jakich elementów brakuje: 1-n = [1,2,3,4,5,...,10], na przykład:<br>
a) n=10;<br>
b) wejście: [2,3,7,4,9], 10;<br>
c) wyjście: [1,5,6,8,10].<br>
*	Wejście – liczba n, lista istniejących elementów;
*	Wyjście – lista brakujących elementów.

### 6) Dataset
<b>Program do generowania kodów pocztowych pomiędzy dwoma podanymi</b><br>
pliki – <i>06_dataset.py</i> (skrypt), <i>06_bank.csv</i> (dane źródłowe)

Moduł wykonano w ramach projektu zaliczeniowego na studiach podyplomowych. Dostarcza szereg funkcjonalności w pracy z datasetem:
*	wczytanie datasetu (funkcja, która po podaniu ścieżki wczytuje dane z pliku do listy. Dodatkowo funkcja przyjmuje parametr, określający czy pierwszy wiersz pliku zawiera etykiety kolumn czy nie. Jeżeli tak, to etykiety wczytywane są do oddzielnej listy);
*	wypisanie etykiet (funkcja wypisująca etykiety lub komunikat, że etykiet nie było w danym datasecie);
*	wypisanie danych datasetu (funkcja wypisuje kolejne wiersze datasetu. Bez podania parametrów wypisywany jest cały dataset, ale możliwe też podanie 2 parametrów, które określają przedział, który ma zostać wyświetlony);
*	podział datasetu na zbiór treningowy, testowy i walidacyjny (funkcja przyjmuje 3 parametry określające procentowo jaka część głównego zbioru danych trafia do poszczególnych zbiorów);
*	wypis liczby klas decyzyjnych;
*	wypisz dane dla podanej wartości klasy decyzyjnej (wypisuje wiersze z zadaną wartością klasy decyzyjnej);
*	zapisanie danych do pliku csv (jako parametr przyjmowana jest dowolna lista, która może być podzbiorem datasetu, zmienną przechowującą dane treningowe, itp. Dodatkowo podawana jest nazwa pliku, do którego dane zostaną zapisane).

Funkcjonalność zrealizowano dla pliku bank.csv (https://archive.ics.uci.edu/ml/machine-learning-databases/00222/bank.zip).

*	Wejście – ścieżka do pliku źródłowego CSV;
*	Wyjście – zgodnie z funkcjonalnością i wybranymi odpowiedziami w trakcie wykonania programu.
