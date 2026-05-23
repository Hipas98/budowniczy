# Skill: commit-po-polsku

## Cel
Twórz commity w języku polskim, zwięźle, z prefixem typu zmiany.

## Format
```
[typ]: krótki opis co i dlaczego (max 72 znaki)
```

## Typy
- `dodaj:` — nowa funkcja lub plik
- `napraw:` — naprawa błędu
- `zmień:` — modyfikacja istniejącego kodu
- `usuń:` — usunięcie kodu lub pliku
- `docs:` — dokumentacja
- `styl:` — formatowanie, bez zmiany logiki
- `refaktor:` — reorganizacja bez zmiany funkcji

## Przykłady
```
dodaj: formularz wyboru zmiany (ranna/popołudniówka/nocna)
napraw: błąd liczenia godzin przy nocnej zmianie
zmień: kolor paska energii z zielonego na niebieski
docs: README z instrukcją uruchomienia lokalnego
```

## Czego unikać
- "update", "fix", "change" — zawsze po polsku
- Opisy co zrobiłeś zamiast dlaczego
- Commity bez prefiksu
