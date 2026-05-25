SYSTEM_PROMPT = """Jesteś doświadczonym konsultantem marketingowym z 15+ latami praktyki z małymi i średnimi firmami w Polsce.
Twoja specjalność to diagnoza problemów marketingowych i wskazywanie konkretnych, szybkich poprawek — bez buzzwordów i ogólników.

Zasady odpowiedzi:
- Pisz po polsku, bezpośrednio i konkretnie
- Nie używaj motywacyjnych fraz ("świetny pomysł!", "gratulacje za odwagę!")
- Każda rekomendacja musi być możliwa do wdrożenia w ciągu 30 dni
- Wskazuj liczby, przedziały czasowe i konkretne działania — nie "popraw komunikację", tylko "dodaj na stronę główną jedno zdanie opisujące efekt dla klienta, nie cechę produktu"
- Jeśli coś jest źle zrobione — powiedz to wprost, bez owijania w bawełnę
- Diagnoza ma pomagać właścicielowi firmy, nie sprawiać żeby się dobrze poczuł"""


def build_prompt(data: dict) -> str:
    """Buduje prompt użytkownika z danych formularza."""

    traffic_sources = ", ".join(data.get("traffic_sources", [])) or "nie podano"

    prompt = f"""Przeprowadź diagnozę marketingową firmy na podstawie poniższych danych.
Odpowiedz w strukturze którą podaję na końcu.

---
## DANE O FIRMIE

**Oferta i wartość dla klienta:**
{data.get("offer", "brak danych")}

**Historia i najlepszy miesiąc:**
{data.get("history", "brak danych")}

**Model sprzedaży:** {data.get("business_model", "brak danych")}

**Średnia wartość transakcji / LTV:**
{data.get("aov", "brak danych")}

---
## KLIENT

**Najlepszy klient (opis):**
{data.get("best_customer", "brak danych")}

**Problem który rozwiązujesz (co klient robiłby bez Ciebie):**
{data.get("problem_solved", "brak danych")}

**Dlaczego klienci wybierają właśnie Ciebie:**
{data.get("why_you", "brak danych")}

**Zły klient / kto NIE jest Twoim klientem:**
{data.get("bad_customer", "brak danych")}

---
## LICZBY I KANAŁY

**Miesięczny budżet marketingowy:** {data.get("budget", "brak danych")} PLN

**Źródła klientów:** {traffic_sources}

**Kanał z najlepszymi klientami:** {data.get("best_channel", "brak danych")}

**Zamówienia miesięcznie:** {data.get("monthly_orders", "brak danych")}

**Świadomość CAC:** {data.get("cac_awareness", "brak danych")}

**Szacowany koszt pozyskania klienta:** {data.get("cac", "brak danych")} PLN

---
## CO DZIAŁA, CO NIE

**Co działa marketingowo:**
{data.get("what_works", "brak danych")}

**Co nie zadziałało:**
{data.get("what_failed", "brak danych")}

**Gdzie w lejku tracisz klientów:**
{data.get("funnel_leak", "brak danych")}

**Największa frustracja z marketingiem:**
{data.get("frustration", "brak danych")}

---
## KONKURENCJA

**Główni konkurenci:**
{data.get("competitors", "brak danych")}

**Co robią lepiej od Ciebie:**
{data.get("competitor_advantage", "brak danych")}

**Co Ty masz czego oni nie mają:**
{data.get("my_advantage", "brak danych")}

---

## STRUKTURA DIAGNOZY (odpowiedz dokładnie w tej strukturze)

### 🔍 Główny problem marketingowy
[Jedno zdanie opisujące najpoważniejszą przyczynę słabych wyników. Nie listuj — wskaż jedną, główną przyczynę.]

### 🚑 3 szybkie wygrane (do 30 dni)
[3 konkretne działania które można wdrożyć w ciągu miesiąca bez dużego budżetu. Dla każdego: co zrobić + dlaczego to pomoże + szacowany efekt.]

### 📊 Diagnoza kanałów
[Oceń obecne kanały: które warto rozwijać, które ciąć, czego brakuje. Bądź konkretny — nie "rozważ LinkedIn", tylko "LinkedIn odpada przy tym budżecie i tym targecie; zostań przy X bo Y".]

### 🔧 Lejek sprzedażowy — gdzie jest dziura
[Wskaż dokładnie gdzie tracisz klientów i co to konkretnie naprawia. Jedno główne miejsce, jedna konkretna poprawka.]

### ⚡ Priorytet na najbliższe 90 dni
[Jedna rzecz — gdyby właściciel mógł zrobić tylko jedną zmianę w marketingu przez najbliższe 3 miesiące, co to powinno być i dlaczego.]
"""

    return prompt
