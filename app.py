import streamlit as st

# Настройка страницы (максимально чисто, без лишних элементов)
st.set_page_config(
    page_title="Прогноз САД",
    initial_sidebar_state="collapsed"
)

# --- CSS Стилизация ---
st.markdown("""
    <style>
    /* Скрываем меню и футер */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Центрируем заголовок */
    h1 {
        text-align: center;
        font-size: 26px;
        font-weight: 700;
        margin-bottom: 30px;
        color: #000;
        font-family: sans-serif;
    }
    
    /* Стилизация подписей к полям */
    .input-label {
        font-weight: 600;
        font-size: 16px;
        margin-bottom: 5px;
        margin-top: 10px;
        font-family: sans-serif;
    }

    /* Зеленая кнопка "Рассчитать" */
    div.stButton > button {
        width: 100%;
        background-color: #28a745;
        color: white;
        font-weight: bold;
        font-size: 18px;
        border: none;
        border-radius: 5px;
        padding: 12px 0;
        margin-top: 25px;
    }
    div.stButton > button:hover {
        background-color: #218838;
        color: white;
        border: none;
    }
    div.stButton > button:active {
        background-color: #1e7e34;
        color: white;
    }
    div.stButton > button:focus {
        color: white; 
        background-color: #28a745;
    }

    /* Серое поле результата */
    .result-box {
        background-color: #e9ecef;
        padding: 20px;
        border-radius: 5px;
        margin-top: 20px;
        text-align: center;
        border: 1px solid #ced4da;
    }
    .result-text {
        font-size: 18px;
        color: #333;
        margin-bottom: 5px;
        font-family: sans-serif;
    }
    .result-value {
        font-size: 28px;
        font-weight: 800;
        color: #000;
        font-family: sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# --- Заголовок ---
st.markdown("<h1>Прогнозирование значение систолического артериального давления перед операцией</h1>", unsafe_allow_html=True)

# --- Ввод данных ---

# 1. Вес
st.markdown('<div class="input-label">Вес пациента (кг)</div>', unsafe_allow_html=True)
weight = st.number_input(
    "label_weight", 
    min_value=30.0, 
    max_value=250.0, 
    value=70.0, 
    step=0.5, 
    label_visibility="collapsed"
)

# 2. Гематокрит
st.markdown('<div class="input-label">Уровень гематокрита (Ht)</div>', unsafe_allow_html=True)
ht_option = st.selectbox(
    "label_ht",
    options=["Менее 44%", "44% и выше"],
    label_visibility="collapsed"
)

# --- Расчет ---
# Логика: Если выбрали "44% и выше", то X = 1, иначе X = 0
ht_factor = 1 if ht_option == "44% и выше" else 0

# Новое уравнение: 109.116 + 0.224*Вес + 8.749*Ht
prediction = 109.116 + (0.224 * weight) + (8.749 * ht_factor)

# --- Кнопка и Вывод ---
if st.button("Рассчитать"):
    st.markdown(f"""
        <div class="result-box">
            <div class="result-text">Прогнозируемое САД:</div>
            <div class="result-value">{prediction:.1f} мм рт. ст.</div>
        </div>
    """, unsafe_allow_html=True)
