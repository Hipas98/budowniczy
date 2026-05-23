# Token Budget — log sprintów

## Format wpisu
```
## Sprint N — [data] — [nazwa]
- Tokeny: ~X (szacunek)
- Co zjadło najwięcej: [opis]
- Co można było zrobić taniej: [opis]
- Lekcja: [1 reguła na przyszłość]
```

---

## Sprint 0 — 2026-05-21 — Inicjalizacja struktury
- Tokeny: ~5000 (szacunek)
- Co zjadło najwięcej: tworzenie wielu plików naraz (Write calls)
- Co można było zrobić taniej: subagent do generowania plików RPG zamiast robienia tego w głównym kontekście
- Lekcja: powtarzalne zadania (generowanie JSON-ów, tworzenie plików szablonowych) deleguj do subagenta — Twój kontekst nie puchnie
