import streamlit as st
from obliczenia import porownaj, ZUS_PREFERENC, ZUS_NORMALNY

st.set_page_config(page_title="Kalkulator JDG", page_icon="🧮", layout="centered")

st.title("🧮 Kalkulator JDG")
st.caption("Ile zostaje netto przy różnych formach opodatkowania? Porównanie w 10 sekund.")
st.warning("Wartości orientacyjne dla 2026 r. Skonsultuj wybór formy z księgową.", icon="⚠️")

st.divider()

col1, col2 = st.columns(2)
with col1:
    przychod = st.number_input(
        "Miesięczny przychód brutto (zł)",
        min_value=0, max_value=500_000,
        value=8_000, step=500,
    )
with col2:
    koszty = st.number_input(
        "Miesięczne koszty firmowe (zł)",
        min_value=0, max_value=100_000,
        value=0, step=200,
        help="Sprzęt, oprogramowanie, telefon — tylko przy liniowym i skali",
    )

zus_opcja = st.radio(
    "Składka ZUS",
    ["Preferencyjny (pierwsze 24 mc) — ~415 zł/mc",
     "Normalny (po preferencyjnym) — ~1 773 zł/mc"],
    horizontal=True,
)
zus_mc = ZUS_PREFERENC if "Preferencyjny" in zus_opcja else ZUS_NORMALNY

st.divider()

if przychod == 0:
    st.info("Wpisz miesięczny przychód żeby zobaczyć porównanie.")
    st.stop()

wyniki = porownaj(przychod, koszty, zus_mc)
najlepsza = wyniki[0]["forma"]

st.subheader("Porównanie roczne — od najlepszego netto")

for i, w in enumerate(wyniki):
    medal = ["🥇", "🥈", "🥉", "4️⃣"][i]
    etykieta = f"{medal} {w['forma']}"
    kolor = "green" if i == 0 else ("orange" if i == 1 else "gray")

    with st.expander(f"{etykieta} — netto **{w['netto']:,.0f} zł/rok** ({w['netto']/12:,.0f} zł/mc)", expanded=(i == 0)):
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Podatek", f"{w['podatek']:,.0f} zł")
        c2.metric("ZUS", f"{w['zus']:,.0f} zł")
        c3.metric("Zdrowotna", f"{w['zdrowotna']:,.0f} zł")
        c4.metric("Eff. obciążenie", f"{w['efektywna']:.1f}%")

st.divider()

najlepsza_wynik = wyniki[0]
roznica = wyniki[0]["netto"] - wyniki[-1]["netto"]
st.success(
    f"**{najlepsza}** daje Ci **{najlepsza_wynik['netto']/12:,.0f} zł netto / miesiąc** "
    f"({najlepsza_wynik['netto']:,.0f} zł / rok). "
    f"Różnica między najlepszą a najgorszą formą: **{roznica:,.0f} zł rocznie**."
)

st.caption("Kalkulator nie uwzględnia ulg, IP Box, wspólnego rozliczenia z małżonkiem ani wszystkich wyjątków. "
           "Przed wyborem formy opodatkowania skonsultuj się z doradcą podatkowym lub księgową.")
