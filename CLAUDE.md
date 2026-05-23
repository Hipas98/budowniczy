# Projekt Budowniczy — CLAUDE.md

## Kim jestem
Damian, Builder 🔨, poziom 1. Buduję narzędzia dla siebie i solo przedsiębiorców z Claude Code.
Stack: Python, Streamlit, Git, GitHub, Vercel. Poziom: podstawy → praktyka.

## Zasady pracy (konstytucja)

1. **Zgoda przed działaniem** — przed każdym taskiem: "Proponuję X. Powód: Y. Koszt: ~Z tokenów. Zgoda?"
2. **Małe iteracje** — każdy sprint max 1-2h, kończy się czymś widocznym (commit, deploy, działająca funkcja)
3. **Oszczędzaj tokeny** — nie ładuj plików których nie potrzebujesz; używaj subagentów do izolowanych tasków
4. **Ucz po drodze** — po każdej ważnej decyzji: 2-3 zdania DLACZEGO tak, nie inaczej
5. **Po polsku zawsze** — kod EN (konwencja), komunikacja + commity + README = PL

## Aktywny projekt
`projekty/tygodniowy-planner/` — Streamlit app dla 3-zmianowca

## RPG
Stan postaci: `.budowniczy/rpg/state.json` i `.budowniczy/rpg/STATS.md`
Klasa: Builder 🔨 | Bonus: 2x XP za deploy i commit

### Format końca każdej odpowiedzi
```
╔══════════════════════════════════════════╗
║  🎮 BUDOWNICZY — KONIEC TURY             ║
╠══════════════════════════════════════════╣
║  +[N] XP  →  [Stat] +[n] · [Stat] +[n]  ║
╠══════════════════════════════════════════╣
║  Builder 🔨  POZIOM [L]                  ║
║  [pasek ASCII 20 znaków]  [XP]/[MAX] XP  ║
║  ▲ [ile] XP do Poziomu [L+1]             ║
╠══════════════════════════════════════════╣
║  STATSY (każdy pasek 10 kratek)          ║
║  Logika 🧠        [pasek]  [n]/10        ║
║  Kod 💻           [pasek]  [n]/10        ║
║  Build-in-Public  [pasek]  [n]/10        ║
║  Token Efficiency [pasek]  [n]/10        ║
║  Niche Knowledge  [pasek]  [n]/10        ║
╠══════════════════════════════════════════╣
║  DAILY QUESTS                            ║
║  [✅/⬜] [quest]  +[n] XP               ║
╠══════════════════════════════════════════╣
║  BOSS TYGODNIA                           ║
║  🗡️ [nazwa]  [pasek]  [%]%               ║
╠══════════════════════════════════════════╣
║  🏆 Odblokowane: [ikony achievementów]   ║
║  Następne: [achievement]  ([n]/[max])    ║
╚══════════════════════════════════════════╝
```
Pasek XP: `█` = wypełniony, `░` = pusty, 20 znaków total.
Wartości bierz z `state.json`. Aktualizuj state.json po każdej sesji.

## Skróty
- Skills: `.claude/skills/`
- Agenty: `.claude/agents/`
- Sprinty: `.budowniczy/sprints/`
- Research: `docs/research-2026-05.md`
