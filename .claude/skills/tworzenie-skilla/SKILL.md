# Skill: tworzenie-skilla

## Cel
Wzorzec do tworzenia nowego skilla w `.claude/skills/nazwa-skilla/SKILL.md`.

## Kiedy tworzyć skill
Gdy wykonujesz tę samą instrukcję po raz drugi. Zamiast pisać 200 słów za każdym razem — skill wywoła się jednym zdaniem.

## Struktura każdego SKILL.md
```markdown
# Skill: nazwa-skilla

## Cel
Jedno zdanie — co ten skill robi.

## Kiedy używać
Konkretne warunki wyzwalające (nie ogólne).

## Kroki
1. Krok pierwszy
2. Krok drugi
3. ...

## Przykład
Krótki przykład wejścia → wyjścia.

## Czego unikać
Lista antywzorców.
```

## Zasady
- Nazwa folderu: kebab-case, po polsku
- Max 50 linii — jeśli dłuższy, podziel na dwa skille
- Konkretne kroki, nie ogólne opisy
- Skill musi dać się wywołać bez dodatkowego kontekstu
