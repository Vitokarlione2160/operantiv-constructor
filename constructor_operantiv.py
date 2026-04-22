import streamlit as st

st.set_page_config(page_title="Конструктор оперантів", layout="centered", page_icon="🧩")

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

@keyframes fadeSlideIn {
  from { opacity: 0; transform: translateY(16px); }
  to   { opacity: 1; transform: translateY(0); }
}
@keyframes popIn {
  0%   { transform: scale(0.75); opacity: 0; }
  70%  { transform: scale(1.04); opacity: 1; }
  100% { transform: scale(1);    opacity: 1; }
}

html, body, [class*="css"] {
  font-family: 'Inter', sans-serif;
}

/* Прибираємо стандартний відступ Streamlit зверху */
.block-container { padding-top: 2rem !important; }

/* Заголовок */
.app-title {
  font-size: 22px; font-weight: 600;
  color: #1a1a1a; margin-bottom: 4px;
}
.app-subtitle {
  font-size: 14px; color: #888; margin-bottom: 24px;
}

/* Рядок тегів */
.tags-row {
  display: flex; flex-wrap: wrap; gap: 8px;
  margin-bottom: 20px;
  animation: fadeSlideIn 0.3s ease both;
}
.tag {
  font-size: 12px; font-weight: 500;
  padding: 5px 14px; border-radius: 20px;
  border: 0.5px solid transparent;
  transition: opacity 0.4s ease, transform 0.3s ease;
  user-select: none;
}
.tag.dimmed  { opacity: 0.28; }
.tag.highlighted { transform: scale(1.07); }
.tag.mand  { background:#E1F5EE; color:#085041; border-color:#9FE1CB; }
.tag.takt  { background:#E6F1FB; color:#0C447C; border-color:#85B7EB; }
.tag.intra { background:#EEEDFE; color:#3C3489; border-color:#AFA9EC; }
.tag.echo  { background:#FAEEDA; color:#633806; border-color:#FAC775; }
.tag.read  { background:#FAECE7; color:#712B13; border-color:#F0997B; }
.tag.trans { background:#EAF3DE; color:#27500A; border-color:#C0DD97; }

/* Картка питання */
.q-card {
  background: #ffffff;
  border: 0.5px solid #e0e0e0;
  border-radius: 14px;
  padding: 24px 28px 20px;
  animation: fadeSlideIn 0.32s cubic-bezier(0.22,1,0.36,1) both;
  margin-bottom: 10px;
}
.q-label {
  font-size: 11px; font-weight: 600;
  letter-spacing: 0.08em; text-transform: uppercase;
  color: #aaa; margin-bottom: 8px;
}
.q-text {
  font-size: 18px; font-weight: 500;
  color: #1a1a1a; line-height: 1.45;
  margin-bottom: 0;
}
.q-hint {
  font-size: 12px; color: #bbb;
  text-align: center; margin-top: 6px;
}

/* Кнопки питання */
div[data-testid="stButton"] > button {
  border-radius: 9px !important;
  font-size: 15px !important;
  font-weight: 500 !important;
  padding: 13px 10px !important;
  transition: transform 0.12s ease, filter 0.12s ease !important;
  border: 0.5px solid transparent !important;
}
div[data-testid="stButton"] > button:active {
  transform: scale(0.96) !important;
}

/* Кнопка ТАК */
div[data-testid="stButton"]:first-child > button {
  background-color: #E1F5EE !important;
  color: #085041 !important;
  border-color: #5DCAA5 !important;
}
div[data-testid="stButton"]:first-child > button:hover {
  background-color: #9FE1CB !important;
}

/* Кнопка НІ */
div[data-testid="stButton"]:last-child > button {
  background-color: #FAECE7 !important;
  color: #712B13 !important;
  border-color: #F0997B !important;
}
div[data-testid="stButton"]:last-child > button:hover {
  background-color: #F5C4B3 !important;
}

/* Картка результату */
.result-card {
  background: #ffffff;
  border: 0.5px solid #e0e0e0;
  border-radius: 14px;
  padding: 36px 28px 32px;
  text-align: center;
  animation: popIn 0.42s cubic-bezier(0.22,1,0.36,1) both;
}
.result-icon  { font-size: 40px; margin-bottom: 12px; display:block; }
.result-name  { font-size: 28px; font-weight: 600; color: #1a1a1a; margin-bottom: 8px; }
.result-desc  {
  font-size: 14px; color: #666; line-height: 1.65;
  max-width: 380px; margin: 0 auto 20px;
}
.result-badge {
  display: inline-block; font-size: 12px; font-weight: 500;
  padding: 5px 16px; border-radius: 20px; margin-bottom: 24px;
}
.badge-mand  { background:#E1F5EE; color:#085041; }
.badge-takt  { background:#E6F1FB; color:#0C447C; }
.badge-intra { background:#EEEDFE; color:#3C3489; }
.badge-echo  { background:#FAEEDA; color:#633806; }
.badge-read  { background:#FAECE7; color:#712B13; }
.badge-trans { background:#EAF3DE; color:#27500A; }

/* Кнопка reset */
.reset-btn > button {
  background-color: #f4f4f4 !important;
  color: #444 !important;
  border: 0.5px solid #ddd !important;
  border-radius: 8px !important;
  font-size: 14px !important;
  padding: 11px 28px !important;
}
.reset-btn > button:hover { background-color: #e8e8e8 !important; }

/* Футер */
.footer { font-size: 12px; color: #ccc; text-align: center; margin-top: 28px; }
</style>
""", unsafe_allow_html=True)

# ── Дані ──────────────────────────────────────────────────────────────────────
OPERANTS = [
    {"id": "mand",  "label": "Манд",              "cls": "mand"},
    {"id": "takt",  "label": "Такт",              "cls": "takt"},
    {"id": "intra", "label": "Інтравербалізація", "cls": "intra"},
    {"id": "echo",  "label": "Ехо",               "cls": "echo"},
    {"id": "read",  "label": "Прочитування",      "cls": "read"},
    {"id": "trans", "label": "Транскрипція",       "cls": "trans"},
]

QUESTIONS = [
    {
        "label":    "Питання 1",
        "text":     "Чи присутні мотиваційні умови (депривація, EO)?",
        "hint":     "Так → Манд",
        "possible": ["mand","takt","intra","echo","read","trans"],
        "yes":      {"result": "mand"},
        "no":       {"next": 1, "possible": ["takt","intra","echo","read","trans"]},
    },
    {
        "label":    "Питання 2",
        "text":     "Чи присутній невербальний стимул (предмет, картинка, подія)?",
        "hint":     "Так → Такт",
        "possible": ["takt","intra","echo","read","trans"],
        "yes":      {"result": "takt"},
        "no":       {"next": 2, "possible": ["intra","echo","read","trans"]},
    },
    {
        "label":    "Питання 3",
        "text":     "Чи є буквальна відповідність між стимулом і відповіддю?",
        "hint":     "Ні → Інтравербалізація",
        "possible": ["intra","echo","read","trans"],
        "yes":      {"next": 3, "possible": ["echo","read","trans"]},
        "no":       {"result": "intra"},
    },
    {
        "label":    "Питання 4",
        "text":     "Чи збігається модальність реакції зі стимулом (почув — повторив вголос)?",
        "hint":     "Так → Ехо",
        "possible": ["echo","read","trans"],
        "yes":      {"result": "echo"},
        "no":       {"next": 4, "possible": ["read","trans"]},
    },
    {
        "label":    "Питання 5",
        "text":     "Чи є антецедент друкованим стимулом (текст, символи)?",
        "hint":     "Так → Прочитування  ·  Ні → Транскрипція",
        "possible": ["read","trans"],
        "yes":      {"result": "read"},
        "no":       {"result": "trans"},
    },
]

RESULTS = {
    "mand":  {"name": "Манд",              "icon": "🔊", "desc": "Під контролем мотиваційних умов. Людина просить те, чого хоче. Наслідок: специфічне підкріплення.",                           "cls": "mand"},
    "takt":  {"name": "Такт",              "icon": "🖼️", "desc": "Під контролем невербального стимулу. Людина називає те, що бачить. Наслідок: генералізоване умовне підкріплення.",              "cls": "takt"},
    "intra": {"name": "Інтравербалізація", "icon": "💬", "desc": "Вербальний стимул без буквальної відповідності. Модальність: будь-яка. Наслідок: генералізоване умовне підкріплення.",         "cls": "intra"},
    "echo":  {"name": "Ехо",               "icon": "🔁", "desc": "Вербальний стимул, модальність збігається. Людина повторює почуте. Наслідок: генералізоване умовне підкріплення.",               "cls": "echo"},
    "read":  {"name": "Прочитування",      "icon": "📖", "desc": "Друкований стимул → усна відповідь. Модальність різна. Наслідок: генералізоване умовне підкріплення.",                           "cls": "read"},
    "trans": {"name": "Транскрипція",      "icon": "📝", "desc": "Вокальний стимул → письмова відповідь (запис або дактиль). Наслідок: генералізоване умовне підкріплення.",                      "cls": "trans"},
}

# ── Стан ──────────────────────────────────────────────────────────────────────
if "step" not in st.session_state:
    st.session_state.step = 0
if "possible" not in st.session_state:
    st.session_state.possible = [o["id"] for o in OPERANTS]
if "result" not in st.session_state:
    st.session_state.result = None

# ── Хелпери ───────────────────────────────────────────────────────────────────
def tags_html(possible, highlight=None):
    parts = []
    for o in OPERANTS:
        extra = ""
        if highlight and o["id"] == highlight:
            extra = " highlighted"
        elif o["id"] not in possible:
            extra = " dimmed"
        parts.append(f'<span class="tag {o["cls"]}{extra}">{o["label"]}</span>')
    return '<div class="tags-row">' + "".join(parts) + "</div>"

def answer(yes):
    q = QUESTIONS[st.session_state.step]
    branch = q["yes"] if yes else q["no"]
    if "result" in branch:
        st.session_state.result = branch["result"]
        st.session_state.possible = [branch["result"]]
    else:
        st.session_state.step = branch["next"]
        st.session_state.possible = branch["possible"]

def reset():
    st.session_state.step = 0
    st.session_state.possible = [o["id"] for o in OPERANTS]
    st.session_state.result = None

# ── Заголовок ─────────────────────────────────────────────────────────────────
st.markdown('<div class="app-title">🧩 Конструктор оперантів</div>', unsafe_allow_html=True)
st.markdown('<div class="app-subtitle">Визначення типу вербального операнту за схемою</div>', unsafe_allow_html=True)

# ── Головний UI ───────────────────────────────────────────────────────────────
if st.session_state.result:
    r = RESULTS[st.session_state.result]
    st.markdown(tags_html(st.session_state.possible, highlight=r["cls"]), unsafe_allow_html=True)
    st.markdown(f"""
    <div class="result-card">
      <span class="result-icon">{r['icon']}</span>
      <div class="result-name">{r['name']}</div>
      <div class="result-desc">{r['desc']}</div>
      <span class="result-badge badge-{r['cls']}">{r['name']}</span>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    col = st.columns([1, 2, 1])[1]
    with col:
        st.markdown('<div class="reset-btn">', unsafe_allow_html=True)
        st.button("🔄 Пройти заново", use_container_width=True, on_click=reset)
        st.markdown('</div>', unsafe_allow_html=True)

else:
    q = QUESTIONS[st.session_state.step]
    st.markdown(tags_html(st.session_state.possible), unsafe_allow_html=True)
    st.markdown(f"""
    <div class="q-card">
      <div class="q-label">{q['label']}</div>
      <div class="q-text">{q['text']}</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown(f'<div class="q-hint">{q["hint"]}</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.button("Так", use_container_width=True, on_click=answer, args=(True,))
    with col2:
        st.button("Ні", use_container_width=True, on_click=answer, args=(False,))

st.markdown('<div class="footer">Конструктор оперантів · Логіка відповідає таблиці</div>', unsafe_allow_html=True)
