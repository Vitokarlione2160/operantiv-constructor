import streamlit as st

st.set_page_config(page_title="Конструктор оперантів", layout="centered", page_icon="🧩")

st.title("🧩 Конструктор оперантів")
st.markdown("### Визначення типу вербального операнту за схемою Скінера")

# Ініціалізація
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'path' not in st.session_state:
    st.session_state.path = []

questions = [
    "Чи присутні **мотиваційні умови** (мотивація, депривація, EO)?",
    "Чи присутній **невербальний дискримінативний стимул** (предмет, картинка, подія)?",
    "Чи присутній **вербальний дискримінативний стимул** (слово, фраза, інструкція)?",
    "Чи є **буквальна відповідність** (точне повторення стимулу)?",
    "Чи є **формальна схожість** між стимулом і відповіддю?"
]

def get_result():
    answers = st.session_state.path
    
    if answers and answers[0] == "Так":
        return "МАНД", "🔊 **Манд** — оперант, контрольований мотиваційними умовами. Дитина просить те, чого хоче."
    
    elif len(answers) >= 2 and answers[1] == "Так":
        return "ТАКТ", "🖼️ **Такт** — оперант, контрольований невербальним стимулом (предметом або подією). Дитина називає те, що бачить."
    
    elif len(answers) >= 3 and answers[2] == "Так":
        if len(answers) >= 4 and answers[3] == "Ні":
            return "ІНТРАВЕРБАЛІЗАЦІЯ", "💬 **Інтравербалізація** — відповідь на вербальний стимул без формальної схожості (розмова, відповідь на питання)."
        elif len(answers) >= 5 and answers[4] == "Так":
            return "ЕХО", "🔁 **Ехо** — повторення почутого (імітація вербального стимулу)."
        else:
            return "ЕХО", "🔁 **Ехо** — повторення почутого."
    
    else:
        return "ТРАНСКРИПЦІЯ або ПРОЧИТУВАННЯ", "📝 **Транскрипція / Прочитування** — запис сказаного або читання тексту."

# Дизайн
st.markdown("---")

# Прогрес
progress = min((st.session_state.step / len(questions)) * 100, 100)
st.progress(progress / 100)
st.caption(f"Питання {st.session_state.step + 1} з {len(questions)}")

# Основна логіка
if st.session_state.step < len(questions):
    st.subheader(f"Питання {st.session_state.step + 1}")
    st.markdown(f"**{questions[st.session_state.step]}**")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Так", use_container_width=True, type="primary"):
            st.session_state.path.append("Так")
            st.session_state.step += 1
            st.rerun()
    with col2:
        if st.button("❌ Ні", use_container_width=True, type="secondary"):
            st.session_state.path.append("Ні")
            st.session_state.step += 1
            st.rerun()

else:
    # Результат
    operant, explanation = get_result()
    
    st.success(f"**Оперант: {operant}**")
    st.markdown(explanation)
    
    st.markdown("### Ваш шлях відповідей:")
    for i, ans in enumerate(st.session_state.path, 1):
        st.write(f"{i}. **{ans}**")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Пройти заново", type="primary", use_container_width=True):
            st.session_state.step = 0
            st.session_state.path = []
            st.rerun()
    with col2:
        if st.button("📋 Скопіювати результат", use_container_width=True):
            st.code(f"Оперант: {operant}\n{explanation}", language=None)

st.caption("Конструктор оперантів • Створено для ABA-терапії")
