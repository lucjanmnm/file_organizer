# Organizer Plików

Prosty organizer plików w Pythonie — automatycznie sortuje pliki w wybranym folderze do podfolderów według ich typu/rozszerzenia (np. zdjęcia do `Pictures`, dokumenty do `Documents` itd.).

## Funkcje

- Sortowanie plików na podstawie rozszerzenia do folderów:
  - Pictures (obrazy)
  - Documents (dokumenty)
  - Music (muzyka)
  - Videos (wideo)
  - Archives (archiwa)
  - Code (kody źródłowe)
  - Other (pozostałe)
- Automatyczne tworzenie folderów, jeśli nie istnieją.
- Prosty log w terminalu — pokazuje co zostało przeniesione.

## Szybki start

1. **Klonuj repo lub pobierz plik**  
   Możesz skopiować `organizer.py` lub sklonować repozytorium.

2. **Uruchom skrypt**
   ```bash
   python organizer.py /ścieżka/do/folderu
