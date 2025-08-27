# Portfolio
<i><b>Moje portfolio zawierające kilka prywatnych projektów, zrealizowanych w Python</b></i>

Poniższe projekty zostały zrealizowane jako: 
* rozwiązanie zadań praktycznych, z którymi miałem do czynienia;
* próba napisania programów wymaganych do aplikowania na stanowisko juniora;
* projekt zaliczeniowy z przedmiotu na studiach podyplomowych "Data Science w praktyce".

---

# 1) API CEPiK – Automatyczne Pobieranie Danych do CSV

**📌 Program do pobierania danych z API CEPiK dla wybranego roku i zapisywania ich w plikach CSV (dla wszystkich województw).**  

## 📌 Opis  
Ten program automatyzuje pobieranie danych o pojazdach z **Centralnej Ewidencji Pojazdów i Kierowców (CEPiK)**.  
Dane są zapisywane w osobnych plikach **CSV** dla każdego województwa i miesiąca, co ułatwia ich analizę.

🔹 **Plik skryptu:** `04_API_CEPiK.py`  
🔹 **Źródło danych:** [API CEPiK](http://www.cepik.gov.pl/interfejs-dla-cepik)  
🔹 **Format danych:** CSV  

## 🔧 Funkcjonalność  

✔ **Automatyczne pobieranie danych** – program pobiera informacje o pojazdach dla wszystkich województw w wybranym roku.  
✔ **Obsługa paginacji API** – jeżeli liczba rekordów przekracza limit API, program automatycznie pobiera kolejne strony.  
✔ **Zapis do plików CSV** – każdy miesiąc jest zapisywany jako osobny plik w katalogu odpowiadającym kodowi województwa (`w14`, `w02` itd.).  
✔ **Obsługa błędów i ponawianie zapytań** – jeśli API zwróci zbyt mało wyników lub wystąpi błąd, program ponawia pobieranie.  
✔ **Niestandardowa obsługa SSL** – dzięki specjalnej konfiguracji, program radzi sobie z problemami związanymi z certyfikatami.  

## 🚀 Jak uruchomić?

1. **Zainstaluj wymagane biblioteki**  
   ```sh
   pip install requests
   ```

2. **Uruchom skrypt**  
   ```sh
   python 04_API_CEPiK.py
   ```

3. **Podaj rok** – program pobierze dane dla każdego miesiąca i zapisze je w plikach CSV.

## 📂 Struktura wyników  

Dane są zapisywane w katalogach według województw i miesięcy:

```
📂 2023
 ├── 📂 w02  (Dolnośląskie)
 │    ├── w02_r2023_m01.csv
 │    ├── w02_r2023_m02.csv
 │    ├── ...
 ├── 📂 w14  (Mazowieckie)
 │    ├── w14_r2023_m01.csv
 │    ├── w14_r2023_m02.csv
 │    ├── ...
```
Każdy plik zawiera dane w formacie **CSV**.

## 📌 Dlaczego warto?

✅ **Automatyzacja pobierania danych z API CEPiK**  
✅ **Obsługa błędów i ponowne próby pobrania**  
✅ **Struktura danych ułatwiająca analizę w Excelu, Pandas itp.**  
✅ **Radzenie sobie z problemami SSL w API CEPiK**  

## 🔗 **Plany na przyszłość**
- 📊 Możliwość eksportu danych do bazy SQL  
- 📈 Wizualizacja danych w Power BI  
- 📉 Filtrowanie rekordów według parametrów  

---

# 2) 📌 API NBP – Pobieranie historycznych kursów walut

**📂 Plik:** `02_pobieranie_z_API_NBP.py`

Ten program automatyzuje pobieranie historycznych kursów walut (tabela A) z **Narodowego Banku Polskiego (NBP)**. Dane są pobierane dla wybranego zakresu dat i zapisywane w pliku CSV.

🔹 **Źródło danych:** [API NBP](http://api.nbp.pl/)  
🔹 **Zakres pobierania:** maks. 93 dni na jedno zapytanie  
🔹 **Format danych:** CSV  

## 🔧 Funkcjonalność
✔ **Pobieranie kursów walut dla wybranego przedziału czasowego**  
✔ **Obsługa ograniczeń API (93 dni na jedno zapytanie)**  
✔ **Zapis danych do pliku CSV**  

## 🚀 Jak uruchomić?
1. **Uruchom skrypt**  
   ```sh
   python 02_pobieranie_z_API_NBP.py
   ```
2. **Podaj zakres dat** (początkową i końcową).  

---

# 3) 📌 Dostosowanie CSV – Przekształcanie bazy pacjentów

**📂 Plik:** `03_przeksztalcanie_plikow_csv.py`

Program służy do normalizacji struktury danych w **bazie pacjentów**, w której każda kolumna reprezentuje lek.  
Baza składa się z **65 plików CSV**, zawierających średnio **13 tys. rekordów** każdy.

## 🔧 Funkcjonalność
✔ **Wczytywanie i przekształcanie plików CSV**  
✔ **Dodawanie brakujących kolumn według nazw leków**  
✔ **Zapis danych w nowej strukturze do plików CSV**  

## 🚀 Jak uruchomić?
1. **Uruchom skrypt**  
   ```sh
   python 03_przeksztalcanie_plikow_csv.py
   ```
2. **Podaj katalog wejściowy i wyjściowy**  

---

# 4) 📌 Generator kodów pocztowych

**📂 Plik:** `04_generator_kodów_pocztowych.py`

Skrypt generuje listę kodów pocztowych w zakresie podanym przez użytkownika.  
Przykładowo, dla **'79-900' – '80-155'**, program zwróci wszystkie kody pomiędzy nimi.

## 🔧 Funkcjonalność
✔ **Generowanie zakresu kodów pocztowych**  
✔ **Obsługa kodów w formacie `XX-XXX`**  
✔ **Zapis wyników do listy**  

## 🚀 Jak uruchomić?
1. **Uruchom skrypt**  
   ```sh
   python 04_generator_kodów_pocztowych.py
   ```
2. **Podaj dwa kody pocztowe** (początkowy i końcowy).  

---

# 5) 📌 Lista brakujących elementów

**📂 Plik:** `05_lista_brakujących_elementów.py`

Program identyfikuje brakujące wartości w ciągu liczb od `1` do `n`.  
Dla przykładu, jeśli `n=10` i podana lista to `[2,3,7,4,9]`, wynik to `[1,5,6,8,10]`.

## 🔧 Funkcjonalność
✔ **Analiza listy i znajdowanie brakujących wartości**  
✔ **Obsługa dowolnych zakresów**  
✔ **Zapis wyników do listy**  

## 🚀 Jak uruchomić?
1. **Uruchom skrypt**  
   ```sh
   python 05_lista_brakujących_elementów.py
   ```
2. **Podaj `n` oraz listę wartości**  

---

# 6) 📌 Dataset – Przekształcanie zbiorów danych

**📂 Pliki:** `06_dataset.py` (skrypt), `06_bank.csv` (dane źródłowe)

Moduł realizuje szereg operacji na zbiorach danych, takich jak podział na zestawy treningowe, analiza klas decyzyjnych i zapis wyników.

## 🔧 Funkcjonalność
✔ **Wczytywanie datasetu i analiza etykiet kolumn**  
✔ **Podział danych na zbiór treningowy, testowy i walidacyjny**  
✔ **Filtrowanie danych według wartości klasy decyzyjnej**  
✔ **Zapis przekształconego datasetu do CSV**  

## 🚀 Jak uruchomić?
1. **Uruchom skrypt**  
   ```sh
   python 06_dataset.py
   ```
2. **Podaj ścieżkę do pliku CSV**  
