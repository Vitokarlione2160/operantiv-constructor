import streamlit as st

st.set_page_config(page_title="Конструктор оперантів", layout="centered", page_icon="🧩")

st.title("🧩 Конструктор оперантів")
st.markdown("### Визначення типу вербального операнту за схемою")

if 'step' not in st.session_state:
    st.session_state.step = 0
if 'path' not in st.session_state:
    st.session_state.path = []

questions = [
    "1. Чи присутні **мотиваційні умови** (мотивація, депривація, EO)?",
    "2. Чи присутній **невербальний дискримінативний стимул** (предмет, картинка, подія)?",
    "3. Чи присутній **вербальний дискримінативний стимул** (слово, фраза, інструкція)?",
    "4. Чи є **буквальна відповідність** (точне повторення стимулу)?",
    "5. Чи є **формальна схожість** між стимулом і відповіддю?"
]

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
        if st.button("❌ Ні", use_container_width=True):
            st.session_state.path.append("Ні")
            st.session_state.step += 1
            st.rerun()

else:
    # === ПРАВИЛЬНА ЛОГІКА ЗА ДІАГРАМОЮ ===
    answers = st.session_state.path
    result = ""
    explanation = ""

    if len(answers) > 0 and answers[0] == "Так":
        result = "МАНД"
        explanation = "🔊 **Манд** — оперант під контролем мотиваційних умов. Людина просить те, чого хоче."

    elif len(answers) > 1 and answers[1] == "Так":
        result = "ТАКТ"
        explanation = "🖼️ **Такт** — оперант під контролем невербального дискримінативного стимулу. Людина називає те, що бачить."

    elif len(answers) > 2 and answers[2] == "Ні":
        result = "ТРАНСКРИПЦІЯ або ПРОЧИТУВАННЯ"
        explanation = "📝 **Транскрипція або Прочитування** — оперант під контролем письмового або аудіального стимулу без мотивації та невербального стимулу."

    elif len(answers) > 2 and answers[2] == "Так":
        if len(answers) > 3 and answers[3] == "Ні":
            result = "ІНТРАВЕРБАЛІЗАЦІЯ"
            explanation = "💬 **Інтравербалізація** — відповідь на вербальний стимул без буквальної відповідності."
        else:
            # Питання 5
            if len(answers) > 4 and answers[4] == "Так":
                result = "ЕХО"
                explanation = "🔁 **Ехо** — повторення почутого (формальна схожість з вербальним стимулом)."
            else:
                result = "ІНТРАВЕРБАЛІЗАЦІЯ"
                explanation = "💬 **Інтравербалізація** — вербальний стимул без формальної схожості."

    st.success(f"**Оперант: {result}**")
    st.markdown(explanation)

    st.markdown("### Ваш шлях відповідей:")
    for i, ans in enumerate(answers, 1):
        st.write(f"{i}. **{ans}**")

    if st.button("🔄 Пройти заново", type="primary"):
        st.session_state.step = 0
        st.session_state.path = []
        st.rerun()

st.caption("Конструктор оперантів • Логіка відповідає діаграмі")
