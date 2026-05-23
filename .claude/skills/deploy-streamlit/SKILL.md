# Skill: deploy-streamlit

## Cel
Krok po kroku deploy aplikacji Streamlit na Streamlit Cloud (darmowy hosting).

## Wymagania wstępne
- Repo publiczne lub prywatne na GitHub (konto Hipas98)
- Plik `requirements.txt` w folderze projektu
- Plik `app.py` jako punkt wejścia

## Kroki
1. **Commit i push** — upewnij się że ostatnie zmiany są na GitHubie
   ```bash
   git add -A && git commit -m "dodaj: [opis]" && git push
   ```
2. **Wejdź na** `share.streamlit.io` → zaloguj się GitHubem (Hipas98)
3. **Kliknij** "Create app" (prawy górny róg)
4. **Wypełnij formularz:**
   - Repository: `Hipas98/budowniczy`
   - Branch: `main`
   - Main file path: `projekty/[nazwa-projektu]/app.py`
   - App URL: wybierz własną nazwę (np. `kalkulator-jdg`)
5. **Kliknij** "Deploy" — czekaj 1-3 minuty
6. **Po deployu** — skopiuj URL i wklej do `README.md` projektu

## Aktualizacja po zmianach
Po każdym `git push` Streamlit Cloud **automatycznie** przebudowuje aplikację. Nie musisz nic robić.

## Jeśli deploy się nie udaje
- Sprawdź logi w panelu Streamlit Cloud (zakładka "Manage app")
- Najczęstszy błąd: brakująca paczka w `requirements.txt`
- Drugi najczęstszy: błąd składni w `app.py` (sprawdź lokalnie najpierw)
