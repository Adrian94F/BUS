# Bezpieczeństwo Usług Sieciowych

## Lab 1

### Wymagania
- Python 2.7

### Uruchamianie

W osobnych oknach terminala: `./server.py port` i `./client.py ip port [szyfrowanie]` (na przykład: `./server.py 2580` i `./client.py localhost 2580`). Można uruchomić kilka instancji klienta.

### TODO
- serwer
	- p i g: generowanie / z pliku
	- wymiana kluczy
	- szyfrowanie
  - opakowanie wiadomości w JSONa
- klient
	- wymiana kluczy
	- szyfrowanie
  - opakowanie wiadomości w JSONa

### Opis działania
```
A (client)                                                            B (server)

    Po połączeniu do serwera klient prosi o liczby p oraz g.
{ “request”: “keys” } --> 

    Serwer wysyła do klienta liczby p oraz g.
                                                      <-- { “p”: 123, “g”: 123 }
						      
    Serwer i klient wymieniają się publicznymi wartościami A oraz B:
    Klient wysyła do serwera obliczoną wartość A.
    Serwer wysyła do klient obliczoną wartość B.
    UWAGA: a) oraz b) mogą nastąpić w dowolnej kolejności
  { “a”: 123 } -->                                              <-- { “b”: 123 }
  
    [OPCJONALNIE] Klient wysyła do serwera informację o żądanym sposobie szyfrowania wiadomości.
    UWAGA: Krok ten jest opcjonalny. Jeżeli klient nie wyśle tej informacji, to strony przyjmują domyśle szyfrowanie ustawione na “none”.
  { “encryption”: “none” } -->  
  
    Klient oraz serwer wymieniają się szyfrowanymi wiadomościami.
  { “msg”: “...”, “from”: “John” } -->      <-- { “msg”: “...”, “from”: “Anna” }
  ```
