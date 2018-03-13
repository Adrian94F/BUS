# Bezpieczeństwo Usług Sieciowych - lab 1

## Wymagania
- Python 2.7
- Crypto (pip install crypto)

## Uruchamianie
W osobnych oknach terminala: `./server.py port` i `./client.py ip port [szyfrowanie]` (na przykład: `./server.py 8000` i `./client.py localhost 8000`). Można uruchomić kilka instancji klienta.

Dostępne tryby szyfrowania:
- none (brak szyfrowania)
- cezar
- xor

Zmiana szyfrowania poprzez wpisanie wiadomości `@@@nazwa_szyfrowania` (na przykład `@@@xor`)