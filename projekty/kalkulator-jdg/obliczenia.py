"""
Obliczenia podatkowe dla JDG w Polsce (2026).
Wartości orientacyjne — nie stanowi porady podatkowej.
"""

# ZUS 2026 (zł/mc)
ZUS_PREFERENC = 415    # pierwsze 24 mc działalności
ZUS_NORMALNY = 1773    # po preferencyjnym

# Progi podatkowe 2026
KWOTA_WOLNA = 30_000
PROG_SKALI = 120_000

# Minimalna składka zdrowotna (zł/mc)
ZDROWOTNA_MIN_MC = 314.96


def _zdrowotna_ryczalt_roczna(przychod_roczny: float) -> float:
    """Składka zdrowotna przy ryczałcie — zależy od progu przychodu."""
    if przychod_roczny <= 60_000:
        return 376.16 * 12
    elif przychod_roczny <= 300_000:
        return 626.93 * 12
    return 1128.48 * 12


def ryczalt(przychod_mc: float, stawka: float, zus_mc: float) -> dict:
    p = przychod_mc * 12
    zus = zus_mc * 12
    zdrowotna = _zdrowotna_ryczalt_roczna(p)
    podatek = p * stawka
    lacznie = podatek + zus + zdrowotna
    return {
        "forma": f"Ryczałt {int(stawka * 100)}%",
        "przychod": p,
        "podatek": podatek,
        "zus": zus,
        "zdrowotna": zdrowotna,
        "lacznie_daniny": lacznie,
        "netto": p - lacznie,
        "efektywna": lacznie / p * 100 if p else 0,
    }


def liniowy(przychod_mc: float, koszty_mc: float, zus_mc: float) -> dict:
    p = przychod_mc * 12
    k = koszty_mc * 12
    zus = zus_mc * 12
    dochod = max(0.0, p - k - zus)
    podatek = dochod * 0.19
    zdrowotna = max(ZDROWOTNA_MIN_MC * 12, dochod * 0.049)
    lacznie = podatek + zus + zdrowotna
    return {
        "forma": "Liniowy 19%",
        "przychod": p,
        "dochod": dochod,
        "podatek": podatek,
        "zus": zus,
        "zdrowotna": zdrowotna,
        "lacznie_daniny": lacznie,
        "netto": p - k - lacznie,
        "efektywna": lacznie / p * 100 if p else 0,
    }


def skala(przychod_mc: float, koszty_mc: float, zus_mc: float) -> dict:
    p = przychod_mc * 12
    k = koszty_mc * 12
    zus = zus_mc * 12
    dochod = max(0.0, p - k - zus)
    podstawa = max(0.0, dochod - KWOTA_WOLNA)
    if podstawa <= (PROG_SKALI - KWOTA_WOLNA):
        podatek = podstawa * 0.12
    else:
        podatek = (PROG_SKALI - KWOTA_WOLNA) * 0.12 + (podstawa - (PROG_SKALI - KWOTA_WOLNA)) * 0.32
    zdrowotna = max(ZDROWOTNA_MIN_MC * 12, dochod * 0.09)
    lacznie = podatek + zus + zdrowotna
    return {
        "forma": "Skala 12%/32%",
        "przychod": p,
        "dochod": dochod,
        "podatek": podatek,
        "zus": zus,
        "zdrowotna": zdrowotna,
        "lacznie_daniny": lacznie,
        "netto": p - k - lacznie,
        "efektywna": lacznie / p * 100 if p else 0,
    }


def porownaj(przychod_mc: float, koszty_mc: float = 0.0, zus_mc: float = ZUS_PREFERENC) -> list[dict]:
    """Zwraca listę wyników dla wszystkich form — posortowaną od najwyższego netto."""
    wyniki = [
        ryczalt(przychod_mc, 0.085, zus_mc),
        ryczalt(przychod_mc, 0.12, zus_mc),
        liniowy(przychod_mc, koszty_mc, zus_mc),
        skala(przychod_mc, koszty_mc, zus_mc),
    ]
    return sorted(wyniki, key=lambda w: w["netto"], reverse=True)
