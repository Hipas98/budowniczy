# Freelance "AI-assisted development" w PL 2026 — ścieżki z Claude Code i Codex jako rdzeniem (raport dla Damiana)

**TL;DR**
- **Najlepsze ścieżki dla Damiana** (Asperger, pull, 2-3h/dzień, Toruń, klient PL MŚP) to: (1) **Niche tools maker dla streamerów na Kick.com**, (2) **Custom web-app developer dla MŚP** (Next.js + Supabase budowane Claude Code), (3) **AI Agent builder dla konkretnych workflow** (np. biura rachunkowe, e-commerce). Wszystkie trzy nagradzają logikę "działa/nie działa", pozwalają budować portfolio publicznie i nie wymagają agresywnego sprzedawania.
- **Polski rynek vibe coding 2026 jest realny, ale stawki są niższe niż amerykański hype**. Freelance custom web-app / AI agent dla MŚP w PL: junior 75-150 zł/h (kontrakty B2B, Useme), mid 150-300 zł/h (bezpośrednie zlecenia Oferia/WorkConnect), senior/ekspert 300-500 zł/h w wąskich niszach lub przy klientach zagranicznych. Liczby 500-1000 zł/h z briefu występują głównie u senior AI/ML/Architecture w korporacjach lub przy klientach US/UK.
- **Pull działa, ale wolno.** Realnie 4-9 miesięcy od pierwszego posta do pierwszej faktury — pod warunkiem publikowania spójnie 2-3 razy/tydzień + posiadania 3 widocznych projektów na GitHub + dem na Vercelu. W PL polską niszę bardziej "kupuje" LinkedIn (decydenci MŚP) niż X. Z czasem dochodzi YouTube (dłuższe demo) i Discord/meetupy (AI Tinkerers Warsaw, 10xDevs, AI_devs).

---

## Key Findings

1. **Claude Code i Codex CLI to dziś realny "core" freelance'u** — webinar Przeprogramowanych o Claude Code zgromadził ponad 600 osób na żywo, a Adam Gospodarczyk (overment), Maciej Aniserowicz (devstyle/„Gang Kodziaków"), Jakub Mrugalski i Mateusz Chrobok publicznie pokazują workflowy z Claude Code (m.in. reverse proxy, lokalne modele, agentów uruchamianych z terminala). W maju 2026 Anthropic ogłosił akwizycję Stainless ("Today, Anthropic is acquiring Stainless, a leader in SDKs and MCP server tooling", anthropic.com/news/anthropic-acquires-stainless, 18 maja 2026) — sygnał że ekosystem dojrzewa.
2. **Polski rynek custom web-app dla MŚP jest większy niż micro-SaaS B2C w PL.** Klient PL pyta o NIP/fakturę i jednorazowy projekt, a nie o subskrypcję Stripe. To preferuje model "wykonawca konkretnego problemu" (CRM-y wewnętrzne, kalkulatory, czytniki faktur) nad "ja sprzedaję SaaS za 29 zł/mc".
3. **Build in public + portfolio-led realnie ma trakcję w PL — ale przez niszowe społeczności.** AI Tinkerers (globalnie 106 000+ członków w 223 miastach; warsztawskie meetupy mają 97-326 osób, hackathony do 964+ wg historii na warsaw.aitinkerers.org), AI_devs (>2 tys. uczestników edycji 2-3), 10xDevs (1 250 uczestników 1. edycji i 1,5 mln zł przychodu wg Jakuba Czarkowskiego na przeprogramowani.substack.com), Bartek Pucek newsletter (top 20 Substack PL biznes). Tu zachodzą inboundy, nie na cold mailach.
4. **Vibe coding bez fundamentów = pułapka.** Maciej Aniserowicz wprost ostrzega w odcinku "Bliskie Spotkania z AI #27", że "vibe coding bez wiedzy technicznej to prosta droga do katastrofy, w której AI niepostrzeżenie 'czyści' Twoją kartę kredytową". Każdy z polskich pull-builderów ma za sobą lata programowania albo bardzo świadomie weryfikuje każdy commit Claude Code'a.
5. **MCP servery to otwarta nisza w PL.** MCP osiągnął 97 mln miesięcznych pobrań SDK w marcu 2026 oraz 10 000+ publicznych serwerów (wzrost ~970x w 16 miesięcy od listopada 2024, dane Toloka AI / rdworldonline.com). Polskich autorów MCP serwerów w globalnym rejestrze prawie nie ma — luka rynkowa pod pull. Brak polskiej certyfikacji Anthropic, brak polskiego rejestru, ale Smyrdek/Czarkowski uczą tego w 10xDevs.

---

## Details — 6 ścieżek specjalizacji

### 1) Niche Tools Maker — narzędzia dla konkretnej grupy (streamerzy CS2/Kick, podcasterzy, sprzedawcy Allegro, twórcy)

**A. Opis:** Budujesz małe, wyspecjalizowane narzędzia (overlaye, automaty do klipowania, panele statystyk, czytniki Allegro) dla wyraźnie zdefiniowanej grupy. Claude Code i Codex CLI są rdzeniem — opisujesz problem w terminalu, AI generuje kod Next.js / Tauri / Electron, ty czytasz i poprawiasz.

**B. Co buduje, stack:** Web overlays (Next.js + Tailwind + WebSockets), desktop tools (Tauri = Rust + frontend), integracje API (Kick API, Twitch API, Allegro Open API, Vinted, Discord). Praca z AI ~60% promptowania + iteracji w Claude Code, ~25% czytania i debugowania kodu, ~15% testowania na żywym streamie/koncie. Przykłady: overlay z live statami CS2 dla streamera Kick.com (browser source w OBS), bot Discord do moderacji polskiego serwera CS2, automatyczne klipowanie najlepszych momentów z transkrypcji audio (Whisper API).

**C. Dlaczego pull działa:** Streamerzy, podcasterzy i mali sprzedawcy mają WIDOCZNE społeczności (Discord, Twitch chat, FB grupy "Streamerzy PL"). Demo na żywo własnego overlaya na streamie kolegi = darmowy marketing. Damian zna kontekst CS2/Kick — autentyczność bije marketing. Publikujesz krótkie video YT "zbudowałem overlay X w 3 godziny z Claude Code", thread na X z timelapse'em + link do repo.

**D. Realny podział czasu:** ~55% promptowanie Claude Code + iteracja, ~20% czytanie generowanego kodu (musisz zrozumieć dlaczego coś nie działa), ~10% deploy/testowanie, ~15% content (video, posty, README).

**E. Wymagania wejściowe:** Podstawowy JS/TS (potrafisz przeczytać funkcję React'a i powiedzieć co robi), Git (commit/push/branch), deploy na Vercel/Netlify, HTTP/REST/WebSocket na poziomie "co to GET vs POST", podstawy baz danych (Supabase z tabelą users). Zero potrzeby pisania od zera — ale czytania DUŻO.

**F. Plan 3-6 mc:**
- **Mc 1-2:** ukończ darmowy quickstart Claude Code (docs.claude.com/en/docs/claude-code), zbuduj pierwszy overlay CS2 dla kolegi na Kick, deploy na Vercelu, repo public na GitHub.
- **Mc 3-4:** 2-3 publiczne projekty (overlay, auto-klip z Whisper, panel statystyk dla 3-5 streamerów), pierwszy post "Day 1" thread, kanał YT z krótkimi demo (≤3 min).
- **Mc 5-6:** dystrybucja w polskich Discordach CS2/streamerów, jeden pełny case study na LinkedIn + X, pierwsze inboundy od streamerów "fajne, zrób mi też".

**G. Źródła nauki:**
- Oficjalne: docs.claude.com/en/docs/claude-code, OpenAI Codex CLI docs (developers.openai.com/codex)
- PL YT: Przeprogramowani (webinar Claude Code ~600 widzów, repo github.com/przeprogramowani/claude-code-gha), overment (Adam Gospodarczyk)
- EN: Latent.space podcast (swyx), Builder.io blog, anthropic.com/news, Cole Medin (YT)
- Społeczność: AI Tinkerers Warsaw Discord (discord.gg/8WsqnC6Hk3), 10xDevs Slack

**H. Stack:**
| Must-have | Cena/mc |
|---|---|
| Claude Pro (zawiera Claude Code od 2026) | ~85 zł |
| Cursor / VS Code | 0–80 zł |
| GitHub | 0 zł |
| Vercel hobby | 0 zł |
| Supabase free | 0 zł |
| Domena .pl | ~15 zł/mc amortyzowane |
| **Razem must-have** | **~100-180 zł/mc** |

Nice-to-have: Lovable / Bolt.new (do szybkich prototypów landingu, ~80 zł/mc), v0.dev (UI), Cloudflare Workers (zaawansowane), ElevenLabs (TTS, ~25 zł/mc start), Whisper API (płatne per request). Łącznie zostawiasz budżet 300-500 zł/mc.

**I. 3 projekty portfolio (CS2/streaming):**
1. **Overlay "CS2 PolaSCOPE"** — live HUD na Kick.com pokazujący K/D, top weapon, mapę, integracja z Steam Web API + nade lineups. Demo na streamie kolegi, repo public, video YT.
2. **Auto-klip AI z transkrypcji** — narzędzie biorące VOD z Kick/Twitcha, transkrybuje przez Whisper, Claude wybiera najlepsze 30s "klipów". Demo: "Z mojej 4h sesji wyciąłem 8 klipów w 12 minut".
3. **Discord stat bot** — bot na polski serwer CS2, pokazuje statystyki na żądanie `/stats`, podłączony do FACEIT API, deploy na Cloudflare Workers.

**Alternatywy:** Allegro Stat Tracker (sprzedawca widzi spadek konwersji), Vinted Bulk Editor (masowa edycja ofert), Podcaster Show Notes Generator (z audio do shownotes), TikTok Hook Tester.

**J. Pull dla Asperger:** **9/10**. Streamerzy/twórcy reagują na konkretne efekty ("ten overlay wygląda inaczej niż wszystko"), nie na bullshit. Damian zna ich język. Polskie społeczności: Discord serwery polskich streamerów CS2, grupy FB "Streamerzy Polska", subreddit r/PolskiGaming, X-PL community gaming. AI Tinkerers Warsaw idealny dla pokazywania demo.

**K. Stawki:** Projektowo: prosty overlay 800-2500 zł, średnie narzędzie 3000-7000 zł, kompletny dashboard 8000-15000 zł. Godzinowo: na start 80-150 zł/h przy małych zleceniach na Useme, po 6-12 mc 150-250 zł/h bezpośrednio od klienta. Źródła: oferia.com.pl/pl/zleceniobiorcy/uslugi/programowanie (60-250 zł/h potwierdzone na platformie), useme.com (średnio 5014 zł/zlecenie wg Index Useme).

**L. Ryzyka:** Streamerzy ze średnich półek nie mają budżetu — bierz tylko top 5% (xQc/Adin Ross-tier w PL = Izak, Diabeuu, KuroNooKii). Halucynacje AI w integracji z grą = ban konta. Robisz overlay = bezpieczeństwo: nigdy nie wymuszaj loginu Steam, używaj OpenID/OAuth.

---

### 2) Custom Web-App Developer dla polskich MŚP (Next.js + Supabase, Claude Code jako rdzeń)

**A. Opis:** Robisz dedykowane wewnętrzne narzędzia dla małych firm — biuro rachunkowe, mechanik, biuro nieruchomości, restauracja, hurtownia. CRM-y, kalkulatory wycen, panele wewnętrzne, zamienniki Excela. Każdy projekt = jedna firma, jeden problem, jedno rozwiązanie.

**B. Stack:** Next.js 15 + Tailwind + shadcn/ui + Supabase (Postgres + Auth + Storage) + Vercel. Praca z AI ~50% Claude Code w terminalu (generowanie features), ~30% czytanie/debugowanie/integracja, ~20% spotkania z klientem, dokumentacja, deploy. Typowe projekty: czytnik faktur PDF dla biura rachunkowego (OCR + automatyczne księgowanie), kalkulator wyceny naprawy auta z OCR ze zdjęcia VIN, mini-CRM dla biura nieruchomości z synchronizacją z Otodom RSS.

**C. Pull:** LinkedIn jest tu kluczowy — polscy decydenci MŚP (właściciele 1-15 osobowych firm) są na LinkedIn, nie na X. Publikujesz case studies: "Zrobiłem dla biura rachunkowego z Bydgoszczy panel, który skraca czas pracy z fakturami o 40%". Polski blog na własnej domenie + nagrania demo na YT po polsku. Maciej Aniserowicz pokazał, że można zbudować "sklep z perfumami w godzinę" z Claude Code — taki content sprzedaje sam.

**D. Podział:** ~45% Claude Code + Codex, ~25% czytanie kodu i bezpieczeństwo (Supabase RLS, auth, secrets), ~15% klient (spotkania, wymagania, demo), ~15% content + utrzymanie portfolio.

**E. Wymagania:** Czytanie TS/React na poziomie "rozumiem co robi useEffect", Supabase RLS (KRYTYCZNE — bez tego wyciekniesz dane klientów), Git + GitHub Actions, deploy Vercel + DNS, podstawy Zod/walidacji formularzy, HTTP status codes, RODO/GDPR (podstawowy poziom — dane osobowe wymagają zgody i polityki prywatności).

**F. Plan:**
- **Mc 1-2:** zbuduj jeden mini-CRM "dla siebie" (np. tracker zleceń freelance), naucz się Supabase RLS, deploy na własnej domenie.
- **Mc 3-4:** dwa projekty portfolio dla konkretnych nisz PL (biuro rachunkowe + mechanik). Open source obu na GitHubie, demo na Vercel + readonly konto demo.
- **Mc 5-6:** 1-2 case studies LinkedIn long-form, jeden post w grupie FB "Biuro Rachunkowe w Polsce" / "Wracam do IT", YT video "Jak zbudowałem CRM dla biura rachunkowego w weekend".

**G. Źródła:** docs.claude.com/en/docs/claude-code (oficjalna), Next.js docs (nextjs.org/learn), Supabase docs, CLAUDE.md best practices Przeprogramowanych (github.com/przeprogramowani/10x-astro-starter/blob/master/CLAUDE.md — wzorzec do skopiowania), Vercel docs. Kursy PL: AI_devs 4 (aidevs.pl, ~1500-2500 zł, 5 tygodni), 10xDevs (10xdevs.pl), Przeprogramowani podcast Opanuj.AI (darmowy).

**H. Stack:** must-have jak wyżej (~150 zł/mc), dodatkowo: Anthropic API credits (~100 zł/mc na start), domeny dla każdego klienta (15 zł/mc każda). Łącznie 250-400 zł/mc na start.

**I. 3 projekty portfolio:**
1. **"FakturOCR" dla biur rachunkowych** — webapp do uploadu PDF faktur, OCR przez Claude Vision, automatyczna kategoryzacja kosztów, eksport do KPiR. Inspiracja: case study na live-sales.pl, gdzie autor zbudował podobny dashboard z Claude Code w 2 dni za ~$80 OpenAI credits.
2. **"WyceniarkaMechanika"** — formularz: zdjęcie auta + opis usterki → Claude analizuje, zwraca przybliżony zakres cenowy + listę części + szacowany czas. Open source. Niche: mechanicy z FB grup "Mechanik w Polsce".
3. **Mini-CRM dla biura nieruchomości** — synchronizacja z RSS Otodom/Olx, panel z lead'ami, podgląd interakcji, prosty mail tracking przez Postmark/Resend. Multi-tenant z Supabase RLS.

**Alternatywy:** Asystent dla mikrofirm rzemieślniczych (kosztorys z OCR i głosem), Cennik usług kosmetycznych z AI (analiza zdjęcia twarzy + rekomendacja), Tracker absencji dla małych biur (alternatywa płatnego HR softu za 200 zł/mc).

**J. Pull dla Asperger:** **8/10**. MŚP w PL kupuje przez **rekomendacje i konkretne dema**, nie przez perswazję. Damian może być "tym co dostarcza co obiecał". Polskie społeczności: LinkedIn (najważniejsze), FB "Wracam do IT", grupy branżowe FB ("Księgowi w Polsce", "Mechanicy Samochodowi PL"), AI Tinkerers Warsaw (gdy będzie miał demo). Plus meetupy: AI Tinkerers #8 (18 czerwca 2026), WarsawJS, AI Bootcamp.

**K. Stawki:** Projektowo (potwierdzone na oferia.com.pl/pl/zleceniobiorcy/uslugi/programowanie): aplikacja webowa od 8 000 zł, rozbudowane systemy z CRM/API: 30 000-80 000 zł. Godzinowo: 60-250 zł/h na Oferii, 120-300 zł/h na WorkConnect (workconnect.app/zlecenia/programowanie-i-it). Hays IT Contracting Salary Guide 2026 dla seniorów full-stack: do 60 000 zł/mc na B2B = ~375 zł/h. Realnie dla Damiana w 6-12 mc: 100-180 zł/h na małych zleceniach Useme, 150-250 zł/h przy bezpośrednim kliencie po pierwszych projektach.

**L. Ryzyka:** Klient PL nie wie czego chce — MUSISZ zrobić pisemny zakres ZANIM zaczniesz kodzić, inaczej scope creep zabije marżę. Supabase RLS — jedna źle skonfigurowana polityka i dane wszystkich klientów lecą jednemu. Halucynacje AI w produkcji księgowości to ogromne ryzyko prawne (KSeF od 1 kwietnia 2026, błędne księgowanie = kary). Trzymaj się "Claude pomaga, ja czytam linijka po linijce dla każdej krytycznej rzeczy". RODO — wymagaj umowy powierzenia danych (DPA) przy każdym kontrakcie.

---

### 3) AI Agent Builder — agenty rozwiązujące konkretne workflow w firmach

**A. Opis:** Budujesz autonomiczne agenty (Claude Agent SDK / własne w TS lub Python) wykonujące powtarzalne procesy — czytanie maili z fakturami, syncowanie systemów, automatyczne odpowiedzi na zapytania ofertowe, monitoring konkurencji. Claude Code jest narzędziem do BUDOWANIA agentów, Claude Agent SDK / Codex CLI do ich URUCHAMIANIA.

**B. Stack:** Python (LangChain / native Anthropic SDK) lub TypeScript (@anthropic-ai/claude-code, OpenAI Agents SDK), Supabase / Postgres do stanu, Resend/Postmark do maili, Redis dla kolejek, Docker do izolacji. Praca z AI: ~50% promptowanie + projektowanie systemu + iteracja w Claude Code, ~30% czytanie i debugowanie agentów (HALUCYNACJE są największym ryzykiem), ~20% monitoring, alerty, dokumentacja.

**C. Pull:** Agentowy nisz wymaga DUŻO wyjaśniania klientowi — content edukacyjny świetnie konwertuje. Przykład polski: Mateusz Chrobok (linkedin.com/in/mateuszchrobok/) publicznie pokazuje swój homelab zarządzany lokalnymi modelami + reverse proxy Claude Code. Bartek Pucek (pucek.com) buduje "Proofs" — wg EU-Startups Proofs "uses AI agents to build proof-of-concept apps and integrations to help API-first companies close more customers"; runda €2.4M w czerwcu 2024 prowadzona przez Earlybird Digital East Fund (z Expeditions Fund, Step Function Ventures, RTP Global).

**D. Podział:** ~40% promptowanie + system design, ~30% czytanie + bezpieczeństwo + tests, ~15% klient, ~15% content. Tu STAJESZ SIĘ POSZUKIWANY pisząc edukacyjnie, nie sprzedażowo.

**E. Wymagania:** Solid TS/Python (musisz potrafić napisać klasę i pętlę bez Claude'a), async/await, kolejki/eventy, podstawy systemów rozproszonych ("co jeśli agent crashuje w 3. kroku"), monitoring (Sentry/Posthog), secrets management (Doppler/Vault), prompt engineering. To ścieżka **trudniejsza** wejściowo.

**F. Plan:**
- **Mc 1-2:** zbuduj jednego prostego agenta DLA SIEBIE (np. czyta moje GitHub notification + robi summary do Telegrama). Dokumentuj proces na blogu.
- **Mc 3-4:** dwa agentowe projekty dla niszy PL: (a) klasyfikator maili biura rachunkowego z auto-odpowiedzią, (b) monitoring zmian na stronach konkurencji dla sklepu Allegro.
- **Mc 5-6:** webinar / live demo, posty case-study, dołączenie do AI Tinkerers Warsaw z prelekcją.

**G. Źródła:** docs.claude.com/en/docs/claude-code, anthropic.com/news (Agent SDK), AI_devs 4 (aidevs.pl — kurs PL stricte o agentach), kanał YT Mateusza Chroboka, "Bliskie Spotkania z AI" podcast (bliskiespotkaniazai.pl), latent.space (EN), DeepLearning.AI "Building Effective Agents".

**H. Stack:** must-have (~150 zł/mc) + Anthropic API (300-500 zł/mc) + Doppler (~0-80 zł/mc) + Sentry hobby (0 zł) + VPS dla agenta produkcyjnego (~50 zł/mc Hetzner). Razem ~500-700 zł/mc — najwyżej z wszystkich ścieżek.

**I. 3 projekty:**
1. **"InboxClerk" dla biur rachunkowych** — agent czyta IMAP, wyciąga faktury, kategoryzuje, dodaje do CSV/Notion, alarmuje przy nietypowych przelewach.
2. **"AllegroSpy"** — agent monitoruje 5 ofert konkurencji dla wybranego sprzedawcy, raportuje zmiany cen, brak stanu, nowe oferty. Publikujesz raport co tydzień na blogu jako sample.
3. **"ZapytaniobotPL"** — agent czyta zapytania z formularza www, klasyfikuje (lead/spam/wsparcie), odpowiada wstępnie po polsku, wrzuca do CRM (np. EspoCRM). Sample na własnej stronie.

**Alternatywy:** Personal Knowledge Agent (czyta Twoje notatki Obsidian + Slack archiwa + maile), Procurement Agent (zbiera oferty z 5 hurtowni dla sklepu), Recruiter Agent (przesiewa CV).

**J. Pull dla Asperger:** **7/10**. Trochę za techniczne na start — Damian może się gubić w prompt engineering + bezpieczeństwie. Ale silna logika + zero presji sprzedażowej = pasuje. Społeczności: AI_devs (wymaga zakupu kursu, ale dostęp do zamkniętej społeczności builderów), AI Tinkerers Warsaw (Discord discord.gg/8WsqnC6Hk3), 10xDevs Slack.

**K. Stawki:** Tu są wyższe stawki, bo nisza mała i ryzyko wysokie. Hays/JJI 2026 dla AI/ML senior B2B: do 99 490 zł/mc max (Just Join IT Raport 2025/2026 — itwiz.pl/boom-na-specjalistow-ai-stawki-dochodza-nawet-do-30-tys-zl-netto), realnie mid 12 000-17 000 zł/mc, senior 25 000-35 000 zł/mc. Per godzina: 150-400 zł/h, w niszy AI/ML do 600+ zł/h. Projektowo: prosty agent 5 000-12 000 zł, produkcyjny z monitoringiem 15 000-40 000 zł.

**L. Ryzyka:** Halucynacje agenta w produkcji = realna katastrofa (Mateusz Chrobok cytuje przykład agentów kasujących maile). Klient nie rozumie "to nie jest deterministyczne" — wymagaj testów + soft launch + human-in-the-loop. Bezpieczeństwo secrets — agent z dostępem do skrzynki klienta to bomba. Zawsze sandbox.

---

### 4) Indie Hacker / Micro-SaaS Builder PL (budowa własnego produktu)

**A. Opis:** Budujesz SWÓJ produkt — micro-SaaS, zwykle abonament 29-99 zł/mc dla niszy. To NIE jest freelance, to przedsiębiorczość. Claude Code jest motorem szybkiego prototypowania.

**B. Stack:** Next.js + Stripe + Supabase + Resend + Vercel. AI: 60% Claude Code generuje features, 20% bezpieczeństwo/płatności, 20% marketing.

**C. Pull:** Najsilniejszy. Senja.io zbudowała "Wall of Love" testimonial SaaS od $0 do $83k MRR (≈$1M ARR), startując od pierwszego płacącego klienta w czerwcu 2022 i osiągając ten poziom w listopadzie 2025 — 3 lata i 5 miesięcy (kamienie milowe: $30k MRR maj 2024, $50k MRR październik 2024, wg thesuccessfulprojects.com). Ale w PL jest TRUDNIEJ — polski rynek B2C nie kupuje SaaS-a tak chętnie. Wilson Wilson i Olly Meakings z Senji budowali globalnie po angielsku.

**D. Podział:** ~35% Claude Code, ~30% marketing + content (więcej niż przy freelancie!), ~20% support użytkowników, ~15% finansowy/operacyjny.

**E. Wymagania:** Wszystko jak ścieżka #2 PLUS marketing/copywriting (SŁABA STRONA DAMIANA), Stripe Billing, retencja, analytics (Posthog), customer development. Słabość Damiana w "czy tekst jest dobry" = duża bariera.

**F. Plan:** 6 miesięcy zwykle wystarczy tylko na **walidację**, nie na MRR. Realnie 12-24 miesiące do pierwszego $1k MRR w PL.

**G. Źródła:** IndieHackers.com, microsaas.io, Bartek Pucek newsletter (newsletter.pucek.com), "Friends, come warm yourselves by the flaming wreckage of my micro-SaaS" (indiehackers.com — must-read o porażkach), szkolenia przeprogramowani.pl.

**H. Stack:** ~400-600 zł/mc początkowo (Stripe ma fees, Resend płatny po 100 maili/dzień, analytics).

**I. 3 pomysły niszowe PL:**
1. **TerminMechanika.pl** — kalendarz online dla mechaników jednoosobowych (alternatywa Booksy za 49 zł/mc zamiast 149).
2. **OFERTOWNIK** — generator wyceny dla rzemieślników (płytkarz, hydraulik) z OCR ze zdjęcia + LLM kosztorys.
3. **PolskaKsiazka.app** — narzędzie do prowadzenia KPiR dla mikrofirm < 200 zł/mc (gdzie Wfirma jest za drogie/skomplikowane).

**J. Pull dla Asperger:** **5/10** — wymaga DUŻO komunikacji z użytkownikami, mocnego copy, ciągłej promocji. To ścieżka dla TWÓRCÓW z mocną stroną tekstową. **Pułapka X-owa** — wszystkim się wydaje, że jest super.

**K. Stawki:** SaaS w PL: średnia cena 29-149 zł/mc. Realnie 100-300 klientów = 4 000-30 000 zł MRR po 12-24 miesiącach (jeśli się uda). Większość kończy z $0.

**L. Ryzyka:** Polski klient płaci za fakturę z NIP, nie za Stripe subscription — musisz mieć poprawny model z VAT. Niższa skłonność do płacenia za SaaS niż na rynkach EN. "Wyglądasz cool na X" ≠ MRR.

---

### 5) AI-Powered Browser Extension Developer

**A. Opis:** Budujesz rozszerzenia do Chrome/Edge/Firefox/Arc/Brave wykorzystujące Claude/OpenAI API dla konkretnych zadań — auto-aplikacja na pracę, parser cen w Allegro, summarizer artykułów po polsku, asystent Otomoto.

**B. Stack:** Chrome Extension Manifest V3 + Vite + React + Claude/OpenAI API + Supabase (jeśli user accounts). Claude Code może wygenerować 80% kodu rozszerzenia z pojedynczego promptu opisującego use case.

**C. Pull:** Rozszerzenia są łatwe do demonstrowania (1 video, 10 sekund, "wow"). Chrome Web Store ma natywną dystrybucję. Threads "Day 1 → Day 7: I have 1000 installs" są popularne.

**D. Podział:** ~50% Claude Code/Codex, ~20% czytanie/poprawki (CSP, permissions), ~15% testy w 3 przeglądarkach, ~15% content/store optimization.

**E. Wymagania:** Chrome Extensions API (manifest, content scripts, background, permissions — KRYTYCZNE), JS/TS, message passing, podstawy DOM manipulation, OAuth.

**F. Plan:** Mc 1-2: jedno proste rozszerzenie published. Mc 3-4: 2-3 publikacje, pierwszy "Show HN" lub Product Hunt launch. Mc 5-6: monetyzacja przez Stripe (premium features) lub freemium z reklamą.

**G. Źródła:** developer.chrome.com/docs/extensions (oficjalne), Sebastian Lopez (chromehq YT), wxt.dev framework.

**H. Stack:** ~150-250 zł/mc, plus opłata Chrome Developer 5$ jednorazowo.

**I. 3 pomysły:**
1. **AllegroSnap** — przy oglądaniu produktu pokazuje historię cen + alternatywy konkurencyjne.
2. **CV TLDR** — dla rekruterów: skrót CV z LinkedIn po polsku w 3 zdania.
3. **OtoMoto Vetting** — analiza ogłoszenia używanego auta + czerwone flagi (VIN check, dziwna cena).

**J. Pull dla Asperger:** **7/10** — łatwe do demonstracji, ale konkurencja globalna duża. Społeczności: Subreddit r/chrome_extensions, Product Hunt, polski rynek niszowy mały.

**K. Stawki:** Freemium standard. Płatna wersja $5-15/mc. Klient enterprise (B2B), 5000-20 000 zł projekt. Custom extension dla polskiego sklepu: 3000-12 000 zł.

**L. Ryzyka:** Chrome Web Store review (zmiany polityki Manifest V3), permissions creep, kradzież pomysłu (extensions są łatwe do kopiowania).

---

### 6) MCP Server Builder / Open Source Contributor

**A. Opis:** Tworzysz serwery MCP (Model Context Protocol) — łączące Claude/Cursor/Codex z konkretnymi systemami (np. polski KSeF, IBKR, Allegro, Otomoto). Hostujesz repo open source, publikujesz w globalnym rejestrze registry.modelcontextprotocol.io.

**B. Stack:** TypeScript SDK MCP (@modelcontextprotocol/sdk) lub Python, FastMCP, Cloudflare Workers do hostingu remote MCP, stdio dla local. Claude Code idealnie generuje boilerplate MCP.

**C. Pull:** Tu jest **realna luka rynkowa w PL**. Anthropic ogłosił akwizycję Stainless 18 maja 2026 (anthropic.com/news/anthropic-acquires-stainless: "Today, Anthropic is acquiring Stainless, a leader in SDKs and MCP server tooling"), a MCP osiągnął 97 mln miesięcznych pobrań SDK i 10 000+ publicznych serwerów do marca 2026 (wzrost ~970x w 16 miesięcy od listopada 2024). Polskich autorów MCP serwerów w globalnym rejestrze prawie nie ma. Otwierając niszę "polskie integracje MCP" (KSeF, GUS, NBP API, PUE ZUS) zyskujesz "first mover" globalnie.

**D. Podział:** ~45% Claude Code/Codex (idealne do MCP), ~25% specyfikacja protokołu + testy, ~15% bezpieczeństwo (MCP daje LLM-owi dostęp do narzędzi!), ~15% content + dokumentacja.

**E. Wymagania:** TypeScript / Python intermediate, JSON-RPC podstawy, OAuth, SSE / stdio transports, GitHub workflow (releases, semver, tests w CI).

**F. Plan:** Mc 1-2: pierwszy MCP server publiczny (np. dla NBP exchange rates). Mc 3-4: 2-3 wyspecjalizowane MCP (KSeF, Allegro, GUS REGON). Mc 5-6: case study YT, prelekcja AI Tinkerers Warsaw, możliwa współpraca z polskim ISV jako konsultant.

**G. Źródła:** modelcontextprotocol.io/docs/develop/build-server (oficjalne Anthropic), github.com/modelcontextprotocol/servers, Anthropic eng blog. Polski przewodnik: decodethefuture.org/mcp-model-context-protocol/.

**H. Stack:** ~150 zł/mc (Cloudflare Workers free tier wystarczy, Anthropic API niskie zużycie).

**I. 3 projekty MCP polskie:**
1. **mcp-nbp-pl** — Claude pyta o kurs walut NBP, MCP zwraca aktualne dane z api.nbp.pl. Trywialny do zrobienia, idealny pierwszy projekt.
2. **mcp-gus-regon** — wyszukiwanie firm PL po NIP/REGON dla agentów obsługi klienta.
3. **mcp-allegro-pl** — search + watch ofert dla agentów e-commerce.

**Alternatywy:** mcp-ksef-pl (po pełnym ksef-cie), mcp-pue-zus, mcp-cepik.

**J. Pull dla Asperger:** **8/10** — silnie techniczne, "działa/nie działa", deterministyczne (protokół jasny), nie wymaga sprzedawania. Społeczności: globalny Discord MCP, AI Tinkerers Warsaw, Anthropic Discord.

**K. Stawki:** Wczesnie open source = $0. Z czasem konsulting dla firm wdrażających MCP: 250-600 zł/h, projekty 15 000-60 000 zł. Akwizycja Stainless (maj 2026) sygnalizuje, że talenty MCP będą cenne.

**L. Ryzyka:** MCP spec ciągle ewoluuje (breaking changes), bezpieczeństwo (LLM otrzymuje narzędzia — prompt injection przez treść zwracaną z MCP to realny atak). Brak gwarancji że nisza dojrzeje na lokalnym rynku PL w 6 mc.

---

## TOP 3 ścieżki dla Damiana

### 🥇 TOP 1: Niche Tools Maker — start od CS2/Kick.com (ścieżka #1)

**Dlaczego:** Damian zna kontekst (pomaga koledze ze streamingiem CS2 na Kick.com). Profil Asperger pasuje idealnie — overlays i statystyki to deterministyczne "działa/nie działa", a streamerzy reagują na konkretne efekty, nie na storytelling. Polskie społeczności streamerów CS2 są zwarte, łatwo wejść z demo. Po zbudowaniu reputacji "tego co robi narzędzia dla streamerów" naturalnie przechodzisz do **podcasterów → twórców → sprzedawców Allegro**, każdy z tym samym wzorcem: niche tools + Claude Code jako rdzeń. Pull realnie zaczyna działać po 3-4 miesiącach, bo demo na żywym streamie kolegi = 50-500 widzów dziennie ogląda Twoje narzędzie.

### 🥈 TOP 2: Custom Web-App Developer dla polskich MŚP (ścieżka #2)

**Dlaczego:** Po 3-4 mc niche tools, naturalne rozszerzenie na MŚP daje większe stawki (8000-30 000 zł/projekt vs. 2000-5000 zł za narzędzie streamerskie). Damian zna polski lokalny rynek (OBI, Leroy Merlin, biura rachunkowe). Klient PL MŚP **kupuje konkret** ("zrobisz mi panel do faktur z OCR za 10 000 zł?") nie storytelling. Stack Next.js + Supabase + Claude Code jest dziś najlepiej udokumentowanym workflow w polskiej społeczności (10xDevs, Przeprogramowani GitHub).

### 🥉 TOP 3: AI Agent Builder dla konkretnych workflow (ścieżka #3) — rozwinięcie po 6+ mc

**Dlaczego:** Najwyższe stawki (do 600 zł/h), ale wymaga twardszych fundamentów technicznych. Damian z Aspergerem może mieć przewagę bo systematyczność + obsesja deterministyczności = idealny mindset do debugowania agentów. **Ale nie zaczynaj tu** — wejdź po 4-6 mc z fundamentami z TOP 1+2.

---

## Ścieżki-pułapki (nie idź tu na start)

1. **Indie hacker / Micro-SaaS po polsku jako PIERWSZY ruch (ścieżka #4)** — na X widzisz Senja.io, Pieter Levels'a, polskich indie hackerów, ale wszyscy mają lata pisania kodu PRZED Claude Code'em i mocny copywriting. Polski rynek SaaS B2C ma niską skłonność do płacenia abonamentów — kupują **fakturę z NIP-em**, nie subskrypcję Stripe. Realnie: 18-24 mc do pierwszego $1k MRR w PL — Senja, jeden z głośniejszych pull-buildowanych SaaS-ów na świecie, potrzebowała 3 lat i 5 miesięcy do $83k MRR.

2. **"Vibe coding everything" bez fundamentów** — kursy typu "Vibe Coding bez kodu" obiecują wszystko bez czytania kodu. **Maciej Aniserowicz wprost:** "vibe coding bez wiedzy technicznej to prosta droga do katastrofy". Bez umiejętności czytania kodu Claude'a (`useEffect`, async, RLS, secrets) **zamordujesz swojego pierwszego prawdziwego klienta** w produkcji. Damian potrzebuje 1-2 mc na czytanie kodu zanim weźmie płatne zlecenie.

3. **"Sprzedam SaaS dla US/UE z Polski w 3 mies."** — jeśli nie znasz EN copy + nie masz sieci na X, w 3 mc zbudujesz produkt którego nikt nie zobaczy.

4. **Cold outreach do biur rachunkowych** — Damian explicite tego nie chce, i słusznie. Polski klient MŚP jest scoldoutreachowany do nieprzytomności, **rekomendacje i widoczne demo bije outbound 10:1**.

5. **AI Agency style "Setup for Clients $10k/mc"** — tiktokowy hype Liama Ottleya, Helena Liu. W PL klient MŚP nie zapłaci $10k miesięcznie za "AI workflow setup". Ten model działa w US/UAE/Singapurze, nie w PL/Toruniu.

6. **Open source MCP bez planu monetyzacji jako PIERWSZY ruch (ścieżka #6)** — świetna luka, ale wczesny dochód = $0. Trzymaj jako "side project budujący reputację", nie jako źródło utrzymania w 6 mc.

**Wspólny mianownik pułapek:** wszystkie wyglądają sexy na X/YT, ale w polskim kontekście (małe rynki niszowe + klient mówi "wystaw fakturę" + niska skłonność do SaaS abonamentu + brak network'u zagranicznego) **nie generują dochodu w 3-6 mies.**

---

## Realny tygodniowy plan dla TOP 1 (Niche Tools Maker, start od CS2/Kick.com)

### Format (2-3h/dziennie, 6 dni/tydzień)

**Poniedziałek-Piątek:**
- **45 min nauka** (lektura docs, kurs, watching demo)
- **75-90 min budowanie** (kodzenie w Claude Code, deploy, czytanie generowanego kodu)
- **15-30 min publikowanie** (post X/LinkedIn, krótkie video, commit z opisem)

**Sobota:** 2-3h głębszej pracy nad projektem tygodnia + jedno długie video YT (15-30 min)

**Niedziela:** wolne lub 1h przeglądania Discord/community (AI Tinkerers, 10xDevs, polskich serwerów streamerskich)

### Co publikować

| Kanał | Częstotliwość | Format |
|---|---|---|
| **X (Twitter)** | 4-5/tydzień | Thread "Day 1/7/14" budowy projektu, krótkie clip z timelapse'em Claude Code, screenshoty UI |
| **LinkedIn** | 1-2/tydzień | Polski long-form post, "ekspert od narzędzi dla streamerów / mikro-CRM-ów", case study |
| **YouTube** | 1/tydzień | 5-15 min demo "Zbudowałem X w Y czasu z Claude Code", po polsku |
| **GitHub** | codzienne commity | README po polsku + EN, demo link, gif |
| **Polskie Discordy** | 2-3/tydzień | Niedrażniąco — reagujesz na pytania, dropujesz demo gdy pasuje |

### Miesięczne checkpointy "działa / nie działa"

| Mies. | Cel "działa" | Cel "nie działa" — przerwij i zmień |
|---|---|---|
| **1** | Skończony quickstart Claude Code, 1 deploy na Vercelu, 5 postów na X, GitHub z 1 publicznym repo | Brak commitów >2 tyg., zero deployów, nawet jeden post — RETHINK setup |
| **2** | 1. mini-projekt (np. CS2 overlay) publicznie, 30 followers X, 1 video YT, 5 connections LinkedIn z niszy | Mniej niż 5 followers X po 2 mc = problem z formatem postów |
| **3** | 2. projekt portfolio publicznie, 50 followers X, 10 reakcji na pierwszy LinkedIn post, 100 wyświetleń YT | Zero zainteresowania portfolio = projekty są za hermetyczne / źle pokazane |
| **4** | **Ktoś sam napisał DM "fajne to co robisz"** (pierwszy realny sygnał pull), 100 followers X | Zero DM-ów = niedostateczna widoczność, zwiększ częstotliwość lub zmień format |
| **5** | Pierwsza darmowa konsultacja / wycena (15-30 min calla z potencjalnym klientem), 3. projekt | Brak konsultacji = popraw call-to-action w bio, dodaj sekcję "Zlecenia" |
| **6** | **Pierwsza faktura** (5 000-12 000 zł projekt streamerski lub MŚP), publiczny case study | Brak faktury = analiza: niewystarczająca widoczność / źle wyceniony zakres / scope creep |

### Jak wygląda realny "pull moment"

**Scenariusz miesiąc 4:**
*Discord serwera "Polish CS2 Community" (~3k członków). Damian wrzuca tydzień wcześniej krótkie video swojego overlaya na streamie kolegi. Inny streamer Maciek (700 widzów na Kick) DMuje: "Hej, fajne to. Mam stream w środy, chciałbym podobny overlay ale z trackingiem mojego ranku FACEIT. Ile by to kosztowało?". Damian: "Mogę zrobić 2-3 wieczory pracy, 1500 zł netto, dorzucam darmowy update jeśli coś się rozjedzie". Maciek zgadza się. Wystawienie faktury z Damianowej JDG (ryczałt 8.5% lub liniowy 19%). Po 5 dniach overlay jest live, Maciek robi shoutout na streamie. 2 jego widzów też pyta o swoje. **Snowball.**

**Scenariusz miesiąc 5-6:** post Damiana na LinkedIn (long-form) "Jak zbudowałem czytnik faktur dla siostry z biurem rachunkowym w 1 weekend z Claude Code" zbiera 80 reakcji. Komentuje go właściciel biura rachunkowego z Bydgoszczy: "Robimy podobny projekt na zlecenie — chcielibyśmy pogadać". Pierwsza rozmowa w 5 dni. Wycena: 18 000 zł netto za panel z OCR + Supabase auth.

---

## Pierwszy krok na ten tydzień (Damian wciąż za granicą)

### Setup techniczny (dzień 1-2, łącznie ~3h)

1. **Konto Anthropic Claude Pro** (claude.com/pricing) — 20 USD/mc, zawiera Claude Code od 2026. Konto OpenAI Pro (20 USD/mc) opcjonalnie dla Codex CLI.
2. **Instalacja Claude Code:** `npm install -g @anthropic-ai/claude-code`. Pierwsze 30 min: tutorial z docs.claude.com/en/docs/claude-code (oficjalna dokumentacja, najlepsze źródło, polskie blogi NIE wystarczą).
3. **Codex CLI:** `npm install -g @openai/codex` (developers.openai.com/codex).
4. **GitHub Pro free + repo `damianbuild`** z README po polsku ("Cześć, jestem Damian. Buduję publicznie narzędzia z Claude Code i Codex. Tu są moje projekty.")
5. **Vercel Hobby** podpięte do GitHuba (auto-deploy)
6. **Supabase free** z jednym projektem `damianbuild`
7. **VS Code + Cursor (free)** zainstalowane lokalnie

### Pierwszy mini-projekt do skończenia w 7 dni: "TimerOverlay CS2"

**Cel:** prosty browser overlay (Next.js + Tailwind + Vercel) który pokazuje na streamie:
- Aktualny czas grania
- Liczbę win/loss z dzisiejszej sesji (ręczne klikanie + / -)
- Customowy tekst z chatu (Kick chat poll integration)

**Krok 1 (dzień 3-4):** Otwierasz folder, `claude` w terminalu, prompt:
> "Stwórz Next.js 15 app z Tailwindem, jedną stroną /overlay która ma transparent background, w lewym górnym rogu pokazuje: HH:MM (czas), W: 0 L: 0 (z plus/minus przyciskami niewidocznymi w stream mode), bottom-bar z tekstem 'CS2 Live'. Stronę można dodać do OBS jako Browser Source (1920x1080). Deploy na Vercel."

Claude generuje. Czytasz każdy plik LINIJKA PO LINIJCE i pytasz Claude'a "co robi useState w tym pliku" — to KRYTYCZNE dla budowy fundamentów.

**Krok 2 (dzień 5):** Dodaj prosty stan w Supabase. Streamer otwiera /overlay?streamer=damian, dane są zapisane.

**Krok 3 (dzień 6):** Deploy publicznie na demo-overlay.damianbuild.dev. Test w OBS.

**Krok 4 (dzień 7):** Wystaw publiczne repo + README + gif demo.

### Pierwszy post "build in public" (dzień 7-8, jeden wieczór)

**X (po polsku, thread 5-7 tweetów):**
> 1/ Wracam do IT po 5 latach pracy fizycznej za granicą. Nie umiem programować od zera, ale od dziś buduję publicznie narzędzia z Claude Code i Codex.
>
> 2/ Pierwszy mini-projekt: overlay dla mojego kolegi streamującego CS2 na Kick.com.
>
> 3/ Stack: Next.js + Tailwind + Vercel. Czas budowy: 4 wieczory po 2h.
>
> 4/ Pokazuje czas streamu, W/L z sesji, customowy tekst.
>
> 5/ Repo: github.com/damianbuild/cs2-timer-overlay
> Demo: demo-overlay.damianbuild.dev
>
> 6/ Co zbudowałem dzięki Claude Code (a sam bym pewnie nie umiał miesiąc temu): cały plik /app/overlay/page.tsx z animacjami i Supabase.
>
> 7/ Co czytałem linijka po linijce: API routes, RLS w Supabase. Bo bez tego dane wyciekają. To dla mnie najważniejsza lekcja tygodnia. ➡️ obserwuj po więcej.

**LinkedIn (po polsku, long-form):**
> Po 5 latach pracy fizycznej za granicą wracam do Polski w lipcu. Nie wracam do tej samej pracy. Wracam, żeby budować narzędzia z AI.
>
> Ostatni tydzień: zbudowałem mini-overlay dla streamera CS2 na Kick. Nie pisałem kodu — opisywałem co chcę osiągnąć Claude Code'owi w terminalu, a on generował kod. Ja go czytałem, zatwierdzałem, deployowałem.
>
> Co działa? Dokumentowanie wszystkiego publicznie. Repo na GitHubie, demo na Vercelu, post tutaj.
>
> Plan na 6 miesięcy: 3 publiczne projekty z konkretnymi efektami. Z założenia: chcę pomagać małym polskim firmom dostać narzędzia za 10x mniej niż "agencja IT" je policzy.
>
> Pierwsze projekty będą prawdopodobnie:
> - narzędzia dla streamerów (zaczynam tu)
> - mini-aplikacje dla biur rachunkowych (czytniki faktur)
> - asystenci dla mechaników (wyceny z OCR)
>
> Repo i demo: [link]
>
> Jeśli prowadzisz firmę 1-15 osób i masz zadanie które robisz w Excelu i bolą Cię od tego oczy — daj znać. W tym kwartale szukam projektów do portfolio.

---

## Recommendations

1. **Zacznij dziś od Claude Pro + Claude Code installa + 1h tutorialu.** Nie kupuj kursów PL zanim nie zrobisz oficjalnego quickstartu. Dopiero po 2-3 tygodniach rozważ AI_devs 4 (aidevs.pl, ~1500-2500 zł) lub 10xDevs (10xdevs.pl) jako głębszą inwestycję — gdy będziesz już rozumiał o co chodzi w Claude Code i co dodaje kurs.

2. **W tygodniu 1 zbuduj mini-overlay dla CS2 i wrzuć publicznie.** Lepiej mieć krzywe demo dziś niż perfekcyjne za 3 miesiące. Pierwszy pull moment przychodzi po 3-4 widocznych projektach + ~50 polskich followersów X / connections LinkedIn z niszy.

3. **W mc 2 dołącz do AI Tinkerers Warsaw Discord (discord.gg/8WsqnC6Hk3) i ich meetupów (#8 18 czerwca 2026 Warszawa).** Zacznij od słuchania, ale po 1-2 wizytach zaprezentuj swoje demo (5 min, bez slajdów, tylko działający kod — to ich format).

4. **W mc 3 zacznij dystrybuować w polskich Discordach streamerów + grupach FB.** Nie spam. Dropujesz demo gdy ktoś pyta o overlay/automatyzację. Twoja strona damianbuild.pl powinna mieć "Zlecenia: pisz na hello@damianbuild.pl" + form.

5. **W mc 4 zacznij robić jeden YouTube video tygodniowo (15-30 min, po polsku, "jak zbudowałem X").** Polski YT o Claude Code ma 2-3 kanały (Przeprogramowani, overment, Mateusz Cisowski). Miejsce na nowego głosu z konkretnymi build-in-public projektami JEST.

6. **Faktura JDG, nie umowa zlecenie.** Otwórz JDG przy powrocie do Torunia. Ryczałt 8.5% dla usług programistycznych (lub 12% jeśli będziesz "pisał oprogramowanie sensu stricto") + składka zdrowotna ~315 zł/mc + ZUS dla nowych przedsiębiorców (preferencyjny ~415 zł przez 24 mc). Skonsultuj z księgową, możliwa IP Box 5%.

7. **Próg "działa": miesiąc 6 = pierwsza faktura na 3 000-12 000 zł.** Jeśli nie wpadła, **NIE zmieniaj ścieżki** — popraw publikowanie (więcej widocznych projektów, lepsze pierwsze 3 sekundy każdego video). Większość rzuca po 5 mc i traci całą zbudowaną reputację.

8. **Bezpieczeństwo od dnia 1:** Supabase RLS testuj na każdym projekcie. Secrets nigdy w repo (Vercel env vars, lokalnie `.env.local` w `.gitignore`). Halucynacje Claude'a w produkcji księgowej = realny problem prawny. **NIE przyjmuj zleceń z księgowości w pierwszych 6 mc** — zacznij od projektów gdzie błąd = "ojej, restart" a nie "klient ma kary skarbowe".

---

## Caveats

- **Briefowe stawki 500-1000 zł/h dla ekspertów** weryfikują się tylko częściowo w polskich raportach. Hays IT Contracting Salary Guide 2026 i Just Join IT Raport 2025/2026 potwierdzają górne stawki w wąskich niszach (Architecture, AI/ML senior, Go/Scala) sięgające ~375-620 zł/h przy 160h/mc (z górnym AI/ML max 99 490 zł/mc wg JJI). Stawki 800-1000 zł/h pojawiają się głównie u top consultingu dla klientów zagranicznych albo na bardzo krótkich engagementach. Dla "vibe coderów" w PL realna ścieżka po 12 mc to 200-350 zł/h, ekspercka 400-500 zł/h.
- **Polski rynek vibe coding jeszcze się formuje.** VibeConf 2026 (Gdynia, 20 kwietnia 2026) była PIERWSZĄ polską konferencją w 100% o vibe codingu. Polska agencja "Vibe Code Polska" (vibecodepolska.pl) reklamuje się jako pierwsza tego rodzaju. To **wczesny rynek** — szanse dla pierwszych, ale brak utartych szlaków.
- **Konkretne polskie ogłoszenia o "vibe coderów" są jeszcze rzadkie.** Useme, oferia.pl, justjoin.it pełne ogólnych ofert "AI Engineer", ale ofert wprost "AI-assisted developer / vibe coder" było jedynie kilkanaście aktywnych w kwietniu-maju 2026 (pl.indeed.com/q-vibe-code: m.in. "Vibe Coding Intern" YO IT Consulting Wrocław, "Mid Full Stack & AI Developer" Vazco zdalnie). Większa wartość freelance'u Damiana = dotarcie do bezpośrednich klientów (streamerów, biur, mechaników) niż czekanie aż portal wymyśli kategorię.
- **Pull strategy = długie cykle**. Realnie 4-9 miesięcy do pierwszej faktury. Niektórzy z polskich indie hackerów (Pucek, Aniserowicz, Smyrdek) mają **lata doświadczenia w programowaniu PRZED Claude Code'em**. Damian startuje z niższej bazy, więc realistycznie pierwsza faktura w mc 5-7, a nie 3.
- **Asperger + budowanie publiczne** — wymaga JEDNEGO formatu publikowania, który Damian utrzyma 6 mc. Nie eksperymentuj 5 formatami naraz. Sugeruję: GitHub README + krótkie X threads + 1 LinkedIn long-form na tydzień + 1 YT video na 2 tygodnie. Reszta = opcjonalne.
- **Claude Code i Codex zmieniają się co kwartał.** Plan ten jest aktualny dla maja 2026. Anthropic w styczniu 2026 wprowadził Claude Cowork; 18 maja 2026 przejął Stainless. Co 3 mc zrób review swojego workflow vs. nowości w docs.claude.com.
- **NIE ma polskiego programu partnerskiego Anthropic, polskiej oficjalnej certyfikacji Claude Code.** Wszystko po polsku to oddolne społeczności (10xDevs, AI_devs, Przeprogramowani, AI Tinkerers). To trochę luka i trochę szansa.