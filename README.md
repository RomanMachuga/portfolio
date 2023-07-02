# Portfolio
<i><b>Moje portfolio zawierające kilka prywatnych projektów, zrealizowanych w Python</b></i>

Zawiera kilka prywatnych projektów, które zostały zrealizowane jako:
* rozwiązanie zadań praktycznych, z którymi miałem doczynienie;
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

Program pobiera dane historyczne kursów walut (tabela A) z API NBP (Narodowy Bank Poski) - http://api.nbp.pl/. W jednym pobraniu można sciągnąć dane z okresu, który nie przekracza 93 dni (ograniczenie NBP)
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


