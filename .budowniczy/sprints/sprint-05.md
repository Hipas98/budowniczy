# Sprint 05 — 2026-05-23 — Generator Ofert dla Lokalnych Biznesów

## Cel
Działający generator copywriterskich tekstów na stronę www dla lokalnych biznesów.
Wejście: dane firmy. Wyjście: hero, opis usług, wyróżniki, CTA — gotowe do wklejenia.

## Pliki
- `projekty/generator-ofert/app.py` — UI Streamlit
- `projekty/generator-ofert/generator.py` — integracja Claude API (Haiku)
- `projekty/generator-ofert/prompts.py` — system prompt + builder promptu użytkownika
- `projekty/generator-ofert/requirements.txt`
- `projekty/generator-ofert/README.md`

## Status
🔄 W trakcie — gotowe do testu lokalnego

## Następny krok
1. `export ANTHROPIC_API_KEY="..."` + `streamlit run app.py`
2. Test z przykładowym biznesem (np. salon fryzjerski Toruń)
3. Commit po polsku
4. Deploy na Streamlit Cloud (`/deploy-streamlit`)
5. Post build-in-public (`/build-in-public-post`)
