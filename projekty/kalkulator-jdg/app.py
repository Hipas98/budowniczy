import streamlit as st
from obliczenia import porownaj, ZUS_PREFERENC, ZUS_NORMALNY

st.set_page_config(
    page_title="Kalkulator JDG 2026",
    page_icon="📊",
    layout="centered",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', system-ui, sans-serif;
}

.stApp { background: #0F172A; }
[data-testid="stToolbar"] { display: none; }
[data-testid="stDecoration"] { display: none; }
header[data-testid="stHeader"] { display: none; }

/* hero */
.hero {
    padding: 48px 0 36px;
    text-align: center;
}
.hero-title {
    font-size: 38px;
    font-weight: 800;
    color: #F8FAFC;
    letter-spacing: -0.02em;
    line-height: 1.1;
    margin-bottom: 12px;
}
.hero-sub {
    font-size: 17px;
    color: #94A3B8;
    max-width: 480px;
    margin: 0 auto;
    line-height: 1.6;
}

/* panel inputów */
.input-panel {
    background: #1E293B;
    border-radius: 16px;
    padding: 32px;
    margin-bottom: 28px;
    border: 1px solid #334155;
}

/* display kwoty */
.amount-display {
    text-align: center;
    padding: 24px 0 16px;
}
.amount-value {
    font-size: 52px;
    font-weight: 800;
    color: #38BDF8;
    letter-spacing: -0.03em;
    line-height: 1;
}
.amount-label {
    font-size: 14px;
    color: #64748B;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-top: 6px;
}

/* override Streamlit slider */
div[data-testid="stSlider"] > label {
    font-size: 14px !important;
    font-weight: 600 !important;
    color: #94A3B8 !important;
    text-transform: uppercase;
    letter-spacing: 0.06em;
}

/* sekcja opcji */
.options-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-top: 24px;
}
.option-box {
    background: #0F172A;
    border-radius: 10px;
    padding: 16px 18px;
    border: 1px solid #334155;
}
.option-label {
    font-size: 12px;
    font-weight: 600;
    color: #64748B;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-bottom: 8px;
}

/* karta zwycięzcy */
.winner {
    background: linear-gradient(135deg, #1D4ED8 0%, #0EA5E9 100%);
    border-radius: 16px;
    padding: 32px;
    margin-bottom: 28px;
    position: relative;
    overflow: hidden;
}
.winner::before {
    content: "NAJLEPSZA FORMA";
    position: absolute;
    top: 20px;
    right: 20px;
    font-size: 11px;
    font-weight: 700;
    color: rgba(255,255,255,0.6);
    letter-spacing: 0.1em;
}
.winner-name {
    font-size: 15px;
    font-weight: 600;
    color: rgba(255,255,255,0.8);
    margin-bottom: 8px;
}
.winner-amount {
    font-size: 56px;
    font-weight: 800;
    color: #FFFFFF;
    letter-spacing: -0.03em;
    line-height: 1;
    margin-bottom: 8px;
}
.winner-period {
    font-size: 16px;
    color: rgba(255,255,255,0.7);
    margin-bottom: 20px;
}
.winner-stats {
    display: flex;
    gap: 24px;
    padding-top: 20px;
    border-top: 1px solid rgba(255,255,255,0.2);
}
.winner-stat { flex: 1; }
.winner-stat-val {
    font-size: 20px;
    font-weight: 700;
    color: #FFFFFF;
}
.winner-stat-key {
    font-size: 12px;
    color: rgba(255,255,255,0.6);
    margin-top: 2px;
}

/* karty porównania */
.section-label {
    font-size: 12px;
    font-weight: 700;
    color: #64748B;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 14px;
}
.compare-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-bottom: 28px;
}
.ccard {
    background: #1E293B;
    border-radius: 12px;
    padding: 20px;
    border: 1px solid #334155;
    position: relative;
}
.ccard-accent {
    width: 100%;
    height: 3px;
    border-radius: 2px;
    margin-bottom: 14px;
}
.ccard-rank {
    font-size: 11px;
    font-weight: 700;
    color: #64748B;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 4px;
}
.ccard-name {
    font-size: 14px;
    font-weight: 600;
    color: #E2E8F0;
    margin-bottom: 12px;
}
.ccard-netto {
    font-size: 26px;
    font-weight: 800;
    color: #F8FAFC;
    letter-spacing: -0.02em;
    line-height: 1;
}
.ccard-period { font-size: 12px; color: #64748B; margin-top: 2px; margin-bottom: 12px; }
.ccard-row {
    display: flex;
    justify-content: space-between;
    font-size: 12px;
    color: #64748B;
    padding: 5px 0;
    border-top: 1px solid #0F172A;
}
.ccard-row span { color: #94A3B8; }

/* alert */
.alert {
    background: #450A0A;
    border: 1px solid #DC2626;
    border-radius: 10px;
    padding: 14px 18px;
    font-size: 14px;
    color: #FCA5A5;
    margin-bottom: 20px;
}

/* disclaimer */
.disclaimer {
    text-align: center;
    font-size: 12px;
    color: #475569;
    padding: 24px 16px;
    line-height: 1.7;
}

/* override toggle i radio */
div[data-testid="stToggle"] label { color: #CBD5E1 !important; font-size: 14px !important; }
div[data-testid="stRadio"] label { color: #CBD5E1 !important; }
div[data-testid="stRadio"] > label { font-size: 13px !important; font-weight: 600 !important; color: #94A3B8 !important; text-transform: uppercase !important; letter-spacing: 0.06em !important; }
</style>
""", unsafe_allow_html=True)

# ── KOLORY FORM ──────────────────────────────────────────────────────────────
KOLORY = {
    "Ryczałt 8%":     "#10B981",   # zielony
    "Ryczałt 12%":    "#F59E0B",   # żółty
    "Liniowy 19%":    "#F97316",   # pomarańczowy
    "Skala 12%/32%":  "#8B5CF6",   # fioletowy
}

# ── HERO ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-title">Kalkulator JDG 2026</div>
    <div class="hero-sub">
        Przesuń suwak i od razu sprawdź, ile zostaje na rękę
        przy każdej formie opodatkowania.
    </div>
</div>
""", unsafe_allow_html=True)

# ── INPUTY ───────────────────────────────────────────────────────────────────
st.markdown('<div class="input-panel">', unsafe_allow_html=True)

przychod = st.slider(
    "MIESIĘCZNY PRZYCHÓD NA FAKTURZE",
    min_value=2_000, max_value=50_000,
    value=8_000, step=500,
)

st.markdown(f"""
<div class="amount-display">
    <div class="amount-value">{przychod:,} zł</div>
    <div class="amount-label">miesięcznie brutto</div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    zus_pref = st.toggle(
        "Preferencyjny ZUS (pierwsze 24 mc)",
        value=True,
        help="~415 zł/mc zamiast ~1 773 zł/mc"
    )
with col2:
    ma_koszty = st.toggle(
        "Mam koszty firmowe",
        value=False,
        help="Sprzęt, oprogramowanie, telefon — odliczane przy liniowym i skali"
    )

koszty = 0
if ma_koszty:
    koszty = st.slider(
        "MIESIĘCZNE KOSZTY FIRMOWE",
        min_value=0, max_value=10_000,
        value=500, step=100,
    )

zus_mc = ZUS_PREFERENC if zus_pref else ZUS_NORMALNY
st.markdown('</div>', unsafe_allow_html=True)

# ── OBLICZENIA ────────────────────────────────────────────────────────────────
wyniki = porownaj(przychod, koszty, zus_mc)
najlepsza = wyniki[0]
roznica = wyniki[0]["netto"] - wyniki[-1]["netto"]

# ── ALERT ────────────────────────────────────────────────────────────────────
if przychod * 12 > 120_000:
    st.markdown("""<div class="alert">
        ⚠️ Roczny przychód powyżej 120 000 zł — przy skali podatkowej wchodzisz w próg 32%.
    </div>""", unsafe_allow_html=True)

# ── WINNER CARD ───────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="winner">
    <div class="winner-name">{najlepsza['forma']}</div>
    <div class="winner-amount">{najlepsza['netto']/12:,.0f} zł</div>
    <div class="winner-period">miesięcznie na rękę</div>
    <div class="winner-stats">
        <div class="winner-stat">
            <div class="winner-stat-val">{najlepsza['netto']:,.0f} zł</div>
            <div class="winner-stat-key">rocznie netto</div>
        </div>
        <div class="winner-stat">
            <div class="winner-stat-val">{najlepsza['efektywna']:.1f}%</div>
            <div class="winner-stat-key">obciążenie</div>
        </div>
        <div class="winner-stat">
            <div class="winner-stat-val">+{roznica:,.0f} zł</div>
            <div class="winner-stat-key">vs najgorsza forma / rok</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── PORÓWNANIE ────────────────────────────────────────────────────────────────
RANKI = ["🥇 1. miejsce", "🥈 2. miejsce", "🥉 3. miejsce", "4️⃣ 4. miejsce"]

st.markdown('<div class="section-label">Porównanie wszystkich form</div>', unsafe_allow_html=True)
st.markdown('<div class="compare-grid">', unsafe_allow_html=True)

for i, w in enumerate(wyniki):
    kolor = KOLORY.get(w["forma"], "#64748B")
    st.markdown(f"""
    <div class="ccard">
        <div class="ccard-accent" style="background:{kolor}"></div>
        <div class="ccard-rank">{RANKI[i]}</div>
        <div class="ccard-name">{w['forma']}</div>
        <div class="ccard-netto">{w['netto']/12:,.0f} zł</div>
        <div class="ccard-period">/ miesiąc &nbsp;·&nbsp; {w['efektywna']:.1f}% obciążenia</div>
        <div class="ccard-row">Podatek dochodowy <span>{w['podatek']:,.0f} zł/rok</span></div>
        <div class="ccard-row">ZUS <span>{w['zus']:,.0f} zł/rok</span></div>
        <div class="ccard-row">Zdrowotna <span>{w['zdrowotna']:,.0f} zł/rok</span></div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ── DISCLAIMER ────────────────────────────────────────────────────────────────
st.markdown("""<div class="disclaimer">
    Wartości orientacyjne dla 2026 r. Nie uwzględnia ulg, IP Box ani wszystkich wyjątków.<br>
    Przed wyborem formy opodatkowania skonsultuj się z księgową lub doradcą podatkowym.
</div>""", unsafe_allow_html=True)
