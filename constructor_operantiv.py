import streamlit as st

st.set_page_config(page_title="Конструктор оперантів", layout="centered", page_icon="🧩")

st.title("🧩 Конструктор оперантів")
st.markdown("### Визначення типу вербального операнту за схемою")

if 'step' not in st.session_state:
    st.session_state.step = 0
if 'result' not in st.session_state:
    st.session_state.result = None

def show_result(name, explanation, emoji):
    st.session_state.result = {"name": name, "explanation": explanation, "emoji": emoji}

def answer(yes):
    step = st.session_state.step

    if step == 0:  # Q1: Мотиваційні умови?
        if yes:
            show_result("МАНД", "Оперант під контролем мотиваційних умов. Людина просить те, чого хоче.", "🔊")
        else:
            st.session_state.step = 1

    elif step == 1:  # Q2: Невербальний Sd?
        if yes:
            show_result("ТАКТ", "Оперант під контролем невербального дискримінативного стимулу. Людина називає те, що бачить.", "🖼️")
        else:
            st.session_state.step = 2

    elif step == 2:  # Q3: Вербальний Sd?
        if not yes:
            show_result("ІНТРАВЕРБАЛІЗАЦІЯ", "Відповідь на вербальний стимул без буквальної відповідності стимулу.", "💬")
        else:
            st.session_state.step = 3

    elif step == 3:  # Q4: Буквальна відповідність?
        if not yes:
            show_result("ІНТРАВЕРБАЛІЗАЦІЯ", "Відповідь на вербальний стимул без буквальної відповідності стимулу.", "💬")
        else:
            st.session_state.step = 4

    elif step == 4:  # Q5: Формальна схожість?
        if yes:
            show_result("ЕХО", "Повторення почутого — формальна схожість між стимулом і відповіддю.", "🔁")
        else:
            st.session_state.step = 5

    elif step == 5:  # Q6: Письмовий Sd?
        if yes:
            show_result("ПРОЧИТУВАННЯ", "Письмовий стимул → усна відповідь. Людина читає вголос.", "📖")
        else:
            show_result("ТРАНСКРИПЦІЯ", "Усний стимул → письмова відповідь. Людина записує почуте.", "📝")

def reset():
    st.session_state.step = 0
    st.session_state.result = None

# --- Показуємо результат ---
if st.session_state.result:
    r = st.session_state.result
    st.success(f"{r['emoji']} **Оперант: {r['name']}**")
    st.markdown(f"> {r['explanation']}")
    st.divider()
    st.button("🔄 Пройти заново", type="primary", on_click=reset)

# --- Показуємо питання ---
else:
    questions = {
        0: ("Питання 1", "Чи присутні **мотиваційні умови** (мотивація, депривація, EO)?"),
        1: ("Питання 2", "Чи присутній **невербальний дискримінативний стимул** (предмет, картинка, подія)?"),
        2: ("Питання 3", "Чи присутній **вербальний дискримінативний стимул** (слово, фраза, інструкція)?"),
        3: ("Питання 4", "Чи є **буквальна відповідність** (точне повторення стимулу)?"),
        4: ("Питання 5", "Чи є **формальна схожість** між стимулом і відповіддю?"),
        5: ("Питання 6", "Чи є стимул **письмовим** (текст, символи)?"),
    }

    step = st.session_state.step
    label, question = questions[step]

    st.subheader(label)
    st.markdown(f"**{question}**")

    col1, col2 = st.columns(2)
    with col1:
        st.button("✅ Так", use_container_width=True, type="primary", on_click=answer, args=(True,))
    with col2:
        st.button("❌ Ні", use_container_width=True, on_click=answer, args=(False,))

st.caption("Конструктор оперантів • Логіка відповідає діаграмі")
