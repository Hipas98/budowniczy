import streamlit as st
from obliczenia import porownaj, ZUS_PREFERENC, ZUS_NORMALNY

st.set_page_config(
    page_title="Kalkulator JDG",
    page_icon="🧮",
    layout="centered",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', system-ui, -apple-system, sans-serif;
    font-size: 16px;
}

/* tło strony */
.stApp { background: #F8F9FA; }

/* ukryj toolbar Streamlit */
[data-testid="stToolbar"] { display: none; }

/* główna karta wyniku */
.winner-card {
    background: #EFF6FF;
    border-left: 5px solid #2563EB;
    border-radius: 12px;
    padding: 24px 28px;
    margin: 16px 0;
}
.winner-label {
    font-size: 13px;
    font-weight: 600;
    color: #2563EB;
    text-transform: uppercase;
    letter-spacing: .06em;
    margin-bottom: 4px;
}
.winner-amount {
    font-size: 42px;
    font-weight: 700;
    color: #1E3A5F;
    line-height: 1.1;
}
.winner-sub {
    font-size: 14px;
    color: #64748B;
    margin-top: 6px;
}

/* karty porównania */
.compare-card {
    background: white;
    border-radius: 12px;
    padding: 18px 20px;
    margin-bottom: 10px;
    box-shadow: 0 1px 4px rgba(0,0,0,.07);
    border-left: 4px solid #E2E8F0;
}
.compare-card.best { border-left-color: #2563EB; }
.compare-card.good { border-left-color: #10B981; }
.compare-card.bad  { border-left-color: #94A3B8; }

.compare-title {
    font-weight: 600;
    font-size: 15px;
    color: #1E293B;
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 10px;
}
.compare-netto {
    font-size: 22px;
    font-weight: 700;
    color: #1E293B;
}
.compare-mc {
    font-size: 13px;
    color: #64748B;
    margin-top: 2px;
}
.compare-row {
    display: flex;
    justify-content: space-between;
    font-size: 13px;
    color: #64748B;
    padding: 3px 0;
    border-top: 1px solid #F1F5F9;
    margin-top: 8px;
}
.compare-row span { color: #334155; font-weight: 500; }

/* alert przekroczenia progu */
.prog-alert {
    background: #FEF2F2;
    border-left: 4px solid #DC2626;
    border-radius: 8px;
    padding: 12px 16px;
    font-size: 14px;
    color: #991B1B;
    margin: 8px 0;
}

/* sekcja inputów */
.input-section {
    background: white;
    border-radius: 12px;
    padding: 24px 24px 16px;
    box-shadow: 0 1px 4px rgba(0,0,0,.06);
    margin-bottom: 20px;
}

/* disclaimer */
.disclaimer {
    font-size: 12px;
    color: #94A3B8;
    text-align: center;
    padding: 16px;
    margin-top: 8px;
}

/* usuń padding Streamlit z number_input label */
div[data-testid="stNumberInput"] label { font-weight: 600; }
div[data-testid="stSlider"] label { font-weight: 600; color: #1E293B; }
</style>
""", unsafe_allow_html=True)


# ── NAGŁÓWEK ────────────────────────────────────────────────────────────────

st.markdown("## 🧮 Kalkulator JDG")
st.markdown("<p style='color:#64748B;margin-top:-10px;margin-bottom:20px;'>Ile zostaje na rękę przy różnych formach podatku? Wynik od razu.</p>", unsafe_allow_html=True)


# ── INPUTY ──────────────────────────────────────────────────────────────────

st.markdown('<div class="input-section">', unsafe_allow_html=True)

przychod = st.slider(
    "💰 Co miesięcznie zarabiasz? (zł brutto)",
    min_value=2_000, max_value=50_000,
    value=8_000, step=500,
    help="Kwota na fakturze — bez odejmowania czegokolwiek",
)

col1, col2 = st.columns(2)
with col1:
    ma_koszty = st.toggle("Mam koszty firmowe", value=False,
                          help="Sprzęt, oprogramowanie, telefon na firmę — tylko przy liniowym i skali")
with col2:
    zus_pref = st.toggle("Preferencyjny ZUS (~415 zł/mc)",
                         value=True,
                         help="Dostępny przez pierwsze 24 miesiące działalności")

koszty = 0
if ma_koszty:
    koszty = st.slider(
        "📦 Miesięczne koszty firmowe (zł)",
        min_value=0, max_value=10_000,
        value=500, step=100,
    )

zus_mc = ZUS_PREFERENC if zus_pref else ZUS_NORMALNY

st.markdown('</div>', unsafe_allow_html=True)


# ── OBLICZENIA ───────────────────────────────────────────────────────────────

wyniki = porownaj(przychod, koszty, zus_mc)
najlepsza = wyniki[0]
roznica_roczna = wyniki[0]["netto"] - wyniki[-1]["netto"]


# ── WYNIK GŁÓWNY ─────────────────────────────────────────────────────────────

st.markdown(f"""
<div class="winner-card">
    <div class="winner-label">🏆 Najlepsza forma: {najlepsza['forma']}</div>
    <div class="winner-amount">{najlepsza['netto']/12:,.0f} zł / miesiąc</div>
    <div class="winner-sub">
        {najlepsza['netto']:,.0f} zł rocznie &nbsp;·&nbsp;
        efektywne obciążenie: {najlepsza['efektywna']:.1f}% &nbsp;·&nbsp;
        różnica z najgorszą formą: <strong>{roznica_roczna:,.0f} zł / rok</strong>
    </div>
</div>
""", unsafe_allow_html=True)

# alert 32% próg
if przychod * 12 > 120_000:
    st.markdown("""<div class="prog-alert">
        ⚠️ Twój roczny przychód przekracza 120 000 zł — wchodzisz w próg 32% przy skali podatkowej.
    </div>""", unsafe_allow_html=True)


# ── PORÓWNANIE KART ──────────────────────────────────────────────────────────

st.markdown("#### Porównanie wszystkich form")

MEDALE = ["🥇", "🥈", "🥉", "4️⃣"]
KLASY  = ["best", "good", "bad", "bad"]

for i, w in enumerate(wyniki):
    st.markdown(f"""
    <div class="compare-card {KLASY[i]}">
        <div class="compare-title">{MEDALE[i]} {w['forma']}</div>
        <div class="compare-netto">{w['netto']/12:,.0f} zł / miesiąc</div>
        <div class="compare-mc">{w['netto']:,.0f} zł rocznie &nbsp;·&nbsp; obciążenie {w['efektywna']:.1f}%</div>
        <div class="compare-row">Podatek dochodowy <span>{w['podatek']:,.0f} zł/rok</span></div>
        <div class="compare-row">Składka ZUS <span>{w['zus']:,.0f} zł/rok</span></div>
        <div class="compare-row">Składka zdrowotna <span>{w['zdrowotna']:,.0f} zł/rok</span></div>
    </div>
    """, unsafe_allow_html=True)


# ── DISCLAIMER ───────────────────────────────────────────────────────────────

st.markdown("""<div class="disclaimer">
Wartości orientacyjne dla 2026 r. Nie stanowi porady podatkowej.<br>
Przed wyborem formy opodatkowania skonsultuj się z księgową lub doradcą podatkowym.
</div>""", unsafe_allow_html=True)
