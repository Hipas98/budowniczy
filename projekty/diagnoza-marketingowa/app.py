import streamlit as st


st.set_page_config(page_title="Diagnoza marketingowa", page_icon="📋", layout="centered")

if "step" not in st.session_state:
    st.session_state.step = 1

if "data" not in st.session_state:
    st.session_state.data = {}

if "report" not in st.session_state:
    st.session_state.report = None


def go_next(updates=None):
    if updates:
        st.session_state.data.update(updates)
    st.session_state.step += 1
    st.rerun()


def go_back():
    st.session_state.step -= 1
    st.rerun()


def show_progress():
    st.progress(st.session_state.step / 5)
    st.caption(f"Krok {st.session_state.step} z 5")


def safe_index(options, value, default=0):
    return options.index(value) if value in options else default


def step_1():
    st.subheader("Krok 1 — Twój biznes")
    show_progress()

    business_models = [
        "Jednorazowy zakup produktu",
        "Subskrypcja / abonament",
        "Usługa jednorazowa",
        "Usługa cykliczna / retainer",
        "Mix kilku modeli",
    ]

    with st.form("form_1"):
        p1 = st.text_area(
            "Co sprzedajesz i jaką wartość to daje klientowi? *",
            help="Jak opisałbyś to obcej osobie w jednym zdaniu — nie nazwą produktu, tylko efektem, który dostaje?",
            placeholder="np. Sprzedaję kursy online z zarządzania czasem dla freelancerów, którzy mają za dużo projektów i nie wyrabiają z terminami. Po kursie pracują mniej godzin i nie spóźniają się z deadlinami.",
            height=120,
            value=st.session_state.data.get("offer", ""),
            key="p1_offer",
        )
        p2 = st.text_area(
            "Jak długo działasz i kiedy miałeś najlepszy miesiąc sprzedażowy? *",
            help="Co wtedy działało inaczej niż teraz?",
            placeholder="np. Działam 2 lata. Najlepszy miesiąc był w październiku — współpracowałem z influencerem i miałem 3x więcej zamówień. Teraz już nie współpracujemy.",
            height=100,
            value=st.session_state.data.get("history", ""),
            key="p2_history",
        )
        p3 = st.selectbox(
            "Model sprzedaży",
            options=business_models,
            index=safe_index(business_models, st.session_state.data.get("business_model", "")),
            key="p3_business_model",
        )
        p4 = st.text_input(
            "Średnia wartość jednej transakcji (PLN)",
            help="A ile wynosi wartość klienta przez cały czas współpracy (LTV)?",
            placeholder="np. Średnie zamówienie to 180 zł, ale klienci wracają 4x w roku — rocznie ok. 720 zł na klienta.",
            value=st.session_state.data.get("aov", ""),
            key="p4_aov",
        )

        submit_col1, submit_col2 = st.columns([1, 4])
        with submit_col2:
            submitted_next = st.form_submit_button("Dalej →", type="primary")

        if submitted_next:
            if not p1.strip() or not p2.strip():
                st.error("Uzupełnij wszystkie wymagane pola oznaczone *.")
                return
            go_next(
                {
                    "offer": p1,
                    "history": p2,
                    "business_model": p3,
                    "aov": p4,
                }
            )


def step_2():
    st.subheader("Krok 2 — Twój klient")
    show_progress()
    st.info("To najważniejsza sekcja. Im dokładniej opiszesz klienta, tym precyzyjniejsza diagnoza.")

    with st.form("form_2"):
        p5 = st.text_area(
            "Opisz swojego najlepszego klienta — tego, który kupił, był zadowolony i wrócił lub polecił Cię dalej *",
            help="Kim był (zawód, sytuacja), jak trafił do Ciebie, co go przekonało do zakupu?",
            placeholder="np. Kasia, 38 lat, prowadzi studio jogi. Szukała fotografa produktowego, bo zdjęcia telefonem wyglądały słabo. Znalazła mnie przez Instagram, zapytała o pakiet i kupiła od razu — powiedziała, że moje przykłady wyglądają dokładnie jak to, czego szukała.",
            height=130,
            value=st.session_state.data.get("best_customer", ""),
            key="p5_best_customer",
        )
        p6 = st.text_area(
            "Jaki konkretny problem rozwiązujesz? Gdybyś nie istniał — co klient robiłby zamiast? *",
            help="Co by stracił lub co by go kosztowało gdyby musiał rozwiązać ten problem bez Ciebie?",
            placeholder="np. Bez mnie właściciel sklepu pisałby opisy produktów sam — 3h tygodniowo, i tak słabe i nie sprzedające. Albo płaciłby agencji 3000 zł/mc.",
            height=110,
            value=st.session_state.data.get("problem_solved", ""),
            key="p6_problem_solved",
        )
        p7 = st.text_area(
            'Dlaczego klienci wybierają właśnie Ciebie, a nie konkurencję lub "zrobię to sam"?',
            help="Co słyszysz najczęściej w opiniach? Co klientów zaskoczyło lub ucieszyło?",
            placeholder="np. Mówią, że jestem jedyną osobą, która tłumaczy co robi i dlaczego — czują się zaopiekowani, nie tylko obsłużeni.",
            height=100,
            value=st.session_state.data.get("why_you", ""),
            key="p7_why_you",
        )
        p8 = st.text_area(
            "Kto NIE jest Twoim klientem? Kto był złym klientem?",
            help="Jaki typ klienta sprawia Ci problemy lub kończy się niezadowoleniem / zwrotem?",
            placeholder="np. Firmy szukające najtańszej opcji i targujące się na każdą złotówkę. Zawsze są niezadowolone nawet gdy daję więcej niż obiecałem.",
            height=90,
            value=st.session_state.data.get("bad_customer", ""),
            key="p8_bad_customer",
        )

        col1, col2 = st.columns([1, 4])
        with col1:
            submitted_back = st.form_submit_button("← Wróć")
        with col2:
            submitted_next = st.form_submit_button("Dalej →", type="primary")

        if submitted_back:
            go_back()

        if submitted_next:
            if not p5.strip() or not p6.strip():
                st.error("Uzupełnij wszystkie wymagane pola oznaczone *.")
                return
            go_next(
                {
                    "best_customer": p5,
                    "problem_solved": p6,
                    "why_you": p7,
                    "bad_customer": p8,
                }
            )


def step_3():
    st.subheader("Krok 3 — Liczby i źródła klientów")
    show_progress()

    traffic_source_options = [
        "Polecenia od obecnych klientów",
        "Google (organicznie / SEO)",
        "Facebook / Meta Ads",
        "Instagram (organicznie)",
        "Google Ads",
        "Allegro",
        "LinkedIn",
        "TikTok",
        "Email marketing",
        "Inne",
    ]
    cac_awareness_options = [
        "Nie liczę tego",
        "Szacuję orientacyjnie",
        "Liczę dokładnie",
    ]

    with st.form("form_3"):
        p9 = st.text_input(
            "Miesięczny budżet na marketing łącznie (PLN)",
            help="Wlicz: reklamy płatne + narzędzia + wszystko co wydajesz na marketing",
            placeholder="np. Ok. 800 zł — 500 zł Facebook Ads, 150 zł Canva Pro i Buffer, 150 zł inne",
            value=st.session_state.data.get("budget", ""),
            key="p9_budget",
        )
        p10a = st.multiselect(
            "Skąd pochodzi większość Twoich klientów? (zaznacz wszystkie pasujące)",
            options=traffic_source_options,
            default=st.session_state.data.get("traffic_sources", []),
            key="p10a_traffic_sources",
        )
        p10b = st.text_input(
            "Który kanał przynosi NAJLEPSZYCH klientów (nie: najwięcej)?",
            placeholder="np. Najwięcej z poleceń, ale najlepsi klienci przychodzą z LinkedIn.",
            value=st.session_state.data.get("best_channel", ""),
            key="p10b_best_channel",
        )
        p11 = st.text_input(
            "Ile zamówień / klientów pozyskujesz miesięcznie (orientacyjnie)?",
            help="Ile z nich to nowi klienci, a ile powracający?",
            placeholder="np. Ok. 15 zamówień — 10 nowi, 5 powracający",
            value=st.session_state.data.get("monthly_orders", ""),
            key="p11_monthly_orders",
        )
        p12a = st.selectbox(
            "Czy wiesz ile kosztuje Cię pozyskanie jednego nowego klienta?",
            options=cac_awareness_options,
            index=safe_index(cac_awareness_options, st.session_state.data.get("cac_awareness", "")),
            key="p12a_cac_awareness",
        )
        p12b = st.text_input(
            "Ile orientacyjnie kosztuje Cię pozyskanie jednego klienta (PLN)?",
            help="Wpisz 0, jeśli nie liczysz tego wskaźnika.",
            placeholder="np. Ok. 80–120 zł, biorąc pod uwagę czas i budżet reklamowy",
            value=st.session_state.data.get("cac", ""),
            key="p12b_cac",
        )

        col1, col2 = st.columns([1, 4])
        with col1:
            submitted_back = st.form_submit_button("← Wróć")
        with col2:
            submitted_next = st.form_submit_button("Dalej →", type="primary")

        if submitted_back:
            go_back()

        if submitted_next:
            go_next(
                {
                    "budget": p9,
                    "traffic_sources": p10a,
                    "best_channel": p10b,
                    "monthly_orders": p11,
                    "cac_awareness": p12a,
                    "cac": p12b,
                }
            )


def step_4():
    st.subheader("Krok 4 — Co działa, co nie działa")
    show_progress()

    with st.form("form_4"):
        p13 = st.text_area(
            "Wymień 2–3 działania marketingowe, które DZIAŁAJĄ — przynoszą klientów lub zapytania",
            help="Co konkretnie robisz w tym kanale? Jak często? Od kiedy?",
            placeholder="np. 1) Posty na Facebooku pokazujące kulisy pracy — dużo komentarzy i 3–4 zapytania miesięcznie.\n2) Opinie w Google — kilka osób powiedziało, że znalazło mnie przez recenzje.",
            height=120,
            value=st.session_state.data.get("what_works", ""),
            key="p13_what_works",
        )
        p14 = st.text_area(
            "Wymień 2–3 rzeczy, które próbowałeś i NIE zadziałały",
            help="Jak długo to robiłeś? Ile wydałeś? Czemu Twoim zdaniem nie zadziałało?",
            placeholder="np. Google Ads — 2 miesiące, 3000 zł, 0 sprzedaży. Nie wiem dlaczego.\nInstagram — 3 miesiące codziennych postów, 50 nowych obserwujących ale żadnej sprzedaży.",
            height=120,
            value=st.session_state.data.get("what_failed", ""),
            key="p14_what_failed",
        )
        p15 = st.text_area(
            "Gdzie w procesie sprzedaży tracisz klientów? *",
            help="Opisz, co się dzieje od momentu, gdy ktoś Cię znajdzie, do zakupu. Na którym etapie rezygnują? Jakie słyszysz obiekcje?",
            placeholder='np. Dużo ludzi wchodzi na stronę, ogląda cennik i wychodzi. Jak już piszą zapytanie, to kupują w 80% przypadków. Problem jest PRZED kontaktem. Słyszę też "muszę się zastanowić" i nie wracają.',
            height=120,
            value=st.session_state.data.get("funnel_leak", ""),
            key="p15_funnel_leak",
        )
        p16 = st.text_area(
            "Jaka jest Twoja największa frustracja z marketingiem? *",
            placeholder="",
            height=100,
            value=st.session_state.data.get("frustration", ""),
            key="p16_frustration",
        )

        col1, col2 = st.columns([1, 4])
        with col1:
            submitted_back = st.form_submit_button("← Wróć")
        with col2:
            submitted_next = st.form_submit_button("Dalej →", type="primary")

        if submitted_back:
            go_back()

        if submitted_next:
            if not p15.strip() or not p16.strip():
                st.error("Uzupełnij wszystkie wymagane pola oznaczone *.")
                return
            go_next(
                {
                    "what_works": p13,
                    "what_failed": p14,
                    "funnel_leak": p15,
                    "frustration": p16,
                }
            )


def step_5():
    st.subheader("Krok 5 — Konkurencja i Twoja pozycja")
    show_progress()

    with st.form("form_5"):
        p17 = st.text_area(
            "Kim są Twoi 2-3 główni konkurenci? (nazwy lub adresy www)",
            placeholder="np. FotoXYZ (fotoxyz.pl), Studio ABC w Toruniu, fotografowie z Allegro w kategorii sesje produktowe",
            height=80,
            value=st.session_state.data.get("competitors", ""),
            key="p17_competitors",
        )
        p18 = st.text_area(
            "Co oni robią lepiej od Ciebie marketingowo?",
            help="Czy wiesz skąd oni biorą klientów? Co widzisz u nich czego Ci brakuje?",
            placeholder="np. Studio ABC ma więcej opinii Google, ładniejszą stronę i aktywny Instagram. FotoXYZ jest tańszy i ma Allegro z setkami opinii.",
            height=100,
            value=st.session_state.data.get("competitor_advantage", ""),
            key="p18_competitor_advantage",
        )
        p19 = st.text_area(
            "Co masz Ty czego NIE mają konkurenci?",
            help="Za co klienci Cię chwalą, a co pomijają w recenzjach konkurencji?",
            placeholder="np. Daję zdjęcia w 24h i pakiet 50 ujęć zamiast 20. Nikt inny nie oferuje konsultacji przed sesją — klienci mówią, że to zmienia jakość efektu.",
            height=100,
            value=st.session_state.data.get("my_advantage", ""),
            key="p19_my_advantage",
        )

        col1, col2 = st.columns([1, 4])
        with col1:
            submitted_back = st.form_submit_button("← Wróć")
        with col2:
            submitted_next = st.form_submit_button("✅ Zakończ formularz", type="primary")

        if submitted_back:
            go_back()

        if submitted_next:
            go_next(
                {
                    "competitors": p17,
                    "competitor_advantage": p18,
                    "my_advantage": p19,
                }
            )


def step_6():
    st.success("✅ Formularz wypełniony — trwa przygotowanie diagnozy")
    st.info("Tu będzie generowanie raportu diagnostycznego — zostanie zbudowane w Etapie 3.")
    st.json(st.session_state.data)

    if st.button("Wypełnij ponownie", type="primary"):
        st.session_state.step = 1
        st.session_state.data = {}
        st.session_state.report = None
        st.rerun()


STEPS = {
    1: step_1,
    2: step_2,
    3: step_3,
    4: step_4,
    5: step_5,
    6: step_6,
}


STEPS[st.session_state.step]()
