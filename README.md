# Portfolio
<i><b>My portfolio of private Python projects</b></i>

Zawiera kilka prywatnych projektów, które zostały zrealizowane jako:<br>
    a) rozwiązanie zadań praktycznych, z którymi miałem doczynienie;<br>
    b) próba napisania programów wymaganych do aplikowania na stanowisko juniora;<br>
    c) projekt zaliczeniowy z przedmiotu na studiach podyplomowych "Data Science w praktyce".

### 1) API CEPiK
<b>Program do pobierania danych dla wybranego roku z API CEPiK i zapisywania do plików CSV (dla wszystkich województw)</b><br>
plik <i>01_pobieranie_z_API_NBP.py</i><br>

Program pobiera dane z API CEPiK (Centralna Ewidencja Pojazdów i Kierowców - http://www.cepik.gov.pl/interfejs-dla-cepik) dla wszystkich województw dla podanego roku (każdy miesiąc jako osobny plik). Wynik jest zapisywany w plikach CSV w katalogu z kodem województwa, na przykład "w14".<br>
Przykładowy adres URL: https://api.cepik.gov.pl/pojazdy?wojewodztwo=14&data-od=20100101&data-do=20101231&typ-daty=2&tylko-zarejestrowane=true&pokaz-wszystkie-pola=true&limit=500<br>
*	Wejście – rok;
*	Wyjście – dwanaście plików CSV

