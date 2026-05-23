# Skill: nowy-projekt

## Cel
Inicjalizuje nowy projekt w `projekty/nazwa/` z gotową strukturą plików.

## Kiedy używać
Na początku każdego nowego projektu, przed napisaniem pierwszej linijki kodu.

## Kroki
1. Stwórz folder `projekty/[nazwa]/`
2. Stwórz `app.py` z minimalnym stub:
   ```python
   import streamlit as st
   st.set_page_config(page_title="[Nazwa]", page_icon="🔧")
   st.title("[Nazwa]")
   st.write("W budowie...")
   ```
3. Stwórz `requirements.txt` z `streamlit>=1.32.0`
4. Stwórz `README.md` z sekcjami: opis, jak uruchomić, stack
5. Dodaj wpis do `.budowniczy/sprints/sprint-NN.md`
6. Zaktualizuj `active_project` w `state.json`

## Czego unikać
- Nie twórz podfolderów na start (jeden plik wystarczy do ~200 linii)
- Nie instaluj paczek "na zapas"
- Nie pisz logiki przed strukturą
