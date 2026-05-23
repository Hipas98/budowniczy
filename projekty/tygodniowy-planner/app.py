import streamlit as st

st.set_page_config(page_title="Planner 3-zmianowca", page_icon="📅", layout="centered")

ZMIANY = {
    "🟢 Popołudniówka (14–22) — najlepszy tydzień": {
        "godz_tydzien": 15,
        "deep_work": True,
        "zalecenia": [
            "Deep work rano 7–10 (zanim wyjdziesz do pracy)",
            "Planuj nowe funkcje, trudne decyzje, deploy",
            "Najlepszy tydzień na weekly bossa",
        ],
        "ostrzezenie": None,
    },
    "🟡 Ranna (6–14) — średni tydzień": {
        "godz_tydzien": 12,
        "deep_work": True,
        "zalecenia": [
            "Deep work wieczorem 19–22",
            "Planuj zadania średniej wagi",
            "Unikaj trudnych decyzji architektonicznych",
        ],
        "ostrzezenie": None,
    },
    "🔴 Nocna (22–6) — tydzień przetrwania": {
        "godz_tydzien": 7,
        "deep_work": False,
        "zalecenia": [
            "Tylko lekkie zadania: odpowiedzi, monitoring, drobne poprawki",
            "Nie planuj deployów ani ważnych decyzji",
            "Skup się na utrzymaniu tempa",
        ],
        "ostrzezenie": "⚠️ Tydzień przetrwania. Nie planuj niczego krytycznego.",
    },
    "🟢 Weekend — fundament": {
        "godz_tydzien": 10,
        "deep_work": True,
        "zalecenia": [
            "10h stabilnie niezależnie od zmiany",
            "Idealne na sprint i deploy",
            "Tu idzie ciężka praca tygodnia",
        ],
        "ostrzezenie": None,
    },
}

st.title("📅 Planner 3-zmianowca")
st.caption("Planuj tydzień zgodnie z realnym budżetem energii, nie złudzeniami.")

zmiana = st.selectbox("Jaki masz tydzień?", options=list(ZMIANY.keys()))
dane = ZMIANY[zmiana]

col1, col2 = st.columns(2)
with col1:
    st.metric("Budżet godzin", f"~{dane['godz_tydzien']}h / tydzień")
with col2:
    st.metric("Deep work", "✅ Tak" if dane["deep_work"] else "❌ Nie")

if dane["ostrzezenie"]:
    st.warning(dane["ostrzezenie"])

st.subheader("Co planować w ten tydzień")
for z in dane["zalecenia"]:
    st.markdown(f"- {z}")

st.divider()

st.subheader("Zadania na ten tydzień")
zadania_raw = st.text_area(
    "Wpisz zadania (jedno na linię):",
    height=150,
    placeholder="zbudować formularz wyboru zmiany\nnaprawić błąd w plannerze\nzrobić commit z opisem",
)

if zadania_raw.strip():
    zadania = [z.strip() for z in zadania_raw.strip().splitlines() if z.strip()]
    godz_na_zadanie = round(dane["godz_tydzien"] / len(zadania), 1)
    st.success(
        f"Masz **{len(zadania)} zadań** na **~{dane['godz_tydzien']}h** → "
        f"średnio **{godz_na_zadanie}h** na zadanie."
    )
