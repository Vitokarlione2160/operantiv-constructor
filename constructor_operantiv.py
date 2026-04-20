import streamlit as st

st.set_page_config(page_title="Конструктор оперантів", layout="centered")
st.title("🧩 Конструктор оперантів")
st.markdown("### Визначення типу вербального операнту за схемою")

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

def get_operant_result():
    path = "".join(st.session_state.path)
    
    if st.session_state.path[0] == "Так":
        return "МАНД", "Оперант під контролем мотиваційних умов."
    
    elif len(st.session_state.path) >= 2 and st.session_state.path[1] == "Так":
        return "ТАКТ", "Оперант під контролем невербального дискримінативного стимулу."
    
    elif len(st.session_state.path) >= 3 and st.session_state.path[2] == "Так":
        if len(st.session_state.path) >= 4 and st.session_state.path[3] == "Ні":
            return "ІНТРАВЕРБАЛІЗАЦІЯ", "Вербальний стимул без формальної схожості."
        elif len(st.session_state.path) >= 5 and st.session_state.path[4] == "Так":
            return "ЕХО", "Формальна схожість з вербальним стимулом."
        else:
            return "ЕХО", "Формальна схожість з вербальним стимулом."
    
    else:
        # Якщо дійшли до кінця без попередніх гілок
        return "ТРАНСКРИПЦІЯ або ПРОЧИТУВАННЯ", "Оперант під контролем письмового або аудіального вербального стимулу без формальної схожості."

# Відображення прогресу
progress = min(st.session_state.step / len(questions) * 100, 100)
st.progress(progress / 100)

# Основна логіка
if st.session_state.step < len(questions):
    st.subheader(f"Питання {st.session_state.step + 1} з {len(questions)}")
    st.write(questions[st.session_state.step])
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Так", type="primary", use_container_width=True):
            st.session_state.path.append("Так")
            st.session_state.step += 1
            st.rerun()
    with col2:
        if st.button("❌ Ні", type="secondary", use_container_width=True):
            st.session_state.path.append("Ні")
            st.session_state.step += 1
            st.rerun()

else:
    # Результат
    operant, explanation = get_operant_result()
    
    st.success(f"**Оперант: {operant}**")
    st.info(explanation)
    
    st.write("### Ваш шлях відповідей:")
    for i, ans in enumerate(st.session_state.path, 1):
        st.write(f"{i}. {ans}")
    
    if st.button("🔄 Пройти заново", type="primary"):
        st.session_state.step = 0
        st.session_state.path = []
        st.rerun()

st.caption("Конструктор оперантів • Логіка повністю відповідає діаграмі")
