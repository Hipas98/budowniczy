import json
import os
import streamlit as st
from fpdf import FPDF
from fpdf.enums import XPos, YPos
from datetime import date

st.set_page_config(page_title="Planner 3-zmianowca", page_icon="📅", layout="centered")

# --- RPG sidebar ---
STATE_PATH = os.path.join(os.path.dirname(__file__), "..", "..", ".budowniczy", "rpg", "state.json")

with st.sidebar:
    st.markdown("## 🎮 Budowniczy RPG")
    try:
        with open(STATE_PATH) as f:
            rpg = json.load(f)
        poziom = rpg["level"]
        xp = rpg["xp"]
        xp_next = rpg["xp_to_next_level"]
        postep = xp / xp_next
        st.markdown(f"**{rpg['class_icon']} {rpg['class']}** — Poziom {poziom}")
        st.progress(postep, text=f"{xp} / {xp_next} XP")
        st.caption(f"Do awansu: {xp_next - xp} XP")
        st.divider()
        st.markdown("**Statsy**")
        statsy = rpg["stats"]
        for nazwa, war in [("Logika 🧠", statsy["logika"]),
                           ("Kod 💻", statsy["kod"]),
                           ("Build-in-Public 📢", statsy["build_in_public"]),
                           ("Token Efficiency 💎", statsy["token_efficiency"])]:
            st.progress(war / 10, text=f"{nazwa}  {war}/10")
    except FileNotFoundError:
        st.caption("state.json nie znaleziony")

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

_ZAMIANA = {
    "ą": "a", "ć": "c", "ę": "e", "ł": "l", "ń": "n",
    "ó": "o", "ś": "s", "ź": "z", "ż": "z",
    "Ą": "A", "Ć": "C", "Ę": "E", "Ł": "L", "Ń": "N",
    "Ó": "O", "Ś": "S", "Ź": "Z", "Ż": "Z",
    "–": "-", "—": "-",
    "“": '"', "”": '"',
    "‘": "'", "’": "'",
}


def _ascii(text: str) -> str:
    for stary, nowy in _ZAMIANA.items():
        text = text.replace(stary, nowy)
    return text


def generuj_pdf(zmiana: str, dane: dict, zadania: list) -> bytes:
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Helvetica", style="B", size=18)
    pdf.cell(0, 12, "Plan tygodnia", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.set_font("Helvetica", size=11)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 8, f"Data: {date.today().strftime('%d.%m.%Y')}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(4)

    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Helvetica", style="B", size=13)
    zmiana_czysta = _ascii(zmiana.encode("ascii", "ignore").decode().strip())
    pdf.cell(0, 10, zmiana_czysta, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(2)

    pdf.set_font("Helvetica", size=11)
    pdf.cell(0, 8, f"Budzet godzin: ~{dane['godz_tydzien']}h / tydzien", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 8, f"Deep work: {'Tak' if dane['deep_work'] else 'Nie'}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(4)

    pdf.set_font("Helvetica", style="B", size=12)
    pdf.cell(0, 8, "Zalecenia na ten tydzien:", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Helvetica", size=11)
    for z in dane["zalecenia"]:
        pdf.cell(0, 7, f"  - {_ascii(z)}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(4)

    if zadania:
        pdf.set_font("Helvetica", style="B", size=12)
        pdf.cell(0, 8, f"Zadania ({len(zadania)}):", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_font("Helvetica", size=11)
        for i, z in enumerate(zadania, 1):
            pdf.cell(0, 7, f"  {i}. {_ascii(z)}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    return bytes(pdf.output())


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

zadania = []
if zadania_raw.strip():
    zadania = [z.strip() for z in zadania_raw.strip().splitlines() if z.strip()]
    godz_na_zadanie = round(dane["godz_tydzien"] / len(zadania), 1)
    st.success(
        f"Masz **{len(zadania)} zadań** na **~{dane['godz_tydzien']}h** → "
        f"średnio **{godz_na_zadanie}h** na zadanie."
    )

st.divider()

pdf_bytes = generuj_pdf(zmiana, dane, zadania)
st.download_button(
    label="📄 Pobierz plan jako PDF",
    data=pdf_bytes,
    file_name=f"plan-tygodnia-{date.today()}.pdf",
    mime="application/pdf",
)
