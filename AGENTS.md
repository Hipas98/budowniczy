# Projekt Fenix — AGENTS.md (Codex)

## Kontekst projektu

Budujemy: AI autopilot reputacji dla polskich firm usługowych (opinie Google, widoczność lokalna).
Owner: Damian — solo marketer, działa z Claude Code (interaktywnie) + Codex (async build).
Stack: Python, Streamlit → docelowo Flask/FastAPI + frontend, Claude API, Google Business Profile API, SMSAPI.pl.

## Zasady dla Codex

1. **Kod EN, komunikacja PL** — nazwy zmiennych, funkcji, pliki = angielski. Komentarze, commity, README = polski.
2. **Mały, testowalny output** — każde zadanie kończy się działającym kodem z minimum 1 testem lub manual test instruction.
3. **Żadnych nowych zależności bez listy** — jeśli dodajesz bibliotekę, wymień ją w PR description z uzasadnieniem.
4. **Polskie realia** — API, integracje, ceny, przepisy = polska perspektywa. SMS przez SMSAPI.pl (nie Twilio), płatności przez Przelewy24/Stripe PL, faktury przez iFirma API jeśli potrzeba.
5. **PRO standard** — żadnego placeholder UI, żadnych TODO w kodzie produkcyjnym, żadnych hardcoded secrets.

## Podział pracy: Claude Code vs Codex

### Claude Code robi:
- Decyzje architektoniczne
- Planowanie sprintów z Damianem
- Eksploracja kodu, debugowanie złożonych problemów
- Code review outputu Codexa
- Integracja i łączenie modułów
- Praca z lokalnym środowiskiem i sekretami

### Codex robi:
- Implementacja dobrze zdefiniowanych modułów (po briefie od Claude Code)
- Generowanie testów jednostkowych
- Powtarzalne komponenty (wiele podobnych widoków/endpointów)
- Refaktor i cleanup wskazanego kodu
- Dokumentacja techniczna (docstrings, README sekcje)

## Protokół handoff Claude Code → Codex

Przed delegowaniem do Codexa Claude Code przygotowuje brief w formacie:

```
TASK: [jednozdaniowy opis]
INPUT: [co Codex dostaje — pliki, dane, kontekst]
OUTPUT: [co ma zwrócić — plik, funkcja, test]
CONSTRAINTS: [co NIE wolno zmienić, jakie zależności, polskie realia]
DONE WHEN: [kryterium akceptacji — jak sprawdzić że działa]
```

## Aktywny moduł do budowy

**Produkt:** AI autopilot reputacji — QR kod + opinie Google + AI odpowiedzi po polsku.

Moduły w kolejności:
1. `qr_generator/` — generuje QR kod przekierowujący na wizytówkę Google firmy
2. `review_fetcher/` — pobiera opinie z Google Business Profile API
3. `reply_generator/` — Claude API generuje polską odpowiedź na opinię
4. `sms_sender/` — SMSAPI.pl integracja (plan premium)
5. `dashboard/` — panel właściciela firmy (Streamlit MVP → Flask docelowo)

## Środowisko

- Python 3.9+
- venv: `.venv/`
- Secrets: `.env` (nigdy do repo)
- Deploy: Streamlit Cloud (MVP) → VPS/Railway (produkcja)
- Repo: GitHub Hipas98

## Skróty

- Sprinty: `.budowniczy/sprints/`
- Brief do Codexa: `.budowniczy/codex-briefs/`
- Claude Code context: `CLAUDE.md`
