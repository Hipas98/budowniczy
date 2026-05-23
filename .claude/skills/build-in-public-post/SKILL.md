# Skill: build-in-public-post

## Cel
Generuje draft posta X (thread) i LinkedIn po ukończonym sprincie. Wywołuje agenta content-writer.

## Kiedy używać
Po każdym sprincie który kończy się czymś widocznym (deploy, nowa funkcja, działające demo).

## Kroki
1. Zbierz info o sprincie:
   - Co zbudowano (1 zdanie)
   - Stack użyty
   - Czas budowy (h)
   - Link do demo lub repo
   - Co było trudne / czego się nauczyłem
2. Wywołaj agenta `content-writer` z tymi danymi
3. Pokaż Damianowi draft do zatwierdzenia
4. Damian publikuje samodzielnie — agent NIE publikuje

## Format wejścia dla content-writer
```
Sprint: [numer i nazwa]
Co zbudowano: [opis]
Stack: [technologie]
Czas: [Xh]
Demo: [URL lub "brak"]
Trudność: [co było trudne]
Lekcja: [czego się nauczyłem]
```

## Czego unikać
- Nie publikuj bez zatwierdzenia Damiana
- Nie generuj posta jeśli nie ma widocznego efektu (brak demo = brak posta)
