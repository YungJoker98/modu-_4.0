import logging

# Konfiguracja logowania
logging.basicConfig(level=logging.INFO, format='%(message)s')

def pobierz_liczby(ile=2):
    liczby = []
    for i in range(1, ile + 1):
        while True:
            try:
                liczba = float(input(f"Podaj składnik {i}: "))
                liczby.append(liczba)
                break
            except ValueError:
                print("Podaj prawidłową liczbę!")
    return liczby

def kalkulator():
    # Menu wyboru operacji
    dzialania = {
        1: 'Dodawanie',
        2: 'Odejmowanie',
        3: 'Mnożenie',
        4: 'Dzielenie'
    }

    while True:
        try:
            operacja = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
            if operacja not in dzialania:
                print("Wybierz prawidłową opcję!")
                continue
            break
        except ValueError:
            print("Podaj prawidłową liczbę!")

    # Jeśli wybrano dodawanie lub mnożenie, pozwalamy na więcej niż dwie liczby
    if operacja in [1, 3]:
        try:
            ile_liczb = int(input(f"Podaj, ile liczb chcesz użyć do {dzialania[operacja].lower()}: "))
            if ile_liczb < 2:
                print("Musisz podać co najmniej dwie liczby.")
                return
        except ValueError:
            print("Podaj prawidłową liczbę!")
            return
        liczby = pobierz_liczby(ile_liczb)
    else:
        liczby = pobierz_liczby(2)

    # Logowanie wybranej operacji i liczb
    logging.info(f"{dzialania[operacja]} {' i '.join(map(str, liczby))}")

    # Wykonywanie obliczeń
    if operacja == 1:
        wynik = sum(liczby)
    elif operacja == 2:
        wynik = liczby[0] - liczby[1]
    elif operacja == 3:
        wynik = 1
        for liczba in liczby:
            wynik *= liczba
    elif operacja == 4:
        try:
            wynik = liczby[0] / liczby[1]
        except ZeroDivisionError:
            print("Nie można dzielić przez zero!")
            return

    # Wyświetlanie wyniku
    print(f"Wynik to {wynik:.2f}")

if __name__ == "__main__":
    kalkulator()
